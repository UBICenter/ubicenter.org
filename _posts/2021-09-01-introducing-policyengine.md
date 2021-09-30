---
layout: post
current: post
cover: assets/images/policyengine.png
navigation: True
title: Introducing PolicyEngine UK
date: 2021-09-01
tags: [policyengine, uk]
subclass: 'post'
author: [max,nikhil]
excerpt: Our new product democratises tax and benefit analysis. Try it at policyengine.org. 
class: post-template
---

## Try it at [policyengine.org](https://policyengine.org)


Here at the UBI Center, technology has long supported our mission to make universal basic income the world's most thoroughly researched economic policy.
Along with our [first analysis](https://www.ubicenter.org/distributional-analysis-of-andrew-yangs-freedom-dividend), we created [Plan Explorer](plans.ubicenter.org) to help people understand the impact of Andrew Yang's Freedom Dividend on households like theirs.
We've since integrated interactive graphics to a growing share of our reports.
And just last month, we launched the [Basic Income Builder](bib.ubicenter.org) to enable anyone to model the impact of various budget-neutral UBI policies on poverty and inequality in the US.

We've also built technology behind the scenes to model taxes and benefits as demanded by UBI policies.
Over the past year, we've developed [OpenFisca UK](https://github.com/PSLmodels/openfisca-uk/), the UK's first open source tax and benefit microsimulation model, and we've used it to produce [four reports](https://www.ubicenter.org/tag/uk/) and [three conference presentations](https://www.ubicenter.org/bien-2021) on UBI in the UK.
All of our technologies are open source, and they wouldn't be possible without the prior work of other open source projects ([OpenFisca](openfisca.org), [pandas](https://pandas.pydata.org/), [plotly](https://github.com/plotly), and [Tax-Calculator](http://taxcalc.pslmodels.org/), just to name a few).

Today, we're bringing together these interactive and microsimulation technologies into a new product: **[PolicyEngine](https://policyengine.org)**.
With PolicyEngine, anyone can reform the UK tax and benefit system, and see how it would affect the UK population as well as their own household.
See the video below for a quick overview of how PolicyEngine works.

<iframe width="420" height="315" src="https://www.youtube.com/embed/nv_gVtokikU" frameborder="0" allowfullscreen></iframe>

As an example, let's reproduce the reform we studied in July to [replace the personal allowance with a UBI](https://www.ubicenter.org/personal-allowance).
On the _Policy_ page, start by selecting _Tax > Income tax > Allowances_, and drag the _Personal allowance_ slider to £0.[^params]
Then head to _Benefits > UBI_, and toggle _AutoUBI_ to calculate the budget-neutral UBI.
PolicyEngine finds that repealing the personal allowance funds a UBI of £29 per week, matching our July report.

[^params]: PolicyEngine uses policy parameters as of 2021-01-01, when the personal allowance was £12,500, rather than its current value of £12,570. We're working on updating policy parameters to the current date. Our FAQ shows other caveats.

From there, you can click _Simulate on the population_ to see the poverty impact (-29%, mirroring our report), the budget impact by provision, and other distributional effects.
You can also enter information about your household to see how the reform would affect your net income, as well as the impact to your net income and marginal tax rates depending on your earnings.

PolicyEngine supports millions of policy reforms, including those not involving UBI.
We'll be enhancing it every week and leveraging it for all future UK research.
We're also working on bringing PolicyEngine to the US and hope to expand its reach more broadly (please consider [supporting these development and hosting costs](https://ubicenter.org/donate)).

What policy reforms have you been waiting to simulate?
Try them out at [policyengine.org](https://policyengine.org) and [let us know what you think](https://zej8fnylwn9.typeform.com/to/XFFu15Xq)!

[_Join us at 6PM BST today for a tour and Q&A of PolicyEngine._](https://us02web.zoom.us/meeting/register/tZAlde6prz4sHNH7Pj1AWRokyrnr7yJDK7tt)
