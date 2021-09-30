---
layout: post
current: post
cover: 
navigation: True
title: How a tax-funded UBI can improve the lives of Indigenous Americans
date: 2020-10-12
tags: [us, indigenous americans]
class: post-template
cover: assets/images/2020-10-12-indigenous/cover.jpg
subclass: 'post'
author: nate
excerpt: Policies of at least $250 per month would close the Indigenous/non-Indigenous poverty gap.
useplotly: true
---


Indigenous People’s Day is a time to celebrate and honor Indigenous Americans, while also recognizing the history of discrimination, oppression, and genocide they have faced since Europeans arrived in the Americas more than 500 years ago.

For centuries, American public policy has treated Indigenous Americans as second class citizens—enforcing migration, barring citizenship, and refusing to give them the fundamental rights granted to them by the Constitution. All of this produced large economic disparities that continue to this day.  Indigenous Americans are 35 percent more likely to be in poverty than non-Indigenous Americans, and their median income is a third lower.  While public policy has historically been used to marginalize Indigenous Americans, it can also be used as a tool to build them up. In this paper, I examine how a tax-funded Universal Basic Income (UBI) would impact Indigenous Americans.

## Background

To conduct the simulation I used data from the Census Bureau’s Annual Social and Economic Supplement (ASEC), which reports on data from 2019.  For each simulation, a UBI is given to every American of all ages and funded by a flat tax on Adjusted Gross Income (AGI).  AGI includes labor and capital income, and subtracts specific deductions like half of the self-employment taxes and contributions to certain retirement accounts.  Unlike taxable income, AGI does not account for most itemized deductions or the standard deduction. I assume no labor supply responses to the new taxes or income.

For each UBI amount ranging from $0 per month to $1,000 per month, I calculated the necessary tax rates (below; each $100 per month requires a 3.3 percent tax on AGI), and change in poverty rates and income distributions for both Indigenous and non-Indigenous Americans after taxes and the UBI.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
# Import Libraries
import numpy as np
import pandas as pd
import microdf as mdf
import plotly.express as px

# Import data
person = pd.read_csv('https://github.com/ngpsu22/indigenous-peoples-day/raw/main/cps_00021.csv.gz')

# Create Demographic Columns
person.columns = person.columns.str.lower()
person['child'] = person.age < 18
person['adult'] = person.age >= 18
person['native'] = person.race == 300
person['non_native'] = person.race != 300

# Calculate total AGI
person['adjginc'].replace({99999999: 0}, inplace=True)
population = person.asecwt.sum()
person['weighted_agi'] = person.adjginc * person.asecwt
total_agi = person.weighted_agi.sum()

# Calculate AGI tax rate per dollar of UBI
fed_tax_rate_per_dollar_ubi_monthly = (population * 12) / total_agi

# Create table showing tax amounts
tax_rates = pd.DataFrame(np.arange(0,1001, 50))
tax_rates.columns = ['monthly_ubi']

def tax(monthly_ubi):
    return (monthly_ubi * fed_tax_rate_per_dollar_ubi_monthly * 100).round(1)

def tax_row(row):
    return tax(row.monthly_ubi)

tax_rates['tax_rate'] = tax_rates.apply(tax_row, axis=1)
tax_rates.columns = ['monthly_ubi', 'tax_rate']

fig = px.line(tax_rates, x='monthly_ubi', y='tax_rate')
fig.update_layout(
    title='Tax rate on AGI needed to fund each UBI level',
    xaxis_title='Monthly UBI amount',
    yaxis_title='Required tax rate on adjusted gross income',
    yaxis_ticksuffix='%',
    font=dict(family='Roboto'),
    hovermode='x', 
    xaxis_tickprefix='$',
    xaxis_ticksuffix='',
    plot_bgcolor='white',
    legend_title_text=''
)
fig.update_traces(mode='markers+lines', hovertemplate=None)

fig.show(config={'displayModeBar': False})
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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/indigenous/2020-10-12-indigenous-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

## Results
The simulation shows that a tax-funded UBI has the potential to drastically reduce the poverty rate of Indigenous Americans. A UBI of $100 per month would drop Indigenous poverty below the current non-Indigenous poverty rate.  At $250 per month Indigenous poverty rates fall by more than half.  A larger UBI of $1,000 per month would drive Indigenous poverty to less than one percent.

