---
layout: post
current: post
cover:
navigation: True
title: Northern Ireland UBI Feasibility Study
date: 2022-08-31
tags: [northern-ireland, uk]
subclass: "post"
author: [nikhil, max]
excerpt: New research supported by UBI Labs NI.
class: post-template
useplotly: true

---

# Executive summary

Northern Ireland is both unusually egalitarian and unusually supportive of universal basic income, the idea to provide everyone in society a regular unconditional payment. But so far, no study has quantified how the nation might enact a universal basic income (UBI) through tax and benefit reforms.

Following proposals by the UBI Lab Northern Ireland, we fill that gap. This paper begins with a description of Northern Ireland's economy, then identifies over 120 tax-funded UBI policies, and zooms in on three in particular. These policies cover the space of UBI amounts (£200 to £400 per adult, and half for children) and tax reforms (lowering the personal allowance and increasing tax rates). As shown below, each of the policies significantly lowers poverty and inequality in Northern Ireland, while benefiting a narrow minority of the population.

**Table 1**


<table>
  <tr>
   <td><strong>Monthly UBI amount for adults</strong>
   </td>
   <td><strong>Monthly UBI for children</strong>
   </td>
   <td><strong>Personal allowance</strong>
   </td>
   <td><strong>Basic rate increase</strong>
   </td>
   <td><strong>Additional and higher rate increase</strong>
   </td>
   <td><strong>Poverty impact</strong>
   </td>
   <td><strong>Inequality impact (Gini)</strong>
   </td>
   <td><strong>Percent of population benefiting</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=26_5&higher_rate=52&add_rate=57&personal_allowance=1000&higher_threshold=50270&adult_bi=46_15&senior_bi=46_15&child_bi=23_08&baseline_country_specific=NORTHERN_IRELAND">£200</a>
   </td>
   <td>£100
   </td>
   <td>£2,000
   </td>
   <td>6.5p
   </td>
   <td>13p
   </td>
   <td>-61%
   </td>
   <td>-15%
   </td>
   <td>52%
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=34&higher_rate=54&add_rate=59&personal_allowance=0&higher_threshold=50270&adult_bi=69_23&senior_bi=69_23&child_bi=34_62&baseline_country_specific=NORTHERN_IRELAND">£300</a>
   </td>
   <td>£150
   </td>
   <td>£0
   </td>
   <td>14p
   </td>
   <td>14p
   </td>
   <td>-69%
   </td>
   <td>-23%
   </td>
   <td>53%
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=40.4&higher_rate=40.0&add_rate=45.0&personal_allowance=0&higher_threshold=50270&adult_bi=92.31&senior_bi=92.31&child_bi=46.15&baseline_country_specific=NORTHERN_IRELAND">£400</a>
   </td>
   <td>£200
   </td>
   <td>£0
   </td>
   <td>24p
   </td>
   <td>0p
   </td>
   <td>-82%
   </td>
   <td>-30%
   </td>
   <td>54%
   </td>
  </tr>
</table>


We follow our population-level analysis with a household analysis, visualising how each of these three policies would affect the net income and work incentives of archetypical households. While each policy benefits low-income households and families with children, it leaves childless singles worse off when their income exceeds about £10,000. It also lowers the payoff to working for most workers, though it smooths out some of the most severe disincentives in the current system.

UBI is a significant economic proposition, and our analysis finds that it would leave a major mark on most Northern Ireland residents—in an undeniably progressive fashion. We conclude with caveats of our analysis, opportunities for less disruptive models, and room for more research.


# Northern Ireland today

The demographic and economic characteristics of Northern Ireland (NI) differ from those of the UK and other UK nations. In the main, this is lower economic output, but higher levels of social security spending. NI has a GDP per capita roughly 20% below the UK average,[^1] and the population of 1.9 million generates around £2.8 billion in Income Tax liabilities.[^2] Higher levels of public spending (with a net fiscal deficit of £9,500 per capita)[^3] in NI increase disposable incomes to offset this. As a result, we estimate that 6.1% of NI is in absolute poverty, compared to 5.5% across the UK.[^4] We also find that NI is more equal, with a Gini index of 0.274 against the UK's 0.333.

