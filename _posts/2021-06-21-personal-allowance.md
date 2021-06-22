---
layout: post
current: post
cover: assets/images/personal-allowance.png
navigation: True
title: Funding UBI by eliminating the personal allowance
date: 2021-06-21
tags: [uk,ubi]
subclass: 'post'
author: ines
excerpt: A budget-neutral plan exchanging tax exemption for universal basic income
class: post-template
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

# Funding UBI by eliminating the personal allowance
The personal allowance is a feature of the UK tax system which designates a certain amount of individual income as non-taxable. This amount is currently set at £12,500, meaning the first £12,500 of an individual’s earnings are not taxed. Ever since it was [first introduced in 1979](http://taxhistory.co.uk/Income%20Tax%20Allowances.htm) at £1,165 (equivalent to around [£6,028 today)](https://www.bankofengland.co.uk/monetary-policy/inflation/inflation-calculator), it has been steadily increasing almost every year.

#### Benefits & Criticisms of PA

The personal allowance is fairly popular in the UK, as it allows people to retain a greater portion of their income. At current levels, the average individual saves over £1,600 annually in taxes thanks to the personal allowance.

Moreover, it is often thought of as fiscally progressive since it allows the lowest income earners—those making under £12,500—to be free from any income tax at all, while it phases out for the highest earners making above £100,000. Many people support raising the personal allowance thinking that the higher it is, the greater the number of low-income earners who fall below the threshold, allowing these individuals to retain more of their income. Thus, by this logic, it should serve as a mechanism for reducing poverty.

Though this sounds good on paper, the personal allowance has been found to be regressive in practice. This does not mean that the poor do not benefit from it, but that the affluent benefit from it more. There are two main reasons for this. Firstly, many of the UK’s poorest already fall below the personal allowance threshold, and raising the personal allowance does nothing for them. Rather, it exclusively helps higher income earners who make above the threshold and up to [£125,140](https://www.gov.uk/income-tax-rates/income-over-100000). Though some at the bottom of the income scale may benefit, the [overwhelming majority of the benefits do not go to them](https://leftfootforward.org/2013/03/the-10000-personal-tax-allowance-anything-but-progressive/) but to those more affluent.

The second reason has to do with the phaseout of Universal Credit and similar means-tested benefits. Since Universal Credit is based on post-tax income, then when taxes are reduced and post-tax income rises, recipients see their Universal Credit amount reduced as well. As [explained](https://www.politics.co.uk/opinion-former/press-release/2018/10/29/personal-allowance-increase-does-little-for-those-on-lowest-income/) by Victoria Todd, Head of the Low Income Tax Reform Group, about the 2019 changes: 

> “[Universal credit recipients] will not see the full tax gain of £130 from the increase in the personal allowance; instead, they will only gain overall by £48.10, as their Universal Credit award will be reduced by £81.90. However, those earning above £11,850 who receive tax credits will benefit from the full £130 because tax credits are based on gross income.”

Again, this means that higher-income earners benefit more than low-income earners from personal reform increases. In fact, according to [one report](https://www.resolutionfoundation.org/app/uploads/2014/12/Missing-the-target1.pdf) by the Resolution Foundation, the most recent increase of the personal allowance to £12,500 gave only around £18 of additional income to the bottom 10% of households and £203 to the top 10%.

The [New Economics Foundation](https://neweconomics.org/) also looked in a [report](https://neweconomics.org/2019/03/nothing-personal) at replacing the Personal Allowance with a Weekly National Allowance paid to adults and the Child Benefit increased, with the payments non-taxable but included in means tests, finding progressive results.
#### Party proposals regarding personal allowance and UBI

The regressivity of the personal allowance suggests that its elimination would lead the income of the UK’s poorest to be reduced only negligibly, while the more affluent would see a greater burden. This makes it a good candidate for helping fund a progressive UBI proposal.

Both UK parties who have released UBI proposals have found a role for personal allowance to help fund their programs. The Liberal Democrats have conceded that there will be a reduction, but insist their proposal involves [“in all cases leaving some level of Personal Allowance (at least £2,500 a year)”](https://d3n8a8pro7vhmx.cloudfront.net/libdems/pages/1811/attachments/original/1621669347/145_-_Universal_Basic_Income.docx_%281%29.pdf?1621669347). Meanwhile, the Green Party states that in their model, UBI will be taxable, but [“all income tax payers will have a tax-free allowance which is the equivalent to their Universal Basic Income amount”](https://www.greenparty.ie/wp-content/uploads/2018/07/Green-Party-Universal-Basic-Income-Policy.pdf). This means that, in practice, the UBI would not be taxed and the personal allowance would effectively be eliminated. Both parties also include UBI when means-testing.

In the following analysis, we will explore the effect of a UBI funded exclusively through the elimination of a personal allowance. The UBI amount in this simulation is equal amount for everyone, regardless of age or disability, and does not count towards means-testing.
#### Our findings
Under this policy, our simulation finds that we could fund a UBI of around £1,634 per person. The following graph shows the effect this would have across different among deciles:

<button onclick="show_code_8()">Click to show code</button>
<div id="code_block_8" style="display: none;">
  <pre>
    <code>
# Setup
from openfisca_uk import Microsimulation
from openfisca_uk import *
from openfisca_core.model_api import Reform
from openfisca_uk.entities import Person, BenUnit, Household
from openfisca_core.model_api import *
from openfisca_uk.tools.general import *
from ubicenter import format_fig

import plotly.express as px
import plotly.io as pio
#pio.renderers.default = "browser"
#change "browser" to "notebook" when working on non-ines computers

sim = Microsimulation(input_year=2020)

from openfisca_core import periods
def make_PA_reform(PA_amount):
    
    def update_PA_parameter(parameters):
        parameters.tax.income_tax.allowances.personal_allowance.amount.update(period=periods.period("year:2020:1"), value=PA_amount)
        return parameters
    
    class reform(Reform):
        def apply(self):
            self.modify_parameters(update_PA_parameter)
    
    sim_less_PA = Microsimulation(reform, input_year=2020)
    revenue = sim.calc("net_income").sum()
    revenue_diff = revenue - sim_less_PA.calc("net_income").sum()
    BI_amount = revenue_diff/(sim.calc("people").sum())
    
    class BI(Variable):
        value_type = float
        entity = Person
        label = u"UBI"
        definition_period = YEAR
        def formula(person, period, parameters):
            return(BI_amount)

    class gross_income(Variable):
        value_type = float
        entity = Person
        label = u"Gross income, including benefits"
        definition_period = YEAR

        def formula(person, period, parameters):
            COMPONENTS = [
                "employment_income",
                "pension_income",
                "self_employment_income",
                "property_income",
                "savings_interest_income",
                "dividend_income",
                "miscellaneous_income",
                "benefits",
                "BI"
            ]
            return add(person, period, COMPONENTS)   

    class basic_income(Reform):
        def apply(self):
            self.add_variable(BI)
            self.update_variable(gross_income)
            
    sim_BI = Microsimulation(reform, basic_income, input_year=2020)
    
    return sim_BI

sim_BI = make_PA_reform(0)

income_diff = sim_BI.calc("household_net_income") - sim.calc("household_net_income")
income = sim.calc("household_net_income")

chart1 = format_fig(px.bar(income_diff.groupby(income.decile_rank()).mean()).update_layout(
    title_text='Mean difference in household net income for each income decile',
    xaxis_title ="Income decile",
    yaxis_title ="Change in income",
    showlegend= False,
    yaxis_tickprefix="£"
))

    </code>
  </pre>
</div>

<script>
function show_code_8() {
  var x = document.getElementById("code_block_8");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_8_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_8_1.html");
    });
  </script>
</div>
<div id = "graph_graph_8_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_8_2").load("{{site.baseurl}}assets/images/personal-allowance/graph_8_2.html");
    });
  </script>
</div>
<div id = "graph_graph_8_2"></div>

This policy would, in general, serve as a wealth transfer from the richest 40% to the poorest 60%. 

Median household income would increase by about £564, and this number is over five times greater for those living in poverty. Hence, poverty would be reduced by about 29%, while deep poverty (people living at under half the poverty line) would be reduced by about 46%.

<button onclick="show_code_10()">Click to show code</button>
<div id="code_block_10" style="display: none;">
  <pre>
    <code>
#Median difference in household net income for different poverty groups
effect = sim_BI.calc("household_net_income", map_to="person") - sim.calc("household_net_income", map_to="person")
isDeepPoor = sim.calc("in_deep_poverty_bhc", map_to ="person")
isPoor = sim.calc("in_poverty_bhc", map_to = "person") & ~isDeepPoor
#isPoor excludes those in deep poverty
overall = sim_BI.calc("household_net_income").median() - sim.calc("household_net_income").median()


chart2 = format_fig(px.bar(x=["Deep poverty", "In poverty, but not deep", "Not in poverty", "Overall"], y=[effect[isDeepPoor].mean(), effect[isPoor].mean(), effect[~isPoor].mean(), overall]).update_layout(
    title_text='Median gain in household net income for different poverty groups',
    xaxis_title ="Group",
    yaxis_title ="Median gain in household net income",
    yaxis_tickprefix="£"
))
    </code>
  </pre>
</div>

<script>
function show_code_10() {
  var x = document.getElementById("code_block_10");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_10_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_10_1.html");
    });
  </script>
</div>
<div id = "graph_graph_10_1"></div>


<button onclick="show_code_11()">Click to show code</button>
<div id="code_block_11" style="display: none;">
  <pre>
    <code>
#Reductions in poverty rates

import plotly.graph_objects as go

poverty_before = sim.calc("in_poverty_bhc", map_to="person").sum()/sim.calc("people").sum() * 100
poverty_now = sim_BI.calc("in_poverty_bhc", map_to="person").sum()/sim.calc("people").sum() * 100

deep_poverty_before = sim.calc("in_deep_poverty_bhc", map_to="person").sum()/sim.calc("people").sum() * 100
deep_poverty_now = sim_BI.calc("in_deep_poverty_bhc", map_to="person").sum()/sim.calc("people").sum() * 100

poverty_types=['Poverty', "Deep poverty"]

chart3 = format_fig(go.Figure(data=[
    go.Bar(name='Before reform', x=poverty_types, y=[poverty_before, deep_poverty_before]),
    go.Bar(name='After reform', x=poverty_types, y=[poverty_now, deep_poverty_now])
]).update_layout(
    barmode='group', 
    title_text='Poverty rates before and after reform', 
    xaxis_title ="Poverty type",
    yaxis_title ="Rate",
    yaxis_ticksuffix="%", ))
    </code>
  </pre>
</div>

<script>
function show_code_11() {
  var x = document.getElementById("code_block_11");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_11_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_11_1.html");
    });
  </script>
