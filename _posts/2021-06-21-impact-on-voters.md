---
layout: post
current: post
cover: assets/images/2021-06-15-yang-nyc/cover.jpg
navigation: True
title: The impact of a UBI on likely voters
date: 2021-06-21
tags: [us,ubi,elections]
subclass: 'post'
author: max
excerpt: A UBI would leave the majority of likely voters off in most states
class: post-template
---

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# The impact of universal basic income on likely voters


## Nate Golden   |   June 2021



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



# Abstract

While previous UBI Center research has focused on the policy implications of a UBI it is important to also discuss its politics. Most non-UBI proposals from politicians involve an array of complicated tax credits and deductions that leave many voters confused about how they are impacted personally by the policy. A UBI funded by simple taxation would not only bring more winners than losers, it would be clear to the winners that they will benefit from the plan. In this paper I simulate two different UBI policies and find that about two-thirds of Americans would be better off with a budget neutral UBI funded by a flat tax on income. However, not all Americans are eligible so I zoom in on eligible and predicted voters and find that 59 percent and 53 percent would be winners respectively. Those numbers rise to 65 and 60 percent if non-voting populations (children and non-citizens) are excluded from a UBI. Political research suggests that there is some link between a person’s economic self-interest and their vote suggesting that there may be political benefits to targeting eligible voters and demonstrating the natural tension between policy and politics.


# Introduction

Unlike more complicated policies, a flat income tax funded UBI creates clear cut-off points for winners and losers based solely on a family's size and income. Empirical evidence has shown that voters are at least partially motivated to vote in their own economic self-interest. Thus, there may be some political advantages to UBI proposals that create a majority of winners. Yet, the percentage of winners from UBI proposals does not not perfectly align with support. A recent [review](https://www.jainfamilyinstitute.org/assets/how-to-frame-guaranteed-income-policy-lit-review-jfi.pdf) of UBI polling conducted by the Jain Family Institute found that support for a UBI typically ranges between 40 and 50 percent. Literature suggests that these numbers could rise if voters trust that the UBI will materially benefit their lives.

These findings may have implications for the 2022 congressional elections. If the Democrats maintain or build on their majority, they may be able to pass a larger share of President Biden’s agenda. If Republicans are able to grab control of either chamber, they will be able to block the Democrats plans until the next presidential election. With so much on the line, party strategists will be developing plans to win voters, particularly in key battleground states. One strategy is simply to run on policy reforms that will benefit the voters and hope that this will sway their decision. In the following section of this paper I conduct a literature review on whether voters act in their own self-interests.


# Are voters self-interested?

