---
layout: post
current: post
cover: assets/images/2022-04-23-uk-carbon-dividend.jpeg
navigation: True
title: The progressivity of a UK carbon dividend
date: 2022-04-23
tags: [uk, carbon pricing]
subclass: "post"
author: [max, nikhil]
excerpt: "A £100-per-tonne carbon dividend would cut poverty by 14% and deep child poverty by 33%."
class: post-template
useplotly: true

---

## [*See a £100/tonne carbon dividend in PolicyEngine*](https://policyengine.org/uk/population-impact?adult_bi=15_55&carbon_tax=100&child_bi=15_55&senior_bi=15_55)

Earlier this month, the International Panel on Climate Change ([IPCC](https://www.ipcc.ch/)) released the [third installment](https://report.ipcc.ch/ar6wg3/) of its Sixth Assessment Report, titled "Mitigation of Climate Change."
The report covered a wide range of policy options to reduce carbon emissions, as well as a wide range of benefits such policies would have for humanity.

As [Dana Nuccitelli of Citizens' Climate Lobby wrote](https://citizensclimatelobby.org/blog/policy/the-latest-ipcc-report-has-a-lot-to-say-about-carbon-fee-and-dividend/), the report has a lot to say about one policy in particular: it contains 680 mentions of carbon pricing, from the economic theory and evidence to policy design and political support.
While most climate change proposals require funding, carbon pricing policies raise revenue by charging fossil fuel companies for their carbon pollution.
That means it also raises costs in isolation; to address this, the IPCC says, "Carbon pricing is most effective if revenues are redistributed or used impartially."
What's more impartial than redistributing to everyone equally?

For Earth Day weekend, we're following up [our report on US carbon dividends](https://www.ubicenter.org/us-carbon-dividend) with an analysis of the policy in the UK.
Using [PolicyEngine](http://policyengine.org), we find that levying a fee on each tonne of carbon emissions, and redistributing the proceeds equally to all UK residents, would have a progressive distributional impact.
A carbon dividend would significantly reduce poverty and inequality, and the larger the program, the more of each it does.

## Methodology

As we've written on the [PolicyEngine blog today](https://blog.policyengine.org/how-policyengine-estimates-the-effects-of-uk-carbon-taxes-260ccfc5d97c), PolicyEngine uses a range of data sources and techniques to estimate how carbon taxes would affect different types of households.
PolicyEngine is a *static* app, so it assumes that behaviour, including carbon emissions, do not respond to policy changes.

In this analysis, we use PolicyEngine to first explore a single policy of a [£100 per tonne carbon dividend](https://policyengine.org/uk/population-impact?adult_bi=15_55&carbon_tax=100&child_bi=15_55&senior_bi=15_55).
From there, we show that the poverty impacts of carbon dividends increase roughly in proportion to the size of the carbon tax.
In each case, we assume that consumers bear 100% of the incidence of the carbon tax; changing this assumption doesn't significantly change the policy's income-based distributional impact.

## [£100/tonne carbon dividend](https://policyengine.org/uk/population-impact?adult_bi=15_55&carbon_tax=100&child_bi=15_55&senior_bi=15_55)

To create a carbon dividend in [PolicyEngine UK](https://policyengine.org/uk), first go to the `UBI Center` parameter menu, then the `Carbon tax` submenu, and set the carbon tax to £100.
Then, go to the `Basic income` submenu and click `Direct surplus revenue into UBI` at the bottom.
This will create a UBI of £15.55 per week.
From there, the `Calculate UK impact` button will show [this page](https://policyengine.org/uk/population-impact?adult_bi=15_55&carbon_tax=100&child_bi=15_55&senior_bi=15_55).

Overall, PolicyEngine shows that the carbon dividend would have essentially no net budgetary impact (by design), that it would cut poverty by 14%, and that two thirds of the UK would come out ahead.
The policy would disproportionately lift children out of poverty, while still significantly reducing the poverty rate in other age groups.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_1_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_1_1.html");
    });

  </script>
</div>
<div id = "graph_graph_1_1"></div>

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_1_2").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_1_2.html");
    });

  </script>
</div>
<div id = "graph_graph_1_2"></div>

On average, the carbon dividend would benefit each of the bottom seven income deciles.
The bottom decile would gain 6.2%, and the top decile would lose 2.1%.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_3_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_3_1.html");
    });

  </script>
</div>
<div id = "graph_graph_3_1"></div>

While the carbon dividend benefits each of the seven deciles on average, it would have have heterogeneous effects within deciles.
For example, 12% of the bottom decile would come out behind, and 26% of the top decile would gain.
Any household whose members consume less than the national average per-capita carbon emissions would come out ahead, and this correlates strongly but imperfectly to income.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_5_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_5_1.html");
    });

  </script>
</div>
<div id = "graph_graph_5_1"></div>

Nevertheless, the carbon dividend would substantially reduce income inequality on a net basis.
For example, the Gini index, a comprehensive measure of inequality, would fall 3.4%

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_7_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_7_1.html");
    });

  </script>
</div>
<div id = "graph_graph_7_1"></div>

## Varying the price

Since PolicyEngine is static, the revenue--and therefore the dividend--increases linearly with the carbon price.
Each £10 per tonne funds a weekly dividend of £1.56 per person.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_10_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_10_1.html");
    });

  </script>
</div>
<div id = "graph_graph_10_1"></div>

As the carbon dividend increases in price, impacts on poverty and deep poverty (the population share with income below half the poverty line) increase roughly linearly, with some slight diminishing returns starting around £90 per tonne.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_12_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_12_1.html");
    });

  </script>
</div>
<div id = "graph_graph_12_1"></div>

At each level of the carbon tax, deep poverty and child poverty (and especially deep child poverty) fall fastest.

<div>
  <script>

    $(document).ready(function(){
      $("#graph_graph_14_1").load("{{site.baseurl}}assets/markdown_assets/uk-carbon-dividend/graph_14_1.html");
    });

  </script>
</div>
<div id = "graph_graph_14_1"></div>

Perhaps uniquely in today's political climate, carbon dividends are a broadly supported form of universal basic income, albeit a small one.
They can be integrated into larger UBI policies, such as the [Green Party's 2019 manifesto](https://blog.policyengine.org/the-green-party-manifesto-at-policyfest-ee05a2d3b06d) or [Andrew Yang's Freedom Dividend](https://www.ubicenter.org/distributional-analysis-of-andrew-yangs-freedom-dividend), or adopted in isolation, like the [Energy Innovation and Carbon Dividend Act](https://energyinnovationact.org) in the US.
Experts agree that carbon dividends would help avert climate change and deaths from air pollution, and, like other poverty researchers, we've found that they would reduce poverty and inequality as well.

*Thanks to ​​Inés Fernández Barhumi and Reema Mohanty for their research assistance on our carbon tax model.*
