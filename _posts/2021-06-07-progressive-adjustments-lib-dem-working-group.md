---
layout: post
current: post
cover: assets/images/2021-06-07-libdem-ubi-analysis2.jpg
navigation: True
title: Progressive adjustments to the Liberal Democrat UBI Working Group's reforms
date: 2021-06-07
tags: [uk,UK Liberal Democrats]
subclass: 'post'
author: [max,nikhil]
excerpt: More generous and inclusive basic income plans would reduce poverty and inequality more, and benefit more people.
class: post-template
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

Yesterday, we published an [analysis]({% post_url 2021-06-06-lib-dem-policy-paper %}) of universal basic income reforms described in the Liberal Democrat UBI Working Group's [discussion paper](https://d3n8a8pro7vhmx.cloudfront.net/libdems/pages/1811/attachments/original/1621669347/145_-_Universal_Basic_Income.docx_%281%29.pdf?1621669347). In the working group's words, their paper "is designed to stimulate debate and discussion within the Party and outside; based on the response generated and on the deliberations of the working group a full policy paper will be drawn up and presented to Conference for debate."

In this follow-up, we model a budget-neutral version of the reforms put forth in the working group paper, as well as a variety of (also budget-neutral) adjustments to those reforms. While the working group's reform would reduce poverty and inequality, we find that these adjustments, which make the UBIs more generous and inclusive, would augment their effects substantially.

## The working group's UBI reform

The working group paper suggested a range of UBI amounts: 45, 60, 75, and 95 pounds per week for working-age adults. The cost was partly offset by lowering the annual Personal Allowance (for working-age adults) from £12,500 to £2,500 and the weekly National Insurance Primary Threshold from £184 to £50;[^1] these both reduce the amount of earnings one can receive before being taxed. The reform also treated the UBI as earned income for the purposes of means-tested benefits.

The result was progressive: poverty would fall by at least 17 percent, deep poverty (the population share with income below half the poverty threshold) by at least 50 percent, and inequality (as measured by the [Gini index](https://en.wikipedia.org/wiki/Gini_coefficient)) by at least 2.8 percent. However, even the least generous of the four UBI policies added over £20 billion to the deficit.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_verbal_tonight_1").load("{{site.baseurl}}assets/markdown_assets/libdem-ubi-analysis/graph_verbal_tonight_1.html");
    });
  </script>
</div>
<div id = "graph_graph_verbal_tonight_1"></div>

If made budget-neutral, this structure of pay-fors will fund a UBI of £42 per week. That policy would reduce poverty by 11%, deep poverty by 46%, and inequality by 2.4%, while leaving 39% of Britons better off and 47% worse off. For an apples-to-apples comparison, we consider this the baseline reform against which other adjustments are evaluated.

## Adjustments to the working group's UBI reform

We apply several modifications to the working group's UBI reform that broaden the tax base (funding larger UBIs), broaden the recipient base, and change how the UBI is treated. Specifically, we model:
- Including children in the UBI
- Repealing the Personal Allowance and National Insurance Primary Threshold entirely
- Including pensioners in both the Personal Allowance reduction and the UBI
- Exempting the UBI from means-testing

In addition to modeling each of these changes individually, we consider applying all four changes together.

[^1]: For the £45 per week UBI reform, the working group modeled lowering the Personal Allowance and Primary Threshold less than other reforms, to £4,000 and £50, respectively.

<button onclick="show_code_disciplinary_beginning()">Click to show code</button>
<div id="code_block_disciplinary_beginning" style="display: none;">
  <pre>
    <code>
from ubicenter import format_fig
from openfisca_uk import Microsimulation
import numpy as np
import pandas as pd
import plotly.express as px
from reform import (
    WA_adult_UBI,
    all_UBI,
    adult_UBI,
    non_pensioner_UBI,
    set_PA,
    set_PT,
    set_PA_for_WA_adults,
    include_UBI_in_means_tests,
    net_cost,
)

