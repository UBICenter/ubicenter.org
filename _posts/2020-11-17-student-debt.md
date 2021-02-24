---
layout: post
current: post
cover: 
navigation: True
title: Student debt cancellation is less progressive than universal payments
date: 2020-11-17
tags: [blog]
class: post-template
subclass: 'post'
author: nate
---

<head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>


Over 40 million Americans possess over \\$1.5 trillion in student debt. And as new borrowers take out loans faster than old borrowers pay them back, that number is [increasing with time](https://www.newyorkfed.org/microeconomics/hhdc.html).

This problem has led to Democrats across the ideological spectrum to advocate for student debt relief. In the 2020 primary, Bernie Sanders had the most generous [plan](https://berniesanders.com/issues/free-college-cancel-debt/), calling for the cancellation of all outstanding student debt regardless of a person’s income. Also in the primary, Elizabeth Warren [proposed](https://elizabethwarren.com/plans/affordable-higher-education) cancelling up to \\$50,000 in student debt, phasing out for households with income above \\$100,000; in September 2020, she and Senate Minority Leader Chuck Schumer [introduced a resolution](https://www.politico.com/f/?id=00000174-9b5b-d59c-a174-df5f0b960000) calling on Biden to cancel \\$50,000 in debt per person through executive order (the resolution didn't mention phasing out the cancellation with income).   Back in April, President-elect Joe Biden [recommended](https://medium.com/@JoeBiden/joe-biden-outlines-new-steps-to-ease-economic-burden-on-working-people-e3e121037322) forgiving a minimum of \\$10,000 of student debt per person.

In this paper, I analyze which Americans would benefit the most from student debt cancellation and examine how it compares to budget-equivalent universal payments. I find that, across a range of distributional outcomes, each student debt cancellation plan would be less progressive than a universal payment of the same total cost.
## Who holds the debt?

First, a caveat: data on student debt is incomplete. The Federal Reserve's Survey of Consumer Finances (SCF) is the primary source of wealth microdata, powering inequality statistics, detailed breakdowns of assets and liabilities, and microsimulations like mine. However, it only counts people in a household's \Primary Economic Unit,\ meaning economically independent young adults living with parents are excluded. As a result, the SCF understates total student debt by about a third, compared to aggregate data sources like the [G.19](https://www.federalreserve.gov/releases/g19/current/) and [Consumer Credit Panel](https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/pdf/hhdc_2019q4.pdf). The missing student debt is disproportionately held by [young people](https://www.peoplespolicyproject.org/2019/06/27/low-income-people-have-more-student-debt-than-realized/) and people in the [bottom and top income quintiles](https://www.brookings.edu/blog/up-front/2019/06/28/who-owes-the-most-student-debt/). While my colleagues and I aim to refine the data, the SCF is currently the best available source for this sort of analysis, so I use it here while acknowledging its limitations.

That said, the 2019 SCF reports \\$1.1 trillion of total student debt,[^debt] held by households representing one in four Americans. Some demographics are more likely to hold debt than others:[^hhdemo]

[^debt]: The Federal Reserve Bank of New York has [estimated](https://www.newyorkfed.org/microeconomics/hhdc.html) total student debt to be $1.54 trillion as of the second quarter of 2020.

[^hhdemo]: Because the SCF collects data at the household level, all demographics are represented by the demographic of the head of household.

*   Black Americans are the most likely to have student debt, while Hispanic Americans are the least likely, with 33 percent and 18 percent of people possessing student debt respectively.
*   Young people are more likely to hold student debt than any other age group: 40 percent of people under 35 have student debt compared to just 2 percent of those who are 75 or older.  
*   Income quintiles[^quintiles] follow a bell curve, with the highest amount of debt held by the middle class and smaller amounts held by the lowest and highest quintile.
*   Americans living in poverty[^poverty] are less likely to possess student debt than Americans living above the poverty line.

The chart below (and others like it included in this paper) allow you to compare the results across race, education level, age groups, income quintiles, net worth quintiles, and poverty status.


[^quintiles]: I assign households to income and net worth quintiles based on per-capita income and net worth, respectively, weighted by person such that each quintile has the same population. Inequality statistics are also based on per-capita income and net worth and weighted by person.

[^poverty]: I classify a household as in poverty if its official [2019 poverty guideline](https://aspe.hhs.gov/2019-poverty-guidelines) (defined by Health and Human Services) exceeds its total income (including in-kind benefits like food assistance, and in this case, student loan forgiveness).

<button onclick="f1()">Click to show code</button>
<div id="code_graph1" style="display: none;">
  <pre>
    <code>
# Import libraries
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import microdf as mdf
import plotly.graph_objects as go

race = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/race_debt_ubi%20(1).csv')
education = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/education_debt_ubi.csv')
age = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/age_debt_ubi.csv')
income = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/income_debt_ubi%20(1).csv')
networth = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/networth_debt_ubi%20(1).csv')
poor = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/poor_debt_ubi.csv')
all2 = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/all2.csv')
racial_wealth_gap = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/racial_wealth_gap%20(2)')
scf = pd.read_csv('https://github.com/UBICenter/ed_debt_vs_ubi/raw/main/scf_raw2')

race2 = race.drop([4])
education2 = education.drop([4])
age2 = age.drop([6])
income2 = income.drop([5])
networth2 = networth.drop([5])
poor2 = poor.drop([2])

# Colors from https://material.io/design/color/the-color-system.html
BLUE = '#1976D2'
DARK_BLUE = '#1565C0'
LIGHT_BLUE = '#90CAF9'
GRAY = '#BDBDBD'

colors = [GRAY,] * 5

colors2 = [GRAY,] * 7

colors3 = [GRAY,] * 6

colors4 = [GRAY,] * 3

fig = go.Figure()

fig.add_trace(go.Bar(x=race2['race'], y=race2['percent_has_debt'], 
                     text=race2['percent_has_debt'], name='race',
                     showlegend=False, marker_color=colors))

fig.add_trace(go.Bar(x=education2['edcl'], y=education2['percent_has_debt'],
                     text=education2['percent_has_debt'], name='education',
                     visible = False, showlegend=False, marker_color=colors))

fig.add_trace(go.Bar(x=age2['agecl'], y=age2['percent_has_debt'], name='age',
                     text=age2['percent_has_debt'], visible = False,
                     showlegend=False, marker_color=colors2))

fig.add_trace(go.Bar(x=income2['income_pp_quintile'], y=income2['percent_has_debt'],
                     text=income2['percent_has_debt'], name='income', visible = False,
                     showlegend=False, marker_color=colors3))

fig.add_trace(go.Bar(x=networth2['networth_pp_quintile2'],
                     text=networth2['percent_has_debt'], y=networth2['percent_has_debt'],
                     name='networth', visible = False, showlegend=False, marker_color=colors3))

fig.add_trace(go.Bar(x=poor2['original_poor'], y=poor2['percent_has_debt'],
                     text=poor2['percent_has_debt'], name='poor',
                     visible = False, showlegend=False, marker_color=colors4))


fig.update_layout(uniformtext_minsize=13, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Share of people in households with student debt',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,50])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Population share with student debt by race')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,False,False,False,False,False]},
                       {'title':'Population share with student debt by race',
                        'showlegend':True}]),
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False,True,False, False,False, False]},
                       {'title':'Population share with student debt by education level',
                        'showlegend':True}]),
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False,False,True, False, False, False]},
                       {'title':'Population share with student debt by age',
                        'showlegend':True}]),
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False, True, False, False]},
                       {'title':'Population share with student debt by income quintile',
                        'showlegend':True}]),
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False,False,False, False, True, False]},
                       {'title':'Population share with student debt by net worth quintile',
                        'showlegend':True}]),
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False,False,False, False, False, True]},
                       {'title':'Population share with student debt by poverty status',
                        'showlegend':True}]), 
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f1() {
  var x = document.getElementById("code_graph1");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph1").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph1.html");
    });
  </script>
