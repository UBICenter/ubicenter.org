---
layout: post
current: post
cover: assets/images/2021-06-05-libdem-ubi-analysis.jpg
navigation: True
title: "Liberal Democrat UBI Policy Paper: An Analysis"
date: 2021-06-06
tags: [uk]
subclass: 'post'
author: nikhil
excerpt: "The UK party is exploring UBI reforms that would reduce poverty and inequality."
class: post-template
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

Last month, the Liberal Democrat UBI Working Group published a [policy paper](https://d3n8a8pro7vhmx.cloudfront.net/libdems/pages/1811/attachments/original/1621669347/145_-_Universal_Basic_Income.docx_%281%29.pdf?1621669347) exploring possible universal basic income policies for the party’s platform.[^1] This release follows the [September Liberal Democrat Conference vote](https://www.libdems.org.uk/a20-ubi) to campaign for universal basic income in future elections. The working group invites comments on the paper until tomorrow, 7th June.

In this post, I assess the four UBI reforms described in the paper, which are partly offset by tax and benefit reforms.[^2] I find that each would reduce poverty by at least a sixth and deep poverty by half, while benefiting 7 in 10 Britons, though they would also add at least £20 billion to the annual deficit.

## Policy outlines

The details of the four reforms are shown in the table below. The reforms are mainly funded by tax changes, and recover additional costs through the benefit system. See Appendix A for more details and a comparison to estimates in the Liberal Democrat discussion paper.

[^1]: The findings from the Working Group’s paper were presented by Paul Noblet, the chair, in the [recorded Social Liberal Forum event](https://www.socialliberal.net/what_kind_of_ubi_recording) What Kind of UBI?, in which Jane Dodds (Leader of the Liberal Democrats in Wales), Christine Jardine (Liberal Democrat MP for Edinburgh West) and Max Ghenis (Founder of the UBI Center) gave first responses to the proposals. 

[^2]: Modeling was carried out using the open-sourced static microsimulation model [OpenFisca-UK](https://github.com/PSLmodels/openfisca-uk). The code to reproduce all figures and findings is available on [GitHub](https://github.com/ubicenter/libdem-ubi-analysis).

<button onclick="show_code_structured_mobile()">Click to show code</button>
<div id="code_block_structured_mobile" style="display: none;">
  <pre>
    <code>
import pandas as pd

table = pd.DataFrame(
    {
        "UBI amount (£/week)": [45, 60, 75, 90],
        "Personal Allowance (£/year)": [4000, 2500, 2500, 2500],
        "NI Primary Threshold (£/week)": [90, 50, 50, 50],
        "Eligible groups": ["Working-age adults"] * 4,
        "UBI in benefit means tests": ["Included"] * 4,
    }
).set_index("UBI amount (£/week)")
table
    </code>
  </pre>
</div>

<script>
function show_code_structured_mobile() {
  var x = document.getElementById("code_block_structured_mobile");
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
      $("#graph_graph_structured_mobile_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_structured_mobile_1.html");
    });
  </script>
</div>
<div id = "graph_graph_structured_mobile_1"></div>

### Tax changes

The Liberal Democrat UBI Working Group proposes two tax changes to fund the UBI expenditure: reducing the Personal Allowance (for working-age adults only) and reducing the National Insurance Primary Threshold.

The Personal Allowance is a disregard for general income available to every individual with respect to Income Tax. In 2020, it had the value of £12,500 a year. For example, for an individual earning £22,500 a year, the Personal Allowance is deducted from taxable income to arrive at £10,000, which is taxed at the basic rate of 20%, resulting in a tax charge of £2,000. Reducing the Personal Allowance to £2,500 leaves the individual with £20,000 taxable income, resulting in a £4,000 Income Tax charge. The Working Group proposes lowering the Personal Allowance to £4,000 for the UBI of £45/week, and to £2,500 for the UBIs of £60, £75, and £90 per week.[^3]

National Insurance (NI) is a tax paid on employment earnings, comprising both employee and employer contributions. The Working Group proposes increasing employee NI contributions by reducing the Primary Threshold (PT). The threshold is currently set at £184/week: earnings under this are not taxed, earnings above this but under the Upper Earnings Limit (UEL, currently £967/week) are taxed at 12%, and earnings over the UEL are taxed at 2%.  The Working Group proposes reducing the PT to £90/week for the UBI of £45/week and to £50 for the larger UBI reforms.

[^3]: The higher allowance and threshold in the first reform increases the net cost by around £8bn.

### UBI and benefit changes

The Working Group proposes providing the basic income to working-age adults: individuals aged between 18 (inclusive) and the State Pension age (exclusive). This takes the form of a weekly payment in the amounts detailed below. The policies would not change existing benefit programs; however, UBI payments would be treated as earnings when existing benefits are means-tested. For example, if a person receives £70/week from Universal Credit and then is paid £60/week in UBI, their Universal Credit payment would be reduced at the 63% taper (assuming work allowances, set amounts of income disregarded by means tests, are exhausted) to arrive at £32.20 (which, combined with the £60 UBI, results in £93.20 - an increase of 33%).
### Funding breakdown

Across reforms, the Personal Allowance reduction accounts for about two-thirds of the revenue, with the National Insurance threshold reduction accounting for a bit more than half of the remaining third. 

<button onclick="show_code_funky_portland()">Click to show code</button>
<div id="code_block_funky_portland" style="display: none;">
  <pre>
    <code>
from ubicenter import format_fig
from openfisca_uk import Microsimulation
from reform import (
    WA_adult_UBI,
    include_UBI_in_means_tests,
    set_PA,
    set_PA_for_WA_adults,
    set_PT,
    net_cost,
)
import numpy as np
import pandas as pd
from tqdm import trange, tqdm
import plotly.express as px

baseline = Microsimulation(year=2020)
funding = (
    set_PA_for_WA_adults(2500),
    set_PT(50),
    include_UBI_in_means_tests(),
)
ubi_45 = (
    WA_adult_UBI(45 * 52),
    set_PA_for_WA_adults(4000),
    set_PT(90),
    include_UBI_in_means_tests(),
)
ubi_60 = (WA_adult_UBI(60 * 52), *funding)
ubi_75 = (WA_adult_UBI(75 * 52), *funding)
ubi_95 = (WA_adult_UBI(95 * 52), *funding)

breakdowns = []
for reform, name in zip((ubi_45, ubi_60, ubi_75, ubi_95), (45, 60, 75, 95)):
    net_costs = []
    component_names = [
        "UBI",
        "Lower PA",
        "Lower PT",
        "Reduced benefits",
        "Remaining",
    ]
    for i in range(len(reform) + 1):
        net_costs += [
            net_cost(baseline, Microsimulation(reform[:i], year=2020))
        ]
    net_costs = np.array(net_costs)

    resulting_costs = pd.Series(net_costs[1:] - net_costs[:-1])
    resulting_costs = pd.Series(list(resulting_costs) + [net_costs[-1]])
    breakdown = pd.DataFrame(
        dict(
            UBI=f"£{name}/week",
            component=component_names * 2,
            amount=[0]
            + list(resulting_costs.cumsum()[1:-1])
            + [0]
            + list(np.abs(resulting_costs)),
            Type=["Unaffected"] * 5
            + ["Spending"]
            + ["Revenue"] * 3
            + ["Spending"],
        )
    )
    breakdowns += [breakdown]

fig = format_fig(
    px.bar(
        pd.concat(breakdowns),
        x="component",
        y="amount",
        color="Type",
        animation_frame="UBI",
        barmode="stack",
        color_discrete_sequence=["white", "#1976D2", "#BDBDBD"],
    ).update_layout(
        title="Funding breakdown by reform",
        xaxis_title="Component",
        yaxis_title="Amount",
        yaxis_tickprefix="£",
        yaxis_range=[0, 210e9],
    )
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_funky_portland() {
  var x = document.getElementById("code_block_funky_portland");
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
      $("#graph_graph_funky_portland_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_funky_portland_1.html");
    });
  </script>
</div>
<div id = "graph_graph_funky_portland_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_funky_portland_2").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_funky_portland_2.html");
    });
  </script>
