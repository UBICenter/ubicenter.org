---
layout: post
current: post
cover: assets/images/2022-04-21-california-vehicle-payment.png
navigation: True
title: What if California gave money to everyone, not only vehicle owners?
date: 2022-04-21
tags: [us, california]
subclass: "post"
author: [max, nikhil]
excerpt: Benchmarking Governor Newsom's proposed per-vehicle payment against a per-person payment.
class: post-template
useplotly: true

---

Last month, Governor Gavin Newsom [proposed an $11 billion package](https://www.gov.ca.gov/2022/03/23/governor-newsom-proposes-11-billion-relief-package-for-californians-facing-higher-gas-prices/) for Californians facing higher gas prices. Newsom reserved $9 billion of this to send each vehicle owner $400 for each registered vehicle, up to two per person.

In this report, we estimate the poverty impact of this policy and compare it against a budget-neutral universal payment of about $270 per person. We find that 93% of Californians are in households that would benefit from the per-vehicle payment. Replacing that policy with a per-person payment would leave 56% of Californians better off, cut poverty 32% more, deep child poverty 118% more, and inequality 29% more.

## Why Californians might get $400 per vehicle

Like other goods and services, gasoline has gotten more expensive over the past year. But when [Russia invaded Ukraine on February 24](https://www.usnews.com/news/best-countries/slideshows/a-timeline-of-the-russia-ukraine-conflict), the global oil market contracted in anticipation of sanctions against the [world's third-largest oil producer](https://www.eia.gov/tools/faqs/faq.php?id=709&t=6). In the first two weeks of March, [gas prices jumped 20 percent nationwide](https://fred.stlouisfed.org/series/GASREGW).

<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=OoCX&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden; width:670px; height:525px;" allowTransparency="true" loading="lazy"></iframe>

The oil crunch has affected California similarly to the rest of the country. Compared to a year ago, as of April 19, AAA reports that [gasoline is up 44% in California and 43% nationwide](https://gasprices.aaa.com/?state=CA).

Governor Newsom announced his $11 billion package to address high gas prices on March 23, a week after they peaked. This package pauses the inflation adjustment for the gas and diesel taxes ($1.1 billion, as [Newsom's January budget](https://www.ebudget.ca.gov/2022-23/pdf/BudgetSummary/FullBudgetSummary.pdf#page=216) previously called for) and creates grants to encourage transit agencies to make transit free for three months ($750 million). The most expensive element is the $9 billion vehicle payment.

## How many cars California households own

The 2019 American Community Survey, which we use for this analysis[^1], reports a total of 25.7 million vehicles owned by households[^2]. That's an average of 0.92 per adult, though that ratio increases with income, and adults in poverty[^3] own 26% fewer vehicles than those not in poverty.


[^1]: This analysis uses PolicyEngine's open-source OpenFisca US microsimulation model. The code is available at [github.com/UBICenter/california-vehicle-payment](https://github.com/UBICenter/california-vehicle-payment).

[^2]: As of 2021, the DMV reported that California had [36.2 million registered vehicles and 27.5 million licensed drivers](https://www.dmv.ca.gov/portal/file/california-dmv-statistics-pdf/). 

[^3]: Our poverty estimates use the Census Bureau's [Supplemental Poverty Measure (SPM) research file](https://www.census.gov/data/datasets/time-series/demo/supplemental-poverty-measure/acs-research-files.html) for the American Community Survey. Unlike the Official Poverty Measure, the [SPM considers taxes, non-cash benefits, and local housing costs](https://www.census.gov/topics/income-poverty/supplemental-poverty-measure.html). California has had the highest SPM poverty rate of any state since the measure was introduced, [largely due to its high housing costs](https://www.ubicenter.org/california-ab65-calubi).


<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_1_1").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_1_1.html");
    });
  </script>
</div>
<div id = "graph_graph_1_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_1_2").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_1_2.html");
    });
  </script>
</div>
<div id = "graph_graph_1_2"></div>

## Benchmarking against a universal per-person payment

