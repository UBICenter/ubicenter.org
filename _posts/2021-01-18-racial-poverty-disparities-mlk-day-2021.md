---
layout: post
current: post
cover: 
navigation: True
title: Basic income would shrink racial poverty disparities
date: 2021-01-18
tags: [us, race, poverty]
class: post-template
cover: assets/images/2021-01-18-racial-poverty-disparities-mlk-day-2021/cover.jpeg
subclass: 'post'
author: [max, connor, nate]
excerpt: $600 per month or more would end one measure of the Black-White poverty disparity.
useplotly: true
---

Dr. Martin Luther King Jr. is remembered chiefly for his leadership of the civil rights movement,
but toward the end of his life, King extended this leadership to the cause of poverty.
In his [final book](http://www.thekinglegacy.org/books/where-do-we-go-here-chaos-or-community),
he wrote:

>The time has come for us to civilize ourselves by the total, direct and immediate abolition of poverty. [...] I'm now convinced that the simplest approach will prove to be the most effective — the solution to poverty is to abolish it directly by a now widely discussed measure: the guaranteed income.

We honor King's call by showing how a universal basic income (UBI), funded by a flat income tax, would not only reduce overall poverty, but also shrink the poverty disparities between Black and White people. [^modeling]


[^modeling]: Data was gathered from the US Census Bureau's March Supplement, which covers economic circumstances in 2019. We use the Supplemental Poverty Measure, which incorporates taxes and transfers (including in-kind benefits like SNAP), and adjusts for local housing costs. The flat income tax is applied on positive adjusted gross income. We calculate per-capita poverty gaps by race as the total poverty gap of SPM units with at least one person of that race, divided by the number of people in SPM units with at least one person of that race.


Black Americans today are 75 percent more likely to be in poverty than White Americans, with a rate of 18.4 percent compared to 10.5 percent.
A $250 monthly UBI would cut both Black and White poverty roughly in half (this is similar to what we found in a [July 2020 post](https://medium.com/ubicenter/how-universal-basic-income-would-affect-the-black-white-poverty-and-wealth-gaps-452e2af1497b), which used older data and did not simulate taxes to fund the UBI).
A $1,000 monthly UBI funded by a flat income tax would reduce poverty for both White and Black people to about 1 percent.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
import pandas as pd
import numpy as np
import microdf as mdf
import plotly.express as px

SPM_COLS = [
    "spm_" + i for i in ["id", "weight", "povthreshold", "resources", "numper"]
]
raw = pd.read_csv(
    "https://github.com/MaxGhenis/datarepo/raw/master/pppub20.csv.gz",
    usecols=["PRDTRACE", "MARSUPWT", "AGI"] + [i.upper() for i in SPM_COLS],
)
person = raw.copy(deep=True)
person.columns = person.columns.str.lower()
person["weight"] = person.marsupwt / 100
person.spm_weight /= 100
person = person.rename(columns={"prdtrace": "race"})
# Add indicators for white only and black only (not considering other races).
person["white"] = person.race == 1
person["black"] = person.race == 2
# Limit to positive AGI.
person["agi_pos"] = np.maximum(person.agi, 0)
# Need total population to calculate UBI and total AGI for required tax rate.
total_population = person.weight.sum()
total_agi = mdf.weighted_sum(person, "agi_pos", "weight")
# Sum up AGI for each SPM unit and merge that back to person level.
spm = person.groupby(SPM_COLS)[["agi_pos", "white", "black"]].sum()
spm.columns = ["spm_" + i for i in spm.columns]
# Merge these back to person to calculate population in White and Black spmus.
person = person.merge(spm, on="spm_id")
pop_in_race_spmu = pd.Series(
    {
        "Black": person[person.spm_black > 0].weight.sum(),
        "White": person[person.spm_white > 0].weight.sum(),
    }
)
spm.reset_index(inplace=True)


def pov_gap(df, resources, threshold, weight):
    # df: Should be SPM-unit level.
    gaps = np.maximum(df[threshold] - df[resources], 0)
    return (gaps * df[weight]).sum()


def pov(race, monthly_ubi):
    # Total cost and associated tax rate.
    cost = monthly_ubi * total_population * 12
    tax_rate = cost / total_agi
    # Calculate new tax, UBI and resources per SPM unit.
    spm["new_spm_resources"] = (
        spm.spm_resources - 
        (tax_rate * spm.spm_agi_pos) +  # New tax
        (12 * monthly_ubi * spm.spm_numper))  # UBI
    # Merge back to person.
    person2 = person.merge(spm[["spm_id", "new_spm_resources"]], on="spm_id")
    # Based on new resources, calculate
    person2["new_poor"] = person2.new_spm_resources < person2.spm_povthreshold
    # Calculate poverty rate for specified race.
    poverty_rate = mdf.weighted_mean(
        person2[person2[race.lower()]], "new_poor", "weight"
    )
    # Calculate poverty gap for specified race.
    poverty_gap = pov_gap(
        spm[spm["spm_" + race.lower()] > 0], "new_spm_resources",
        "spm_povthreshold", "spm_weight"
    )
    poverty_gap_per_capita = (poverty_gap / pop_in_race_spmu[race])

    return pd.Series({
        "poverty_rate": poverty_rate,
        "poverty_gap_per_capita": poverty_gap_per_capita
    })


def pov_row(row):
    return pov(row.race, row.monthly_ubi)


summary = mdf.cartesian_product(
    {"race": ["White", "Black"], "monthly_ubi": np.arange(0, 1001, 50)}
)
summary = pd.concat([summary, summary.apply(pov_row, axis=1)], axis=1)
# Format results.
summary.poverty_rate = 100 * summary.poverty_rate.round(3)
summary.poverty_gap_per_capita = summary.poverty_gap_per_capita.round(0)
wide = summary.pivot_table(
    ["poverty_rate", "poverty_gap_per_capita"], "monthly_ubi", "race"
)
wide.columns = ["pg_black", "pg_white", "pr_black", "pr_white"]
wide["pg_ratio"] = (wide.pg_black / wide.pg_white).round(2)
wide["pr_ratio"] = (wide.pr_black / wide.pr_white).round(2)
wide.reset_index(inplace=True)
ratios = wide.melt(id_vars="monthly_ubi", value_vars=["pr_ratio", "pg_ratio"])
# Change for chart.
ratios.variable.replace({"pr_ratio": "Poverty rate",
                         "pg_ratio": "Poverty gap per capita"},
                        inplace=True)


def add_ubi_center_logo(fig, x=0.98, y=-0.14):
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/UBICenter/ubicenter.org/master/assets/images/logos/wide-blue.jpg",
            # See https://github.com/plotly/plotly.py/issues/2975.
            # source="../_static/logos/wide-blue.jpg",
            xref="paper", yref="paper",
            x=x, y=y,
            sizex=0.12, sizey=0.12,
            xanchor="right", yanchor="bottom"
        )
    )


def line_graph(
    df,
    x,
    y,
    color,
    title,
    xaxis_title,
    yaxis_title,
    color_discrete_map,
    yaxis_ticksuffix,
    yaxis_tickprefix,
):
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
    fig = px.line(
        df, x=x, y=y, color=color, color_discrete_map=color_discrete_map
    )
    fig.update_layout(
        title=title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        yaxis_ticksuffix=yaxis_ticksuffix,
        yaxis_tickprefix=yaxis_tickprefix,
        font=dict(family="Roboto"),
        hovermode="x",
        xaxis_tickprefix="$",
        plot_bgcolor="white",
        legend_title_text="",
        height=600,
        width=1000,
    )

    fig.update_layout(
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.9)
    )

    fig.update_traces(mode="markers+lines", hovertemplate=None)
    
    add_ubi_center_logo(fig)

    return fig
    