Many of Northern Ireland’s taxes and benefits operate under centralised UK rules, though exceptions to this include local property taxes such as [domestic rates](https://www.finance-ni.gov.uk/topics/property-rating/domestic-rating) (and rates rebates), which exist in place of Council Tax and Council Tax Benefit. Unlike Scotland, Northern Ireland does not set alternative tax rates for Income Tax.

When it comes to basic income, Northern Ireland is broadly supportive. A 2017 poll by Ipsos MORI found that 66% of Northern Irish people favoured a basic income, compared to 49% of UK residents.[^5] Northern Ireland's net favourability of +55 was more than double that of any other region surveyed.

**Figure 1: UBI favourability by UK subregion**


![UBI favourability by UK subregion](images/polls.png "UBI favourability by UK subregion")


A full UBI in NI would align with the nation's egalitarianism and public opinion. The next section models how NI could do it.


# Exploring the space of feasible policies

One could model an infinite number of basic income policies for Northern Ireland. We constrained the problem by defining UBI parameter values, tax variables to adjust, and requirements for the resulting policy.

In particular, we limited to UBI policies of the following form:


* Amounts per adult (aged 18 or over) of £200, £300, and £400 per month
* Amounts per child of half the adult amount
* UBI payments do not count as income for tax or means-tested benefits

To fund the UBI, we considered three levers:


* Personal allowance, from zero to the current value of £12,570 (we also adjusted the higher rate threshold to keep it at £50,270)
* Basic rate increase
* Ratio of higher and additional rate increases to the basic rate increase, of 0x (not changing the higher and additional rates), 1x, and 2x

Finally, we constrained the end policy to:


* Be budget-neutral (assuming no behavioural responses)
* Avoid raising marginal tax rates above 100%,[^6] either via the normal tax rates, the phase-out of the personal allowance or benefit phase-outs
Figure 2 represents this exploratory exercise: each point in these lines is a feasible policy. For example, the leftmost line shows the set of all policies that provide £200 per month to adults (£100 to children), and in which the higher and additional rates rise two percentage points per percentage point increase in the basic rate. It varies by the basic rate and personal allowance. The top-left point in this line is a policy that abolishes the Personal Allowance (reduces it by the full £12,570), increases the basic rate by 4p, and increases the higher and additional rates by 8p ([see it in PolicyEngine here](https://policyengine.org/uk/population-impact?basic_rate=24.4&higher_rate=48.8&add_rate=53.8&personal_allowance=0&higher_threshold=50270&adult_bi=46.15&senior_bi=46.15&child_bi=23.08&baseline_country_specific=NORTHERN_IRELAND)).

**Figure 2: Budget neutral UBI funding models**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_1_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_1_1.html");
    });
  </script>
</div>
<div id = "graph_graph_1_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_1_2").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_1_2.html");
    });
  </script>
</div>
<div id = "graph_graph_1_2"></div>

These lines are incomplete because they do not show policies that would increase marginal tax rates (MTRs) above 100%. For example, the leftmost line ends at the policy that would raise the basic rate by 11p and reduce the personal allowance to £5,000. Extending that line would require increasing the basic rate to allow for a larger personal allowance. However, doing so would increase the MTR above 100% for people earning £100,000, as their personal allowance phases out.[^7]

