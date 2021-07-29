---
layout: post
current: post
cover: assets/images/personal-allowance.png
navigation: True
title: Funding UBI by eliminating the UK personal allowance
date: 2021-07-26
tags: [uk]
subclass: 'post'
author: ines
excerpt: The budget-neutral reform would lower poverty by up to 29%.
class: post-template
useplotly: true
---

Among several potential pay-fors in their recent [UBI discussion paper](https://d3n8a8pro7vhmx.cloudfront.net/libdems/pages/1811/attachments/original/1621669347/145_-_Universal_Basic_Income.docx_%281%29.pdf?1621669347), the Liberal Democrats considered lowering the personal allowance from its current value of £12,570 to £2,500. That is, the first £2,500 of an individual's annual earnings would be exempted from taxation, rather than the first £12,570. [As my colleague Nikhil Woodruff found](https://www.ubicenter.org/lib-dem-policy-paper), this would raise about £60 billion which, when funding a UBI, significantly lowers poverty and inequality.

The Liberal Democrats were not the first to connect the personal allowance and UBI. The Green Party has also [proposed](https://www.greenparty.ie/wp-content/uploads/2018/07/Green-Party-Universal-Basic-Income-Policy.pdf) effectively exchanging the two policies,[^1] and several think tanks have modeled UBIs involving reductions or repeals of the personal allowance. While the personal allowance is highly salient— a 2014 poll found that [85% of the public](https://www.ipsos.com/ipsos-mori/en-uk/personal-allowances-rise-most-popular-conference-season-tax-pledges) supported raising it—it's also a large source of potential revenue for the costly proposition of paying every member of society every month.

In this analysis, I extend the literature around the personal allowance and UBI by modeling a range of personal allowance values and outcomes. I find that repealing the personal allowance could fund a £29 weekly UBI to all members of society, including children. This reform would cut the overall poverty rate by 29%, deep poverty by 46%, and child poverty by 51%. I also find that personal allowance reductions matter on the margin: each £2,000 cut, when funding a UBI, yields around a 5% decrease in poverty. 

### How the personal allowance works

The personal allowance was [introduced in 1979](http://taxhistory.co.uk/Income%20Tax%20Allowances.htm), and it has grown almost every year since. Liberal Democrats accelerated its growth by [calling](https://www.standard.co.uk/news/politics/libdems-to-let-1-3m-low-earners-avoid-paying-tax-8506838.html) for expanding it from £10,000 in 2015 to £12,500 in 2020; this succeeded, and it now sits at £12,570, where it is [expected to remain until April 2026](https://www.reuters.com/article/uk-health-coronavirus-britain-budget-inc-idUSKBN2AV1LP).

While many countries have a tax-free band like the personal allowance, the UK also makes the uncommon decision to phase it out for higher earners. Individuals earning above £100,000 lose £1 of personal allowance for every £2 in earnings, phasing out fully for those earning £125,140 per year and creating 62% marginal tax rates for earners in this range.

These components combine to produce a policy that is neither clearly progressive nor clearly regressive. Because households in the bottom decile have little to no earned income, the personal allowance provides them only small benefits. And while those in the upper individual decile are mostly excluded from the personal allowance, those in the upper household decile [still benefit significantly from it](https://ifs.org.uk/publications/6045), due to marriage between high earners and non-high earners.[^2] Repealing the personal allowance would raise £97 billion (£3,585 per worker) and raise the Gini inequality index from 0.386 to 0.396,[^3] indicating that the personal allowance is slightly progressive on a net basis.

[^1]: The Green Party states that in their model, UBI will be taxable, but “all income tax payers will have a tax-free allowance which is the equivalent to their Universal Basic Income amount”; this means that, in practice, the UBI would not be taxed and the personal allowance would effectively be eliminated. 

[^2]: This and the remaining analysis uses the OpenFisca-UK microsimulation model with data from 2020, when the personal allowance was set at £12,500. Source code is at [github.com/UBICenter/personal-allowance](https://github.com/ubicenter/personal-allowance).

[^3]: The Gini coefficients used throughout are calculated using total household net income weighted by people.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_3_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_3_1.html");
    });
  </script>
</div>
<div id = "graph_graph_3_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_3_2").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_3_2.html");
    });
  </script>
</div>
<div id = "graph_graph_3_2"></div>

The benefit for low earners is also constrained by its interaction with means tested benefits. Since Universal Credit phases out with respect to post-tax income, any tax reduction also reduces Universal Credit payments. As [explained](https://www.politics.co.uk/opinion-former/press-release/2018/10/29/personal-allowance-increase-does-little-for-those-on-lowest-income/) by Victoria Todd, Head of the Low Income Tax Reform Group, regarding the 2019 changes:

>“[Universal credit recipients] will not see the full tax gain of £130 from the increase in the personal allowance; instead, they will only gain overall by £48.10, as their Universal Credit award will be reduced by £81.90. However, those earning above £11,850 who receive tax credits will benefit from the full £130 because tax credits are based on gross income.”

Similarly, the [Resolution Foundation](https://www.resolutionfoundation.org/app/uploads/2014/12/Missing-the-target1.pdf) found that the Liberal Democrats’ plan to increase the personal allowance from £10,600 in 2015 to £12,500 by 2020 gave only around £18 of additional annual income to the bottom 10% of households and £203 to the top 10%.
### Replacing the personal allowance with UBI

While the personal allowance is only slightly progressive by itself, using revenue from repealing the personal allowance to fund a UBI is highly progressive. Fully repealing the Personal Allowance could fund a weekly UBI of £29 per person, and this lowers the Gini index from 0.386 to 0.369.

Each £1,000 decrease in the personal allowance could fund an increase in the UBI amount of around £110 annually, or just over £2 a week.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_6_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_6_1.html");
    });
  </script>