</div>
<div id = "graph1"></div>
The average person holds about \\$3,700 in student debt, including those who have no debt at all, with demographic trends similar to the share of households holding debt.  As expected, households headed by college graduates possess the most debt, holding 18 times the amount of debt for those headed by people without a high school diploma (whose student debt is ostensibly held by a spouse or child).  Those at the bottom of the net worth distribution have more student debt than those at the top. This too is unsurprising as younger people hold a disproportionate amount of debt and the student debt itself decreases one's net worth.

<button onclick="f2()">Click to show code</button>
<div id="code_graph2" style="display: none;">
  <pre>
    <code>
# Average debt by demographic

fig = go.Figure()

fig.add_trace(go.Bar(x=race2['race'], y=race2['mean_debt'], 
                     text=race2['mean_debt'], name='race',
                     showlegend=False, marker_color=colors))

fig.add_trace(go.Bar(x=education2['edcl'], y=education2['mean_debt'],
                     text=education2['mean_debt'], name='education',
                     visible = False, showlegend=False, marker_color=colors))

fig.add_trace(go.Bar(x=age2['agecl'], y=age2['mean_debt'], name='age',
                     text=age2['mean_debt'], visible = False,
                     showlegend=False, marker_color=colors2))

fig.add_trace(go.Bar(x=income2['income_pp_quintile'], y=income2['mean_debt'],
                     text=income2['mean_debt'], name='income', visible = False,
                     showlegend=False, marker_color=colors3))

fig.add_trace(go.Bar(x=networth2['networth_pp_quintile2'],
                     text=networth2['mean_debt'], y=networth2['mean_debt'],
                     name='networth', visible = False, showlegend=False, marker_color=colors3))

fig.add_trace(go.Bar(x=poor2['original_poor'], y=poor2['mean_debt'],
                     text=poor2['mean_debt'], name='poor',
                     visible = False, showlegend=False, marker_color=colors4))


fig.update_layout(uniformtext_minsize=11, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='$%{text}', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Average student debt per person',
        tickprefix ='$',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,12_000])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Average student debt by race')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,False,False,False,False,False]},
                       {'title':'Average student debt by race',
                        'showlegend':True}]),
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False,True,False, False,False, False]},
                       {'title':'Average student debt by education level',
                        'showlegend':True}]),
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False,False,True, False, False, False]},
                       {'title':'Average student debt by age',
                        'showlegend':True}]),
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False, True, False, False]},
                       {'title':'Average student debt by income quintile',
                        'showlegend':True}]),
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False,False,False, False, True, False]},
                       {'title':'Average student debt by net worth quintile',
                        'showlegend':True}]),
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False,False,False, False, False, True]},
                       {'title':'Average student debt by poverty status',
                        'showlegend':True}]), 
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f2() {
  var x = document.getElementById("code_graph2");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph2").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph2.html");
    });
  </script>
</div>
<div id = "graph2"></div>
## Comparing \\$50,000 debt cancellation to a budget-equivalent universal payment

According to the 2019 SCF, the Warren-Schumer proposal to cancel \\$50,000 in student debt would cost approximately \\$700 billion, or about \\$2,300 for every adult and child. What if that \\$2,300 was given directly as a universal payment?

On average, groups that would receive more money from student debt cancellation include the top two income quintiles, Black Americans, college graduates, and people not in poverty; other groups would receive more from the universal payment.


### Average benefit per policy

<button onclick="f3()">Click to show code</button>
<div id="code_graph3" style="display: none;">
  <pre>
    <code>
## Average Benefit by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_change_50,
    text=race2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))


fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_change_50,
    text= race2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))


fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_change_50,
    text=education2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_change_50,
    text=education2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_change_50,
    text=age2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_change_50,
    text=age2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_change_50,
    text=income2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_change_50,
    text=income2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_change_50,
    text=networth2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_change_50,
    text=networth2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_change_50,
    text=poor2.ed_debt_change_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_change_50,
    text=poor2.ubi_change_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='$%{text}', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Average benefit per person',
        ticksuffix ='',
        tickprefix ='$',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,12_000])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Average benefit by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Average benefit of reform by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Average benefit of reform by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Average benefit of reform by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])


    </code>
  </pre>
</div>

<script>
function f3() {
  var x = document.getElementById("code_graph3");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph3").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph3.html");
    });
  </script>
</div>
<div id = "graph3"></div>
### Share better off in each policy

While Black Americans on the whole receive more under student debt cancellation, 74 percent of Black Americans would be better off with the universal payment.  For those at the bottom quintile of the net worth distribution, 65 percent would receive more money with the universal payment.  88 percent of people living in poverty would receive a larger benefit with the universal payment.  In total, 82 percent of Americans would be better off with a budget-equivalent universal payment compared to \\$50,000 in student debt cancellation.\n

<button onclick="f4()">Click to show code</button>
<div id="code_graph4" style="display: none;">
  <pre>
    <code>
## Percent better off with universal payment ##
fig = go.Figure()