To avoid exceeding 100% MTRs, more generous UBI policies require broader-base tax reforms focused on the personal allowance and basic rate. Indeed, the £400 per month policy can only increase the higher and additional rates at double the basic rate if the personal allowance is repealed entirely. At this point, the basic rate would rise by 16p to 37p, the higher rate would rise by 32p to 75p, and the additional rate would rise by 32p to 80p ([see that policy in PolicyEngine here](https://policyengine.org/uk/population-impact?basic_rate=36&higher_rate=72&higher_threshold=50270&add_rate=77&personal_allowance=0&child_bi=46.1538461538462&adult_bi=92.3076923076923&senior_bi=46.1538461538462&baseline_country_specific=NORTHERN_IRELAND)); even a pound of personal allowance would create a MTR above 100% for people in the phase-out range.

We have listed all 126 policies represented in the chart in [this spreadsheet](https://docs.google.com/spreadsheets/d/17_xYwxvc119MrVLpo1gzGEVwL7uIM0Vn8-jaf6uN9s0/edit#gid=0). In the next section, we provide a deeper dive into three policies—one for each UBI level.


# Policy deep dive

We selected three of the 126 feasible policies to describe in more detail. These show the space of policies—not only in terms of UBI amount, but also the funding mechanisms. These three policies are shown in Table 1, the first column of which directs to the reform in PolicyEngine.

**Table 1**


<table>
  <tr>
   <td><strong>Monthly UBI amount for adults</strong>
   </td>
   <td><strong>Monthly UBI for children</strong>
   </td>
   <td><strong>Personal allowance</strong>
   </td>
   <td><strong>Basic rate increase</strong>
   </td>
   <td><strong>Additional and higher rate increase</strong>
   </td>
   <td><strong>Poverty impact</strong>
   </td>
   <td><strong>Inequality impact (Gini)</strong>
   </td>
   <td><strong>Percent of population benefiting</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=26_5&higher_rate=52&add_rate=57&personal_allowance=1000&higher_threshold=50270&adult_bi=46_15&senior_bi=46_15&child_bi=23_08&baseline_country_specific=NORTHERN_IRELAND">£200</a>
   </td>
   <td>£100
   </td>
   <td>£2,000
   </td>
   <td>6.5p
   </td>
   <td>13p
   </td>
   <td>-61%
   </td>
   <td>-15%
   </td>
   <td>52%
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=34&higher_rate=54&add_rate=59&personal_allowance=0&higher_threshold=50270&adult_bi=69_23&senior_bi=69_23&child_bi=34_62&baseline_country_specific=NORTHERN_IRELAND">£300</a>
   </td>
   <td>£150
   </td>
   <td>£0
   </td>
   <td>14p
   </td>
   <td>14p
   </td>
   <td>-69%
   </td>
   <td>-23%
   </td>
   <td>53%
   </td>
  </tr>
  <tr>
   <td><a href="https://policyengine.org/uk/population-impact?basic_rate=40.4&higher_rate=40.0&add_rate=45.0&personal_allowance=0&higher_threshold=50270&adult_bi=92.31&senior_bi=92.31&child_bi=46.15&baseline_country_specific=NORTHERN_IRELAND">£400</a>
   </td>
   <td>£200
   </td>
   <td>£0
   </td>
   <td>24p
   </td>
   <td>0p
   </td>
   <td>-82%
   </td>
   <td>-30%
   </td>
   <td>54%
   </td>
  </tr>
</table>


Each of the reforms substantially lowers or eliminates the personal allowance, and increases the basic rate; the cost of the policies requires broad-based tax reform. Each of the reforms also cuts poverty by at least 60% and inequality by at least 15%, with the more generous programs producing stronger effects. A slim majority of the population comes out ahead from each, as well.

Digging into the poverty impacts reveals stronger impacts on child poverty, with the most generous plan all but eradicating it.[^8] [Many studies find](child-allowance.ubicenter.org/empirical) that child poverty causes deleterious developmental and lifelong outcomes. Senior poverty is unaffected, as it is eliminated in the baseline due to a combination of recent policy changes (for example, cost-of-living payments) and long-standing benefit programs (for example, Pension Credit).

**Figure 3: Poverty impact by age group and UBI policy**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_4_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_4_1.html");
    });
  </script>
</div>
<div id = "graph_graph_4_1"></div>

Each policy reduces various measures of inequality, especially the Gini index, roughly in proportion to the UBI amount. They also cut narrower measures of inequality: depending on the policy, the share held by the top 1 and 10 percent of the population falls by 5 to 15 percent.

**Figure 4: Inequality impact by metric and UBI policy**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_6_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_6_1.html");
    });
  </script>
</div>
<div id = "graph_graph_6_1"></div>

The next sections provide more detailed population impacts on each of the three policies.


## [£200 per month option](https://policyengine.org/uk/population-impact?basic_rate=26_5&higher_rate=53&add_rate=58&personal_allowance=1000&higher_threshold=50270&adult_bi=46_15&senior_bi=46_15&child_bi=23_08&baseline_country_specific=NORTHERN_IRELAND)

_£200 per month for adults and £100 for children, funded by lowering the personal allowance to £2,000, increasing the basic rate by 6.5p, and increasing the higher and additional rates by 13p_

The smallest policy in our analysis reduces the allowance to £2,000 per year, raises the basic rate to 26.5%, the higher rate to 52% and the additional rate to 57%. 52% of the population sees their income rise as a result of the policy.

The policy is highly progressive: the lowest income decile sees an increase of 34% to its aggregate disposable income. The top four deciles are net contributors to the scheme, but lose at most 6.8% of their income.

**Figure 5: Change to net income by income decile under a £200 per month UBI**



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_8_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_8_1.html");
    });
  </script>
</div>
<div id = "graph_graph_8_1"></div>