</div>
<div id = "graph_graph_funky_portland_2"></div>

## Reform effects

All four of the reforms reduce poverty and inequality, and leave most better off. Their net costs range from £22bn  for the £45 UBI (about the cost of Housing Benefit) to £101bn for the £90 UBI (about the cost of State Pension). The below table shows the effects on the budget, as well as to poverty (absolute before housing costs), deep poverty (defined at half the poverty line) and inequality (measured by the Gini coefficient of disposable income).

<button onclick="show_code_verbal_tonight()">Click to show code</button>
<div id="code_block_verbal_tonight" style="display: none;">
  <pre>
    <code>
from openfisca_uk.api import *


def get_results(reform: Reform):
    sim = Microsimulation(reform, year=2020)
    cost = net_cost(baseline, sim)
    ubi_cost = sim.calc("UBI").sum()
    reform_tax_revenue = sim.calc("tax").sum() - baseline.calc("tax").sum()
    benefit_revenue = ubi_cost - reform_tax_revenue - cost
    baseline_poverty = baseline.calc("in_poverty_bhc", map_to="person").mean()
    baseline_deep_poverty = baseline.calc(
        "in_deep_poverty_bhc", map_to="person"
    ).mean()
    poverty_change = (
        sim.calc("in_poverty_bhc", map_to="person").mean() - baseline_poverty
    ) / baseline_poverty
    deep_poverty_change = (
        sim.calc("in_deep_poverty_bhc", map_to="person").mean()
        - baseline_deep_poverty
    ) / baseline_deep_poverty
    baseline_gini = baseline.calc(
        "household_net_income", map_to="person"
    ).gini()
    inequality_change = (
        sim.calc("household_net_income", map_to="person").gini()
        - baseline_gini
    ) / baseline_gini
    baseline_income = baseline.calc("household_net_income", map_to="person")
    gain = sim.calc("household_net_income", map_to="person") - baseline_income
    percent_winners = (gain > 0).mean()
    percent_losers = (gain < 0).mean()
    return (
        sim,
        cost,
        poverty_change,
        deep_poverty_change,
        inequality_change,
        percent_winners,
        percent_losers,
        ubi_cost,
        benefit_revenue,
        reform_tax_revenue,
    )