fig.add_trace(go.Bar(x=race2['race'], y=race2['percent_better_off_with_ubi_50'], 
                     text=race2['percent_better_off_with_ubi_50'], name='race',
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=education2['edcl'], y=education2['percent_better_off_with_ubi_50'],
                     text=education2['percent_better_off_with_ubi_50'], name='education',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=age2['agecl'], y=age2['percent_better_off_with_ubi_50'], name='age',
                     text=age2['percent_better_off_with_ubi_50'], visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=income2['income_pp_quintile'], y=income2['percent_better_off_with_ubi_50'],
                     text=income2['percent_better_off_with_ubi_50'], name='income', visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=networth2['networth_pp_quintile2'],
                     text=networth2['percent_better_off_with_ubi_50'], y=networth2['percent_better_off_with_ubi_50'],
                     name='networth', visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=poor2['original_poor'], y=poor2['percent_better_off_with_ubi_50'],
                     text=poor2['percent_better_off_with_ubi_50'], name='poor',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))


fig.update_layout(uniformtext_minsize=13, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Percent better off with universal payment',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,110])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Percent better off with universal payments by race')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,False,False,False,False,False]},
                       {'title':'Share better off with universal payment by race',
                        'showlegend':True}]),
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False,True,False, False,False, False]},
                       {'title':'Share better off with universal payment by education level',
                        'showlegend':True}]),
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False,False,True, False, False, False]},
                       {'title':'Share better off with universal payment by age',
                        'showlegend':True}]),
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False, True, False, False]},
                       {'title':'Share better off with universal payment by income quintile',
                        'showlegend':True}]),
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False,False,False, False, True, False]},
                       {'title':'Share better off with universal payment by net worth quintile',
                        'showlegend':True}]),
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False,False,False, False, False, True]},
                       {'title':'Share better off with universal payment by poverty status',
                        'showlegend':True}]), 
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])


    </code>
  </pre>
</div>

<script>
function f4() {
  var x = document.getElementById("code_graph4");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph4").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph4.html");
    });
  </script>
</div>
<div id = "graph4"></div>
### Reduction in net debt rates

Cancelling \\$50,000 in student debt would lift more Americans out of total debt (negative net worth) than a budget-equivalent universal payment.[^static] In total, the student debt cancellation would reduce the number of Americans in debt by 44 percent while the universal payment plan would reduce it by 30 percent. This overall trend is mostly consistent across demographic groups. Exceptions include Hispanics, people with no education beyond high school, people at the bottom quintile of the income distribution, and those living in poverty.

[^static]: Calculations around net debt and other outcomes assume that all cancelled debt and universal payments go directly to net worth; that is, consumption is assumed to be constant.

<button onclick="f5()">Click to show code</button>
<div id="code_graph5" style="display: none;">
  <pre>
    <code>
## Percent decrease of people in debt by reform ##

fig = go.Figure()


fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_debt_reduction_50,
    text=race2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_debt_reduction_50,
    text= race2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_debt_reduction_50,
    text=education2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_debt_reduction_50,
    text=education2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_debt_reduction_50,
    text=age2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_debt_reduction_50,
    text=age2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_debt_reduction_50,
    text=income2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_debt_reduction_50,
    text=income2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_debt_reduction_50,
    text=networth2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_debt_reduction_50,
    text=networth2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_debt_reduction_50,
    text=poor2.ed_debt_debt_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_debt_reduction_50,
    text=poor2.ubi_debt_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Percent decrease of people in debt',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-60,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Percent decrease of people in debt by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Percent decrease of people in debt by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Percent decrease of people in debt by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Percent decrease of people in debt by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Percent decrease of people in debt by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Percent decrease of people in debt by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Percent decrease of people in debt by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f5() {
  var x = document.getElementById("code_graph5");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph5").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph5.html");
    });
  </script>
</div>
<div id = "graph5"></div>
### Racial wealth gaps

While much of the rhetoric surrounding student debt relief has been [centered](https://www.businessinsider.com/how-eliminating-student-debt-would-close-the-racial-wealth-gap-2019-6) around the racial wealth gap, a budget-equivalent universal payment would be stronger at reducing the median gap for both Black and Hispanics Americans. Considering the mean racial wealth gaps, universal payments also reduce the White/Hispanic gap more, though student debt cancellation reduces the White/Black gap more.

<button onclick="f6()">Click to show code</button>
<div id="code_graph6" style="display: none;">
  <pre>
    <code>
racial_wealth_gap = (racial_wealth_gap).round(1)

fig = go.Figure()

groups = ['Hispanic mean', 'Hispanic median', 'Black mean', 'Black median']

status_quo_ratio = [racial_wealth_gap.ratios[1],
                   racial_wealth_gap.ratios[0],
                   racial_wealth_gap.ratios[2],
                   racial_wealth_gap.ratios[3],]

ubi_ratio = [racial_wealth_gap.ratios[5],
            racial_wealth_gap.ratios[4],
            racial_wealth_gap.ratios[6],
            racial_wealth_gap.ratios[7],]

ed_debt_ratio = [racial_wealth_gap.ratios[9],
                racial_wealth_gap.ratios[8],
                racial_wealth_gap.ratios[10],
                racial_wealth_gap.ratios[11],]


fig = go.Figure(data=[
    go.Bar(name='Status quo', x=groups, y=status_quo_ratio, 
                                    marker_color=GRAY,
          text=status_quo_ratio),
    
        
    go.Bar(name='$50k student<br>debt cancellation', x=groups, y=ed_debt_ratio,
                                      marker_color=LIGHT_BLUE,
                                      text=ed_debt_ratio),
    
    go.Bar(name='Budget-equiavalent<br>universal payment', x=groups, y=ubi_ratio, 
                                    marker_color=DARK_BLUE,
          text=ubi_ratio),
])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(title_text='Racial wealth gap by reform')

fig.update_xaxes(
        tickangle = 0,
        title_text = '',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Ratio of white wealth statistic to demographic',
        ticksuffix ='',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,10])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

    </code>
  </pre>
</div>

<script>
function f6() {
  var x = document.getElementById("code_graph6");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph6").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph6.html");
    });
  </script>
</div>
<div id = "graph6"></div>
### Inequality impacts