reform_df = pd.DataFrame(
    {
        "Adult PA (£/year)": [12500, 2500, 0, 2500, 2500, 2500, 0],
        "Pensioner PA (£/year)": [12500, 12500, 12500, 2500, 12500, 12500, 0],
        "NI Primary Threshold (£/week)": [183, 50, 0, 50, 50, 50, 0],
        "UBI for children": [False, False, False, False, True, False, True],
        "UBI for pensioners": [False, False, False, True, False, False, True],
        "UBI in means tests": [False, True, True, True, True, False, False],
    }
)

baseline = Microsimulation(year=2020)


def create_reform(params: dict):
    reform = []
    reform += [set_PA(float(params["Pensioner PA (£/year)"]))]
    reform += [set_PA_for_WA_adults(float(params["Adult PA (£/year)"]))]
    reform += [set_PT(float(params["NI Primary Threshold (£/week)"]))]
    tax_reform_sim = Microsimulation(*reform, year=2020)
    revenue = net_cost(tax_reform_sim, baseline)
    if params["UBI for children"]:  # doesn't handle non-adult UBIs
        if params["UBI for pensioners"]:
            ubi_reform_func = all_UBI
            population = baseline.calc("people").sum()
        else:
            ubi_reform_func = non_pensioner_UBI
            population = (
                baseline.calc("is_child").sum()
                + baseline.calc("is_WA_adult").sum()
            )
    else:
        if params["UBI for pensioners"]:
            ubi_reform_func = adult_UBI
            population = baseline.calc("is_adult").sum()
        else:
            ubi_reform_func = WA_adult_UBI
            population = baseline.calc("is_WA_adult").sum()
    if params["UBI in means tests"]:
        ubi_amount = int(revenue / population / 52) * 52
        net_revenue = -net_cost(
            baseline,
            Microsimulation(
                (
                    reform,
                    ubi_reform_func(ubi_amount),
                    include_UBI_in_means_tests(),
                ),
                year=2020,
            ),
        )
        prev_amounts = []
        while (
            net_revenue > 1e9 or net_revenue < -1e9
        ) and ubi_amount not in prev_amounts:
            old_ubi_amount = ubi_amount
            prev_amounts += [old_ubi_amount]
            ubi_amount += 1 * 52 * (2 * (net_revenue > 0) - 1)
            net_revenue = -net_cost(
                baseline,
                Microsimulation(
                    (
                        reform,
                        ubi_reform_func(ubi_amount),
                        include_UBI_in_means_tests(),
                    ),
                    year=2020,
                ),
            )
        reform += [ubi_reform_func(ubi_amount), include_UBI_in_means_tests()]
    else:
        ubi_amount = int(revenue / population / 52) * 52
        reform += [ubi_reform_func(ubi_amount)]
    return tuple(reform)


def rel(x, y):
    return (y - x) / x


UBI_amounts = []
poverty_changes = []
deep_poverty_changes = []
costs = []
winners = []
losers = []
gini_changes = []

from tqdm import trange

for i in range(len(reform_df)):
    reform = create_reform(reform_df.iloc[i])
    reform_sim = Microsimulation(reform, year=2020)
    UBI_amounts += [reform_sim.calc("UBI").max()]
    poverty_changes += [
        rel(
            baseline.calc("in_poverty_bhc", map_to="person").mean(),
            reform_sim.calc("in_poverty_bhc", map_to="person").mean(),
        )
    ]
    deep_poverty_changes += [
        rel(
            baseline.calc("in_deep_poverty_bhc", map_to="person").mean(),
            reform_sim.calc("in_deep_poverty_bhc", map_to="person").mean(),
        )
    ]
    gini_changes += [
        rel(
            baseline.calc("household_net_income", map_to="person").gini(),
            reform_sim.calc("household_net_income", map_to="person").gini(),
        )
    ]
    winners += [
        (
            reform_sim.calc("household_net_income", map_to="person")
            > baseline.calc("household_net_income", map_to="person") + 1
        ).mean()
    ]
    losers += [
        (
            reform_sim.calc("household_net_income", map_to="person")
            < baseline.calc("household_net_income", map_to="person") - 1
        ).mean()
    ]
    costs += [net_cost(baseline, reform_sim)]
    