</div>
<div id = "graph_graph_6_1"></div>

This policy would, in general, serve as an income transfer from the richest 40% to the poorest 60%. You can adjust the personal allowance amount with the slider to see how partial personal allowance replacements fare: with further cuts to the personal allowance and higher universal basic incomes, reforms achieve stronger redistributive effects.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_9_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_9_1.html");
    });
  </script>
</div>
<div id = "graph_graph_9_1"></div>

For the three lowest deciles, this would mean an annual household income increase of 24%, 11%, and 7% respectively. In contrast, the income reductions for the highest deciles don’t exceed 3%.


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_11_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_11_1.html");
    });
  </script>
</div>
<div id = "graph_graph_11_1"></div>

Additionally, each £1000 reduction in personal allowance buys a 0.0015 reduction in the Gini coefficient.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_13_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_13_1.html");
    });
  </script>
</div>
<div id = "graph_graph_13_1"></div>

Median household income would increase by about £525, and this number is over five times greater for those living in poverty. This is an income gain of 1.4% for the overall population, 21% for people in poverty, and 53% for people in deep poverty.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_15_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_15_1.html");
    });
  </script>
</div>
<div id = "graph_graph_15_1"></div>

Part of the large gains for poor households owe to the fact that poor households tend to have more children, and therefore receive more UBI payments. Similarly, households in deep poverty tend to have fewer children than other poor households, which explains why the median gain is slightly lower for this group.


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_17_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_17_1.html");
    });
  </script>
</div>
<div id = "graph_graph_17_1"></div>

Overall, since households with children receive more UBI payments, they are disproportionately benefited.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_19_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_19_1.html");
    });
  </script>
</div>
<div id = "graph_graph_19_1"></div>

In fact, this policy would benefit children more than any other group, as children do not lose income to a personal allowance decrease, and exclusively gain from the UBI amount given to them. Child poverty would fall 50%, and deep child poverty by 72%. 

Overall poverty would fall by 29% and overall deep poverty would fall by 44%. In contrast, UBI funded through only partial reductions in the personal allowance would produce smaller poverty impacts than a full replacement. Each £2,000 of personal allowance reduced buys around a 5% decrease in poverty, meaning each £2,000 of personal allowance preserved decreases the poverty effect by 5 percentage points.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_23_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_23_1.html");
    });
  </script>
</div>
<div id = "graph_graph_23_1"></div>

On average, the policy would serve as a transfer from older adults to children. The average child under 18 would see their household net income rise by £2,622 under full replacement of the personal allowance with a UBI.  



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_26_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_26_1.html");
    });
  </script>
</div>
<div id = "graph_graph_26_1"></div>

#### Impacts for specific household types
Entirely replacing the personal allowance with UBI would benefit 52% on a net basis, most of them belonging to the bottom four deciles. 91% of the lowest decile, 73% of the second-lowest decile, and 62% of the third-lowest decile would see their incomes rise by over 5%. In contrast, most people who see their income decrease are in the upper deciles, and these people mostly lose less than 5%.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_30_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_30_1.html");
    });
  </script>
</div>
<div id = "graph_graph_30_1"></div>

A single individual living alone would see their income rise when they make under £17,000 and over £117,000.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_33_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_33_1.html");
    });
  </script>
</div>
<div id = "graph_graph_33_1"></div>

Additionally, the marginal tax rate would rise for single individuals earning lower incomes, and decrease for single individuals making between £100,000 and £125,140—the range in which the personal allowance phases out.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_36_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_36_1.html");
    });
  </script>
</div>
<div id = "graph_graph_36_1"></div>

In contrast, for a couple with two children, household net income always rises regardless of employment income.




<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_40_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_40_1.html");
    });
  </script>
</div>
<div id = "graph_graph_40_1"></div>

The effect on their marginal tax rate is similar to that of a single individual, but the rise for those earning lower incomes is less significant.



<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_43_1").load("{{site.baseurl}}assets/markdown_assets/personal-allowance/graph_43_1.html");
    });
  </script>
</div>
<div id = "graph_graph_43_1"></div>

### Conclusion

My research aligns with other analyses showing the progressivity of replacing the personal allowance with UBI. In 2019, the New Economics Foundation [modeled](https://neweconomics.org/2019/03/nothing-personal) replacing the personal allowance with a budget-neutral Weekly National Allowance paid to adults and an increase in the child benefit, making the payments non-taxable but included in means tests. They found progressive results, stating it would “[lift] 200,000 families out of poverty and shift the £8bn currently spent on tax allowances for the 35% highest income families to the remaining 65% of families.” Compass also [modeled](https://www.compassonline.org.uk/wp-content/uploads/2019/03/Compass_BasicIncomeForAll_2019.pdf) replacing the personal allowance with a budget-neutral flat payment of £25 a week for children and adults of working age, as well as a flat rate citizen’s pension of £164.35. They too found progressive results, with the Gini coefficient decreasing from 0.337 to 0.365. Most recently, [my colleagues found](https://www.ubicenter.org/progressive-adjustments-lib-dem-working-group) that the policy in the Liberal Democrats discussion paper could be made more progressive by repealing all, rather than part, of the personal allowance.

Beyond these other papers, I've found that the impacts occur roughly linearly on the margin, meaning that the policy concept can operate incrementally. Furthermore, the policy disproportionately benefits children, and [separate studies](https://child-allowance.ubicenter.org/empirical) show that this will in turn improve educational and health outcomes. The impacts are largely but not uniformly beneficial to low income households, though losses are small.

Reforms that broaden the tax base are often regressive on their own, but how the revenue is spent matters. Repealing the personal allowance is one such instance: using the revenue to fund a UBI switches the distributional sign from regressive to highly progressive.