This does not mean, however, that everyone within a beneficiary decile comes out ahead or vice-versa. But gains broadly correlate with income: in the first decile, 97% of individuals see their household net income rise; in the top decile, all see their income fall. Basic income schemes often create large amounts of low-income households who see a loss, if the policy abolishes or removes elements of the existing welfare system. This and other policies considered in this report avoid creating such low-income losses by not reforming benefit programs.

**Figure 6: Outcome distribution by income decile under a £200 per month UBI**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_10_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_10_1.html");
    });
  </script>
</div>
<div id = "graph_graph_10_1"></div>

Total absolute poverty falls by 61%. This includes a fall of just under half (48%) for working-age poverty and by 81% for child poverty. 


## [£300 per month option](https://policyengine.org/uk/population-impact?basic_rate=34&higher_rate=54&add_rate=59&personal_allowance=0&higher_threshold=50270&adult_bi=69_23&senior_bi=69_23&child_bi=34_62&baseline_country_specific=NORTHERN_IRELAND)

_£300 per month for adults and £150 for children, funded by repealing the personal allowance and increasing all tax rates by 14p_

NI could increase the basic income level from £200 to £300 by eliminating the personal allowance and raising the basic rate to 34%, the higher rate to 54%, and the additional rate to 59%. One counter-intuitive result of this is that the top marginal tax rate actually falls slightly: in the current system, individuals who earn over £100,000 and less than £125,140 pay a 63.25% marginal tax rate.[^9] Under this policy, the top marginal rate becomes 62.25%, as the personal allowance no longer exists to be phased out.

With a larger UBI comes more progressive outcomes: the lowest income decile sees its income increase by over 50%, and the top decile income falls by over 10%. The break-even decile point remains the same, between the sixth and seventh deciles.

**Figure 7: Change to net income by income decile under a £300 per month UBI**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_12_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_12_1.html");
    });
  </script>
</div>
<div id = "graph_graph_12_1"></div>

A similar pattern holds for the distribution of outcomes within each decile, but the results are more pronounced. Almost every household in the top decile sees a loss in income that is over 5%. Countering this, a much larger proportion of individuals are in households with strong (over 5%) increases in income: from 36% (for the £200 per month policy) to 43%.

**Figure 8: Outcome distribution by income decile under a £300 per month UBI**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_14_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_14_1.html");
    });
  </script>
</div>
<div id = "graph_graph_14_1"></div>

## [£400 per month option](https://policyengine.org/uk/population-impact?basic_rate=39&higher_rate=40&higher_threshold=50270&add_rate=45&personal_allowance=0&child_bi=46.1538461538462&adult_bi=92.3076923076923&senior_bi=46.1538461538462&baseline_country_specific=NORTHERN_IRELAND)

_£400 per month for adults and £200 for children, funded by repealing the personal allowance and increasing the basic rate by 24p_

The most generous basic income policy considered is £400 per month for adults (£200 per month for children), funded by repealing the personal allowance and raising the basic rate to 44%, creating a non-progressive nominal tax schedule (though note that the full tax-benefit schedule is already non-progressive). With a total redistribution of £8.4bn in via tax revenues and out via benefit outlays, 54% of individuals see an increase in disposable income. The bottom decile sees an increase of 69% in disposable income, and the bottom sees a fall of 15%.

**Figure 9: Change to net income by income decile under a £400 per month UBI**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_16_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_16_1.html");
    });
  </script>
</div>
<div id = "graph_graph_16_1"></div>

Unlike the previous two policies at £200 and £300 per month, the £400 per month basic income policy leaves no households in the lowest income decile worse off. The share of individuals who see gains greater than 5% rises slightly to 45%, suggesting that it is nearing its maximum under this policy structure.

**Figure 10: Outcome distribution by income decile under a £400 per month UBI**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_18_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_18_1.html");
    });
  </script>
</div>
<div id = "graph_graph_18_1"></div>


## Household impacts

For individual households, each policy changes how the tax-benefit system shapes net incomes in response to earnings. To show this, we continue examining our three policies through the lenses of three example households: a single adult, a married couple with two children, and a pensioner couple.


### Net income

A single adult with no children is a net beneficiary under all three policies only until they reach £10,000 in employment income.[^10] Before this break-even point, the policy that most benefits them is the £400 per month UBI. After that threshold, their net income rises more slowly than it would have under the baseline policy, and their policy preference would flip: The £400 and £300 per month UBI policies (which have higher tax increases) are worse for their net income. However, this preference only lasts until after the higher rate threshold at £50,270: the £400 per month UBI quickly becomes the best policy due to its 0-point changes to the higher and additional rates of income tax.