Allocating each household's vehicles randomly among the adults in each household, we estimate that the vehicle payment would cost $10.0 billion. This likely exceeds Newsom's estimate (which probably uses restricted DMV data) because households may concentrate vehicle ownership among specific adults rather than randomly, which would make fewer vehicles eligible due to the cap of two per person.

That $10 billion vehicle payment would reduce the poverty rate by 3.8%, roughly equally across age groups. However, distributing that $10 billion across each California resident yields a payment of $269 per person, and that would cut poverty by 1.3pp more than the vehicle payment.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_3_1").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_3_1.html");
    });
  </script>
</div>
<div id = "graph_graph_3_1"></div>

The per-person payment especially lowers child poverty, a [major determinant of child development](https://child-allowance.ubicenter.org/empirical.html). Compared to the vehicle payment, a per-person payment would have double the impact on deep child poverty (the share of children below half the poverty line).

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_5_1").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_5_1.html");
    });
  </script>
</div>
<div id = "graph_graph_5_1"></div>

These poverty effects form a pattern: the universal payments would have higher impacts on poverty rates overall, especially for children, but around the same impact on poverty among people aged 65 and older.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_7_1").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_7_1.html");
    });
  </script>
</div>
<div id = "graph_graph_7_1"></div>

On average, the per-person payment is more generous than the per-vehicle payment to households in the first five income deciles,[^4] and less generous to households in higher deciles. As a result, the per-person payment reduces inequality 29% more than the per-vehicle payment (the Gini index falls 0.88%, compared to 0.68%).


[^4]: We group all US households into ten groups of equal population size by their equivalised income according to [the OECD standard](https://www.oecd.org/economy/growth/OECD-Note-EquivalenceScales.pdf) (dividing by the square root of the number of people in the household).

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_9_1").load("{{site.baseurl}}assets/markdown_assets/california-vehicle-payment/graph_9_1.html");
    });
  </script>
</div>
<div id = "graph_graph_9_1"></div>

## Conclusion

California can achieve greater poverty and inequality reductions by replacing its vehicle payment with a personal payment. Doing so would yield other benefits, as well, especially when considering that Californians will expect similar policies in the future.

Most directly, paying people for owning vehicles encourages them to own more vehicles. A [1987 paper](https://lindseyresearch.com/wp-content/uploads/2021/12/NHTSA-2021-0053-1575-Exhibit-41-McCarthy-1996.pdf) found that each 1 percent reduction in vehicle prices increases vehicle purchases by 0.87 percent. Given [new vehicles cost about $47,000](https://www.kbb.com/car-news/average-new-car-price-tops-47000/) and [used vehicles cost about $28,000](https://www.kbb.com/car-news/average-used-car-price-now-over-28000/), a $400 payment lowers the cost by about 0.9 to 1.4 percent, increasing vehicle purchases by about one percent. But that's only one payment; to the extent that this policy announcement suggests to consumers that vehicle payments will repeat when gasoline gets more expensive in the future, that could be thousands of dollars over the life of a vehicle.

Those expectations will increase the number of vehicles on the road, which will harm the environment and public health. [Seven in eight new vehicles sold in California](https://www.gov.ca.gov/2022/02/25/california-leads-the-nations-zev-market-surpassing-1-million-electric-vehicles-sold/#:~:text=Over%20the%20past%2010%20years,other%20zero%2Demission%20vehicle%20metrics%2C) are powered by gasoline, and the transportation sector produces [41 percent of California's carbon emissions](https://ww2.arb.ca.gov/ghg-inventory-data) and [55% of US nitrogen oxide emissions](https://www.epa.gov/transportation-air-pollution-and-climate-change/smog-soot-and-other-air-pollution-transportation), which [causes respiratory diseases like asthma](https://www.epa.gov/no2-pollution/basic-information-about-no2).

More vehicles on the road also means more demand for gasoline, the good whose scarcity the program aims to address. Combined with the gas tax cut, these programs would partly offset themselves as that increased demand raises prices.

Californians without vehicles have not been immune from higher prices, and disproportionately they face inflation with lower incomes. Excluding them from payments misses an opportunity for effective, environmentally-friendly poverty reduction.