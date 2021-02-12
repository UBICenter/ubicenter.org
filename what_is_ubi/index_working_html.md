---
layout: post
current: post
cover: assets/images/bear.jpg
navigation: True
title: A Full and Comprehensive Style Test
date: 2012-09-01 10:00:00
tags:
class: post-template
subclass: 'post'
author: john
---

<head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

</head>





# Overview

1 in 7 children in the United States lives in poverty, [raising](https://heckmanequation.org/resource/invest-in-early-childhood-development-reduce-deficits-strengthen-the-economy/) stress and crime rates, [worsening](https://www.sciencedirect.com/science/article/abs/pii/S1876285915003836) educational outcomes, and [shrinking](https://www.nap.edu/catalog/25246/a-roadmap-to-reducing-child-poverty) the economy by up to \\$1 trillion annually. Research shows that giving money to families with children, as [most developed countries do](https://www.vox.com/future-perfect/2019/3/6/18249290/child-poverty-american-family-act-sherrod-brown-michael-bennet), reduces each of these issues. A child allowance is a policy that gives families an equal amount for each child.

This project examines child allowances through various lenses:
* [**Simulations**](simulation.md) quantifying the effects of child allowance policies (deficit- and tax-funded) on poverty and inequality across US states.
* [**Research**](empirical.md) on the effects of child allowances and similar policies on children, based on randomized controlled trials and other empirical techniques.
* [**Policy context**](policies.md) of existing US child benefits and child allowances in other countries.

For example, this interactive map is one of several visualizations in our [simulations page](simulation.md).
<div>
<script>
$(document).ready(function(){

  $("#div1").load("graph1.html");

});
</script>
</div>
<div id="div1"></div>
We also review the evidence around child allowances from the United States and Canada, and a special deep dive into research from sub-Saharan Africa, where randomized cash transfer rollouts produce particularly high-quality estimates. For example, cash transfer programs consistently reduced consumption poverty (below). See the [**full paper**](empirical.md) for evidence across other outcomes like education and health.
<div>
<script>
$(document).ready(function(){

  $("#div2").load("graph2.html");

});
</script>
</div>
<div id="div2"></div>
Finally, we consider the political state of child allowances, such as the [American Family Act](https://www.bennet.senate.gov/public/index.cfm/american-family-act), which would ensure all low-income children in the US receive the full benefits of the Child Tax Credit, and how such a policy would align US child benefits with those from other developed countries.

By efficiently reducing child poverty, child allowances provide kids with basic needs, improve access to opportunity, and invest in our future.

*Created by Max Ghenis, Nate Golden, John Walker, and Matt Gilbert.*