**Figure 11: Change to annual net income by UBI policy and income (single adult, no children)**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_21_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_21_1.html");
    });
  </script>
</div>
<div id = "graph_graph_21_1"></div>

For a married couple with two children, one of whom has earnings, the net income landscape is more generous. The £400 per month UBI leaves them better off or roughly equal at virtually any earnings level, starting with a bonus of over £14,000 which decreases smoothly until around £63,500 (at this level, they have just phased out of the Child Benefit). At £100,000 earnings, they become significantly better off because they avoid the phase-out of the personal allowance entirely.

**Figure 12: Change to annual net income by UBI policy and income (married couple, two children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_23_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_23_1.html");
    });
  </script>
</div>
<div id = "graph_graph_23_1"></div>

For a pensioner couple, one of whom has income,[^11] the net impact of the basic income policies varies significantly with income, with regions of high gains and high losses. For households with income under £27,000, all of the policies leave them better off (with gains of between £4,000 and £9,000). This is primarily because Pension Credit insulates pensioners from Income Tax rises. The Guarantee Credit element of Pension Credit tops up pensioner incomes to a minimum level, and the income definition used means that pensioners are guaranteed to be better off: it deducts income tax payments (meaning that it shields from the tax rises in each policy) and does not include basic income payments. However, after pensioner income rises out of the range in which Guarantee Credit operates (around £12,500), the gains from the UBI policies diminish, reaching a break-even point at around £27,000. From that point, the policies differ but generally see net income rise more slowly than the baseline.  At £125,000, all UBI policies except the £400 per month policy see the household worse off.

**Figure 13: Change to annual net income by UBI policy and income (pensioner couple, no children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_25_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_25_1.html");
    });
  </script>
</div>
<div id = "graph_graph_25_1"></div>

The appendix contains charts comparing the baseline and reform net incomes as values rather than differences.


### Marginal tax rates

The marginal tax rate (MTR) for a given pound of earnings is defined as the percentage which does not contribute to increasing net income, either by going to taxation instead or by causing a reduction in benefit entitlement. For example, if an earner faces a 20% MTR from taxes and a 15% MTR from benefits, their total MTR is 35% and they take home 65p for each additional £1 of earnings.

Figure X shows the MTR associated with each earnings level for a married couple with two children:[^12] the higher the line at a given income, the lower the incentive to work. Where the MTR is 100%, this means that earning an additional pound will make no difference to net income. Where the MTR is above 100%, earning additional income at the margin will decrease the household’s net income. The interaction of the policies is complex: at different points, some UBI policies would reduce MTRs; at others, they would increase them. Broadly, MTRs rise across the earnings spectrum, but decrease in some specific areas. 

The first of these areas is at £50,270, the higher rate threshold. Under current law, the Marriage Allowance is a tax allowance that reduces tax liability by enabling couples to transfer some (10%) of their personal allowance between them. However, it is only available to couples with one earner under the higher rate threshold, which leads to a sudden increase in tax liability at that income level (creating an MTR over 100%, a ‘cliff’). All UBI policies reduce this cliff because they reduce or eliminate the personal allowance.

The second is at £100,000. Under baseline policy, the personal allowance is phased out after this point at a rate of 50p per pound of income over the threshold. With no personal allowance, there is nothing to phase out, so the £300 per month and £400 per month UBI policies both eliminate this, reducing the MTR by 20pp.

Overall, all policies substantially raise marginal tax rates in the main, and therefore disincentivise work relative to the status quo, while removing some extreme disincentives to work embedded in certain parts of the current tax code. 

**Figure 14: Marginal tax rate by UBI policy and income (married couple, two children)**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_28_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_28_1.html");
    });
  </script>
</div>
<div id = "graph_graph_28_1"></div>

Another way of framing these effects is as the change to effective marginal wages. For example, if a policy increases the MTR from 35% to 40%, that lowers the effective marginal wage from 65% to 60%, or by about 8%. Here we see that effective marginal wages are generally lower under the UBI reforms, except for the regions described above.

**Figure 15: Change to effective marginal wage by UBI policy and income (married couple, two children)**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_31_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_31_1.html");
    });
  </script>
</div>
<div id = "graph_graph_31_1"></div>

# Conclusion

Any one of the UBI policies described here would dramatically reshape Northern Ireland. From a Rawlsian sense, they would lift up the floor upon which many sit, achieving overnight poverty reductions NI has taken years or decades to see naturally.