reforms = (ubi_45, ubi_60, ubi_75, ubi_95)
names = ("£45", "£60", "£75", "£95")
results = list(map(get_results, reforms))
(
    sims,
    costs,
    poverty_changes,
    deep_poverty_changes,
    inequality_changes,
    percent_winners,
    percent_losers,
    ubi_cost,
    benefit_revenue,
    reform_tax_revenue,
) = list(zip(*results))
LD_lower = (13, 22, 48, 84)
LD_upper = (18, 28, 56, 93)
table = pd.DataFrame(
    {
        "UBI (£/week)": names,
        "Net cost (£bn)": pd.Series(costs).apply(lambda x: round(x / 1e9, 1)),
        "Poverty change (%)": pd.Series(poverty_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Deep poverty change (%)": pd.Series(deep_poverty_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Inequality change (%)": pd.Series(inequality_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Winners (%)": pd.Series(percent_winners).apply(
            lambda x: round(x * 100, 1)
        ),
        "Losers (%)": pd.Series(percent_losers).apply(
            lambda x: round(x * 100, 1)
        ),
    }
).set_index("UBI (£/week)")
table
    </code>
  </pre>
</div>

<script>
function show_code_verbal_tonight() {
  var x = document.getElementById("code_block_verbal_tonight");
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
      $("#graph_graph_verbal_tonight_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_verbal_tonight_1.html");
    });
  </script>
</div>
<div id = "graph_graph_verbal_tonight_1"></div>

### Distributional effects

#### Inter-decile effects

