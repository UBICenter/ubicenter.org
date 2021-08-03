---
layout: post
current: post
cover: assets/images/2021-07-21-basic-income-builder/cover.png
navigation: True
title: Introducing the Basic Income Builder
date: 2021-07-21
tags: [us]
subclass: 'post'
author: [will, max, nate]
excerpt: Our new tool lets you design and analyze budget-neutral universal basic income policies in real time.
class: post-template
usemathjax: true
---

# Try the Basic Income Builder at [bib.ubicenter.org](http://bib.ubicenter.org)

Using Python and Plotly Dash’s dashboarding tools, we've created the Basic Income Builder: an interactive calculator that uses U.S. Census microdata to simulate distributional effects of a customizable UBI policy program. Users can experiment with a wide variety of inputs, from the size of the and type of taxation to reforms of the existing safety net programs. The calculator then produces interactive data visualizations that allow the user to explore the proposal's effect on the poverty rate for selected demographics, the poverty gap, and an estimate of what share of individuals come out ahead. Read on for more information, or try it yourself at [bib.ubicenter.org](http://bib.ubicenter.org).


# Background

Our recent research at the UBI Center has demonstrated the remarkable effectiveness of unconditional cash transfers in reducing poverty and inequality across different demographics and regions in the United States. We have found that the UBI shrinks [racial poverty and wealth gaps](https://www.ubicenter.org/how-universal-basic-income-would-affect-the-black-white-poverty-and-wealth-gaps), reduces poverty among [people with disabilities](https://www.ubicenter.org/ada30), and is more progressive than cancelling [student loan debt](https://www.ubicenter.org/student-debt) in terms of wealth inequality.

Inspired by calculators such as [Tax Justice Now](https://taxjusticenow.org/#/#makeYourOwnTaxPlan), [UBI Calculator](https://ubicalculator.com/), and PSL’s [Tax Brain](https://compute.studio/PSLmodels/Tax-Brain/new/), and building on our prior work with the [UBI Plan Explorer](plans.ubicenter.org), we created Basic Income Builder, an interactive, customizable policy simulation tool built on our own research on UBI proposals. We sought to create a tool that is useful for policy analysts and policy makers at both the state and federal level, while yielding comprehensible results for a general audience.

As our research has shown that funding Basic Income with a [flat tax](https://www.ubicenter.org/us-flat-tax) of 25% or more would reduce both poverty and inequality, we can create a funding mechanism that funds a robust UBI program, but does not require the user to create or adjust complicated income tax brackets. 

All code powering this calculator is at [github.com/UBICenter/us-calc](https://github.com/UBICenter/us-calc), and the app is hosted on the open source [Compute Studio platform](http://compute.studio).[^hank]

[^hank]: We're grateful to Hank Doupe of Compute Studio for technical assistance and hosting of this app.


# Data

We use three years of data (2017-2019) from the Annual Social and Economic Supplement (ASEC) of the Current Population Survey (CPS). The CPS is a monthly survey of U.S. households conducted by the U.S. Census Bureau and the Bureau of Labor Statistics. The CPS is conducted for the purposes of finding employment and earnings statistics of all individuals 15 and over in the household. Data is reported on the level of the individual persons in the household.

The ASEC provides additional information such as after-tax money income and non-cash benefits. The ASEC also calculates the poverty thresholds for each unit used in our calculations. The ASEC includes all CPS survey respondents in March, with additional oversamples from other months. 

The ASEC provides weighted individual and household level economic and demographic variables that we use to determine the total revenue impacts of our available tax, benefit, and eligibility criteria, as well as the impact on poverty and inequality for the entire population, and the impact on poverty rates for a number of selected demographics.

We use the Census Bureau’s Supplemental Poverty Measure (SPM) rather than the official poverty measure. The SPM resource measure is cash income plus in-kind benefits minus non discretionary expenses (including taxes, out of pocket health expenses, and work-related expenses). The SPM poverty thresholds are based on a core of annually updated core expenditures, adjusted for the size of the SPM resource unit and geographical variation in the cost of living. 

All of our simulation’s results with respect to poverty are calculated in terms of SPM resources, adjusted for the size of the UBI benefit, as well as any changes to the tax and benefit system selected by the user. 

The SPM resource unit is a broadened definition of the traditional Census family of related individuals, expanded to include any cohabiters and their relatives who are likely to share resources. We use the Gini coefficient of SPM resources among SPM units as our primary inequality measure.

Our data is limited in two primary ways:



1. The systematic underreporting of means-tested benefits in survey responses; depending on the benefit, up to half may be missing from the Current Population Survey ([Meyer Mok and Sullivan 2015](https://harris.uchicago.edu/files/underreporting.pdf)).
2. The underreporting of incomes above one million dollars, due to the Census Bureau’s income “top-coding” which intends to avoid disclosure of respondents’ personally identifiable data.

# Simulation

The user does not select a UBI benefit amount directly – rather, the user selects from a number of budget-neutral “pay-fors”, which produces a benefit size as an output.

On the tax side, users can repeal the personal income tax and the employee-side payroll tax. In addition, there is a slider available for the user to select an additional flat tax of 0% to 50% on all adjusted gross income (AGI) above $0. 

On the benefit side, the user can repeal the Child Tax Credit, Supplemental Security Income (SSI), Supplemental Nutrition Assistance Program (SNAP, formerly food stamps), Earned Income Tax Credit, Unemployment Benefits, and the Low Income Heating and Energy Assistance Program (LIHEAP).

Users may also select whether adults, children, and/or non-citizens are eligible for benefits.

We can describe our model as follows, where $$t$$ is the additional tax rate (0% to 50%) on all AGI above $0 as selected by user and $$NT_i$$ is the value of a new user-specified tax on AGI for SPM unit $$i$$:



$$NT_i = t * \max(AGI_i, 0)$$

RT is the value of SPM unit’s taxes paid that have been repealed by the user, where IT refers to income taxes paid and PT refers to employee-side payroll taxes. Where $$r_n$$ represents a Boolean where a value of $$r_n=1$$ indicates that the user has chosen to repeal the benefit, and $$r_n=0$$ if not.

$$RT_i = r_{IT}IT_i + r_{PT}PT_i$$

We define $$RB$$ as the value of SPM unit’s benefits that have been repealed by the user.

$$RB_i = r_{CTC} * CTC_i + r_{SSI} * SSI_i + r_{SNAP} * SNAP_i + r_{EITC} * EITC_i + r_{UI} * UI_i + r_{LIHEAP} * LIHEAP_i$$

Thus, the total revenue raised by the user is equal to:

$$Revenue = \sum_i NT_i - RT_i + RB_i$$

The new UBI amount paid out to each eligible beneficiary is simply equal to:

$$UBI = \frac{\it Revenue}{\it NumberOfBeneficiaries}$$

We then adjust the SPM resources of each unit to account for the new UBI payment, as well as the earlier changes made to taxes and benefits. The new SPM resource amount is expressed by the following equation, where n represents the number of eligible UBI beneficiaries in the SPM unit.

$$NewSPMResources_i = CurrentSPMResources_i + UBI * n_i + RT_i -NT_i - B_i$$

We then assign a new value indicating poverty status for each person belonging to an SPM unit where their new SPM resources are below the Census-provided SPM poverty threshold. We then divide the count of all individuals living under this poverty line by the total population.

The poverty gap is the sum of the total amount of additional resources required to lift each SPM unit to the SPM poverty threshold. Using our new SPM resources value for each SPM unit i, we calculate the poverty gap with the following formula:

$$PovertyGap = \sum_i \max(SPMPovertyThreshold_i - NewSPMResources_i, 0)$$


# Results

To illustrate Basic Income Builder's capabilities, we present the results of three different budget-neutral UBI reforms. Each reform provides an equal UBI to child and adult citizens.

In the first reform, we repeal all six available benefits while holding all else constant; this funds a $64 monthly UBI. To illustrate how our app works in practice, the below screenshot shows the configuration necessary to create this scenario:

![alt_text](assets/images/2021-07-21-basic-income-builder/us-calc-results-image-1.png)

While this leaves most of the population at least slightly better off, it causes poverty and inequality to increase across all categories, as shown by the simulation results below.

![img](assets/images/2021-07-21-basic-income-builder/us-calc-results-image-2.png)

In the second reform, we keep all taxes and benefits as is, but apply an additional 1% income tax on top of the existing system. This funds a $31 monthly benefit, but reduces poverty and inequality across all measures.

![alt_text](assets/images/2021-07-21-basic-income-builder/us-calc-results-image-3.png)

Our third reform entails a repeal of the existing income tax system (preserving payroll taxes and benefits), replaced with a 25% flat income tax. This funds a $400 monthly UBI while leaving 51% of Americans better off, while reducing poverty overall by 39% and across each demographic group by between 21% and 55%.


<table>
  <tr>
   <td>
   </td>
   <td>Baseline
   </td>
   <td>Repeal All Benefits
   </td>
   <td>1% Income Tax Increase
   </td>
   <td>25% Flat tax, repeal income tax
   </td>
  </tr>
  <tr>
   <td>Monthly UBI
   </td>
   <td> 
   </td>
   <td>$64
   </td>
   <td>$31
   </td>
   <td>$400
   </td>
  </tr>
  <tr>
   <td>Share better off
   </td>
   <td> 
   </td>
   <td>0.641
   </td>
   <td>0.641[^1]
   </td>
   <td>0.513
   </td>
  </tr>
  <tr>
   <td>Average change in resources per person
   </td>
   <td> 
   </td>
   <td>$0
   </td>
   <td>$0
   </td>
   <td>$0
   </td>
  </tr>
  <tr>
   <td>Poverty Gap (Billions USD)
   </td>
   <td>$173 B
   </td>
   <td>+19.1%
   </td>
   <td>-6.1%
   </td>
   <td>-41.7%
   </td>
  </tr>
  <tr>
   <td>Gini Index
   </td>
   <td>0.446
   </td>
   <td>+2.2%
   </td>
   <td>-1.4%
   </td>
   <td>-8.0%
   </td>
  </tr>
  <tr>
   <td>Poverty rate
   </td>
   <td>0.128
   </td>
   <td>+20.9%
   </td>
   <td>-6.1%
   </td>
   <td>-38.5%
   </td>
  </tr>
  <tr>
   <td>  Child
   </td>
   <td>0.139
   </td>
   <td>+42.3%
   </td>
   <td>-8.3%
   </td>
   <td>-45.7%
   </td>
  </tr>
  <tr>
   <td>  Adult
   </td>
   <td>0.125
   </td>
   <td>+13.6%
   </td>
   <td>-5.4%
   </td>
   <td>-36.1%
   </td>
  </tr>
  <tr>
   <td>  People with Disabilities
   </td>
   <td>0.203
   </td>
   <td>+18.2%
   </td>
   <td>-6.2%
   </td>
   <td>-55.1%
   </td>
  </tr>
  <tr>
   <td>  White
   </td>
   <td>0.089
   </td>
   <td>+12.8%
   </td>
   <td>-6.3%
   </td>
   <td>-46.6%
   </td>
  </tr>
  <tr>
   <td>  Black
   </td>
   <td>0.201
   </td>
   <td>+26.4%
   </td>
   <td>-7.5%
   </td>
   <td>-52.3%
   </td>
  </tr>
  <tr>
   <td>  Hispanic
   </td>
   <td>0.201
   </td>
   <td>+28.6%
   </td>
   <td>-5.3%
   </td>
   <td>-21.1%
   </td>
  </tr>
</table>


To demonstrate Basic Income Builder's state-level capabilities, we return to the reform that replaces existing income taxes with a 25% flat income tax, focusing on North Carolina as an example. When selecting North Carolina from the state menu and leaving everything else unchanged, the calculator shows the effect of the federal reform on North Carolina. The UBI amount is the same ($400 per month), but other distributional effects differ, and we can see that North Carolinians come out ahead by an average of $276 per person per year.

When selecting “State” as the Reform level, the 25% flat income tax instead replaces the North Carolina state income tax. This results in a larger UBI, primarily due to North Carolina’s state income tax raising less revenue than the federal income tax in North Carolina. Consequently, the poverty impacts are substantially greater with this reform, even as it’s no longer a net inflow to the state.


<table>
  <tr>
   <td>
   </td>
   <td>Baseline (NC)
   </td>
   <td>25% Flat Tax, Federal
   </td>
   <td>25% Flat Tax, State
   </td>
  </tr>
  <tr>
   <td>Monthly UBI
   </td>
   <td> 
   </td>
   <td>$400
   </td>
   <td>$561
   </td>
  </tr>
  <tr>
   <td>Share better off
   </td>
   <td> 
   </td>
   <td>0.554
   </td>
   <td>0.635
   </td>
  </tr>
  <tr>
   <td>Average change in resources per person
   </td>
   <td> 
   </td>
   <td>$276
   </td>
   <td>$0
   </td>
  </tr>
  <tr>
   <td>Poverty Gap (Billions USD)
   </td>
   <td>$5 B
   </td>
   <td>-44.6%
   </td>
   <td>-58.1%
   </td>
  </tr>
  <tr>
   <td>Gini Index
   </td>
   <td>0.449
   </td>
   <td>-10.2%
   </td>
   <td>-26.6%
   </td>
  </tr>
  <tr>
   <td>Poverty rate
   </td>
   <td>0.136
   </td>
   <td>-44.9%
   </td>
   <td>-68.1%
   </td>
  </tr>
  <tr>
   <td>Child
   </td>
   <td>0.149
   </td>
   <td>-57.8%
   </td>
   <td>-85.6%
   </td>
  </tr>
  <tr>
   <td>Adult
   </td>
   <td>0.132
   </td>
   <td>-40.9%
   </td>
   <td>-62.5%
   </td>
  </tr>
  <tr>
   <td>People with Disabilities
   </td>
   <td>0.210
   </td>
   <td>-55.5%
   </td>
   <td>-73.4%
   </td>
  </tr>
  <tr>
   <td>White
   </td>
   <td>0.099
   </td>
   <td>-49.3%
   </td>
   <td>-69.8%
   </td>
  </tr>
  <tr>
   <td>Black
   </td>
   <td>0.203
   </td>
   <td>-62.8%
   </td>
   <td>-76.2%
   </td>
  </tr>
  <tr>
   <td>Hispanic
   </td>
   <td>0.198
   </td>
   <td>+5.1%
   </td>
   <td>-50.2%
   </td>
  </tr>
</table>


For each of these scenarios, checking the “Children” and “Non-citizens” boxes reveals that including children and non-citizens in the UBI produces larger poverty and inequality reductions. This aligns with other research, such as [Ghenis (2020)](https://www.ubicenter.org/how-universal-basic-income-can-keep-poverty-from-rising-amid-covid19).


# Future research

We aim to improve Basic Income Builder in the future in several ways:

* Addressing income data deficiencies by incorporating data from the IRS Public Use File
* Addressing benefit deficiencies by imputing unreported benefits with algorithms like PSL’s [CPS Transfer Augmentation Model](https://github.com/PSLmodels/C-TAM)
* Adjusting for labor supply responses to the changes in the tax code, any effects of repealed benefits on marginal tax rates for low-income individuals, or the income effects of the UBI itself.
* Supporting side-by-side comparison of different user specified proposals. 
* Including more tax and benefit reforms on both the federal level, such as repealing deductions.
* Relaxing the requirement for budget-neutrality; instead of determining the UBI amount by changing taxes and benefits, the user could select the desired UBI amount and explore different ways to meet that target.


# Conclusion

The UBI Center Basic Income Builder provides users with access to rapid experimentation and analysis to determine the effects of UBI. Some results are intuitive, such as the regressiveness of replacing benefits with UBI without also raising additional tax revenue, while other results may surprise some audiences, such as the large effects on poverty from even modest taxes—even flat income taxes. We hope that this tool and others like it empower the public to learn more about public policy impacts and that they ultimately produce more evidence-based policymaking.