Yet that dramatic reshaping also comes in the form of disruption and potential macroeconomic drag. Nearly half the nation would come out behind, and many by material amounts. And most would face considerably higher marginal tax rates.

Our static model does not fully account for these costs. A [recent paper](http://www.columbia.edu/~wk2110/bin/DeatonReviewChapter.pdf) from IFS and Columbia University found, "Current estimates therefore suggest that the top UK rate [of 47%] is close to revenue maximising, but there is a very large degree of uncertainty around this." Some of these reforms would bring that top rate closer to 80%, and extend it to a thicker part of the earnings distribution. While poverty reduction would benefit the economy, reducing the net marginal wage for hundreds of thousands of workers could shrink it, and more research is needed to understand the full impact of these countervailing forces.

More research could also identify policies that achieve similar distributional benefits without so much disruption. For example, in 2021 we [created an optimisation model](ubicenter.org/uk-blank-slate-ubi) to explore tens of thousands of UBI policies and select the age-dependent amounts that minimised disruption. That UK-wide model could apply to NI specifically, and with potentially more levers such as the tax reforms we applied here.

Our microsimulation approach provides one piece of the puzzle in understanding a transition to universal basic income in Northern Ireland.


## Appendix

**Figure 16: Annual net income by UBI policy and income (single adult, no children)**


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_34_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_34_1.html");
    });
  </script>
</div>
<div id = "graph_graph_34_1"></div>

**Figure 17: Annual net income by UBI policy and income (married couple, two children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_36_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_36_1.html");
    });
  </script>
</div>
<div id = "graph_graph_36_1"></div>

**Figure 18: Annual net income by UBI policy and income (pensioner couple, no children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_38_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_38_1.html");
    });
  </script>
</div>
<div id = "graph_graph_38_1"></div>

**Figure 19: Change to effective marginal wage by UBI policy and income (single adult, no children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_40_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_40_1.html");
    });
  </script>
</div>
<div id = "graph_graph_40_1"></div>

**Figure 19: Change to effective marginal wage by UBI policy and income (pensioner couple, no children)**

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_42_1").load("{{site.baseurl}}assets/markdown_assets/ni-feasibility/graph_42_1.html");
    });
  </script>
</div>
<div id = "graph_graph_42_1"></div>

## Notes

[^1]:
     [Northern Ireland Statistics Research Agency, 2020](https://www.nisra.gov.uk/statistics/economic-output-statistics/gross-value-added-and-gross-domestic-product#:~:text=In%20terms%20of%20GDP%20per,78.6%20per%20cent%20of%20UK).).

[^2]:
     [HMRC, 2019](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/853118/Disaggregated_tax_and_NICs_receipts_-_methodological_note.pdf).

[^3]:
     [ONS, 2021](https://www.ons.gov.uk/economy/governmentpublicsectorandtaxes/publicsectorfinance/articles/countryandregionalpublicsectorfinances/financialyearending2021#:~:text=On%20a%20per%20person%20basis,per%20head%20was%20%C2%A34%2C740.).

[^4]:
     Throughout this paper, we report absolute poverty rates before housing costs, using the OpenFisca UK calibrated Family Resources Survey extrapolated to 2022.

[^5]:
     This is the only poll to ask about basic income for Northern Ireland and the UK, per the [UBI Center's Poll Tracker](polls.ubicenter.org).

[^6]:
     We exclude the Child Benefit High-Income Tax Charge from contributing to this limit, because the MTR addition from that is dependent on the number of children, with no upper bound.

[^7]:
     Specifically, the MTR increases by (higher rate x 1.5)% on the income between £100,000 and (£100,000 + personal allowance x 2). In the baseline, the higher rate is 40% and the personal allowance is £12,570, creating a 60% MTR on income between £100,000 and £125,140.

[^8]:
     The impacts on deep poverty (the population share with net income below half the poverty threshold) are similar, though we do not include them here as the Family Resources Survey has too few records near the deep poverty line to produce reliable results.

[^9]:
     This is because of the personal allowance phase-out, which creates a 60% marginal rate (40% * 1.5), in addition to the National Insurance marginal rate of (as of the time of writing) 3.25%.

[^10]:
     We vary the employment income of only one earner, holding the other (if they exist) at zero.

[^11]:
     We plot based on earnings, but net income responds similarly to earnings as State Pension.

[^12]:
     We focus on the MTR for a married couple with two children because the differences between baseline and reform don't depend much on household structure. See the appendix for more MTR charts for different household archetypes.
