---
layout: post
current: post
cover: assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-0.png 
navigation: True
title: A budget-neutral version of Andrew Yang's Freedom Dividend
date: 2019-06-24T17:49:26.093Z
lastmod: 2021-03-25T15:18:37-04:00
tags: [us, andrew yang, vat]
class: post-template
subclass: 'post'
author: max
excerpt: Cutting the payment by about half would avoid increasing the deficit, but the result remains progressive.
images:
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-0.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-1.jpg"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-2.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-3.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-4.jpg"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-5.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-6.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-7.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-8.png"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-9.jpg"
 - "assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-10.png"


aliases:
- "/a-revenue-neutral-version-of-andrew-yangs-freedom-dividend-d7d517dbeeea"

---

[Part 1](distributional-analysis-of-andrew-yangs-freedom-dividend) of this two-part series analyzing Democratic presidential candidate Andrew Yang’s Freedom Dividend showed that the universal basic income policy would reduce poverty and inequality, while adding $1.4 trillion to the annual deficit. Using the same approach and assumptions (no labor market or macroeconomic effects), I find that a budget-neutral plan would provide each adult citizen $471 per month, rather than the $1,000 proposed by Yang. These payments would be offset by Yang’s funding sources: increases on existing taxes, addition of new taxes, and partial replacement of assistance programs.

Like the original Freedom Dividend, this budget-neutral plan would reduce poverty and inequality, and benefit most Americans. However, each of these effects would be muted, and a larger share of middle-income households would come out behind.