For income inequality (and poverty), I follow [IRS guidelines](https://finaid.org/loans/forgivenesstaxability) in treating student loan forgiveness as income, though I do not estimate its tax liability. I calculate inequality using the Gini index, which goes from zero (perfect equality) to one (one person holds all the income/wealth). Student debt forgiveness reduces wealth inequality slightly more than a budget equivalent-universal payment; however, universal payments reduce income inequality more.

<button onclick="f7()">Click to show code</button>
<div id="code_graph7" style="display: none;">
  <pre>
    <code>
# Gini chart

# Calculate the change in gini index for income of each reform
start_gini = mdf.gini(scf, 'income_pp', w='wgt_numper').round(3)
ubi_gini = mdf.gini(scf, 'ubi_income_pp', w='wgt_numper').round(3)
ed_gini = mdf.gini(scf, 'no_debt_income_pp', w='wgt_numper').round(3)
ubi_gini_50 = mdf.gini(scf, 'ubi_income_pp_50', w='wgt_numper').round(3)
ubi_gini_50_phase_out = mdf.gini(scf, 'ubi_income_pp_50_phase_out', w='wgt_numper').round(3)
ubi_gini_10 = mdf.gini(scf, 'ubi_income_pp_10', w='wgt_numper').round(3)
ed_gini_10 = mdf.gini(scf, 'no_debt_income_pp_10', w='wgt_numper').round(3)
ed_gini_50 = mdf.gini(scf, 'no_debt_income_pp_50', w='wgt_numper').round(3)
ed_gini_50_phase_out = mdf.gini(scf, 'no_debt_income_pp_50_phase_out', w='wgt_numper').round(3)

change_ubi_gini = (((ubi_gini - start_gini) / start_gini) * 100).round(1)
change_ubi_gini_50 = (((ubi_gini_50 - start_gini) / start_gini) * 100).round(1)
change_ubi_gini_50_phase_out = (((ubi_gini_50_phase_out - start_gini) / start_gini) * 100).round(1)
change_ubi_gini_10 = (((ubi_gini_10 - start_gini) / start_gini) * 100).round(1)

change_ed_gini = (((ed_gini - start_gini) / start_gini) * 100).round(1)
change_ed_gini_50 = (((ed_gini_50 - start_gini) / start_gini) * 100).round(1)
change_ed_gini_50_phase_out = (((ed_gini_50_phase_out - start_gini) / start_gini) * 100).round(1)
change_ed_gini_10 = (((ed_gini_10 - start_gini) / start_gini) * 100).round(1)

# Calculate the change in gini index for networth of each reform
start_gini_networth = mdf.gini(scf, 'networth_pp', w='wgt_numper').round(3)
ubi_gini_networth = mdf.gini(scf, 'ubi_networth_pp', w='wgt_numper').round(3)
ed_gini_networth = mdf.gini(scf, 'no_debt_networth_pp', w='wgt_numper').round(3)
ubi_gini_50_networth = mdf.gini(scf, 'ubi_networth_pp_50', w='wgt_numper').round(3)
ubi_gini_50_phase_out_networth = mdf.gini(scf, 'ubi_networth_pp_50_phase_out', w='wgt_numper').round(3)
ubi_gini_10_networth = mdf.gini(scf, 'ubi_networth_pp_10', w='wgt_numper').round(3)
ed_gini_10_networth = mdf.gini(scf, 'no_debt_networth_pp_10', w='wgt_numper').round(3)
ed_gini_50_networth = mdf.gini(scf, 'no_debt_networth_pp_50', w='wgt_numper').round(3)
ed_gini_50_phase_out_networth = mdf.gini(scf, 'no_debt_networth_pp_50_phase_out', w='wgt_numper').round(3)

change_ubi_gini_networth = (((ubi_gini_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ubi_gini_50_networth = (((ubi_gini_50_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ubi_gini_50_phase_out_networth = (((ubi_gini_50_phase_out_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ubi_gini_10_networth = (((ubi_gini_10_networth - start_gini_networth) / start_gini_networth) * 100).round(2)

change_ed_gini_networth = (((ed_gini_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ed_gini_50_networth = (((ed_gini_50_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ed_gini_50_phase_out_networth = (((ed_gini_50_phase_out_networth - start_gini_networth) / start_gini_networth) * 100).round(2)
change_ed_gini_10_networth = (((ed_gini_10_networth - start_gini_networth) / start_gini_networth) * 100).round(2)

racial_wealth_gap = (racial_wealth_gap).round(1)

fig = go.Figure()

metric = ['Wealth', 'Income']

status_quo_gini = [start_gini_networth,
               start_gini]

ubi_gini = [ubi_gini_50_networth,
           ubi_gini_50]

ed_debt_gini = [ed_gini_50_networth,
               ed_gini_50]



fig = go.Figure(data=[
    go.Bar(name='Status quo', x=metric, y=status_quo_gini, 
                                    marker_color=GRAY,
          text=status_quo_gini),
    
        
    go.Bar(name='$50k student<br>debt cancellation', x=metric, y=ed_debt_gini,
                                      marker_color=LIGHT_BLUE,
                                      text=ed_debt_gini),
    
    go.Bar(name='Budget-equivalent<br>universal payment', x=metric, y=ubi_gini, 
                                    marker_color=DARK_BLUE,
          text=ubi_gini)

])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(title_text='Inequality by reform')

fig.update_xaxes(
        tickangle = 0,
        title_text = '',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Gini index',
        ticksuffix ='',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,1])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')
config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f7() {
  var x = document.getElementById("code_graph7");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph7").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph7.html");
    });
  </script>
</div>
<div id = "graph7"></div>
### Poverty impacts

Across every demographic and metric, universal payments would cut poverty rates at a higher rate than student debt cancellation. Overall, universal payments would cut poverty by 52 percent, while cancelling \\$50,000 in student debt would cut poverty by 14 percent. Hispanic and Black poverty would fall 63 percent and 47 percent under universal payments, respectively, but only 7 percent and 11 percent under student debt cancellation. Student debt cancellation would cut poverty for people in households headed by people without a high school diploma by 1 percent, while universal payments would cut it by 46 percent. Universal payments would even eliminate poverty for Americans in the second income quintile.

<button onclick="f8()">Click to show code</button>
<div id="code_graph8" style="display: none;">
  <pre>
    <code>
## Percent reduction in poverty rate by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_poverty_reduction_50\t,
    text=race2.ed_debt_poverty_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_poverty_reduction_50,
    text= race2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_poverty_reduction_50\t,
    text=education2.ed_debt_poverty_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_poverty_reduction_50,
    text=education2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_poverty_reduction_50\t,
    text=age2.ed_debt_poverty_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_poverty_reduction_50,
    text=age2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_poverty_reduction_50,
    text=income2.ed_debt_poverty_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_poverty_reduction_50,
    text=income2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_poverty_reduction_50,
    text=networth2.ed_debt_poverty_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_poverty_reduction_50,
    text=networth2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_poverty_reduction_50,
    text=poor2.ed_debt_poverty_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_poverty_reduction_50,
    text=poor2.ubi_poverty_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty reduction',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-105,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Poverty reduction by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by age group',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Poverty reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])
config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f8() {
  var x = document.getElementById("code_graph8");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph8").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph8.html");
    });
  </script>
</div>
<div id = "graph8"></div>
Universal payments also outperform student debt cancellation across all demographics on poverty gap reduction.  The poverty gap is defined as the sum of the gaps between a household's resources and its poverty threshold across all households in poverty. The poverty gap would fall 69 percent under universal payments and 15 percent under student debt cancellation.

<button onclick="f9()">Click to show code</button>
<div id="code_graph9" style="display: none;">
  <pre>
    <code>
## Percent in poverty by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_gap_reduction_50\t,
    text=race2.ed_debt_gap_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_gap_reduction_50,
    text= race2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_gap_reduction_50\t,
    text=education2.ed_debt_gap_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_gap_reduction_50,
    text=education2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_gap_reduction_50,
    text=age2.ed_debt_gap_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_gap_reduction_50,
    text=age2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_gap_reduction_50,
    text=income2.ed_debt_gap_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_gap_reduction_50,
    text=income2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_gap_reduction_50,
    text=networth2.ed_debt_gap_reduction_50,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_gap_reduction_50,
    text=networth2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_gap_reduction_50\t,
    text=poor2.ed_debt_gap_reduction_50\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_gap_reduction_50,
    text=poor2.ubi_gap_reduction_50,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty gap reduction',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-100,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Poverty gap reduction by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty gap reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty gap reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Percent reduction in poverty gap by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f9() {
  var x = document.getElementById("code_graph9");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph9").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph9.html");
    });
  </script>
</div>
<div id = "graph9"></div>
## Comparing other student debt proposals

While this paper focuses on comparing the \\$50,000 forgiveness currently proposed by Senators Warren and Schumer, I found similar results comparing other proposals. Whether comparing full forgiveness to a budget-equivalent universal payment of \\$3,650, or Warren's phased-out \\$50,000 forgiveness to \\$2,100 payments, or \\$10,000 forgiveness to \\$770 payments, universal payments benefit a larger share of Americans and reduce poverty and income inequality by a larger amount, while student debt cancellation reduces wealth inequality more.

The charts below show how all four plans would impact each metric; for more charts on each plan, see the Appendix.

<button onclick="f10()">Click to show code</button>
<div id="code_graph10" style="display: none;">
  <pre>
    <code>
comparison = race[race['race'] == 'All']

fig = go.Figure()

reform = ['All', '$50k', '$50k phase-out', '$10k']

ubi_all = [comparison.ubi_poverty_reduction[4],
           comparison.ubi_poverty_reduction_50[4],
           all2.ubi_poverty_reduction_50_phase_out[0],
           comparison.ubi_poverty_reduction_10[4]]

ed_debt_all = [comparison.ed_debt_poverty_reduction[4], 
            comparison.ed_debt_poverty_reduction_50[4],
               all2.ed_debt_poverty_reduction_50_phase_out[0],
            comparison.ed_debt_poverty_reduction_10[4]]



fig = go.Figure(data=[
    
    go.Bar(name='Student<br>debt cancellation', x=reform, y=ed_debt_all,
                                      marker_color=LIGHT_BLUE,
          text=ed_debt_all),
    
    go.Bar(name='Budget-equivalent<br>universal payment', x=reform, y=ubi_all, 
                                    marker_color=DARK_BLUE,
          text=ubi_all)
    
])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Poverty reduction by reform')


fig.update_xaxes(
        tickangle = 0,
        title_text = 'Cancellation amount',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Change to poverty rate',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-100,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

    </code>
  </pre>
</div>

<script>
function f10() {
  var x = document.getElementById("code_graph10");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph10").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph10.html");
    });
  </script>
</div>
<div id = "graph10"></div>

<button onclick="f11()">Click to show code</button>
<div id="code_graph11" style="display: none;">
  <pre>
    <code>
# gini_networth chart
fig = go.Figure()

ubi_all_gini_networth = [change_ubi_gini_networth,
           change_ubi_gini_50_networth,
           change_ubi_gini_50_phase_out_networth,
               change_ubi_gini_10_networth]

ed_debt_all_gini_networth = [change_ed_gini_networth,
           change_ed_gini_50_networth,
           change_ed_gini_50_phase_out_networth,
               change_ed_gini_10_networth]



fig = go.Figure(data=[
    go.Bar(name='Student<br>debt cancellation', x=reform,
           y=ed_debt_all_gini_networth,
           marker_color=LIGHT_BLUE,
           text=ed_debt_all_gini_networth),
    
    go.Bar(name='Budget-equivalent<br>universal payment', x=reform, y=ubi_all_gini_networth, 
                                    marker_color=DARK_BLUE,
          text=ubi_all_gini_networth)
    

])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Wealth inequality by reform')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Cancellation amount',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Change in Gini index of per-capita wealth',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-2,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')
fconfig = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f11() {
  var x = document.getElementById("code_graph11");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph11").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph11.html");
    });
  </script>
</div>
<div id = "graph11"></div>

<button onclick="f12()">Click to show code</button>
<div id="code_graph12" style="display: none;">
  <pre>
    <code>
# Gini chart
fig = go.Figure()

ubi_all_gini = [change_ubi_gini,
           change_ubi_gini_50,
           change_ubi_gini_50_phase_out,
               change_ubi_gini_10]

ed_debt_all_gini = [change_ed_gini,
           change_ed_gini_50,
           change_ed_gini_50_phase_out,
               change_ed_gini_10]



fig = go.Figure(data=[
    
    go.Bar(name='Student<br>debt cancellation', x=reform, y=ed_debt_all_gini,
                                      marker_color=LIGHT_BLUE,
          text=ed_debt_all_gini),
    
    go.Bar(name='Budget-equivalent<br>universal payment', x=reform, y=ubi_all_gini, 
                                    marker_color=DARK_BLUE,
          text=ubi_all_gini),
    
])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Income inequality by reform')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Cancellation amount',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Change in Gini index of per-capita income',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-10,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')
config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f12() {
  var x = document.getElementById("code_graph12");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph12").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph12.html");
    });
  </script>
