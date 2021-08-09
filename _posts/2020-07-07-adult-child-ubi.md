---
layout: post
current: post
cover: 
navigation: True
title: To minimize poverty, should UBI be provided for adults, children, or both?
cover: assets/images/2020-07-07-adult-child-ubi/cover.jpg
date: 2020-07-07
tags: [us, child allowance, poverty]
class: post-template
subclass: 'post'
author: nate
excerpt: UBI relieves poverty more when it includes children.
useplotly: true
---

While [US GDP per capita has more than doubled in the past 50 years](https://fred.stlouisfed.org/series/A939RX0Q048SBEA), many Americans still remain in poverty. According to the Census Bureau's 2018 Supplemental Poverty Measure (SPM), over 40 million Americans live below their SPM poverty threshold.

Some [large guaranteed-income programs have been shown to nearly eliminate poverty](https://www.ubicenter.org/plans), but spending constraints can change how program design affects different outcomes. This paper shows the impact of new universal cash programs on poverty alleviation under varying levels of spending.

I examine the poverty rate impacts of three different basic income programs:

* Adult UBI - provides monthly stipends only to adults.
* Child Allowance - provides families monthly stipends based only on how many children are in their household.
* All UBI - provides an equal monthly stipend to all Americans regardless of age (parents would receive it on behalf of their children).

Two years ago, Matt Bruenig produced a similar  [paper](https://www.peoplespolicyproject.org/2018/11/29/a-child-allowance-would-be-very-effective-at-poverty-reduction/) using 2017 data in which he compared the same three programs and their impact on the poverty rate up to $500 billion in new spending. Bruenig found that at all levels of spending up to $500 billion, a Child Allowance was the most effective program at reducing poverty. This paper considers new spending up to $1 trillion with updated data from 2018.

## Background

I used data from the Census Bureau’s 2019 Annual Social and Economic Supplement (ASEC), which uses data collected in 2018. The ASEC survey contains over 180,000 Americans from more than 75,000 households. Each respondent is assigned a sample weight by the Census Bureau so that models can provide consistent national-level estimates.

The Supplemental Poverty Measure classifies respondents' poverty status by comparing their total family income (post tax and transfers) to their family poverty threshold. The Census Bureau defines poverty thresholds based on family size and costs of necessities.

In 2018, 12.7 percent of Americans were in poverty, including 13.6 percent of children and 12.5 percent of adults.

## Results

A Child Allowance reduces overall poverty more than the other two designs, for spending up to $500 billion; this aligns with Bruenig's results. However, at levels beyond $500 billion, a UBI that includes everyone cuts overall poverty more.

Spending $100 billion on a Child Allowance would equate to monthly stipends of $114 per child and lift 4.5 million Americans (1.3 million children and 3.2 million adults) out of poverty. $500 billion on either a Child Allowance or All UBI would lift 12 million Americans out of poverty. Spending $1 trillion on an All UBI would equate to monthly checks of $258 per American and lift over 22 million people out of poverty.

The interactive graph below shows the poverty impacts of each program at different funding levels.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
### LOAD PACKAGES ####

import pandas as pd
import numpy as np
import plotly.express as px
import plotly

### LOAD DATA ###

person_raw = pd.read_csv('https://github.com/MaxGhenis/datarepo/raw/master/pppub19.csv.gz',
                         usecols=['MARSUPWT', 'SPM_ID', 'SPM_POVTHRESHOLD',
                                  'SPM_RESOURCES', 'A_AGE'])

### PREPROCESS ###

person = person_raw.copy(deep=True)
person.columns = person.columns.str.lower()
person['weight'] = person.marsupwt/100
#Compute total children and adults in each resource sharing group.
person['child'] = person.a_age < 18
person['adult'] = person.a_age >= 18
spmu_ages = person.groupby('spm_id')[['child','adult']].sum()
spmu_ages.columns = ['children', 'total_adults']
person2 = person.merge(spmu_ages,left_on='spm_id', right_index=True)
total_children = (person2.child * person2.weight).sum()
total_adults = (person2.adult * person2.weight).sum()

### CALCULATIONS ###

child_allowance_overall = []
child_allowance_child = []
child_allowance_adults = []

# Determine the poverty rate impact of a Child Allownace from $0 in new spending to $1 trillion.

for spending in range(0, 1000000000001, 50000000000):
    child_allowance_per_child = spending/total_children
    total_child_allowance = person2.children * child_allowance_per_child
    new_spm_resources_ca = person2.spm_resources + total_child_allowance
    new_poor_ca = new_spm_resources_ca < person2.spm_povthreshold
    new_total_child_poor = ((person2.child * person2.weight * 
                             new_poor_ca).sum())
    new_child_poverty_rate = ((new_total_child_poor)/
                              (person2.child * person2.weight).sum())
    new_total_adult_poor = ((person2.adult * person2.weight * 
                             new_poor_ca).sum())
    new_adult_poverty_rate = ((new_total_adult_poor)/
                              (person2.adult * person2.weight).sum())
    new_total_poor_ca = (new_poor_ca * person2.weight).sum()
    new_poverty_rate_ca = new_total_poor_ca/person2.weight.sum()
    child_allowance_overall.append(new_poverty_rate_ca)
    child_allowance_child.append(new_child_poverty_rate)
    child_allowance_adults.append(new_adult_poverty_rate)
    
ubi_adults_overall = []
ubi_adults_child = []
ubi_adults_adults = []

# Determine the poverty rate impact of a Adult UBI from $0 in new spending to $1 trillion.

for spending in range(0, 1000000000001, 50000000000):
    adult_ubi = spending/total_adults
    total_adult_ubi = person2.total_adults * adult_ubi
    new_spm_resources_ubi = person2.spm_resources + total_adult_ubi
    new_poor_ubi = new_spm_resources_ubi < person2.spm_povthreshold
    new_total_child_poor = ((person2.child * person2.weight * 
                             new_poor_ubi).sum())
    new_child_poverty_rate = ((new_total_child_poor)/
                              (person2.child * person2.weight).sum())
    new_total_adult_poor = ((person2.adult * person2.weight * 
                             new_poor_ubi).sum())
    new_adult_poverty_rate = ((new_total_adult_poor)/
                              (person2.adult * person2.weight).sum())
    new_total_poor_ubi = (new_poor_ubi * person2.weight).sum()
    new_poverty_rate_ubi = new_total_poor_ubi/person2.weight.sum()
    ubi_adults_overall.append(new_poverty_rate_ubi)
    ubi_adults_child.append(new_child_poverty_rate)
    ubi_adults_adults.append(new_adult_poverty_rate)
    
ubi_all_overall = []
ubi_all_child = []
ubi_all_adults = []

# Determine the poverty rate impact of a All UBI from $0 in new spending to $1 trillion.

for spending in range(0, 1000000000001, 50000000000):
    all_ubi_per_person = spending/(total_adults + total_children)
    total_all_ubi = ((person2.children * all_ubi_per_person) + 
                    (person2.total_adults * all_ubi_per_person))
    new_spm_resources_all_ubi = person2.spm_resources + total_all_ubi
    new_poor_all_ubi = new_spm_resources_all_ubi < person2.spm_povthreshold
    new_total_child_poor = ((person2.child * person2.weight * 
                             new_poor_all_ubi).sum())
    new_child_poverty_rate = ((new_total_child_poor)/
                              (person2.child * person2.weight).sum())
    new_total_adult_poor = ((person2.adult * person2.weight * 
                             new_poor_all_ubi).sum())
    new_adult_poverty_rate = ((new_total_adult_poor)/
                              (person2.adult * person2.weight).sum())
    new_total_poor_all_ubi = (new_poor_all_ubi * person2.weight).sum()
    new_poverty_rate_all_ubi = new_total_poor_all_ubi/person2.weight.sum()
    ubi_all_overall.append(new_poverty_rate_all_ubi)
    ubi_all_child.append(new_child_poverty_rate)
    ubi_all_adults.append(new_adult_poverty_rate)
    
spending_data = []
for spending in range(0, 1001, 50):
    spending = spending/100
    spending_data.append(spending)
    
### ANALYSIS ###

# Create a DataFrame grouped by each plans impact on the overall poverty rate. 
overall = {'spending_in_billions': spending_data,
                       'child_allowance': child_allowance_overall,
                       'adult_ubi': ubi_adults_overall,
                       'all_ubi': ubi_all_overall}
                    
overall_df = pd.DataFrame(overall)
overall_df = pd.DataFrame(overall_df).round(3)

# Create a DataFrame grouped by each plans impact on the child poverty rate.
child = {'spending_in_billions': spending_data,
         'child_allowance': child_allowance_child,
         'adult_ubi': ubi_adults_child,
         'all_ubi': ubi_all_child}
                    
child_df = pd.DataFrame(child)
child_df = pd.DataFrame(child_df).round(3)


# Create a DataFrame grouped by each plans impact on the adult poverty rate.
adult = {'spending_in_billions': spending_data,
         'child_allowance': child_allowance_adults,
         'adult_ubi': ubi_adults_adults,
         'all_ubi': ubi_all_adults}
                    
adult_df = pd.DataFrame(adult)
adult_df = pd.DataFrame(adult_df).round(3)


# Join different programs together for plotly.
program = (pd.melt(overall_df, 'spending_in_billions', 
                   var_name='ubi_type',value_name='poverty_rate'))

def melt_dict(d):
  """ produce long version of data frame represented by dictionary (d).
  
  Arguments
  d: Dictionary where each element represents a differnt UBI type and spending levels and the poverty impacts.
  
  Returns
  DataFrame where every row is the combination of UBI type and spending level.
  """
  df = pd.DataFrame(d).round(3) * 100
  program = pd.melt(df, 'spending_in_billions', var_name='ubi_type',value_name='poverty_rate')
  program['ubi_type'] = program.ubi_type.map({'child_allowance': 'Child allowance',
                                      'adult_ubi': 'Adult UBI',
                                      'all_ubi': 'All UBI'})
  return program

program_overall = melt_dict(overall)
program_child = melt_dict(child)
program_adult = melt_dict(adult)

def line_graph(df, x, y, color, title, xaxis_title, yaxis_title):
    """Style for line graphs.
    
    Arguments
    df: DataFrame with data to be plotted.
    x: The string representing the column in df that holds the new spending in billions.
    y: The string representing the column in df that holds the poverty rate.
    color: The string representing the UBI type.
    xaxis_title: The string represnting the xaxis-title.
    yaxis_title: The string representing the yaxis-title.
    
    Returns
    Nothing. Shows the plot.
    """
    fig = px.line(df, x=x, y=y, color=color)
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        yaxis_ticksuffix='%',
        font=dict(family='Roboto'),
        hovermode='x',
        xaxis_tickprefix='$',
        xaxis_ticksuffix='B',
        plot_bgcolor='white',
        legend_title_text=''
        
    )

    fig.update_traces(mode='markers+lines', hovertemplate=None)

    return fig

fig = line_graph(df=program_overall, x='spending_in_billions', 
           y='poverty_rate', color='ubi_type',
           title='Overall poverty rate and spending on cash transfer programs',
           xaxis_title='Spending in billions',
           yaxis_title='SPM poverty rate')

fig.show()
    </code>
  </pre>
</div>

<script>
function f1() {
  var x = document.getElementById("asset_code_1");
  var b = document.getElementById("button1");
  if (x.style.display === "none") {
    x.style.display = "block";
    b.innerHTML = "&#9660 Click to hide code";
  } else {
    x.style.display = "none";
    b.innerHTML = "&#9654 Click to show code";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/adult_child_ubi/2020-07-07-adult-child-ubi-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

Unsurprisingly, a Child Allowance was the most effective program at reducing child poverty at all levels of spending. Spending $400 billion on a Child Allowance cuts child poverty by over two-thirds, from 13.6 percent to 4.3 percent.

Comparatively, spending $1 trillion on an Adult UBI leaves 7 percent of children still in poverty. For an All UBI and a Child Allowance under the same spending, 4 percent and 1 percent of children would remain in poverty, respectively.


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
fig = line_graph(df=program_child, x='spending_in_billions', 
           y='poverty_rate', color='ubi_type',
           title='Child poverty rate and spending on cash transfer programs',
           xaxis_title='Spending in billions',
           yaxis_title='SPM poverty rate among people aged 17 and under')
fig.show()
    </code>
  </pre>
</div>

<script>
function f2() {
  var x = document.getElementById("asset_code_2");
  var b = document.getElementById("button2");
  if (x.style.display === "none") {
    x.style.display = "block";
    b.innerHTML = "&#9660 Click to hide code";
  } else {
    x.style.display = "none";
    b.innerHTML = "&#9654 Click to show code";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/adult_child_ubi/2020-07-07-adult-child-ubi-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

An Adult UBI and an All UBI have nearly identical effects on the adult poverty rate. A Child Allowance has a smaller impact on adult poverty because the benefits only go to adults with children in their family.


<button class="code-button" id="button3" onclick="f3()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_3" style="display: none;">
  <pre>
    <code>
fig = line_graph(df=program_adult, x='spending_in_billions', 
           y='poverty_rate', color='ubi_type',
           title='Adult poverty rate and spending on cash transfer programs',
           xaxis_title='Spending in billions',
           yaxis_title='SPM poverty rate among people aged 18 and over')
fig.show()
    </code>
  </pre>
</div>

<script>
function f3() {
  var x = document.getElementById("asset_code_3");
  var b = document.getElementById("button3");
  if (x.style.display === "none") {
    x.style.display = "block";
    b.innerHTML = "&#9660 Click to hide code";
  } else {
    x.style.display = "none";
    b.innerHTML = "&#9654 Click to show code";
  }
}
</script> 

<div>
  <script>
    $(document).ready(function(){
      $("#asset3").load("{{site.baseurl}}assets/markdown_assets/adult_child_ubi/2020-07-07-adult-child-ubi-asset-3.html");
    });
  </script>
</div>
<div id = "asset3"></div>

## Conclusion
This analysis finds that (a) including children in basic income plans enhances their anti-poverty effects and (b) optimal policy depends on spending levels.

Given limited political support for added spending, a Child Allowance alleviates poverty most effectively. If the political appetite for anti-poverty spending is more substantial, we should aim to provide a truly universal UBI and provide cash transfers to everyone.