The above effects only show the picture on the population as a whole. Below shows the average gain to members of the population by their household's equivalised disposable income. With deficit funding, the plans are able to show positive impacts on average for every decile in every reform; budget-neutral plans would have result in some deciles coming out behind on average.

<button onclick="show_code_private_princeton()">Click to show code</button>
<div id="code_block_private_princeton" style="display: none;">
  <pre>
    <code>
import plotly.graph_objects as go
from ubicenter import format_fig

fig = go.Figure()

income = baseline.calc("equiv_household_net_income", map_to="person")

LIGHTER_BLUE = "#ABCEEB"  # Blue 100.
LIGHT_BLUE = "#49A6E2"  # Blue 700.
BLUE = "#1976D2"  # Blue 700.
DARK_BLUE = "#0F4AA1"  # Blue 900.

BLUE_COLORS = [LIGHTER_BLUE, LIGHT_BLUE, BLUE, DARK_BLUE]

for sim, name, color in zip(sims, names, BLUE_COLORS):
    gain = sim.calc("household_net_income", map_to="person") - baseline.calc(
        "household_net_income", map_to="person"
    )
    result = gain.groupby(income.decile_rank()).mean()
    fig.add_trace(
        go.Bar(x=result.index, y=result.values, name=name, marker_color=color)
    )

fig = format_fig(
    fig.update_layout(
        title="Change to net income by decile",
        xaxis_tickvals=list(range(1, 11)),
        xaxis_title="Equivalised disposable income decile",
        yaxis_title="Change to annual net income per year",
        yaxis_tickprefix="£",
    )
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_private_princeton() {
  var x = document.getElementById("code_block_private_princeton");
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
      $("#graph_graph_private_princeton_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_private_princeton_1.html");
    });
  </script>
</div>
<div id = "graph_graph_private_princeton_1"></div>

Relative effects are stronger on the lower deciles, with higher amounts of UBI creating particularly strong increases in disposable income for the bottom decile.

<button onclick="show_code_transparent_proxy()">Click to show code</button>
<div id="code_block_transparent_proxy" style="display: none;">
  <pre>
    <code>
fig = go.Figure()

income = baseline.calc("equiv_household_net_income", map_to="person")

LIGHTER_BLUE = "#ABCEEB"  # Blue 100.
LIGHT_BLUE = "#49A6E2"  # Blue 700.
BLUE = "#1976D2"  # Blue 700.
DARK_BLUE = "#0F4AA1"  # Blue 900.

BLUE_COLORS = [LIGHTER_BLUE, LIGHT_BLUE, BLUE, DARK_BLUE]

for sim, name, color in zip(sims, names, BLUE_COLORS):
    gain = sim.calc("household_net_income", map_to="person") - baseline.calc(
        "household_net_income", map_to="person"
    )
    decile_agg_income_baseline = (
        income[income > 0].groupby(income.decile_rank()).sum()
    )
    rel_gain = (
        gain[income > 0].groupby(income.decile_rank()).sum()
        / decile_agg_income_baseline
    )
    fig.add_trace(
        go.Bar(
            x=rel_gain.index, y=rel_gain.values, name=name, marker_color=color
        )
    )

fig = format_fig(
    fig.update_layout(
        title="Relative change to net income by income decile",
        xaxis_tickvals=list(range(1, 11)),
        xaxis_title="Equivalised disposable income decile",
        yaxis_title="Relative change per year",
        yaxis_tickformat="%",
    )
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_transparent_proxy() {
  var x = document.getElementById("code_block_transparent_proxy");
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
      $("#graph_graph_transparent_proxy_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_transparent_proxy_1.html");
    });
  </script>
</div>
<div id = "graph_graph_transparent_proxy_1"></div>

#### Intra-decile effects

While the share of people gaining from the reforms is relatively similar across income groups, people in low-income households are more likely to see substantial gains and less likely to see net losses. Even with the £45 UBI, only about a third of the top three deciles lose income; this follows from the tax and benefit changes mostly affecting lower income sections, as well as people earning over £125,000 being currently ineligible for the Personal Allowance, and therefore unaffected by its reduction.

