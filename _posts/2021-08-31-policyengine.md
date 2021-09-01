---
layout: post
current: post
cover: assets/images/policyengine.png
navigation: True
title: Introducing PolicyEngine UK
date: 2021-08-31
tags: [policyengine, uk]
subclass: 'post'
author: [max,nikhil]
excerpt: Our new product democratises tax and benefit analysis. Try it at policyengine.org. 
class: post-template
---

## Try it at [policyengine.org](https://policyengine.org)


Here at the UBI Center, technology has long supported our mission to make universal basic income the world's most thoroughly researched economic policy. Along with our [first analysis](https://www.ubicenter.org/distributional-analysis-of-andrew-yangs-freedom-dividend), we created [Plan Explorer](plans.ubicenter.org) to help people understand the impact of Andrew Yang's Freedom Dividend on households like theirs. We've since integrated interactive graphics to a growing share of our reports. And just last month, we launched the [Basic Income Builder](bib.ubicenter.org) to enable anyone to model the impact of various budget-neutral UBI policies on poverty and inequality in the US.

We've also built technology behind the scenes to model taxes and benefits as demanded by UBI policies. Over the past year, we've developed [OpenFisca UK](https://github.com/PSLmodels/openfisca-uk/), the UK's first open source tax and benefit microsimulation model, and we've used it to produce [four reports](https://www.ubicenter.org/tag/uk/) and [three conference presentations](https://www.ubicenter.org/bien-2021) on UBI in the UK. All of our technologies are open source, and they wouldn't be possible without the prior work of other open source projects ([OpenFisca](openfisca.org), [pandas](https://pandas.pydata.org/), [plotly](https://github.com/plotly), and [Tax-Calculator](http://taxcalc.pslmodels.org/), just to name a few).

Today, we're bringing together these interactive and microsimulation technologies into a new product: **[PolicyEngine](policyengine.org)**. With PolicyEngine, anyone can reform the UK tax and benefit system, and see how it would affect the UK population as well as their own household.

As an example, let's reproduce the reform we studied in July to [replace the personal allowance with a UBI](https://www.ubicenter.org/personal-allowance). On the _Policy_ page, start by selecting _Tax > Income tax > Allowances_, and drag the _Personal allowance_ slider to £0.[^1] Then head to _Benefits > UBI_, and toggle _AutoUBI _to calculate the budget-neutral UBI. PolicyEngine finds that repealing the personal allowance funds a UBI of £29 per week, matching our July report.

From there, you can 

PolicyEngine supports millions of policy reforms, and we'll be enhancing it every week. 


<!-- Footnotes themselves at the bottom. -->
## Notes

[^1]:
     PolicyEngine uses policy parameters as of 2021-01-01, when the personal allowance was £12,500, rather than its current value of £12,570. We're working on updating policy parameters to the current date. Our FAQ shows other caveats.