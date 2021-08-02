---
layout: post
current: post
cover: assets/markdown_assets/local_child_allowance_maps/pov_child_assembly_map_cover.png
navigation: True
title: "Mapping the impact of a $100 monthly child allowance"
date: 2021-08-02
tags: [us, child allowance, local]
subclass: "post"
author: [ben]
excerpt: "The policy would cut child poverty by a fifth nationwide, but effects would vary geographically."
class: post-template
useplotly: true
---

With the [recent expansion of the Child Tax Credit](http://ubicenter.org/advance-ctc), including full refundability, child poverty has a new relevance. State and local governments also have an opportunity to reduce child poverty through child allowances of their own. Building on our [state-level child allowance impacts](https://www.ubicenter.org/child-allowance-state-simulation), here we present two maps, for upper and lower state legislative districts, of a simple policy: $100 per month for each child under age 18.

_These may take a few seconds to load, and zooming will be slow. Sorry, we're working on it!_

# Map by lower state legislative district

For example, this shows each California Assembly district.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_14_1").load("{{site.baseurl}}assets/markdown_assets/local_child_allowance_maps/us_child_poverty_map_assembly.html");
    });
  </script>
</div>
<div id = "graph_graph_14_1"></div>

# Map by upper state legislative district

For example, this shows each California Senate district.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_14_2").load("{{site.baseurl}}assets/markdown_assets/local_child_allowance_maps/us_child_poverty_map_senate.html");
    });
  </script>
</div>
<div id = "graph_graph_14_2"></div>


# How we built it

All prior UBI Center analyses in the US have used the Current Population Survey March Supplement, which contains official estimates of the Official Poverty Measure and Supplemental Poverty Measure (SPM, which we favor for its inclusion of taxes, transfers, and housing costs). This is the most in-depth household survey, but because of its small sample size, the Census Bureau doesn’t release microdata at the local level.

This analysis instead uses the American Community Survey (ACS), which has a larger sample size and, accordingly, finer geographic detail. Only recently has the ACS provided a comprehensive poverty measure like the SPM, thanks to Census Bureau estimates described in [Fox, Glassman, and Pacas (2020)](https://www.census.gov/content/dam/Census/library/working-papers/2020/demo/SEHSD-WP2020-09.pdf).

To construct this map, we merged multiple datasets:

* Population by block (the Census Bureau’s finest geographical unit) from the 2010 Census Summary File 1 (via the [CensusData Python package](https://github.com/jtleider/censusdata))
* Population by block group from the 2019 ACS (via [NHGIS](https://www.nhgis.org/))
* A crosswalk from block (the Census’s smallest geographic unit) to state legislative district

From these datasets, we produced a block-level dataset with population (adjusted for growth from 2010 to 2019) and all geographic groupings (ACS public use microdata areas, census tracts, counties, and upper and lower state legislative districts). We’ve made this block-level dataset, along with aggregations by PUMA and legislative district which power these maps, available [on GitHub](https://github.com/UBICenter/local-child-allowance/tree/main/data).