</div>
<div id = "graph12"></div>

<button onclick="f13()">Click to show code</button>
<div id="code_graph13" style="display: none;">
  <pre>
    <code>
fig = go.Figure()

ubi_all = [comparison.percent_better_off_with_ubi[4],
           comparison.percent_better_off_with_ubi_50[4],
           all2.percent_better_off_with_ubi_50_phase_out[0],
           comparison.percent_better_off_with_ubi_10[4]]



fig = go.Figure(data=[
    go.Bar(name='Budget-equivalent<br>universal payment', x=reform, y=ubi_all, 
                                    marker_color=DARK_BLUE,
          text=ubi_all)
    
])

fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Share better off with universal payments than student debt cancellation by reform')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Cancellation amount',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Share of people better off with universal payments',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,100])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

    </code>
  </pre>
</div>

<script>
function f13() {
  var x = document.getElementById("code_graph13");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph13").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph13.html");
    });
  </script>
</div>
<div id = "graph13"></div>
## Conclusion

Because the majority of Americans do not have student debt, the majority of Americans will not benefit from student debt cancellation, no matter the size of the proposal.  Student debt cancellation primarily benefits high income earners with a college degree, a demographic [likely to see incomes rise over time](https://fordhaminstitute.org/national/research/what-you-make-depends-on-where-you-live), while leaving out some of the poorest Americans. Still, Senator Warren and other proponents correctly identify it as a way to [cut inequality and the racial wealth gap](https://rooseveltinstitute.org/wp-content/uploads/2020/08/RI_StudentDebtForgiveness_WorkingPaper_202008.pdf). Student debt has reached enormous levels, making its cancellation a major program that would benefit tens of millions, and among degree holders, it would disproportionately benefit those from less-advantaged backgrounds.

But the enormity of the endeavor justifies careful comparison to other policies. While student debt cancellation reduces wealth inequality more than universal payments, it mostly underperforms simply sending every American a check on reducing racial wealth gaps. On all other outcomes, it fares even worse: universal payments would reduce poverty and income inequality more than student debt cancellation, regardless of the particular policy design. This analysis may even understate the relative progressivity of universal payments, given it doesn't capitalize the higher future incomes associated with college education (though limitations of the SCF data may counter that).

Means-testing the student debt cancellation closes some of the gap, but introduces its own challenges. Warren's proposal is effectively a retroactive additional marginal tax of 33 percent on student debtors' earnings between \\$100,000 and \\$250,000. This would make this group some of the most highly taxed in the country, with total marginal tax rates likely exceeding 70 percent after considering state and federal income and payroll taxes (only [low-income benefit recipients](https://aspe.hhs.gov/system/files/aspe-files/260661/brief2-overviewmtranalyses.pdf) would face higher marginal taxes). Retroactive taxation may be [constitutional](https://fas.org/sgp/crs/misc/R42791.pdf), but it arguably [threatens rule of law](https://www.cost.org/globalassets/cost/state-tax-resources-pdf-pages/cost-studies-articles-reports/law360-oped-on-retroactive-taxation-003.pdf); people value knowing the payoff to their labor when making decisions about it.

Universal payments have less quantifiable advantages, as well. A one-time debt cancellation excludes both people who recently paid off their student loans, and those about to incur it; universal payments reach all. By favoring college graduates over non-college graduates, student debt cancellation threatens to exacerbate political tensions between these demographics that [only rose in the 2020 election](https://www.brookings.edu/research/2020-exit-polls-show-a-scrambling-of-democrats-and-republicans-traditional-bases/). If young people expect future rounds of student debt cancellation, they may also choose to take on more debt, which could in turn [raise the cost of higher education](http://taylornadauld.com/research/published_papers/Credit%20Supply%20and%20the%20Rise%20in%20College%20Tuition.pdf).

While student debt cancellation makes progress toward egalitarian goals (and may have the advantage of [skipping congressional approval](https://www.warren.senate.gov/imo/media/doc/Ltr%20to%20Warren%20re%20admin%20debt%20cancellation.pdf?fbclid=IwAR3x7goUzVOpD7vcp7XhPYPlYQPmzv7rTzfNIvwl9Y8claLM0p7fo017N-g)), dollar-for-dollar, those goals are better achieved through universal payments.
## Appendix

### \\$10k relief

<button onclick="f14()">Click to show code</button>
<div id="code_graph14" style="display: none;">
  <pre>
    <code>
## Average Benefit by reform ##

fig = go.Figure()


fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_change_10,
    text=race2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_change_10,
    text= race2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))


fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_change_10,
    text=education2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_change_10,
    text=education2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_change_10,
    text=age2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_change_10,
    text=age2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_change_10,
    text=income2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_change_10,
    text=income2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_change_10,
    text=networth2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_change_10,
    text=networth2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_change_10,
    text=poor2.ed_debt_change_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_change_10,
    text=poor2.ubi_change_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=9, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='$%{text}', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Average benefit',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,2_000])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Average benefit by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Average benefit of reform by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Average benefit of reform by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Average benefit of reform by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f14() {
  var x = document.getElementById("code_graph14");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph14").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph14.html");
    });
  </script>
</div>
<div id = "graph14"></div>

<button onclick="f15()">Click to show code</button>
<div id="code_graph15" style="display: none;">
  <pre>
    <code>
## Percent better off with ed debt ##
fig = go.Figure()

fig.add_trace(go.Bar(x=race2['race'], y=race2['percent_better_off_with_ubi_10'], 
                     text=race2['percent_better_off_with_ubi_10'], name='race',
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=education2['edcl'], y=education2['percent_better_off_with_ubi_10'],
                     text=education2['percent_better_off_with_ubi_10'], name='education',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=age2['agecl'], y=age2['percent_better_off_with_ubi_10'], name='age',
                     text=age2['percent_better_off_with_ubi_10'], visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=income2['income_pp_quintile'], y=income2['percent_better_off_with_ubi_10'],
                     text=income2['percent_better_off_with_ubi_10'], name='income', visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=networth2['networth_pp_quintile2'],
                     text=networth2['percent_better_off_with_ubi_10'], y=networth2['percent_better_off_with_ubi_10'],
                     name='networth', visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=poor2['original_poor'], y=poor2['percent_better_off_with_ubi_10'],
                     text=poor2['percent_better_off_with_ubi_10'], name='poor',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))


fig.update_layout(uniformtext_minsize=13, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Share better off with universal payments',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,100])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Share better off with universal payment by race')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,False,False,False,False,False]},
                       {'title':'Share better off with universal payment by race',
                        'showlegend':True}]),
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False,True,False, False,False, False]},
                       {'title':'Share better off with universal payment by education level',
                        'showlegend':True}]),
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False,False,True, False, False, False]},
                       {'title':'Share better off with universal payment by age',
                        'showlegend':True}]),
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False, True, False, False]},
                       {'title':'Share better off with universal payment by income quintile',
                        'showlegend':True}]),
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False,False,False, False, True, False]},
                       {'title':'Share better off with universal payment by net worth quintile',
                        'showlegend':True}]),
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False,False,False, False, False, True]},
                       {'title':'Share better off with universal payment by poverty status',
                        'showlegend':True}]), 
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f15() {
  var x = document.getElementById("code_graph15");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph15").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph15.html");
    });
  </script>