<button onclick="show_code_computational_indie()">Click to show code</button>
<div id="code_block_computational_indie" style="display: none;">
  <pre>
    <code>
import plotly.express as px
from charts import intra_decile_graph_data

intra = intra_decile_graph_data(baseline, *sims)

GREY = "#BDBDBD"

COLORS = ("#616161", GREY, "#F5F5F5", "#C5E1A5", "#558B2F",)[::-1]

fig = format_fig(
    px.bar(
        intra,
        x="fraction",
        y="decile",
        orientation="h",
        color="Outcome",
        animation_frame="UBI",
        color_discrete_sequence=COLORS,
    ).update_layout(
        yaxis_tickvals=list(range(1, 11)),
        xaxis_tickformat="%",
        yaxis_title="Income decile",
        xaxis_title="Outcome distributions",
        title="Intra-decile outcomes",
    )
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_computational_indie() {
  var x = document.getElementById("code_block_computational_indie");
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
      $("#graph_graph_computational_indie_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_computational_indie_1.html");
    });
  </script>
</div>
<div id = "graph_graph_computational_indie_1"></div>

## Individual effects

The above results show the impact on the population as it stands, but not the theoretical effects on household budgets. An individual living alone and who will claim Universal Credit sees their disposable income increased by the £45/week UBI reform at earnings under £30,000 and over £70,000 (see Appendix B for this analysis of other household types).

<button onclick="show_code_outside_garden()">Click to show code</button>
<div id="code_block_outside_garden" style="display: none;">
  <pre>
    <code>
from openfisca_uk import IndividualSim
from ubicenter import format_fig

individual_colors = [GREY, BLUE]


def plot_budget(household_config, title):
    baseline_policy = IndividualSim()
    household_config(baseline_policy)
    baseline_policy.vary("employment_income")
    employment_income = baseline_policy.calc("employment_income")[0]
    budget_dfs = []
    for reform, name in zip(
        (ubi_45, ubi_60, ubi_75, ubi_95), (45, 60, 75, 95)
    ):
        ubi_policy = IndividualSim(reform)
        household_config(ubi_policy)
        ubi_policy.vary("employment_income")
        df = pd.DataFrame(
            {
                "Net income (Baseline)": baseline_policy.calc(
                    "household_net_income"
                )[0],
                "Net income (Reform)": ubi_policy.calc("household_net_income")[
                    0
                ],
                "Tax (Baseline)": baseline_policy.calc("tax")[0],
                "Tax (Reform)": ubi_policy.calc("tax")[0],
                "Benefits (Baseline)": baseline_policy.calc("benefits")[0],
                "Benefits (Reform)": ubi_policy.calc("benefits")[0],
                "UBI (Reform)": ubi_policy.calc("UBI")[0],
                "Employment income": employment_income,
                "MTR (Baseline)": 1
                - baseline_policy.calc_deriv(
                    "household_net_income",
                    var_target="household",
                    wrt_target="adult",
                ),
                "MTR (Reform)": 1
                - ubi_policy.calc_deriv(
                    "household_net_income",
                    var_target="household",
                    wrt_target="adult",
                ),
                "Tax MTR (Baseline)": baseline_policy.calc_deriv(
                    "tax", var_target="adult", wrt_target="adult"
                ),
                "Tax MTR (Reform)": ubi_policy.calc_deriv(
                    "tax", var_target="adult", wrt_target="adult"
                ),
                "Income Tax MTR (Baseline)": baseline_policy.calc_deriv(
                    "income_tax", var_target="adult", wrt_target="adult"
                ),
                "Income Tax MTR (Reform)": ubi_policy.calc_deriv(
                    "income_tax", var_target="adult", wrt_target="adult"
                ),
                "NI MTR (Baseline)": baseline_policy.calc_deriv(
                    "national_insurance",
                    var_target="adult",
                    wrt_target="adult",
                ),
                "NI MTR (Reform)": ubi_policy.calc_deriv(
                    "national_insurance",
                    var_target="adult",
                    wrt_target="adult",
                ),
                "Benefit MTR (Baseline)": -baseline_policy.calc_deriv(
                    "benefits", var_target="adult", wrt_target="adult"
                ),
                "Benefit MTR (Reform)": -ubi_policy.calc_deriv(
                    "benefits", var_target="adult", wrt_target="adult"
                ),
            }
        )
        df["UBI"] = f"£{name}/week"
        budget_dfs += [df]

    fig = px.line(
        pd.concat(budget_dfs),
        x="Employment income",
        y=[
            "Net income (Baseline)",
            "Net income (Reform)",
            "Tax (Baseline)",
            "Tax (Reform)",
            "Benefits (Baseline)",
            "Benefits (Reform)",
            "UBI (Reform)",
        ],
        animation_frame="UBI",
        color_discrete_sequence=individual_colors,
    ).update_layout(
        title=title,
        yaxis_tickprefix="£",
        xaxis_tickprefix="£",
        yaxis_title="Yearly amount",
        xaxis_title="Employment income",
        legend_title_text="",
    )
    hidden = [False] * 2 + [True] * 5
    for i in range(7):
        if hidden[i]:
            fig.data[i].visible = "legendonly"

    return format_fig(fig), pd.concat(budget_dfs)