As in Part 1, I modeled the plan with the open-source Tax-Calculator software and its version of the Current Population Survey. Code and documentation for the analysis are available [here](https://github.com/UBICenter/ubi-center/tree/master/notebooks/yang).

### Modeling a budget-neutral Freedom Dividend

The Freedom Dividend is a set of seven policies:

1. $1,000 per month to every adult citizen
2. Rescinding of benefits for households who opt for the basic income (they can keep their current benefits if they want); the Freedom Dividend does not replace Social Security, Medicare, Medicaid, unemployment insurance, or housing
3. A 10 percent [value added tax](https://www.yang2020.com/policies/value-added-tax/) (VAT, a form of consumption tax common across Europe)
4. A 0.1 percent, $50 billion per year [financial transaction tax](https://www.yang2020.com/policies/financial-transaction-tax/) (FTT)
5. A $20 per ton [carbon tax](https://www.yang2020.com/policies/carbon-fee-dividend/) (Yang also proposes an additional $20 per ton carbon tax to fund clean energy investments, which is not modeled here)
6. Lifting the cap on Social Security contributions
7. Treating capital gains as ordinary income

Following the approach outlined in Part 1, I assume households decline the UBI if the combined value of their current benefits exceeds the UBI; estimate the incidence of carbon taxes, VAT, and FTT using analyses from the Tax Policy Center and the Treasury Department; and calculate the effect of the payroll and capital gains tax reforms with Tax-Calculator. I also assume that workers don’t respond to the new income or changing tax rates; see Part 1 for a discussion on potential macroeconomic effects.

The gross cost of a $1,000 UBI for adult citizens is $2.8 trillion, and after new taxes and benefit savings, the total deficit impact is $1.4 trillion per year (about 160% of the current deficit). Government saves $151 billion from households giving up benefits or declining the UBI to keep current benefits, and the remaining $1.2 trillion comes from tax reform.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-0.png#layoutTextWidth)

Varying the UBI amount shows that these funding measures with a $0 UBI would reduce the annual budget deficit by $1.2 trillion. The UBI amount that produces a $0 deficit impact is $471 per month.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-1.jpg#layoutTextWidth)

The gross cost of giving each adult citizen $478 per month is $1.3 trillion. $128 billion is saved from households declining the UBI or current benefits, and the remaining $1.17 trillion is from new taxes (tax revenue falls slightly because I assume consumption of goods and services that generate carbon tax revenue rises with the UBI).

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-2.png#layoutTextWidth)

### How the revenue sources work

In the original Freedom Dividend, 57 percent of the benefits savings came from SNAP (food stamps), and this share increases to 70 percent with the budget-neutral version. This follows from SNAP’s relatively wide reach and low monthly amount. For example, TANF and SSI have higher monthly amounts, and the share of dollars for these plans given up for UBI falls from more than half with the $1,000 per month plan to about 30 percent at $471 per month.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-3.png#layoutTextWidth)

The tax side is almost identical to the original Freedom Dividend, since the lower amount affects only the carbon tax. New taxes cost each decile an average of 8 percent of income, except the top decile which is cost 12 percent.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-4.jpg#layoutTextWidth)

### A budget-neutral Freedom Dividend would be progressively redistributive

The average household in the bottom 80 percent would see disposable incomes rise by about $3,000 per year, while the average household in the top 10 percent would lose about $21,000 per year.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-5.png#layoutTextWidth)

As a share of disposable income, those numbers are progressive at every decile, raising the bottom decile 47 percent and lowering the top decile by 9 percent (compared to +119 percent and -4 percent in the $1,000 plan).

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-6.png#layoutTextWidth)

Various measures of poverty and inequality would fall:

- **Poverty falls 35 percent**, as defined by the share of people in households with disposable income below the federal poverty guideline.
    Not an official poverty measure.
- **The Gini index (a measure of general inequality) falls 9 percent.**
- **The top 1 percent’s share of income falls 17 percent.**
- **The top 0.1 percent’s share of income falls 21 percent.**

These inequality measures reflect how the plan compresses the income distribution at both top and bottom: the budget-neutral Freedom Dividend raises the 10th income percentile by 17 percent, raises median income by 6 percent, and reduces the 90th percentile by 2 percent.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-7.png#layoutTextWidth)

### Most come out ahead, many come out behind

While the budget-neutral Freedom Dividend is progressive on a net basis and the bottom 8 deciles benefit on average, the new taxes outweigh the UBI for many households. Two thirds of Americans would benefit, including 46 percent who would see disposable incomes rise more than 5 percent; the third who come out behind includes 18 percent who lose more than 5 percent. While these net contributors are concentrated among households with income of $200,000 or more, about 20 percent of households with income under $75,000 also come out behind.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-8.png#layoutTextWidth)

High income households primarily come out behind because their tax liability would rise considerably, especially payroll and capital gains taxes. For example, using the UBI Center [Plan Explorer](http://plans.ubicenter.org), we can filter to one-adult households with income above $500,000, who would pay an average of $11,411 more in taxes each month. All households in this category would lose.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-9.jpg#layoutTextWidth)

Low income households primarily come out behind because they forego benefits to get the UBI, or vice versa, and only pay new taxes like VAT. For example, one-adult households with income below $25,000 gain an average of $251 per month on net, while 8 percent come out behind.

![](assets/images/2019-06-24-budgetneutral-version-of-andrew-yangs-freedom-dividend-10.png#layoutTextWidth)

Further filtering these to households that receive benefits, the net effect is +$97 per month and 21 percent see incomes fall. This subset includes 12 million people, 40 percent of all one-adult households with income below $25,000.

### Major policy tends toward disruption

Andrew Yang’s Freedom Dividend and its budget-neutral adaptation analyzed here would likely have a greater impact on poverty and inequality than any seriously discussed policy in recent U.S. history. For some, this egalitarian result would be worth major economic costs, including to their own pocketbook; others will oppose it for concern over the macro economy or their personal finances.

One thing is certain though: it’s hard to design major policy without disruption. If society determines how this disruption stacks up against other outcomes of interest (poverty, inequality, work incentives, economic growth), policymakers can design plans accordingly.

But can we have our cake and eat it, too? That’s the question the UBI Center intends to answer in developing UBI plans that balance disruption against other measurable outcomes. Optimizing for the deficit is just the start.

*Updated 2019–07–02 to remove unemployment insurance from the set of replaced benefits.*