</div>
<div id = "graph15"></div>

<button onclick="f16()">Click to show code</button>
<div id="code_graph16" style="display: none;">
  <pre>
    <code>
## Percent decrease of people in debt by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_debt_reduction_10,
    text=race2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_debt_reduction_10,
    text= race2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))


fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_debt_reduction_10,
    text=education2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_debt_reduction_10,
    text=education2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_debt_reduction_10,
    text=age2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_debt_reduction_10,
    text=age2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_debt_reduction_10,
    text=income2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_debt_reduction_10,
    text=income2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_debt_reduction_10,
    text=networth2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_debt_reduction_10,
    text=networth2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_debt_reduction_10,
    text=poor2.ubi_debt_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_debt_reduction_10,
    text=poor2.ed_debt_debt_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')


fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Net debt rate reduction',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-40,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Net debt rate reduction by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Net debt rate reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Net debt rate reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Net debt rate reduction by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Net debt rate reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Net debt rate reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Net debt rate reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f16() {
  var x = document.getElementById("code_graph16");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph16").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph16.html");
    });
  </script>
</div>
<div id = "graph16"></div>

<button onclick="f17()">Click to show code</button>
<div id="code_graph17" style="display: none;">
  <pre>
    <code>
## Percent reduction in poverty rate by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_poverty_reduction_10\t,
    text=race2.ed_debt_poverty_reduction_10\t,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_poverty_reduction_10,
    text= race2.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_poverty_reduction_10\t,
    text=education2.ed_debt_poverty_reduction_10\t,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_poverty_reduction_10,
    text=education2.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_poverty_reduction_10\t,
    text=age2.ed_debt_poverty_reduction_10\t,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_poverty_reduction_10,
    text=age2.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_poverty_reduction_10,
    text=income2.ed_debt_poverty_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_poverty_reduction_10,
    text=income2.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_poverty_reduction_10,
    text=networth2.ed_debt_poverty_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_poverty_reduction_10,
    text=networth2.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor.original_poor,
    y=poor.ed_debt_poverty_reduction_10,
    text=poor.ed_debt_poverty_reduction_10,
    name='$10k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor.original_poor,
    y=poor.ubi_poverty_reduction_10,
    text=poor.ubi_poverty_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty reduction',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-55,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_layout(title_text='Poverty reduction by race')

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by age group',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Poverty reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f17() {
  var x = document.getElementById("code_graph17");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph17").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph17.html");
    });
  </script>