def single_person_UC(sim):
    sim.add_person(age=26, is_benunit_head=True, name="adult"),
    sim.add_benunit(adults=["adult"], claims_UC=True),
    sim.add_household(adults=["adult"])


fig, budget_df = plot_budget(
    single_person_UC,
    "Effect of UBI reforms on the relationship between employment income and net income",
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_outside_garden() {
  var x = document.getElementById("code_block_outside_garden");
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
      $("#graph_graph_outside_garden_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_outside_garden_1.html");
    });
  </script>
</div>
<div id = "graph_graph_outside_garden_1"></div>

The reforms also affect marginal tax rates: the PA decrease imposes the basic, higher and additional rates on taxpayers with lower incomes, the UBI amounts effectively reduce the benefit work disregards, and the PT decrease applies the 12% rate onto lower-income earners.

<button onclick="show_code_nuclear_response()">Click to show code</button>
<div id="code_block_nuclear_response" style="display: none;">
  <pre>
    <code>
mtr_graph = px.line(
    budget_df[::5],
    x="Employment income",
    y=[
        "MTR (Baseline)",
        "MTR (Reform)",
        "Tax MTR (Baseline)",
        "Tax MTR (Reform)",
        "Income Tax MTR (Baseline)",
        "Income Tax MTR (Reform)",
        "NI MTR (Baseline)",
        "NI MTR (Reform)",
        "Benefit MTR (Baseline)",
        "Benefit MTR (Reform)",
    ],
    animation_frame="UBI",
    color_discrete_sequence=individual_colors,
).update_layout(
    title="Effect of UBI reforms on marginal tax rates",
    yaxis_tickformat="%",
    xaxis_tickprefix="£",
    yaxis_title="Yearly amount",
    xaxis_title="Employment income",
    legend_title_text="",
)
hidden = [False] * 2 + [True] * 8
for i in range(10):
    if hidden[i]:
        mtr_graph.data[i].visible = "legendonly"

fig = format_fig(mtr_graph)
fig
    </code>
  </pre>
</div>

<script>
function show_code_nuclear_response() {
  var x = document.getElementById("code_block_nuclear_response");
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
      $("#graph_graph_nuclear_response_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_nuclear_response_1.html");
    });
  </script>
</div>
<div id = "graph_graph_nuclear_response_1"></div>