Beyond just reducing the overall poverty rate a UBI could shrink or eliminate the poverty gap between Indigenous and non-Indigenous Americans.  At all rates of $250 per month or higher, the gap closes within one percentage point.  At all rates of $600 per month or higher, Indigenous poverty is lower than non-Indigenous poverty.


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
def ubi(race, monthly_ubi):
    """ Calculate the poverty rate, median resources, mean resources, and 
        percent of people better off for Indigenous and Non-Indigenous
        Americans at a given UBI level.
  
    Args:
        race: a person's race, for this simulation, either Indigenous or
            non-Indigenous.
        monthly_ubi: the monthly cash transfer given to each person.
  
    Returns:
        pd.Series with the following attributes:
        - The poverty rate for the selected group.
        - The median resources per person for the selected group.
        - The mean resources per person for the selected group.
        - The percent of people better off under the program for the selected
          group.
    """    

  
    # Create a copy of the person DataFrame
    target_persons = person.copy(deep=True)
    
    # Calculate a person's tax increase
    target_persons['tax_increase'] = (
        fed_tax_rate_per_dollar_ubi_monthly * monthly_ubi * 
        target_persons.adjginc)
    
    # Calculate the total UBI per SPM unit.
    target_persons['total_ubi'] = (
        target_persons.spmnpers * 12 * monthly_ubi)
  
    # Calculate the total tax increase of an SPM unit
    spmu = target_persons.groupby(['spmfamunit'])[['tax_increase']].sum()
    spmu.columns = ['total_tax_increase']
    target_persons = target_persons.merge(spmu,left_on=['spmfamunit'],
                                          right_index=True)
    
    # Calculate each SPM unit's tax rate person
    target_persons['new_spm_resources'] = (target_persons.spmtotres
                                         + target_persons.total_ubi
                                         - target_persons.total_tax_increase)
    
    # Calculate the new resources per person of each SPM unit
    target_persons['new_resources_per_person'] = (
        target_persons.new_spm_resources / target_persons.spmnpers)
      
    # Slice the data based on Race input
    if race == 'native':
        target_persons = target_persons[target_persons.native]
    if race == 'non_native':
        target_persons = target_persons[target_persons.non_native] 
  
    # Calculate the change in poverty rate
    target_persons['poor'] = (target_persons.new_spm_resources 
                            < target_persons.spmthresh)
    total_poor = (target_persons.poor * target_persons.asecwt).sum()
    target_pop = target_persons.asecwt.sum()
    
    # Calculate percent better off
    target_persons['better_off'] = (target_persons.new_spm_resources > 
                                target_persons.spmtotres)
    total_better_off = (
        target_persons.better_off * target_persons.asecwt).sum()
    percent = total_better_off / target_pop * 100

    return pd.Series([
        mdf.weighted_median(target_persons, 'new_resources_per_person',
                            'asecwt').round(0), 
        mdf.weighted_mean(target_persons, 'new_resources_per_person',
                          'asecwt').round(0), 
        (total_poor / target_pop * 100).round(1), percent])

def ubi_row(row):  
    """ Runs the ubi_pov function across the rows of a DataFrame.
  
    Args:
        row: the row of the DataFrame containing a person's race and the
            monthly UBI amount
  
    Returns:
        pd.Series with the following elements:
        - The poverty rate for the selected row.
        - The median resources per person for the selected row.
        - The mean resources per person for the selected row.
        - The percent of people better off under the program for the selected
            row.
    """  
    return ubi(row.race, row.monthly_ubi)

# Create a DataFrame that has each the each monthly UBI amount for each race
# input.
summary = mdf.cartesian_product({'monthly_ubi': np.arange(0, 1001, 50),
                       'race': ['native', 'non_native']})

# Calculate the poverty rate for each row of the summary DataFrame.
summary[['med_resources_per_person', 'mean_resources_per_person',
         'poverty_rate', 'better_off']] = summary.apply(ubi_row, axis=1)

# Format text.
center = {"med_resources_per_person": "Median resources",
          "mean_resources_per_person": "Mean resources"}
race = {"native": "Indigenous",
        "non_native": "Non-Indigenous"}

summary["race"] =  summary.race.map(race)

COLOR_MAP = {'Indigenous': '#1976D2',  # Blue.
             'Non-Indigenous': '#BDBDBD'  # Gray.
            }