DARK_BLUE = "#1565C0"
GRAY = "#9E9E9E"
DARK_GREEN = "#388E3C"
LIGHT_GREEN = "#66BB6A"
CONFIG = {"displayModeBar": False}

fig = line_graph(
    df=summary,
    x="monthly_ubi",
    y="poverty_rate",
    color="race",
    title="Black and White poverty rate by UBI amount",
    xaxis_title="Monthly universal basic income funded by flat income tax",
    yaxis_title="SPM poverty rate (2019)",
    color_discrete_map={"White": GRAY, "Black": DARK_BLUE},
    yaxis_ticksuffix="%",
    yaxis_tickprefix="",
)
fig.show(config=CONFIG)
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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/racial-poverty-disparities-mlk-day-2021/2021-01-18-racial-poverty-disparities-mlk-day-2021-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

The poverty rate only tells part of the story, though.
When someone goes from deep in poverty to just below the poverty line, the poverty rate is left unchanged, despite the person's material conditions improving.

An alternative measure is the *poverty gap*, which aggregates each household's difference between its resources and its poverty threshold. This counts improvements of people who remain in poverty, and can be thought of as the total amount of money required to lift everyone out of poverty, if that money could be perfectly targeted.

Applying this measure and adjusting for population differences, the Black poverty gap exceeds the White poverty gap by 50 percent: $654 per person, vs. $434 per person.
Given a $250 monthly UBI, which cuts poverty rates in half, poverty gaps also fall by about half, and the difference falls such that the Black poverty gap is about 36 percent higher.
For UBIs above $600 per month, the Black poverty gap even falls below the White poverty gap, likely due to Black people living in areas with lower-cost housing.


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
fig = line_graph(
    df=summary,
    x="monthly_ubi",
    y="poverty_gap_per_capita",
    color="race",
    title="Black and White poverty gap per capita by UBI amount",
    xaxis_title="Monthly universal basic income funded by flat income tax",
    yaxis_title="Poverty gap per capita (2019)",
    color_discrete_map={"White": GRAY, "Black": DARK_BLUE},
    yaxis_ticksuffix="",
    yaxis_tickprefix="$",
)
fig.show(config=CONFIG)
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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/racial-poverty-disparities-mlk-day-2021/2021-01-18-racial-poverty-disparities-mlk-day-2021-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