Few political parties around the world have endorsed UBI as the Liberal Democrats have, and in releasing this discussion paper with specific policies, they have taken that endorsement to an unprecedented level of seriousness. While these policies don’t achieve full budget-neutrality, the discussion paper also mentions other revenue options, such as raising NI rates and tax rates on corporations, capital gains, and personal income. And while they don't achieve the progressivity of [more dramatic reforms](({% post_url 2021-05-12-uk-blank-slate-ubi %})), they would nonetheless reduce poverty and inequality more than any policy perhaps since the dawn of the NHS. The party’s final proposal will represent yet another unprecedented step in the UK’s embrace of UBI, and we look forward to reviewing it.

*Update: [Read our follow-up]({% post_url 2021-06-07-progressive-adjustments-lib-dem-working-group %}) describing progressive adjustments that could be made to this framework.*


### Appendix A: Costing estimates

The Working Group used different modelling methods than were used in this analysis, resulting in our analysis producing higher net costs than the Working Group found. This is primarily due to the fact that this analysis used a household simulation method, rather than administrative data from HMRC. This allows for finer levels of detail and distributional analysis, but high incomes and benefit receipts are under-reported, causing an underestimate of the revenue raised by the tax reforms. The Working Group also assumed full Universal Credit take-up, whereas this analysis considers legacy benefits reported in the Family Resources Survey. The details are shown in the table below.

<button onclick="show_code_former_notion()">Click to show code</button>
<div id="code_block_former_notion" style="display: none;">
  <pre>
    <code>
LD_lower = (13, 22, 48, 84)
LD_upper = (18, 28, 56, 93)
table = pd.DataFrame(
    {
        "UBI (£/week)": names,
        "LD net cost (£bn)": [
            f"{low}-{high}" for low, high in zip(LD_lower, LD_upper)
        ],
        "Simulated net cost (£bn)": pd.Series(costs).apply(
            lambda x: round(x / 1e9, 1)
        ),
        "UBI cost": pd.Series(ubi_cost).apply(lambda x: round(x / 1e9, 1)),
        "Tax revenue": pd.Series(reform_tax_revenue).apply(
            lambda x: round(x / 1e9, 1)
        ),
        "Reduced benefits": pd.Series(benefit_revenue).apply(
            lambda x: round(x / 1e9, 1)
        ),
        "Difference from central estimate (£bn)": [
            round((c - (low + high) / 2 * 1e9) / 1e9, 1)
            for c, low, high in zip(costs, LD_lower, LD_upper)
        ],
    }
).set_index("UBI (£/week)")
table
    </code>
  </pre>
</div>

<script>
function show_code_former_notion() {
  var x = document.getElementById("code_block_former_notion");
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
      $("#graph_graph_former_notion_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_former_notion_1.html");
    });
  </script>
</div>
<div id = "graph_graph_former_notion_1"></div>

Thanks to Kevin Langford, who provided more details on the policy proposal by the Working Group not present in the discussion paper, and on the modelling approaches that produced the cost estimates. Some of the mechanics of this type of scheme are set out in Langfords paper, [<i>Money for Nothing?</i>](https://radixuk.org/papers/money-for-nothing/), published in May 2021 with Radix.

### Appendix B: Relationships between employment and net income for other household types

Below is a selection of the theoretical effects on different household types.

<button onclick="show_code_internal_warning()">Click to show code</button>
<div id="code_block_internal_warning" style="display: none;">
  <pre>
    <code>
def couple_UC(sim):
    sim.add_person(age=26, is_benunit_head=True, name="adult"),
    sim.add_person(age=27, is_benunit_head=False, name="adult2"),
    sim.add_benunit(adults=["adult", "adult2"], claims_UC=True),
    sim.add_household(adults=["adult", "adult2"])


fig, budget_df = plot_budget(couple_UC, "Couple on Universal Credit")
fig
    </code>
  </pre>
</div>

<script>
function show_code_internal_warning() {
  var x = document.getElementById("code_block_internal_warning");
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
      $("#graph_graph_internal_warning_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_internal_warning_1.html");
    });
  </script>
</div>
<div id = "graph_graph_internal_warning_1"></div>


<button onclick="show_code_settled_authentication()">Click to show code</button>
<div id="code_block_settled_authentication" style="display: none;">
  <pre>
    <code>