results_df = pd.DataFrame(
    {
        "UBI amount (£/week)": (pd.Series(UBI_amounts) / 52).astype(int),
        "Poverty change (%)": pd.Series(poverty_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Deep poverty change (%)": pd.Series(deep_poverty_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Winners (%)": pd.Series(winners).apply(lambda x: round(x * 100, 1)),
        "Losers (%)": pd.Series(losers).apply(lambda x: round(x * 100, 1)),
        "Inequality change (%)": pd.Series(gini_changes).apply(
            lambda x: round(x * 100, 1)
        ),
        "Net cost (£bn/year)": pd.Series(costs).apply(
            lambda x: round(x / 1e9, 1)
        ),
    }
)

output = pd.concat([reform_df, results_df], axis=1)
output.index = [
    "Baseline",
    "Budget-neutral Working Group reform",
    "Full PA/PT elimination",
    "Include pensioners",
    "Include children",
    "Exclude from means tests",
    "All",
]
output

    </code>
  </pre>
</div>

<script>
function show_code_disciplinary_beginning() {
  var x = document.getElementById("code_block_disciplinary_beginning");
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
      $("#graph_graph_disciplinary_beginning_1").load("{{site.baseurl}}assets/markdown_assets/post/graph_disciplinary_beginning_1.html");
    });
  </script>
</div>
<div id = "graph_graph_disciplinary_beginning_1"></div>

Each of these adjustments produces more progressive outcomes. The most important adjustment for achieving more progressive outcomes is including children, which lowers the weekly amount from £42 to £32: of all the adjustments we considered, this most reduces poverty, inequality, and the population share that comes out behind. Fully eliminating the Personal Allowance and Primary Threshold, which would raise the weekly amount from £42 to £55, produces the greatest reduction in deep poverty.

The most progressive approach is implementing all the adjustments. Fully eliminating the Personal Allowance and Primary Threshold for all workers would fund a £36 weekly payment to each person, without counting as income toward means-tested programs. This would reduce poverty by 40%---3.6 times as much as the plan in the discussion paper. It would also reduce deep poverty 20% more than the discussion paper, and reduce inequality 130% more. Critically for political viability, it is the only approach that benefits the majority of individuals.

# Lessons align with other simulations

This exploration shows that larger UBIs---both in generosity and inclusivity---deliver greater progressivity. The UBI Center's US research findings mirror this lesson with respect to inclusivity:
- [Excluding non-citizens was the primary reason Andrew Yang's Freedom Dividend would leave some low-income people behind.]({% post_url 2019-06-28-why-some-low-income-people-come-out-behind-in-andrew-yangs-freedom-dividend %}) 
- [Including children in UBIs reduces poverty and inequality more.]({% post_url 2021-01-20-child-ubi-share %})
- [Including children and non-citizens makes for a more affordable Covid response.]({% post_url 2020-03-20-how-universal-basic-income-can-keep-poverty-from-rising-amid-covid19 %})
- [Universal transfers (especially including kids) reduce poverty and inequality more than extended unemployment benefits, which reach only a small share of the population.](https://covid.ubicenter.org/fpuc)
- [UBI is more progressive than student debt forgiveness, which is similarly exclusively targeted.]({% post_url 2020-11-17-student-debt %})

Our research on [flat income taxes]({% post_url 2020-12-30-us-flat-tax %}) also shows that more generous UBIs are more progressive, even when tax-funded, as does a comparison between our [Blank Slate UBI model]({% post_url 2021-05-12-uk-blank-slate-ubi %}) and more incremental reforms.

Moreover, poverty, inequality, and how people fare compared to today are not the only factors to judge UBI policies on. Starting with a working age population could rhetorically fill a gap between Child Benefit and State Pension, and treating the UBI as income for means-testing can serve to reduce benefits' scope without changing their structure. But as we showed in [yesterday's analysis]({% post_url 2021-06-06-lib-dem-policy-paper %}), the working group's reforms didn't change overall marginal tax rates substantially; true benefit reform may need to accompany the UBI policy to meaningfully improve work incentives and reduce bureaucratic burdens. So we're left largely with the million Britons lifted out of poverty by a budget-neutral version of the working group's UBI proposal, and the nearly three million more who'd be lifted out of poverty through a more expansive version of it.