Viewing these together, it's clear that UBIs don't only reduce poverty rates and poverty gaps for both races, but also bring them closer together, reducing racial disparities in poverty.


<button class="code-button" id="button3" onclick="f3()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_3" style="display: none;">
  <pre>
    <code>
fig = line_graph(
    df=ratios,
    x="monthly_ubi",
    y="value",
    color="variable",
    title="Black poverty relative to White poverty by UBI amount",
    xaxis_title="Monthly universal basic income funded by flat income tax",
    yaxis_title="Ratio of Black to White poverty measure (2019)",
    color_discrete_map={"Poverty rate": LIGHT_GREEN,
                        "Poverty gap per capita": DARK_GREEN},
    yaxis_ticksuffix="",
    yaxis_tickprefix="",
)
fig.add_hline(1, line_dash="dot")
fig.show(config=CONFIG)
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
      $("#asset3").load("{{site.baseurl}}assets/markdown_assets/racial-poverty-disparities-mlk-day-2021/2021-01-18-racial-poverty-disparities-mlk-day-2021-asset-3.html");
    });
  </script>
</div>
<div id = "asset3"></div>

Dr. King didn't live to see today's renaissance of guaranteed income, with pandemic responses including [generous unconditional cash transfers](https://www.cbsnews.com/news/stimulus-check-600-2000-dollars-eligibility-2021-1-1/), [mayors across America](http://mayorsforagi.org) calling for pilots, and [leaders across the world](https://www.express.co.uk/news/politics/1316702/nicola-sturgeon-news-scotland-ubi-Universal-Basic-Income-SNP-latest-economy) embracing the idea.
But our analysis validates his intuition and the intertwining of his racial justice and economic justice emphases: guaranteed income will produce not only a less impoverished world, but also a less racially disparate one.