mtr_graph = px.line(
    budget_df[::5],
    x="Employment income",
    y=[
        "MTR (Baseline)",
        "MTR (Reform)",
        "Tax MTR (Baseline)",
        "Tax MTR (Reform)",
        "Income Tax MTR (Baseline)",
        "Income Tax MTR (Reform)",
        "NI MTR (Baseline)",
        "NI MTR (Reform)",
        "Benefit MTR (Baseline)",
        "Benefit MTR (Reform)",
    ],
    animation_frame="UBI",
    color_discrete_sequence=individual_colors,
).update_layout(
    title="Effect of UBI reforms on marginal tax rates (Couple, UC)",
    yaxis_tickformat="%",
    xaxis_tickprefix="£",
    yaxis_title="Yearly amount",
    xaxis_title="Employment income",
    legend_title_text="",
)
hidden = [False] * 2 + [True] * 8
for i in range(10):
    if hidden[i]:
        mtr_graph.data[i].visible = "legendonly"

fig = format_fig(mtr_graph)
fig
    </code>
  </pre>
</div>

<script>
function show_code_settled_authentication() {
  var x = document.getElementById("code_block_settled_authentication");
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
      $("#graph_graph_settled_authentication_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_settled_authentication_1.html");
    });
  </script>
</div>
<div id = "graph_graph_settled_authentication_1"></div>


<button onclick="show_code_welsh_seating()">Click to show code</button>
<div id="code_block_welsh_seating" style="display: none;">
  <pre>
    <code>
def couple_children_UC(sim):
    sim.add_person(age=26, is_benunit_head=True, name="adult"),
    sim.add_person(age=27, name="adult2"),
    sim.add_person(age=3, name="child"),
    sim.add_person(age=4, name="child2"),
    sim.add_benunit(
        adults=["adult", "adult2"],
        children=["child", "child2"],
        claims_UC=True,
        claims_child_benefit=True,
    )
    sim.add_household(adults=["adult", "adult2"], children=["child", "child2"])


fig, budget_df = plot_budget(
    couple_children_UC, "Couple with two children on Universal Credit"
)
fig
    </code>
  </pre>
</div>

<script>
function show_code_welsh_seating() {
  var x = document.getElementById("code_block_welsh_seating");
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
      $("#graph_graph_welsh_seating_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_welsh_seating_1.html");
    });
  </script>
</div>
<div id = "graph_graph_welsh_seating_1"></div>


<button onclick="show_code_buried_grounds()">Click to show code</button>
<div id="code_block_buried_grounds" style="display: none;">
  <pre>
    <code>
mtr_graph = px.line(
    budget_df[::5],
    x="Employment income",
    y=[
        "MTR (Baseline)",
        "MTR (Reform)",
        "Tax MTR (Baseline)",
        "Tax MTR (Reform)",
        "Income Tax MTR (Baseline)",
        "Income Tax MTR (Reform)",
        "NI MTR (Baseline)",
        "NI MTR (Reform)",
        "Benefit MTR (Baseline)",
        "Benefit MTR (Reform)",
    ],
    animation_frame="UBI",
    color_discrete_sequence=individual_colors,
).update_layout(
    title="Effect of UBI reforms on marginal tax rates (Couple, two children, UC)",
    yaxis_tickformat="%",
    xaxis_tickprefix="£",
    yaxis_title="Yearly amount",
    xaxis_title="Employment income",
    legend_title_text="",
)
hidden = [False] * 2 + [True] * 8
for i in range(10):
    if hidden[i]:
        mtr_graph.data[i].visible = "legendonly"

fig = format_fig(mtr_graph)
fig
    </code>
  </pre>
</div>

<script>
function show_code_buried_grounds() {
  var x = document.getElementById("code_block_buried_grounds");
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
      $("#graph_graph_buried_grounds_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_buried_grounds_1.html");
    });
  </script>
</div>
<div id = "graph_graph_buried_grounds_1"></div>
