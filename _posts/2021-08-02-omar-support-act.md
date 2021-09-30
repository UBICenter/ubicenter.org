---
layout: post
current: post
cover: assets/images/ilhan-omar.jpg
navigation: True
title: "Ilhan Omar's Near-UBI Guaranteed Income Bill"
date: 2021-08-02
tags: [us]
subclass: "post"
author: [nate,max]
excerpt: "The House representative's SUPPORT Act tax credit would reach 99.6% of Americans."
class: post-template
useplotly: true

---

On Friday, July 30, Representative Ilhan Omar [introduced the SUPPORT Act of 2021](https://omar.house.gov/media/press-releases/rep-omar-introduces-guaranteed-income-bill-and-gdp-alternative-legislation), which would commit the US to studying and eventually implementing a national guaranteed income. The first phase of the bill would provide an annual $500 million in grants to fund and evaluate local guaranteed income pilot programs. In 2028, the bill would establish the Guaranteed Income Tax Credit (GITC), which would create an income floor across the entire United States. This paper describes the GITC's structure and estimates its budgetary and distributional impacts.


# The SUPPORT Act's Guaranteed Income Tax Credit

Beginning in 2028, the GITC would provide $1,200 per month for single filers and $2,400 for joint filers; it would also provide $600 per month for each dependent under age 18, but none for adult dependents like college students.[^1] Tax filers with adjusted gross income (AGI) above $75,000 ($112,500 for heads of household, $150,000 for joint filers) would have their annual payment reduced by $5 per $100 of AGI in excess of those thresholds. For example, a single childless adult with income of $100,000 would receive ($1,200 * 12) - (5% * $25,000) = $14,400 - $1,250 = $13,150.





<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_5_1").load("{{site.baseurl}}assets/markdown_assets/omar-support-act/graph_5_1.html");
    });
  </script>
</div>
<div id = "graph_graph_5_1"></div>

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_5_2").load("{{site.baseurl}}assets/markdown_assets/omar-support-act/graph_5_2.html");
    });
  </script>
</div>
<div id = "graph_graph_5_2"></div>

The 5% phase-out rate is significantly lower than other guaranteed income proposals, such as the New School's [Guaranteed Income for the 21st Century](https://drive.google.com/file/d/1UDFPwUYu2Rf4RGgXuOTacmBj2Gt9paAV/view). Lower phase-out rates avoids stark work disincentives, as benefit phase-outs operate identically to marginal tax rates; the GITC in effect levies a new 5% marginal tax rate on filers with income in the phase-out region. It also makes the bill similar to a full universal basic income; for example, married filers with at least two children would receive at least some of the GITC even with income above $1 million.


# Results

Simulating the policy with the 2019 Current Population Survey, we found that the GITC would cost $3.75 trillion per year if implemented today.[^2] Because the payments phase out slowly starting at relatively high incomes, 99.6% of people live in a family that will receive a payment.

The program would, for all intents and purposes, eliminate poverty, reducing the poverty rate by 96% and deep poverty by 98%, with larger effects for children. Two in three people still in poverty after the program are in families with negative current resources, a scenario typically associated with business losses.






<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_12_1").load("{{site.baseurl}}assets/markdown_assets/omar-support-act/graph_12_1.html");
    });
  </script>
</div>
<div id = "graph_graph_12_1"></div>

The GITC would also reduce inequality. The income share held by the top 10% would fall by 21%, and the income share held by the top 1% would fall by 29%. The Gini index, a broader measure of inequality, would fall 24%.

<div>
  <script>
    $(document).ready(function(){
      $("#graph_graph_14_1").load("{{site.baseurl}}assets/markdown_assets/omar-support-act/graph_14_1.html");
    });
  </script>
</div>
<div id = "graph_graph_14_1"></div>


# Conclusion

As of 2019, the Guaranteed Income Tax Credit would cost about a fifth of GDP, nearly doubling the federal budget. By 2028, however, the Congressional Budget Office [projects](https://www.cbo.gov/publication/57339) that GDP will be more than 40% higher than it was in [2019](https://www.bea.gov/news/2020/gross-domestic-product-fourth-quarter-and-year-2019-advance-estimate), and federal revenues will be more than 50% higher. Since the phase-out thresholds are set in nominal terms, the budgetary impact would be somewhat smaller in 2028 than our estimates suggest; nevertheless, it would be very costly, and without funding provisions, our distributional analysis is limited.

By providing a generous benefit without any work requirement or phase-in, the GITC would virtually end poverty. If the [monthly Child Tax Credit](https://www.ubicenter.org/advance-ctc) is any indication, though, operating the program through the tax code threatens its ability to reach the poorest families who don't normally file taxes. Making the GITC universal would enable it to operate outside the tax code, such as through the Social Security Administration (like [Senator Mitt Romney's child allowance proposal](ubicenter.org/family-security-act)) which could bring it the higher accuracy of Social Security payments; universalizing the GITC would add 11% to its cost.

The SUPPORT Act's Guaranteed Income Tax Credit may be the closest legislation to universal basic income the US has seen. While many important details are as yet undefined, it could mark the beginning of a new conversation around basic income legislation.


## Notes

[^1]: The [SUPPORT Act text](https://omar.house.gov/sites/omar.house.gov/files/OMARMN_046_SUPPORT%20Act.pdf) states: "In the case of an eligible individual, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to—(1) $14,400, plus (2) $600 multiplied by the number of dependents (as defined in section 152) under the age of 18 of the taxpayer." However, the accompanying [one-pager](https://omar.house.gov/sites/omar.house.gov/files/SUPPORT%20Act%20-%20One%20Pager%20and%20Section-By-Section%202021.pdf) specifies that the GITC provides $600 per month for child dependent and $2,400 for two-adult households. We assume the one-pager is correct.

[^2]: Code powering this analysis is available at [github.com/UBICenter/omar-support-act](http://github.com/UBICenter/omar-support-act).

