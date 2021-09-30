---
layout: post
current: post
cover: assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-0.png 
navigation: True
title: Distributional analysis of Andrew Yang's Freedom Dividend
date: 2019-06-24T17:48:10.706Z
lastmod: 2021-03-25T15:18:46-04:00
tags: [us, andrew yang, vat]
class: post-template
subclass: 'post'
author: max


excerpt: The presidential candidate's basic income plan would cut poverty and inequality, but add to the deficit.
subtitle: 
images:
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-0.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-1.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-2.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-3.jpg"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-4.jpg"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-5.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-6.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-7.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-8.jpg"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-9.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-10.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-11.png"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-12.jpg"
 - "assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-13.jpg"


aliases:
- "/distributional-analysis-of-andrew-yangs-freedom-dividend-d8dab818bf1b"

---

Democratic presidential candidate Andrew Yang wants to give every adult citizen $1,000 per month, no strings attached. This idea is called universal basic income (UBI), though Yang calls his a [Freedom Dividend](https://www.yang2020.com/policies/the-freedom-dividend/), which he plans to fund with new taxes and an option for households to switch away from current benefits.

If Yang’s plan were implemented, who would come out ahead or behind? How would poverty, inequality, and the deficit change? What benefit programs would be most affected? To answer these questions, I applied the open-source Tax-Calculator software to the Census Bureau’s Current Population Survey, combined this with established analyses of the new taxes he proposes, and simulated the effect across the distribution of US households. This analysis is static, meaning it ignores behavioral and macroeconomic responses to tax, income, and deficit changes.

While the plan would add $1.4 trillion to the annual deficit, it would be highly progressive, significantly reducing poverty and inequality. 87 percent of Americans would come out ahead, including 90 percent of those in households earning under $50,000 and 54 percent of those in households earning $200,000 or more.

### Modeling the Freedom Dividend

The Freedom Dividend is a set of seven policies, marked here as progressive or regressive by the percentage effect on disposable income:

1. $1,000 per month to every adult citizen [progressive]
2. Rescinding of benefits for households who opt for the basic income (they can keep their current benefits if they want); the Freedom Dividend does not replace Social Security, Medicare, Medicaid, housing, or unemployment insurance [regressive]
3. A 10 percent [value added tax](https://www.yang2020.com/policies/value-added-tax/) (VAT, a form of consumption tax common across Europe) [regressive]
4. A 0.1 percent, $50 billion per year [financial transaction tax](https://www.yang2020.com/policies/financial-transaction-tax/) (FTT) [progressive]
5. A $20 per ton [carbon tax](https://www.yang2020.com/policies/carbon-fee-dividend/) (Yang also proposes an additional $20 per ton carbon tax to fund clean energy investments, which is not modeled here) [roughly flat]
6. Lifting the cap on Social Security contributions [progressive]
7. Treating capital gains as ordinary income [progressive]

My steps for modeling this reform are documented [here](https://github.com/UBICenter/ubi-center/blob/master/notebooks/yang/README.md).

### Pricing out the Freedom Dividend

The total cost of providing $12,000 per year to all 236 million adult citizens is $2.8 trillion. Of these, about 2 million decline the UBI because they get more in current benefits, saving $18 billion. The government saves $133 billion from people who decline their current benefits to get the more generous UBI. The new tax revenue raises $1.2 trillion, leaving the total unfunded cost at $1.4 trillion. This grows the deficit by 160 percent over the $896 billion [projected](https://www.cbo.gov/topics/budget) by the Congressional Budget Office for 2019.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-0.png#layoutTextWidth)

### How the revenue sources work

The Freedom Dividend is paid for with benefit savings and taxes. On the benefits side, roughly half of the savings come from Supplemental Nutrition Assistance Program (SNAP, a.k.a. food stamps). That is, half the benefit savings comes from people declining SNAP because the UBI would be more generous.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-1.png#layoutTextWidth)

Each of the five programs modeled — SNAP, Supplemental Security Income (SSI), Temporary Aid for Needy Families (TANF, a.k.a. “welfare”), and the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) — is mostly superseded by the UBI.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-2.png#layoutTextWidth)

On the other side of the revenue generation are taxes. Taken together, the five new taxes reduce by 7 percent the average income of households currently in the bottom nine deciles. The top decile pays 11 percent of income in new taxes, due largely to the elimination of the payroll tax cap and treatment of capital gains as ordinary income.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-3.jpg#layoutTextWidth)![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-4.jpg#layoutTextWidth)

### The Freedom Dividend benefits low-income households

Households feel the effect of the Freedom Dividend policy suite in multiple ways: they get the UBI itself (unless they are not citizens or elect to keep their current benefits instead), they decline benefits, they pay higher income taxes, and they pay higher prices on goods and services from the non-income taxes. To evaluate the effect of the policy as a whole, I compare their disposable income — income after taxes and transfers — before and after the policy.

Households in the bottom nine deciles see their disposable income rise about $10,000 on average, while households in the top decile lose an average of $8,000.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-5.png#layoutTextWidth)

This represents a highly progressive outcome, more than doubling the average disposable income of households in the bottom decile and reducing top-decile incomes by about 4 percent.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-6.png#layoutTextWidth)

Not all households within each decile experience the tax and benefit changes equally. For example, households in each decile may vary in their levels of SNAP receipt, capital gains, or citizenship. The blue in the chart below shows the share of people in households that would see higher disposable income, while orange is those who see less. Overall, 86 percent of people would come out ahead, though 10 to 15 percent of each income group up to $200,000 would come out behind (these are mostly non-citizens). Almost all households earning more than $500,000 would pay more in taxes than they’d receive from the Freedom Dividend.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-7.png#layoutTextWidth)

### Exploring effects for household types

UBI Center’s [interactive Plan Explorer](http://plans.ubicenter.org) shows the average effect and range of effects for households with selected characteristics. For example, after selecting a one-adult one-child household with income between $25,000 and $50,000 that receives benefits, this shows that households meeting that criteria come out ahead, on average.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-8.jpg#layoutTextWidth)

The calculator also shows the range of effects, similarly to the blue and orange chart above:

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-9.png#layoutTextWidth)

### The Freedom Dividend would reduce poverty and inequality

Across all measures, the Freedom Dividend would reduce poverty and income inequality.

One (unofficial) measure of poverty is the share of people in households with disposable income less than the federal poverty line. The Yang plan reduces this share by 74 percent, from 7.3 percent to 1.9 percent. Child poverty falls 54 percent, from 7.9 percent to 3.6 percent.

A common measure of inequality is the Gini index, which ranges from 0 (perfect equality) to 1 (a single household has all of society’s income). The Yang plan reduces the Gini index of disposable income by 15 percent, from 0.46 to 0.39.

Other measures of income inequality also fall under the Yang plan: the share of disposable income held by the top 1 percent falls by 24 percent, and the share held by the top 0.1 percent falls 29 percent.

These metrics follow from the full distribution of income rising, but rising especially at the low end. For example, median income rises 25 percent from $56k to $70k, and the 90th percentile rises 6 percent from $159k to $168k. But the 10th percentile rises 48 percent, from $19k to $29k.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-10.png#layoutTextWidth)![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-11.png#layoutTextWidth)

### Economic growth reducing the deficit

The [UBI page](https://www.yang2020.com/what-is-ubi/) of Yang’s website states that “The Roosevelt Institute projected that the economy would grow by approximately $2.5 trillion and create 4.6 million new jobs. This would generate approximately $800–900 billion in new revenue from economic growth and activity.”

The Roosevelt [study](https://rooseveltinstitute.org/publications/macroeconomic-effects-universal-basic-income-ubi/) this refers to, authored in 2017, considered a UBI plan that, like Yang’s, gives $1,000 per month to each adult. Unlike Yang’s, it is fully deficit-funded. It projects a GDP increase that phases in over time to reach about $2.4 trillion per year after 6 years (Scenario 3 below, units in billions). It also projects a 9.33 percent deficit increase and 2 percent employment increase.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-12.jpg#layoutTextWidth)

Given the US raises [27 cents](https://www.oecd.org/tax/revenue-statistics-united-states.pdf) per dollar of GDP, this $2.4 trillion would raise about $650 billion in new tax revenue, though this might be higher given the new taxes.

The [Penn-Wharton Budget Model](https://budgetmodel.wharton.upenn.edu/issues/2018/3/29/options-for-universal-basic-income-dynamic-modeling) came to a different conclusion in their analysis of a deficit-funded UBI of $500 per month per adult (a response to the Roosevelt study). They estimate that this would reduce GDP by 6.1 percent and reduce government revenue by 8.0 percent over its first decade. Penn-Wharton explains the difference in results by noting their empirically-driven choices to reduce labor supply in response to new income (the income effect) and reduce capital services in response to higher government debt.

![](assets/images/2019-06-24-distributional-analysis-of-andrew-yangs-freedom-dividend-13.jpg#layoutTextWidth)

Neither Roosevelt nor Wharton model the revenue measures Yang proposes: reducing benefits, increasing tax rates, and levying new taxes. Some of these will reduce labor supply, such as new taxes (through the substitution effect). Others will increase labor supply, such as moving people out of benefit programs with high marginal tax rates (also through the substitution effect), and the income effect of new taxes (which reduce after-tax income). The net effect of these changes is probably lower labor supply — likely due to workers reducing their work hours rather than dropping out of the labor market — but a full study would be warranted to estimate the magnitude.

Overall, Yang’s projection that his plan would raise between $800 and $900 billion in government revenue through economic growth is unlikely.

### An important discussion

Yang’s plan would grow the federal deficit substantially, but it would also produce a more egalitarian income distribution that would lift tens of millions out of poverty — even accounting for potentially lower economic growth. It demonstrates the importance of considering fiscal policies together: while the VAT and benefit reductions would be regressive on their own, the combination with progressive revenue sources and generous universal payments makes the plan highly progressive overall.

This is the first of a two-part series on the Freedom Dividend. Read Part 2 on a revenue-neutral version of the plan [**here**](budget-neutral-version-of-andrew-yangs-freedom-dividend).

*Updated 2019–07–02 to remove unemployment insurance as a replaced benefit.*
