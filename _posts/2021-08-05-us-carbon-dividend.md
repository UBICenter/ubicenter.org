---
layout: post
current: post
cover: assets/markdown_assets/us-carbon-dividend/cover.jpg
navigation: True
title: "Carbon dividends as anti-poverty policy"
date: 2021-08-05
tags: [us, carbon pricing]
subclass: 'post'
author: max
excerpt: "A $100-per-ton carbon dividend would cut poverty by 10% and deep child poverty by 27%."
class: post-template
useplotly: True
---

The International Monetary Fund [estimates](https://www.imf.org/en/Publications/WP/Issues/2019/05/02/Global-Fossil-Fuel-Subsidies-Remain-Large-An-Update-Based-on-Country-Level-Estimates-46509) that the United States subsidized $649 billion of fossil fuels in 2015.
Meanwhile, only about [$20 billion](https://www.eesi.org/papers/view/fact-sheet-fossil-fuel-subsidies-a-closer-look-at-tax-breaks-and-societal-costs) of that is in the form of direct subsidies.
The remainder is the _implicit_ subsidy of misaligning the price of fossil fuels with their societal harms like air pollution and climate change.
That is, the vast majority of fossil fuel subsidies is the _absence of carbon pricing_.

All developed countries except the [US and Australia](https://citizensclimatelobby.org/laser-talks/carbon-prices-around-world/) cut down on fossil fuel subsidies by pricing carbon emissions.
Experts including [scientists](https://academic.oup.com/bioscience/advance-article/doi/10.1093/biosci/biab079/6325731) and the [vast majority](https://www.igmchicago.org/surveys/carbon-taxes-ii/) of [leading economists](http://econstatement.org) have called on the US to follow suit.
To offset higher prices consumers would face as a result of carbon pricing (or other climate measures), many of these experts suggest rebating the revenue to all Americans as a dividend.
[Two thirds](https://clcouncil.org/morning-consult-poll.pdf) of American voters support this policy, and as of this writing, 80 House Democrats have cosponsored the [Energy Innovation and Carbon Dividend Act](https://energyinnovationact.org/) (EICDA) which would make it a reality in the US.

Beyond the climate impacts of carbon dividend---policies like the EICDA are projected to [meet the IPCC's goal](https://www.nature.com/articles/s41558-020-0880-3) of net zero emissions by 2050 and [avert 295,000 deaths](https://www.nature.com/articles/nclimate2935) from air pollution in the first decade---many economists have [documented the](https://www.energypolicy.columbia.edu/sites/default/files/pictures/CGEP_Distributional_Implications_CarbonTax.pdf) [progressive](https://taxfoundation.org/carbon-tax/) [distributional](https://www.rff.org/publications/data-tools/carbon-pricing-calculator/) [impacts](https://www.peoplespolicyproject.org/wp-content/uploads/2018/09/CarbonTax.pdf) of carbon dividends.
As one example, University of Pennsylvania researcher [Kevin Ummel found](https://citizensclimatelobby.org/household-impact-study/) that the EICDA would benefit 96% of households in the bottom consumption quintile and 12% in the top quintile, after considering effects on prices, capital income, and the dividend.

Using Ummel's data[^ummel] and the 2018 American Community Survey,[^acsspm] I extend this research to estimate the poverty impacts of a carbon dividend[^cpsp] across a range of prices.[^code]
I find that carbon dividends reduce poverty roughly linearly with respect to the price, for example by 10% at $100 per ton. Effects are larger for child poverty, deep poverty, and especially deep child poverty.

[^ummel]: I'm grateful to Kevin Ummel for sharing and explaining his data and for his permission to use it in this paper.

[^acsspm]: I use the [American Community Survey Supplemental Poverty Measure research file](https://www.census.gov/data/datasets/time-series/demo/supplemental-poverty-measure/acs-research-files.html), which estimates the poverty measure inclusive of taxes, transfers, and housing costs, historically only available in the [Current Population Survey](https://www.census.gov/library/publications/2020/demo/p60-272.html).

[^cpsp]: The only other study I'm aware of that estimates the impact of a carbon dividend on poverty is from the [Columbia Center on Poverty and Social Policy](https://www.povertycenter.columbia.edu/news-internal/carbontax). They found that a carbon dividend of $42 per ton would reduce poverty by 1.1% and child poverty by 4.6%, where I found effects of 4% and 8%, respectively, for a $40 carbon dividend. Our analyses differed in terms of carbon footprint estimation in the Consumer Expenditure Survey (CPSP only considered direct energy consumption, where Ummel's data considered all consumption categories), poverty dataset (CPSP used the Current Population Survey where I used the American Community Survey), and other factors (e.g., CPSP imputed receipt of underreported benefits with the TRIM3 program, where I did not).

[^code]: All data and code powering this analysis is at [github.com/UBICenter/us-carbon-dividend](http://github.com/UBICenter/us-carbon-dividend).

# How big would the dividend be?

Carbon pricing proposals vary in their initial price and the rate at which they increase over time, though they do all increase in some way.
The EICDA starts at $15 per metric ton in 2021 and rises by $10 per year, while the Senate's [Save Our Future Act](https://www.whitehouse.senate.gov/news/release/whitehouse-and-schatz-introduce-save-our-future-act-to-charge-big-polluters-for-emissions-redirect-trillions-to-american-families-and-communities-harmed-by-pollution) starts at $54 per ton in 2023 and rises by an inflation-adjusted 6% per year (about $4 in the first year).
Since American households currently emit about [5 billion metric tons](https://www.rff.org/publications/data-tools/carbon-pricing-calculator/) of carbon per year, amounting to about 15 tons per person, each $10 carbon price would translate to a monthly dividend of 15 tons * $10 / 12 months = **$13**.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_1_2").load("{{site.baseurl}}assets/markdown_assets/us-carbon-dividend/dividend.html");
    });
  </script>
</div>
<div id = "graph_graph_1_2"></div>

# How would the carbon dividend affect overall poverty?

Poverty and deep poverty (the population share with income below half their poverty threshold) fall roughly linearly with respect to the carbon price: each $10 carbon price would reduce poverty by 1% and deep poverty by 1.2%. A carbon dividend of $100 per ton would reduce poverty by 10% and deep poverty by 12%.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_3_1").load("{{site.baseurl}}assets/markdown_assets/us-carbon-dividend/pov_line.html");
    });
  </script>
</div>
<div id = "graph_graph_3_1"></div>

# How would the carbon dividend affect poverty by age?

Child and adult poverty also fall linearly with the carbon price, but child poverty falls about three times as quickly. A $100 carbon price would reduce child poverty by 19% and deep child poverty by 27%.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_5_1").load("{{site.baseurl}}assets/markdown_assets/us-carbon-dividend/age.html");
    });
  </script>
</div>
<div id = "graph_graph_5_1"></div>

# How would the carbon dividend affect poverty by state?

Poverty impacts also vary geographically, largely in line with states' per-capita carbon emissions, which in turn correlate to [cold weather](https://doi.org/10.1016/S0928-7655(00)00027-0) and [low population density](https://www.sciencedirect.com/science/article/abs/pii/S0301421516300167?via%3Dihub). For example, consider the two extremes of how carbon dividends lower poverty:

* California ranks [#10 on average temperature](http://www.usa.com/rank/us--average-temperature--state-rank.htm), [#3 on population density](https://skyscraperpage.com/forum/showthread.php?t=211827), [#49 on per-capita carbon emissions](https://www.eia.gov/environment/emissions/state/analysis/), and #1 in terms of poverty reduction from a carbon dividend. A \$100 per ton carbon dividend would lower poverty in California by 14%, and lower deep child poverty by 30%.
* North Dakota ranks #49 on average temperature, #32 on population density, #2 on per-capita carbon emissions, and #50 in terms of poverty reduction from a carbon dividend. In fact, North Dakota is the only state for which a carbon dividend would increase poverty, though only by 3% at $100 per ton; child poverty would still fall, and its poverty rate would remain one of the lowest in the country.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_7_1").load("{{site.baseurl}}assets/markdown_assets/us-carbon-dividend/map.html");
    });
  </script>
</div>
<div id = "graph_graph_7_1"></div>

Politicians from [Bernie Sanders](https://grist.org/climate-energy/sanders-and-boxer-introduce-fee-and-dividend-climate-bill-greens-tickled-pink/) to [Pete Buttigieg](https://thehill.com/policy/energy-environment/444330-buttigieg-climate-plan-includes-a-carbon-tax) to [Mitt Romney](https://twitter.com/citizensclimate/status/1369059303995437058) have endorsed carbon dividends, primarily framing the dividend as a way to offset potential regressive effects of the carbon price.
However, the dividend more than neutralizes the carbon price: it makes a significant reduction to poverty in America. A $20 carbon dividend would cut poverty more than a fully-phased-in $15 minimum wage would,[^mw] while a $100 carbon dividend (as the US would reach within a decade under proposed legislation) would approach the impact of the [expanded Child Tax Credit](http://ubicenter.org/advance-ctc).[^ctc]

My estimates may even be conservative. For example, I assume that 100% of the carbon price is passed on to consumers, but [one study finds](https://cowles.yale.edu/sites/default/files/files/pub/d20/d2038-r.pdf) that only 70% is passed on. In his analysis of the EICDA, Ummel applies pass-through rates of 70%, 85%, and 100%, with the remainder borne by people in proportion to their investable assets; he finds that lower pass-through assumptions yield more progressive distributional impacts.

Carbon dividends would also create infrastructure for further cash assistance.
When the US government had to keep Americans afloat with relief checks in the Covid-19 pandemic, they relied on the IRS, and largely failed to reach nonfilers.
Had even a small universal payment program existed at the time, they could have simply increased the amount instead.

The carbon dividend is a simple policy that can help the US progress on a slew of objectives: climate change, air pollution, financial resilience, and, yes, even poverty.

[^mw]: The Congressional Budget Office [estimated](https://www.cbo.gov/publication/55681) that the Raise the Wage Act of 2021 would reduce the number of people in poverty by 0.7 million by 2028, or about 1.8% of the roughly 40 million people in poverty. A $20 carbon dividend would lower poverty by 2%. CBO applied the Official Poverty Measure rather than Supplemental Poverty Measure.

[^ctc]: Carbon dividends may also have greater success fulfilling their theoretical antipoverty potential, since they are universal and thus can be administered outside the tax system. The Child Tax Credit is expected to reach only 90% of eligible children, and the remaining 10% are disproportionately poor children whose parents don't earn enough to have to file taxes.