</div>
<div id = "graph17"></div>

<button onclick="f18()">Click to show code</button>
<div id="code_graph18" style="display: none;">
  <pre>
    <code>
## Percent in poverty by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_gap_reduction_10\t,
    text=race2.ed_debt_gap_reduction_10\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_gap_reduction_10,
    text= race2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_gap_reduction_10\t,
    text=education2.ed_debt_gap_reduction_10\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_gap_reduction_10,
    text=education2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_gap_reduction_10,
    text=age2.ed_debt_gap_reduction_10,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_gap_reduction_10,
    text=age2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_gap_reduction_10,
    text=income2.ed_debt_gap_reduction_10,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_gap_reduction_10,
    text=income2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_gap_reduction_10,
    text=networth2.ed_debt_gap_reduction_10,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_gap_reduction_10,
    text=networth2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_gap_reduction_10\t,
    text=poor2.ed_debt_gap_reduction_10\t,
    name='$50k student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_gap_reduction_10,
    text=poor2.ubi_gap_reduction_10,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Poverty gap reduction by race')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty gap reduction',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-100,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reductionp by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty gap reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty gap reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Poverty gap reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f18() {
  var x = document.getElementById("code_graph18");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph18").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph18.html");
    });
  </script>
</div>
<div id = "graph18"></div>
### All relief

<button onclick="f19()">Click to show code</button>
<div id="code_graph19" style="display: none;">
  <pre>
    <code>
## Average Benefit by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_change,
    text=race2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_change,
    text= race2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_change,
    text=education2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_change,
    text=education2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_change,
    text=age2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_change,
    text=age2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_change,
    text=income2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_change,
    text=income2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_change,
    text=networth2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_change,
    text=networth2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_change,
    text=poor2.ubi_change,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_change,
    text=poor2.ed_debt_change,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=9, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='$%{text}', textposition='outside')
fig.update_layout(title_text='Average benefit by race')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Average benefit',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,12_000])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Average benefit of reform by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Average benefit of reform by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Average benefit of reform by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Average benefit of reform by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

config = {'displayModeBar': False}

    </code>
  </pre>
</div>

<script>
function f19() {
  var x = document.getElementById("code_graph19");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph19").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph19.html");
    });
  </script>
</div>
<div id = "graph19"></div>

<button onclick="f20()">Click to show code</button>
<div id="code_graph20" style="display: none;">
  <pre>
    <code>
## Percent better off with ed debt ##
fig = go.Figure()

fig.add_trace(go.Bar(x=race2['race'], y=race2['percent_better_off_with_ubi'], 
                     text=race2['percent_better_off_with_ubi'], name='race',
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=education2['edcl'], y=education2['percent_better_off_with_ubi'],
                     text=education2['percent_better_off_with_ubi'], name='education',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=age2['agecl'], y=age2['percent_better_off_with_ubi'], name='age',
                     text=age2['percent_better_off_with_ubi'], visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=income2['income_pp_quintile'], y=income2['percent_better_off_with_ubi'],
                     text=income2['percent_better_off_with_ubi'], name='income', visible = False,
                     showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=networth2['networth_pp_quintile2'],
                     text=networth2['percent_better_off_with_ubi'], y=networth2['percent_better_off_with_ubi'],
                     name='networth', visible = False, showlegend=False, marker_color=DARK_BLUE))

fig.add_trace(go.Bar(x=poor2['original_poor'], y=poor2['percent_better_off_with_ubi'],
                     text=poor2['percent_better_off_with_ubi'], name='poor',
                     visible = False, showlegend=False, marker_color=DARK_BLUE))