In 1984, Stanley Feldman, a professor at Stonybrook University, [analyzed](https://www.jstor.org/stable/586090) the existing research on whether people make political changes based on their own financial well-being. Feldman found competing evidence: some research suggested that voters did change behavior and others did not. Feldman ultimately concluded that voter decisions are modestly based on their own economic considerations, saying, “when government policies have a direct impact on them and they attribute responsibility to the government, people do alter their evaluations accordingly.” 

A decade later, Leonard Shabman and Kurt Stephenson questioned the validity of previous papers exploring self-interested voter theorems. The authors contended that preceding papers that used Census tract and voter precinct data do not accurately capture the behaviors of individuals. In their [paper](https://www.jstor.org/stable/4226891?seq=10#metadata_info_tab_contents), Shabman and Stephenson examined the impact of a bond proposal in Roanoke that would benefit about 10,000 out of the 100,000 residents. The taxes from the bill were estimated to increase the average resident's monthly utility bill by approximately $25, suggesting that the policy would have many more losers than winners. The bond passed with 56 percent support, though net winners from the bill were more likely to support the bill than net losers. The authors concluded that many voters are motivated by self-interest, but others do act more altruistically.

More recently, a 2021 [paper](http://economics.mit.edu/files/19248) from Antoine Levy at the Massachusetts Institute of Technology found that Emmanuel Macron’s promise to abolish a broad-based housing tax shifted voters most substantially in areas with higher median home prices. Levy used high frequency online search, polling, and prediction market data to show that the timing of the proposal corresponded with an increase in his polling numbers and his market-based predicted chances of victory.

In aggregate, empirical research suggests that the electorate does change their voting behavior in accordance to their own financial well-being and that proper messaging around proposals can further sway voters.


# Data and methodology

In the first part of my [analysis](https://colab.research.google.com/drive/1kXPES5SdYjIli9vCPOs-b3gnYGBsVCwc?usp=sharing) I ran data from the Current Population Survey voter supplements of November 2018 and 2020 through a Random Forest Classifier to create a model that predicted an adult citizens probability of voting on thirteen key demographics. A more detailed description of each demographic can be found at the Census Bureau's [website](https://www.census.gov/programs-surveys/cps.html). I then combined the vote predicting algorithm with the three years of data from the Census Bureau’s Annual Social and Economic Supplement (ASEC) to assign each individual a predicted probability of voting score ranging from 0 to 1. I used the economic data from the ASEC to simulate the impact of two different UBI models. The first model issued a flat tax of 10 percent and evenly redistributed the revenue to all Americans including children and non-citizens. The second model kept the same tax but only shared the dividends with adult citizens, as to target eligible voters.

Finally, I calculated the share of winners from each proposal across all 50 states and DC and divided my analysis into three categories: the full population, eligible voters (adult citizens), and predicted voters


# Results

Table 1 below displays the thirteen demographics used in my analysis and their feature importance. Age was the strongest indicator on probability to vote and sex was the weakest. 

**Table 1: Importance of features in a random forests model predicting voter turnout in 2018 and 2020**


<table>
  <tr>
   <td><strong>Demographic</strong>
   </td>
   <td><strong>Feature Importance</strong>
   </td>
  </tr>
  <tr>
   <td>Age
   </td>
   <td>0.241
   </td>
  </tr>
  <tr>
   <td>Education level
   </td>
   <td>0.139
   </td>
  </tr>
  <tr>
   <td>State
   </td>
   <td>0.112
   </td>
  </tr>
  <tr>
   <td>Family income
   </td>
   <td>0.083
   </td>
  </tr>
  <tr>
   <td>Citizen
   </td>
   <td>0.074
   </td>
  </tr>
  <tr>
   <td>County
   </td>
   <td>0.073
   </td>
  </tr>
  <tr>
   <td>Marital status
   </td>
   <td>0.069
   </td>
  </tr>
  <tr>
   <td>Employment status
   </td>
   <td>0.069
   </td>
  </tr>
  <tr>
   <td>Core-based statistical area size
   </td>
   <td>0.055
   </td>
  </tr>
  <tr>
   <td>Race
   </td>
   <td>0.026
   </td>
  </tr>
  <tr>
   <td>Hispanic
   </td>
   <td>0.021
   </td>
  </tr>
  <tr>
   <td>Hourly wage
   </td>
   <td>0.019
   </td>
  </tr>
  <tr>
   <td>Sex
   </td>
   <td>0.018
   </td>
  </tr>
</table>


I found that a flat tax funded UBI would benefit 65 percent of Americans but only 59 percent and 53 percent of eligible and predicted voters respectively. Because children and non-citizens cannot vote, including them in UBI proposals reduces the impact on the voting population. On the other hand, 60 percent of all Americans would be winners from a flat tax funded UBI that excluded children and non-citizens. However, these exclusions would generate higher returns for voters. 65 percent of eligible voters would be better off under this model and 60 percent of predicted voters. These differences detail how the optimal policy and optimal politics often do not align. The results for both simulations of every state can be found in Table 4 of the appendix.



**Table 2: Population shares benefiting from UBI policies**


<table>
  <tr>
   <td>UBI scope
   </td>
   <td>Share of Americans
   </td>
   <td>Share of eligible voters
   </td>
   <td>Share of predicted voters
   </td>
  </tr>
  <tr>
   <td>All Americans
   </td>
   <td>64.5
   </td>
   <td>59.0
   </td>
   <td>53.3
   </td>
  </tr>
  <tr>
   <td>Adult citizens
   </td>
   <td>59.1
   </td>
   <td>64.9
   </td>
   <td>59.6
   </td>
  </tr>
</table>


Cook Political Report has identified [six key 2022 Senate races](https://cookpolitical.com/ratings/senate-race-ratings): Arizona, Georgia, North Carolina, Ohio, Pennsylvania, and Wisconsin. In each of the six battleground states a majority of predicted voters are net winners from the budget neutral UBI and flat tax. A higher share of predicted voters are better off when children and non-citizens are excluded.

**Table 3: Population shares benefiting from UBI policies in six 2022 battleground states**


<table>
  <tr>
   <td>
   </td>
   <td colspan="3" >UBI including all Americans
   </td>
   <td colspan="3" >UBI including adult citizens only
   </td>
  </tr>
  <tr>
   <td>State
   </td>
   <td>Overall
   </td>
   <td>Eligible Voters
   </td>
   <td>Predicted Voters
   </td>
   <td>Overall
   </td>
   <td>Eligible Voters
   </td>
   <td>Predicted Voters
   </td>
  </tr>
  <tr>
   <td>Arizona
   </td>
   <td>72.8
   </td>
   <td>68.5
   </td>
   <td>63.1
   </td>
   <td>69.1
   </td>
   <td>73.2
   </td>
   <td>67.8
   </td>
  </tr>
  <tr>
   <td>Georgia
   </td>
   <td>69.1
   </td>
   <td>63.9
   </td>
   <td>58.7
   </td>
   <td>64.1
   </td>
   <td>69.9
   </td>
   <td>65.0
   </td>
  </tr>
  <tr>
   <td>North Carolina
   </td>
   <td>69.0
   </td>
   <td>64.6
   </td>
   <td>59.0
   </td>
   <td>63.7
   </td>
   <td>69.8
   </td>
   <td>64.6
   </td>
  </tr>
  <tr>
   <td>Ohio
   </td>
   <td>64.5
   </td>
   <td>60.1
   </td>
   <td>54.2
   </td>
   <td>64.8
   </td>
   <td>68.0
   </td>
   <td>62.5
   </td>
  </tr>
  <tr>
   <td>Pennsylvania
   </td>
   <td>62.1
   </td>
   <td>57.7
   </td>
   <td>51.7
   </td>
   <td>60.9
   </td>
   <td>65.0
   </td>
   <td>59.4
   </td>
  </tr>
  <tr>
   <td>Wisconsin
   </td>
   <td>62.8
   </td>
   <td>57.7
   </td>
   <td>53.0
   </td>
   <td>63.1
   </td>
   <td>66.5
   </td>
   <td>62.2
   </td>
  </tr>
</table>



# Conclusion

In my model, a flat income tax funded UBI benefits 65 percent of voters. In a previous [analysis](https://www.ubicenter.org/budget-neutral-version-of-andrew-yangs-freedom-dividend), Max Ghenis found similar results with a budget-neutral version of Andrew Yang’s Freedom Dividend (68 percent of people were winners). However, as a tool to win elections, campaigns can increase the share of eligible and predicted voters that are better off by excluding non-voting populations such as children and non-citizens. These results highlight the tensions between optimal policy and optimal politics and leave many open questions for campaigns and politicians to answer.


# 


# Appendix

**Table 4: Population shares benefiting from UBI policies in all states and Washington, D.C.**


<table>
  <tr>
   <td>
   </td>
   <td colspan="3" >UBI including all Americans
   </td>
   <td colspan="3" >UBI excluding children and non-citizens
   </td>
  </tr>
  <tr>
   <td><strong>State</strong>
   </td>
   <td><strong>Overall</strong>
   </td>
   <td><strong>Eligible Voters</strong>
   </td>
   <td><strong>Predicted Voters</strong>
   </td>
   <td><strong>Overall</strong>
   </td>
   <td><strong>Eligible Voters</strong>
   </td>
   <td><strong>Predicted Voters</strong>
   </td>
  </tr>
  <tr>
   <td>US
   </td>
   <td>64.5
   </td>
   <td>59
   </td>
   <td>53.3
   </td>
   <td>59.1
   </td>
   <td>64.9
   </td>
   <td>59.6
   </td>
  </tr>
  <tr>
   <td>AK
   </td>
   <td>65.6
   </td>
   <td>59.1
   </td>
   <td>52.7
   </td>
   <td>62.6
   </td>
   <td>64.2
   </td>
   <td>57.8
   </td>
  </tr>
  <tr>
   <td>AL
   </td>
   <td>71.7
   </td>
   <td>67.6
   </td>
   <td>62.8
   </td>
   <td>69.5
   </td>
   <td>73.8
   </td>
   <td>69
   </td>
  </tr>
  <tr>
   <td>AR
   </td>
   <td>72.8
   </td>
   <td>68.5
   </td>
   <td>63
   </td>
   <td>69.1
   </td>
   <td>73.2
   </td>
   <td>67.7
   </td>
  </tr>
  <tr>
   <td>AZ
   </td>
   <td>67.4
   </td>
   <td>60.5
   </td>
   <td>54.8
   </td>
   <td>59.3
   </td>
   <td>65.1
   </td>
   <td>60
   </td>
  </tr>
  <tr>
   <td>CA
   </td>
   <td>64.6
   </td>
   <td>58.1
   </td>
   <td>51.9
   </td>
   <td>54.5
   </td>
   <td>62.8
   </td>
   <td>57
   </td>
  </tr>
  <tr>
   <td>CO
   </td>
   <td>55.4
   </td>
   <td>48.7
   </td>
   <td>43.8
   </td>
   <td>50.2
   </td>
   <td>56.5
   </td>
   <td>51.7
   </td>
  </tr>
  <tr>
   <td>CT
   </td>
   <td>54.9
   </td>
   <td>48.9
   </td>
   <td>43.4
   </td>
   <td>48.4
   </td>
   <td>54.7
   </td>
   <td>49.5
   </td>
  </tr>
  <tr>
   <td>DC
   </td>
   <td>44.3
   </td>
   <td>39.4
   </td>
   <td>33.1
   </td>
   <td>40.3
   </td>
   <td>43.8
   </td>
   <td>37.3
   </td>
  </tr>
  <tr>
   <td>DE
   </td>
   <td>62.2
   </td>
   <td>58
   </td>
   <td>53.7
   </td>
   <td>60.4
   </td>
   <td>65.8
   </td>
   <td>61.2
   </td>
  </tr>
  <tr>
   <td>FL
   </td>
   <td>69.1
   </td>
   <td>64
   </td>
   <td>59.8
   </td>
   <td>63.1
   </td>
   <td>70.5
   </td>
   <td>66.9
   </td>
  </tr>
  <tr>
   <td>GA
   </td>
   <td>69.1
   </td>
   <td>63.9
   </td>
   <td>58.7
   </td>
   <td>64.1
   </td>
   <td>69.9
   </td>
   <td>65.1
   </td>
  </tr>
  <tr>
   <td>HI
   </td>
   <td>63.3
   </td>
   <td>57.8
   </td>
   <td>52.7
   </td>
   <td>57.9
   </td>
   <td>62.3
   </td>
   <td>57.2
   </td>
  </tr>
  <tr>
   <td>IA
   </td>
   <td>65.5
   </td>
   <td>59.2
   </td>
   <td>55.3
   </td>
   <td>61.6
   </td>
   <td>65.9
   </td>
   <td>62
   </td>
  </tr>
  <tr>
   <td>ID
   </td>
   <td>71.2
   </td>
   <td>64.9
   </td>
   <td>60.3
   </td>
   <td>65.7
   </td>
   <td>69.8
   </td>
   <td>65.4
   </td>
  </tr>
  <tr>
   <td>IL
   </td>
   <td>60.2
   </td>
   <td>54.7
   </td>
   <td>48.9
   </td>
   <td>55.5
   </td>
   <td>60.6
   </td>
   <td>55.2
   </td>
  </tr>
  <tr>
   <td>IN
   </td>
   <td>67.3
   </td>
   <td>61.6
   </td>
   <td>56.2
   </td>
   <td>64.8
   </td>
   <td>67.9
   </td>
   <td>63.2
   </td>
  </tr>
  <tr>
   <td>KS
   </td>
   <td>65.6
   </td>
   <td>60.2
   </td>
   <td>56.1
   </td>
   <td>59.6
   </td>
   <td>65.7
   </td>
   <td>61.7
   </td>
  </tr>
  <tr>
   <td>KY
   </td>
   <td>70.2
   </td>
   <td>66.8
   </td>
   <td>60.9
   </td>
   <td>67.8
   </td>
   <td>71.6
   </td>
   <td>65.8
   </td>
  </tr>
  <tr>
   <td>LA
   </td>
   <td>71.8
   </td>
   <td>67.4
   </td>
   <td>62.1
   </td>
   <td>69.5
   </td>
   <td>72.5
   </td>
   <td>67.6
   </td>
  </tr>
  <tr>
   <td>MA
   </td>
   <td>52
   </td>
   <td>47.6
   </td>
   <td>42.3
   </td>
   <td>46.5
   </td>
   <td>53.3
   </td>
   <td>48.1
   </td>
  </tr>
  <tr>
   <td>MD
   </td>
   <td>52.6
   </td>
   <td>46
   </td>
   <td>40.9
   </td>
   <td>44.5
   </td>
   <td>50.1
   </td>
   <td>44.3
   </td>
  </tr>
  <tr>
   <td>ME
   </td>
   <td>64
   </td>
   <td>59.8
   </td>
   <td>54.7
   </td>
   <td>66
   </td>
   <td>68.6
   </td>
   <td>64.1
   </td>
  </tr>
  <tr>
   <td>MI
   </td>
   <td>63.6
   </td>
   <td>59.5
   </td>
   <td>55
   </td>
   <td>62.7
   </td>
   <td>66.5
   </td>
   <td>62.3
   </td>
  </tr>
  <tr>
   <td>MN
   </td>
   <td>56.1
   </td>
   <td>50.8
   </td>
   <td>45.7
   </td>
   <td>52.7
   </td>
   <td>57.6
   </td>
   <td>53.1
   </td>
  </tr>
  <tr>
   <td>MO
   </td>
   <td>65.2
   </td>
   <td>60.5
   </td>
   <td>55.4
   </td>
   <td>63.5
   </td>
   <td>66.6
   </td>
   <td>62
   </td>
  </tr>
  <tr>
   <td>MS
   </td>
   <td>78.4
   </td>
   <td>74.4
   </td>
   <td>70.2
   </td>
   <td>79
   </td>
   <td>79.7
   </td>
   <td>76.1
   </td>
  </tr>
  <tr>
   <td>MT
   </td>
   <td>68
   </td>
   <td>63.7
   </td>
   <td>59
   </td>
   <td>68.8
   </td>
   <td>70.6
   </td>
   <td>66.2
   </td>
  </tr>
  <tr>
   <td>NC
   </td>
   <td>69
   </td>
   <td>64.6
   </td>
   <td>59.2
   </td>
   <td>63.7
   </td>
   <td>69.8
   </td>
   <td>64.7
   </td>
  </tr>
  <tr>
   <td>ND
   </td>
   <td>62.9
   </td>
   <td>56.9
   </td>
   <td>52.6
   </td>
   <td>59.5
   </td>
   <td>62.7
   </td>
   <td>58.5
   </td>
  </tr>
  <tr>
   <td>NE
   </td>
   <td>63
   </td>
   <td>56.4
   </td>
   <td>50.6
   </td>
   <td>56.8
   </td>
   <td>62.5
   </td>
   <td>57.1
   </td>
  </tr>
  <tr>
   <td>NH
   </td>
   <td>52.9
   </td>
   <td>48.9
   </td>
   <td>45
   </td>
   <td>53.6
   </td>
   <td>57.4
   </td>
   <td>53.6
   </td>
  </tr>
  <tr>
   <td>NJ
   </td>
   <td>54.5
   </td>
   <td>49.9
   </td>
   <td>44.8
   </td>
   <td>49.4
   </td>
   <td>57
   </td>
   <td>52.7
   </td>
  </tr>
  <tr>
   <td>NM
   </td>
   <td>75
   </td>
   <td>69.2
   </td>
   <td>62.6
   </td>
   <td>71.2
   </td>
   <td>74.8
   </td>
   <td>68.6
   </td>
  </tr>
  <tr>
   <td>NV
   </td>
   <td>68.1
   </td>
   <td>61.5
   </td>
   <td>57.1
   </td>
   <td>62.1
   </td>
   <td>67.4
   </td>
   <td>63.4
   </td>
  </tr>
  <tr>
   <td>NY
   </td>
   <td>61.4
   </td>
   <td>55.5
   </td>
   <td>49.8
   </td>
   <td>54.7
   </td>
   <td>61.1
   </td>
   <td>55.5
   </td>
  </tr>
  <tr>
   <td>OH
   </td>
   <td>64.5
   </td>
   <td>60.1
   </td>
   <td>54.2
   </td>
   <td>64.8
   </td>
   <td>68
   </td>
   <td>62.5
   </td>
  </tr>
  <tr>
   <td>OK
   </td>
   <td>70.9
   </td>
   <td>65.2
   </td>
   <td>59.3
   </td>
   <td>65
   </td>
   <td>69.6
   </td>
   <td>64.1
   </td>
  </tr>
  <tr>
   <td>OR
   </td>
   <td>60.4
   </td>
   <td>54.7
   </td>
   <td>49.1
   </td>
   <td>56
   </td>
   <td>61.5
   </td>
   <td>56.1
   </td>
  </tr>
  <tr>
   <td>PA
   </td>
   <td>62.1
   </td>
   <td>57.7
   </td>
   <td>51.6
   </td>
   <td>60.9
   </td>
   <td>65
   </td>
   <td>59.3
   </td>
  </tr>
  <tr>
   <td>RI
   </td>
   <td>59.2
   </td>
   <td>53.9
   </td>
   <td>47.4
   </td>
   <td>56
   </td>
   <td>60.5
   </td>
   <td>54.3
   </td>
  </tr>
  <tr>
   <td>SC
   </td>
   <td>68
   </td>
   <td>63.5
   </td>
   <td>58.9
   </td>
   <td>67.9
   </td>
   <td>70.4
   </td>
   <td>65.8
   </td>
  </tr>
  <tr>
   <td>SD
   </td>
   <td>67.4
   </td>
   <td>61.1
   </td>
   <td>56
   </td>
   <td>65.2
   </td>
   <td>68.1
   </td>
   <td>63.5
   </td>
  </tr>
  <tr>
   <td>TN
   </td>
   <td>70.5
   </td>
   <td>66.1
   </td>
   <td>60.2
   </td>
   <td>69.1
   </td>
   <td>72.2
   </td>
   <td>66.6
   </td>
  </tr>
  <tr>
   <td>TX
   </td>
   <td>68.9
   </td>
   <td>61.8
   </td>
   <td>55.2
   </td>
   <td>58.4
   </td>
   <td>66.7
   </td>
   <td>60.8
   </td>
  </tr>
  <tr>
   <td>UT
   </td>
   <td>67.9
   </td>
   <td>60.2
   </td>
   <td>56
   </td>
   <td>55.7
   </td>
   <td>61.6
   </td>
   <td>57.3
   </td>
  </tr>
  <tr>
   <td>VA
   </td>
   <td>57.9
   </td>
   <td>52.4
   </td>
   <td>46.3
   </td>
   <td>51.5
   </td>
   <td>57.7
   </td>
   <td>51.6
   </td>
  </tr>
  <tr>
   <td>VT
   </td>
   <td>58.9
   </td>
   <td>54.8
   </td>
   <td>49.7
   </td>
   <td>59.5
   </td>
   <td>62.1
   </td>
   <td>57.3
   </td>
  </tr>
  <tr>
   <td>WA
   </td>
   <td>58
   </td>
   <td>52.2
   </td>
   <td>46.9
   </td>
   <td>53
   </td>
   <td>59
   </td>
   <td>54
   </td>
  </tr>
  <tr>
   <td>WI
   </td>
   <td>62.8
   </td>
   <td>57.7
   </td>
   <td>52.9
   </td>
   <td>63.1
   </td>
   <td>66.5
   </td>
   <td>62.1
   </td>
  </tr>
  <tr>
   <td>WV
   </td>
   <td>74.6
   </td>
   <td>71.3
   </td>
   <td>66.1
   </td>
   <td>76.4
   </td>
   <td>78.3
   </td>
   <td>73.9
   </td>
  </tr>
  <tr>
   <td>WY
   </td>
   <td>68.5
   </td>
   <td>63.2
   </td>
   <td>58.4
   </td>
   <td>64.5
   </td>
   <td>67
   </td>
   <td>62.7
   </td>
  </tr>
</table>