def line_graph(df, x, y, color, title, xaxis_title, yaxis_title):
    """Style for line graphs.
    
    Args:
        df: DataFrame with data to be plotted.
        x: The string representing the column in df that holds the new
            spending in billions.
        y: The string representing the column in df that holds the poverty
            rate.
        color: The string representing the UBI type.
        xaxis_title: The string represnting the xaxis-title.
        yaxis_title: The string representing the yaxis-title.
    
    Returns:
        Nothing. Shows the plot.
    """
    fig = px.line(df, x=x, y=y, color=color, color_discrete_map=COLOR_MAP)
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        yaxis_ticksuffix='%',
        font=dict(family='Roboto'),
        hovermode='x', 
        xaxis_tickprefix='$',
        xaxis_ticksuffix='',
        plot_bgcolor='white',
        legend_title_text=''   
    )
    fig.update_traces(mode='markers+lines', hovertemplate=None)

    return fig

fig = line_graph(df=summary, x='monthly_ubi', 
           y='poverty_rate', color='race',
           title='The impact of a UBI on Indigenous and Non-Indigenous poverty',
           xaxis_title='Monthly UBI',
           yaxis_title='SPM poverty rate')
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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/indigenous/2020-10-12-indigenous-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

A UBI funded by a flat tax would not just benefit those currently living in poverty; our simulation finds that 83 percent of Indigenous Americans would be better off under the program, regardless of the amount.  

Further, a UBI could reduce both the median and mean income gaps between Indigenous and non-Indigenous Americans.  A \$500 per month UBI shrinks the gap in both median and mean resources by about a third.


<button class="code-button" id="button3" onclick="f3()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_3" style="display: none;">
  <pre>
    <code>
# Add commas
def comma(num):
    return num.astype(int).apply("{:,}".format)

summary["med_resources_per_person"] = comma(summary.med_resources_per_person)
summary["mean_resources_per_person"] = comma(summary.mean_resources_per_person)

# Create identifier columns
summary_long = pd.melt(summary,
                       id_vars=["monthly_ubi", "race"],
                       value_vars=['med_resources_per_person',
                                   'mean_resources_per_person'],
                       var_name="resource",
                       value_name="y")

summary_long["resource"] = summary_long.resource.map(center)

# Plot
fig = px.bar(summary_long,
             x='resource',
             y="y",
             color="race",
             barmode='group',
             animation_frame='monthly_ubi',
             text='y',
             labels={"race": "Race",
                     "monthly_ubi": "Monthly UBI",
                     "y": "Resources per person",
                     "resource": "Metric"
                    },
             color_discrete_map=COLOR_MAP,
             title="Tax-funded UBI and median/mean resources per person",
             range_y=[0, 32_000]
    )
fig.update_traces(texttemplate='$%{text}')
fig.update_layout(xaxis_title='',
                  yaxis_tickprefix='$',
                  uniformtext_minsize=9,
                  plot_bgcolor='white',
                  font=dict(family='Roboto'),
                  legend_title_text='')
fig.show(config={'displayModeBar': False})
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
      $("#asset3").load("{{site.baseurl}}assets/markdown_assets/indigenous/2020-10-12-indigenous-asset-3.html");
    });
  </script>
</div>
<div id = "asset3"></div>

## Conclusion
Disparities between Indigenous and non-Indigenous Americans are not limited to income: inequities persist in [education](https://education.wsu.edu/documents/2015/08/native-american-achievement-gap-report.pdf/), [health outcomes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2567901/), [incarceration rates](https://www.bjs.gov/content/pub/pdf/aic.pdf), and [life expectancy](http://ssrc-static.s3.amazonaws.com/wp-content/uploads/2015/04/Geographies-of-Opportunity-4.22.2015.pdf).  However, evidence suggests that cash transfers could help close these gaps as well.  One [study](https://www.aeaweb.org/articles?id=10.1257/app.2.1.86) followed a group of Cherokee Indian families that received unconditional cash transfers of approximately $4,000 annually as part of a profit sharing agreement from a local casino. When recipients of the dividend were compared to residents nearby that did not receive it, researchers found that an additional $4,000 per year for the poorest households increased educational attainment of children by one year by age 21, and reduced the chance of committing a minor crime by 22 percent for 16 and 17 year olds.  They also documented a decline in teenage pregnancy and substance abuse.  Other studies found cash transfers reduce [child obesity](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3380033), improve [health outcomes](http://eprints.lse.ac.uk/58059/1/__lse.ac.uk_storage_LIBRARY_Secondary_libfile_shared_repository_Content_STICERD_PEP%20discussion%20papers_pep01.pdf), and increase [life expectancy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5510957/).  

In short, UBI is a policy tool that has already been successfully trialed in Indigenous communities, and which has the potential to radically change the life of the average Indigenous American for the better.
