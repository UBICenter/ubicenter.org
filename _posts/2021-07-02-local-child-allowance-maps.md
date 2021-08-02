---

layout: post

current: post

cover: ubicenter.org/assets/markdown_assets/local_child_allowance_maps/pov_by_assembly_cover.png

navigation: True

title: Mapping a $100 Child Allowance

date: 2021-07-02

tags: [us,child allowance,local]

subclass: 'post'

Author: [ben, nicholas]

excerpt: states could reduce child poverty by around 20%

class: post-template

useplotly: true

---

div>

  script>

    $(document).ready(function(){

  $("#graph_graph_structured_mobile_1").load("{{site.baseurl}}ubicenter.org/assets/markdown_assets/local_child_allowance_maps/“us_child_poverty_map_assembly.html”

);

    });

  /script>

/div>

div id = "graph_graph_structured_mobile_1">/div>

$("#graph_graph_structured_mobile_1").load("{{site.baseurl}}ubicenter.org/assets/markdown_assets/local_child_allowance_maps/“us_child_poverty_map_senate.html.html”

);

    });

  /script>

div>

div id = "graph_graph_structured_mobile_1">/div>

With the recent expansion of the child tax credit, including full refundability, child poverty has a new relevance. Of course, the problem of 1 in 7 children in [poverty](https://child-allowance.ubicenter.org/) was always there. But with Democrats, and some Republicans, aiming at the issue, advocates have a window to further cut the devastating effects of growing up in poverty. We looked at one policy to further reduce child poverty.

All prior UBI Center analyses in the US have used the Current Population Survey March Supplement, which contains official estimates of the Official Poverty Measure and Supplemental Poverty Measure (SPM, which we favor for its inclusion of taxes, transfers, and housing costs). This is the most in-depth household survey, but because of its small sample size, the Census Bureau doesn’t release microdata at the local level.

This analysis instead uses the American Community Survey (ACS), which has a larger sample size and, accordingly, finer geographic detail. Only recently has the ACS provided a comprehensive poverty measure like the SPM, thanks to Census Bureau estimates described in [Fox, Glassman, and Pacas (2020)](https://www.census.gov/content/dam/Census/library/working-papers/2020/demo/SEHSD-WP2020-09.pdf).

To construct this map, we merged multiple datasets:



* Population by block (the Census Bureau’s finest geographical unit) from the 2010 Census Summary File 1 (via the [CensusData Python package](https://github.com/jtleider/censusdata))
* Population by block group from the 2019 ACS (via [NHGIS](https://www.nhgis.org/))
* A crosswalk from block (the Census’s smallest geographic unit) to state legislative district

From these datasets, we produced a block-level dataset with population (adjusted for growth from 2010 to 2019) and all geographic groupings (ACS public use microdata areas, census tracts, counties, and upper and lower state legislative districts). We’ve made this block-level dataset, along with aggregations by PUMA and legislative districts which power this map, available [on GitHub](https://github.com/UBICenter/local-child-allowance/tree/main/data).

Using the mappings, we modeled a reform of a $100 monthly child allowance in every state. Specifically, we looked at the change in child poverty rate by state assembly and senate districts. This allows policy makers and advocates to show local and state-level leaders the difference $100 per month can make.  

Some districts, like Minnesota’s 18B or Wisconsin's 95th, see reductions in poverty of over 50%. The average assembly or senate district district across the country sees a reduction in poverty of just over 20%. Almost every district has a significant drop in poverty, so promoters of this policy almost everywhere can see positive benefits. In the appendix, one can look at how such a policy would affect poverty rates in their state.

### Appendix

#   Change in poverty by state

ubicenter.org/assets/markdown_assets/local_child_allowance_maps/“ff_pov_bs_kids.png”