</div>
<div id = "graph_graph_11_1"></div>

Part of the results above are explained not only by the regressivity of personal allowance, but also by the fact that poor households tend to have more children and would therefore receive more UBI checks per household. Similarly, households in deep poverty tend to have fewer children than other poor households, which explains why the median gain is slightly less for this group.

In fact, this policy would benefit children more than any other group, as children do not lose income to a personal allowance decrease, and exclusively gain from the UBI amount given to them. Child poverty would be reduced by about 51%. As shown below, this would largely serve as a wealth transfer from adults to children.

<button onclick="show_code_13()">Click to show code</button>
<div id="code_block_13" style="display: none;">
  <pre>
    <code>
#Mean difference in household income by age
income_diff_2 = sim_BI.calc("household_net_income", map_to="person") - sim.calc("household_net_income", map_to="person")
age = sim.calc("age", map_to ="person")
chart4 = format_fig(px.bar(income_diff_2.groupby(age).mean()).update_layout(
    title_text='Mean difference in household net income by age',
    yaxis_title="Change in household income",
    yaxis_tickprefix="£",
    xaxis_title="Age",
    showlegend= False,
))
    </code>
  </pre>
</div>

<script>
function show_code_13() {
  var x = document.getElementById("code_block_13");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_13_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_13_1.html");
    });
  </script>