fig.update_layout(uniformtext_minsize=13, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Percent better off with universal payment')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Percent better off with universal payment',
        ticksuffix ='%',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[0,100])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,False,False,False,False,False]},
                       {'title':'Share better off with universal payments by race',
                        'showlegend':True}]),
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False,True,False, False,False, False]},
                       {'title':'Share better off with universal payments by education level',
                        'showlegend':True}]),
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False,False,True, False, False, False]},
                       {'title':'Share better off with universal payments by age',
                        'showlegend':True}]),
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False, True, False, False]},
                       {'title':'Share better off with universal payments by income quintile',
                        'showlegend':True}]),
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False,False,False, False, True, False]},
                       {'title':'Share better off with universal payments by net worth quintile',
                        'showlegend':True}]),
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False,False,False, False, False, True]},
                       {'title':'Share better off with universal payments by poverty status',
                        'showlegend':True}]), 
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f20() {
  var x = document.getElementById("code_graph20");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph20").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph20.html");
    });
  </script>
</div>
<div id = "graph20"></div>

<button onclick="f21()">Click to show code</button>
<div id="code_graph21" style="display: none;">
  <pre>
    <code>
## Reduction in net debt rate by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_debt_reduction,
    text=race2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_debt_reduction,
    text= race2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_debt_reduction,
    text=education2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_debt_reduction,
    text=education2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_debt_reduction,
    text=age2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_debt_reduction,
    text=age2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_debt_reduction,
    text=income2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_debt_reduction,
    text=income2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_debt_reduction,
    text=networth2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_debt_reduction,
    text=networth2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_debt_reduction,
    text=poor2.ed_debt_debt_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_debt_reduction,
    text=poor2.ubi_debt_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Reduction in net debt rate by race')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Reduction in net debt rate',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-100,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Reduction in net debt rate by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Reduction in net debt rate by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Reduction in net debt rate by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Reduction in net debt rate by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Reduction in net debt rate by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Reduction in net debt rate by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f21() {
  var x = document.getElementById("code_graph21");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph21").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph21.html");
    });
  </script>
</div>
<div id = "graph21"></div>

<button onclick="f22()">Click to show code</button>
<div id="code_graph22" style="display: none;">
  <pre>
    <code>
## Percent reduction in poverty rate by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_poverty_reduction\t,
    text=race2.ed_debt_poverty_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_poverty_reduction,
    text= race2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_poverty_reduction\t,
    text=education2.ed_debt_poverty_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_poverty_reduction,
    text=education2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_poverty_reduction\t,
    text=age2.ed_debt_poverty_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_poverty_reduction,
    text=age2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_poverty_reduction,
    text=income2.ed_debt_poverty_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_poverty_reduction,
    text=income2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_poverty_reduction,
    text=networth2.ed_debt_poverty_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_poverty_reduction,
    text=networth2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_poverty_reduction,
    text=poor2.ubi_poverty_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_poverty_reduction,
    text=poor2.ed_debt_poverty_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Reduction in poverty rate by race')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty reduction',
        ticksuffix ='',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-105,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty reduction by age group',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Poverty reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f22() {
  var x = document.getElementById("code_graph22");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph22").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph22.html");
    });
  </script>
</div>
<div id = "graph22"></div>

<button onclick="f23()">Click to show code</button>
<div id="code_graph23" style="display: none;">
  <pre>
    <code>
## Percent in poverty by reform ##

fig = go.Figure()

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ed_debt_gap_reduction\t,
    text=race2.ed_debt_gap_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE
))

fig.add_trace(go.Bar(
    x=race2.race,
    y=race2.ubi_gap_reduction,
    text= race2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ed_debt_gap_reduction\t,
    text=education2.ed_debt_gap_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=education2.edcl,
    y=education2.ubi_gap_reduction,
    text=education2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ed_debt_gap_reduction,
    text=age2.ed_debt_gap_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=age2.agecl,
    y=age2.ubi_gap_reduction,
    text=age2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ed_debt_gap_reduction,
    text=income2.ed_debt_gap_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=income2.income_pp_quintile,
    y=income2.ubi_gap_reduction,
    text=income2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ed_debt_gap_reduction,
    text=networth2.ed_debt_gap_reduction,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=networth2.networth_pp_quintile2,
    y=networth2.ubi_gap_reduction,
    text=networth2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ed_debt_gap_reduction\t,
    text=poor2.ed_debt_gap_reduction\t,
    name='All student<br>debt cancellation',
    marker_color=LIGHT_BLUE,
    visible = False
))

fig.add_trace(go.Bar(
    x=poor2.original_poor,
    y=poor2.ubi_gap_reduction,
    text=poor2.ubi_gap_reduction,
    name='Budget-equivalent<br>universal payment',
    marker_color=DARK_BLUE,
    visible = False
))


fig.update_layout(uniformtext_minsize=10, uniformtext_mode='hide', plot_bgcolor='white')
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(title_text='Poverty gap reduction by race')

fig.update_xaxes(
        tickangle = 0,
        title_text = 'Demographic of head of household',
        tickfont = {'size': 14},
        title_standoff = 25)

fig.update_yaxes(
        title_text = 'Poverty gap reduction',
        ticksuffix ='%',
        tickprefix = '',
        tickfont = {'size':14},
        title_standoff = 25,
        range=[-100,0])

fig.update_xaxes(title_font=dict(size=14, family='Roboto', color='black'))
fig.update_yaxes(title_font=dict(size=14, family='Roboto', color='black'))

fig.update_layout(barmode='group')

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list([
            dict(label='Race',
                 method='update',
                 args=[{'visible':[True,True,False,False,False,False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by race',
                        'showlegend':True}]),
            
            dict(label='Education',
                 method='update',
                 args=[{'visible':[False, False,True,True, False, False,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by education level',
                        'showlegend':True}]),
            
            dict(label='Age',
                 method='update',
                 args=[{'visible':[False, False,False, False, True, True,False,False,False,False,False,False]},
                       {'title':'Poverty gap reduction by age level',
                        'showlegend':True}]),
            
            dict(label='Income',
                 method='update',
                 args=[{'visible':[False,False,False,False,False,False,True,True,False,False,False,False]},
                       {'title':'Poverty gap reduction by income quintile',
                        'showlegend':True}]),
            
            dict(label='Networth',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,True,True,False,False]},
                       {'title':'Poverty gap reduction by net worth quintile',
                        'showlegend':True}]),
            
            dict(label='Poverty Status',
                 method='update',
                 args=[{'visible':[False, False,False, False, False, False,False,False,False,False,True,True]},
                       {'title':'Poverty gap reduction by poverty status',
                        'showlegend':True}])
                        ]),
        
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=-0.35,
            xanchor='left',
            y=1.1,
            yanchor='top'
    
    )])

    </code>
  </pre>
</div>

<script>
function f23() {
  var x = document.getElementById("code_graph23");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#graph23").load("{{site.baseurl}}assets/graphs/2020-11-17-student-debt-graph23.html");
    });
  </script>
</div>
<div id = "graph23"></div>