</div>
<div id = "graph_graph_13_1"></div>


<button onclick="show_code_14()">Click to show code</button>
<div id="code_block_14" style="display: none;">
  <pre>
    <code>
#Poverty reductions

#Child poverty reduction
poor_kids_before = sim.calc("in_poverty_bhc", map_to="person")[sim.calc("is_child")].sum()
poor_kids_after = sim_BI.calc("in_poverty_bhc", map_to="person")[sim_BI.calc("is_child")].sum()
child_pov_reduction = ((poor_kids_before - poor_kids_after)/poor_kids_before) * 100

#Percentage of poverty reduction for adults only
poor_adults_before = sim.calc("in_poverty_bhc", map_to="person")[sim.calc("is_adult")].sum()
poor_adults_after = sim_BI.calc("in_poverty_bhc", map_to="person")[sim_BI.calc("is_adult")].sum()
adult_pov_reduction = ((poor_adults_before - poor_adults_after)/poor_adults_before) * 100

#Overall
poverty_difference = sim_BI.calc("in_poverty_bhc", map_to="person").sum() - sim.calc("in_poverty_bhc", map_to="person").sum()
overall_reduction = (poverty_difference/sim.calc("in_poverty_bhc", map_to="person").sum()) * -100

chart5 = format_fig(px.bar(x=["Children", "Adults", "Overall"], y=[-child_pov_reduction, -adult_pov_reduction, -overall_reduction]).update_layout(
    title_text='Poverty changes by age group',
    yaxis_title="Reduction in poverty",
    xaxis_title="Age group",
    yaxis_ticksuffix="%"
))
    </code>
  </pre>
</div>

<script>
function show_code_14() {
  var x = document.getElementById("code_block_14");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_14_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_14_1.html");
    });
  </script>
</div>
<div id = "graph_graph_14_1"></div>


<button onclick="show_code_15()">Click to show code</button>
<div id="code_block_15" style="display: none;">
  <pre>
    <code>
#Mean income difference grouped by family type
person_income_diff = sim_BI.calc("net_income") - sim.calc("net_income")
family = sim.calc("family_type", map_to = "person")

income_diff_by_family = person_income_diff.groupby(family).mean()

chart6 = format_fig(px.bar(x=["Couple without children", "Couple with children", "Single parent", "Single individual"], y=income_diff_by_family).update_layout(
    title_text='Mean income difference grouped by family type',
    yaxis_title="Change in income",
    xaxis_title="Family type",
    yaxis_tickprefix="£"
))
    </code>
  </pre>
</div>

<script>
function show_code_15() {
  var x = document.getElementById("code_block_15");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_15_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_15_1.html");
    });
  </script>
</div>
<div id = "graph_graph_15_1"></div>

Lastly, the following graph shows that funding UBI through an only partial decrease in personal allowance reduces the aforementioned effects on poverty. Each £2,000 of personal allowance reduced buys around a 5% decrease in poverty, meaning each £2,000 of personal allowance preserved decreases the poverty effect by 5 percentage points. 

This shows that the optimal policy to reduce poverty implies not reduction but full elimination of the personal allowance in favor of funding UBI, since there is a linear relationship between the two.

<button onclick="show_code_17()">Click to show code</button>
<div id="code_block_17" style="display: none;">
  <pre>
    <code>
def find_poverty_diff(sim_BI):
    poverty_difference = sim.calc("in_poverty_bhc", map_to="person").sum() - sim_BI.calc("in_poverty_bhc", map_to="person").sum()
    percentage_difference = (poverty_difference/sim.calc("in_poverty_bhc", map_to="person").sum()) * 100
    return -percentage_difference

PA_amounts = [12500, 11500, 10500, 9500, 8500, 7500, 6500, 5500, 4500, 3500, 2500, 1500, 500, 0]
pov_diffs = [find_poverty_diff(make_PA_reform(i)) for i in (PA_amounts)]

chart7 = format_fig(px.line(x=PA_amounts, y=pov_diffs).update_layout(
    title_text='Effect of UBI on poverty at different levels of personal allowance reduction',
    xaxis_title ="Amount of personal allowance (£)",
    yaxis_title ="Poverty change",
    yaxis_ticksuffix="%"
))
    </code>
  </pre>
</div>

<script>
function show_code_17() {
  var x = document.getElementById("code_block_17");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_17_1").load("{{site.baseurl}}assets/images/personal-allowance/graph_17_1.html");
    });
  </script>
</div>
<div id = "graph_graph_17_1"></div>

#### Conclusion
This analysis shows that replacing personal allowance with UBI is a far more effective mechanism for cutting poverty than maintaining or increasing it. Thus, continued existence of the personal allowance is suboptimal as an antipoverty policy, and in the Liberal Democrats’ explored UBI policies, eliminating it fully could reduce poverty by over an additional 5%. 

Furthermore, a disproportionate amount of this benefit would go to children. Since child poverty has well-documented impacts on educational and health outcomes (see [here](https://www.jrf.org.uk/sites/default/files/jrf/migrated/files/2123.pdf) and [here](https://adc.bmj.com/content/archdischild/101/8/759.full.pdf)), this has the potential to be a high-impact policy for society as a whole.

Hence, UBI proponents in the UK should take a serious look at whether keeping the personal allowance is worthwhile, given the potential benefits of the UBI amount that could be funded through taxing it.