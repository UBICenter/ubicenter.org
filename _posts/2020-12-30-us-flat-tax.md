---
layout: post
current: post
cover: 
navigation: True
title: Basic income can make switching to a flat income tax progressive
date: 2020-12-30
tags: [us, tax]
class: post-template
cover: assets/images/2020-12-30-us-flat-tax/cover.png
subclass: 'post'
author: [nate, max]
excerpt: Flat tax rates of 25 percent or more would reduce poverty and inequality.
useplotly: true
---

The current US income tax code taxes different types of incomes at different rates, includes an array of credits and deductions that primarily benefit the [upper and middle class](https://fivethirtyeight.com/features/the-tax-deductions-economists-hate/), and requires Americans to spend [billions of hours and dollars](https://www.washingtonpost.com/wp-srv/politics/documents/economy082710.pdf) filing taxes each year.
A [2015 Pew survey](https://www.pewresearch.org/fact-tank/2016/04/06/the-biggest-u-s-tax-breaks/) found that 66 percent of Republicans and 48 percent of Democrats support completely changing the tax system.
While there are many ways to reform the tax code, a simple way is taxing every dollar at the same rate; this is often called a "flat tax."
In this paper, we examine the impact of replacing today’s system with a budget-neutral combination of flat income taxes and universal basic incomes (UBIs).

## US flat tax simulations

We simulated the effect of replacing the current federal income tax code and employee side payroll tax with a flat tax over a range of rates.
We allocated any excess revenue to a UBI to make each reform budget-neutral, and filled budget shortfalls with a head tax (equal tax amount per person, essentially a negative UBI). [^modeling]

[^modeling]:We replaced all elements of the personal income tax code, including refundable tax credits, but we retained benefit programs. The analysis is fully static; we did not model changes to labor supply resulting from the changes to marginal tax rates and incomes. We used the Current Population Survey (CPS) March Supplement reflecting income from 2019. The Census Bureau estimates tax liabilities using a microsimulation model, but income and taxes are known to be under-reported in the CPS.

A flat tax of approximately 18 percent would raise the same amount of revenue as federal income taxes and employee side payroll do today.
Each percentage point of flat tax raises enough revenue to fund a UBI of $360 per year for each adult and child.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import microdf as mdf
import statsmodels.api as sm
import stargazer.stargazer as sg
from pandas_datareader import wb


summary = pd.read_csv("data/summary.csv")


BLUE = "#1976D2"
DARK_BLUE = "#1565C0"
LIGHT_BLUE = "#90CAF9"
GRAY = "#BDBDBD"
CONFIG = {"displayModeBar": False}

def add_ubi_center_watermark(fig, x, y=-0.14):
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

fig = px.line()

fig.add_trace(
    go.Scatter(
        x=summary.flat_tax,
        y=summary.ubi.round(),
        mode="markers+lines",
        name="UBI (head tax)",
        line=dict(color=BLUE, width=2),
    )
)

fig.add_shape(
    type="line", line=dict(dash="dot", color="gray"), x0=-1, x1=50, y0=0, y1=0
)

fig.update_xaxes(
    tickangle=0,
    title_text="Flat tax rate",
    tickfont={"size": 14},
    title_standoff=25,
    ticksuffix="%",
    tickprefix="",
)

fig.update_yaxes(
    title_text="Budget-neutral annual UBI (head tax)",
    tickprefix="$",
    tickfont={"size": 14},
    title_standoff=25,
)

fig.update_xaxes(title_font=dict(size=16, color="black"))
fig.update_yaxes(title_font=dict(size=16, color="black"))
fig.update_layout(
    title_text="Budget-neutral UBI (head tax) by flat tax rate",
    hoverlabel_align="right",
    font_family="Roboto",
    title_font_size=20,
)

add_ubi_center_watermark(fig, 0.98)

fig.update_layout(plot_bgcolor="white", hovermode="x")
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.8))
fig.update_traces(mode="markers+lines")

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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

This replacement would increase the poverty rate by 37 percent, increase the poverty gap (the dollar amount needed to lift everyone above the poverty line) by 23 percent, and increase inequality (as measured by the Gini index of resources per person) by 7 percent.

Maintaining current levels of poverty and inequality requires a higher tax rate to raise funds for a UBI.
A 21 percent flat tax, which would give each person $1,200 per year, would maintain the current poverty gap; a rate and poverty gap; a 22 percent tax giving each person about $1,600 per year would maintain the current poverty rate; a 23 percent tax giving each person about $1,900 would maintain current inequality.

Higher taxes funding more generous UBIs reduce poverty and inequality to a greater degree.
A flat tax of 30 percent would fund a UBI (including children) of nearly $4,500---cutting poverty in half and inequality by 9 percent.
Going up to 50 percent funds a $1,000 monthly UBI, leaving the poverty rate at a tenth of its currently level and cutting inequality by a third.

The chart below shows how different flat tax rates up to 50 percent would impact poverty and inequality (the hover function shows the corresponding head tax or UBI for each reform).


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
def trace(col, chg_col, name, string, color):
    """
    Args:
        col: Column name.
        chg_col: Column name of change.
        name: Name of column for printing.
        string: Formatting of customdata[1].
        color: Line color.
    """
    fig.add_trace(
        go.Scatter(
            x=summary.flat_tax,
            y=summary[chg_col],
            mode="markers+lines",
            name=name,
            line=dict(color=color, width=2),
            customdata=np.stack((summary.ubi, summary[col]), axis=-1),
            hovertemplate="<br>Flat tax: %{x}<br>"
            + "UBI (head tax): $%{customdata[0]: .0f}<br>"
            + name
            + ": "
            + string
            + "<br>"
            + "Percent change: %{y:.0f}%<br>",
            marker=dict(size=5),
        )
    )


fig = px.line()
trace(
    "poverty_rate",
    "change_poverty_rate",
    "Poverty rate",
    "%{customdata[1]: .1f}%",
    DARK_BLUE,
)
trace(
    "poverty_gap_billions",
    "change_poverty_gap",
    "Poverty gap",
    "$%{customdata[1]: .0f}B",
    LIGHT_BLUE,
)
trace("gini", "change_gini", "Gini index", "%{customdata[1]}", GRAY)


fig.update_xaxes(
    tickangle=0,
    title_text="Flat tax rate",
    tickfont={"size": 14},
    title_standoff=25,
    ticksuffix="%",
    tickprefix="",
    range=[-2, 51],
)

fig.update_yaxes(
    title_text="Percent change",
    ticksuffix="%",
    tickfont={"size": 14},
    title_standoff=25,
    range=[-101, 301],
)

fig.update_xaxes(title_font=dict(size=16, color="black"))
fig.update_yaxes(title_font=dict(size=16, color="black"))
fig.update_layout(
    title_text=(
        "Replacing employee side FICA and federal income taxes with "
        "a flat tax and UBI (head tax)"
    ),
    title_font_size=20,
    hoverlabel_align="right",
    font_family="Roboto",
)

add_ubi_center_watermark(fig, 1.01)

fig.update_layout(plot_bgcolor="white", hovermode="x")
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor="black")
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.75))

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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

From the point of the flat tax producing a UBI (18 percent), higher rates lead to more Americans benefiting on a net basis.
Replacing today’s taxes on individual income with a 28 percent flat tax would give each person about $3,700 per year, benefiting the majority of Americans.
The share that come out ahead levels off around 60 percent, with flat taxes of 40 percent or more.


<button class="code-button" id="button3" onclick="f3()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_3" style="display: none;">
  <pre>
    <code>
fig = px.line()

fig.add_trace(
    go.Scatter(
        x=summary.flat_tax,
        y=summary.percent_better_off,
        mode="markers+lines",
        name="",
        line=dict(color=BLUE, width=2),
        customdata=np.stack(
            (summary.ubi, summary.percent_better_off), axis=-1
        ),
        hovertemplate="<br>Flat tax: %{x}<br>"
        # TODO: Adapt "UBI" vs "head tax" for value.
        + "UBI (head tax): $%{customdata[0]: .0f}<br>"
        + "Share better off: %{y:.0f}%<br>",
        marker=dict(size=5),
    )
)

fig.add_shape(
    type="line",
    line=dict(dash="dot", color="gray"),
    x0=-1,
    x1=50,
    y0=50,
    y1=50,
)

fig.update_xaxes(
    tickangle=0,
    title_text="Flat tax rate",
    tickfont={"size": 14},
    title_standoff=25,
    ticksuffix="%",
    tickprefix="",
)

fig.update_yaxes(
    title_text="",
    ticksuffix="%",
    tickfont={"size": 14},
    title_standoff=25,
    tickvals=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    range=[20, 80],
)

fig.update_xaxes(title_font=dict(size=16, color="black"))
fig.update_yaxes(title_font=dict(size=16, color="black"))
fig.update_layout(
    title_text=(
        "Share of people who gain from switching to a flat tax and "
        "UBI (head tax)"
    ),
    title_font_size=20,
    hoverlabel_align="right",
    font_family="Roboto",
)

add_ubi_center_watermark(fig, 0.98)

fig.update_layout(plot_bgcolor="white", height=600, width=1000, hovermode="x")
fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.8))
fig.update_traces(mode="markers+lines")

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
      $("#asset3").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-3.html");
    });
  </script>
</div>
<div id = "asset3"></div>

## Generous transfers are the key to inequality reduction

Labor markets don't explain the unusually high level of inequality in the United States, third only to Chile and Mexico among developed countries.
For example, the US has similar "market income" inequality as France, Germany, and Finland---each with Gini indexes of 0.50 to 0.51, as shown in the right bars of this graph from [Our World In Data](https://ourworldindata.org/income-inequality).

![](assets/images/inequality-of-incomes-before-and-after-taxes-and-transfers.png)

What's unusual about the US is how little its government reduces inequality through redistribution.
While France, Germany, and Finland reduce inequality by 0.21, 0.22, and 0.24 on the Gini scale, the US only reduces it by 0.12.

What mechanisms do these other countries utilize to cut inequality twice as much as the US?
Counterintuitively, it's not progressive taxation---the US actually has the most progressive tax code in the OECD,[^progressive-tax] and tax progressivity does not correlate significantly to inequality reduction (if anything the relationship is slightly negative).[^inequality-data]

[^progressive-tax]: As of 2005, the US had the most progressive tax code of any OECD country according to the concentration index (as shown in the graph), as well as two alternative measures: the ratio of concentration coefficients of household taxes to the Gini index of market income, and the ratio of the richest decile's tax share to its market income share ([Table 4.5](https://read.oecd-ilibrary.org/social-issues-migration-health/growing-unequal_9789264044197-en#page108) of *Growing Unequal?*).

[^inequality-data]: Data on inequality reduction comes from Our World In Data's analysis of OECD data reflecting the period 2012 to 2014. Data on the concentration index and income shares of household taxes and cash transfers come from Table 4.6 of the OECD's 2008 report, [*Growing Unequal?*](https://read.oecd-ilibrary.org/social-issues-migration-health/growing-unequal_9789264044197-en#page109), which uses data from around 2005. Country population is as of 2014 from the World Bank. Taxes include income taxes and employee social security contributions, not consumption taxes; however, per [Figure 11.2](https://read.oecd-ilibrary.org/social-issues-migration-health/growing-unequal_9789264044197-en#page296) in *Growing Unequal?*, consumption taxes have a small effect on relative levels of inequality across OECD countries.


<button class="code-button" id="button4" onclick="f4()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_4" style="display: none;">
  <pre>
    <code>
# Get data.
pop = wb.download(indicator="SP.POP.TOTL",
                  country='all', start=2014, 
                  end=2014).reset_index().drop('year', axis=1)
pop.rename({"SP.POP.TOTL": "population"}, axis=1, inplace=True)
# Align countries with Our World In Data and current convention.
pop.country.replace({"Czech Republic": "Czech Rep.",
                     "Slovak Republic": "Slovakia",
                     "Korea, Rep.": "South Korea"},
                     inplace=True)

oecd_raw = pd.read_csv("data/oecd_growing_unequal_2008_table_4_6.csv")
# Align countries with Our World In Data and current convention.
oecd_raw.country.replace({"Korea": "South Korea",
                          "Slovak Rep.": "Slovakia"},
                         inplace=True)
owid = pd.read_csv("data/inequality_pre_post_redistribution.csv")
owid["gini_diff"] = owid.gini_market - owid.gini_disposable
oecd = oecd_raw.merge(owid, on="country").merge(pop, on="country")
oecd["sqrt_pop"] = np.sqrt(oecd.population)

LABELS = {"gini_diff":
          "Gini reduction via taxes and transfers",
          "household_taxes_concentration":
          "Household tax concentration index",
          "public_cash_transfers_income_share":
          "Cash transfer share of household income",
          "population":
          "Population",
          "household_taxes_income_share":
          "Tax share of household income"
         }

# Make plot.
def ineq_scatter(x, xtitle, title, logo_x=1):
    fig = px.scatter(oecd, x=x, y="gini_diff", hover_name="country",
                     size="sqrt_pop", #trendline="ols",
                     labels=LABELS,
                     size_max=30)
    # Remove sqrt_pop from hover template.
    hovertemplate = ("<b>%{hovertext}</b><br><br>" +
                     LABELS[x] + "=%{x}<br>"
                     "Gini reduction via taxes and transfers=%{y}")
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(
        title_text=title,
        title_font_size=20,
        font_family="Roboto",
    )

    fig.update_xaxes(
        tickangle=0,
        title_text=xtitle,
        tickfont={"size": 14},
        title_standoff=25,
        ticksuffix="",
        tickprefix="",
    )

    fig.update_yaxes(
        title_text="Difference between market and disposable income Gini index",
        ticksuffix="",
        tickfont={"size": 14},
        title_standoff=25,
    )
    if x == "public_cash_transfers_income_share":
        fig.update_xaxes(ticksuffix="%")

    fig.update_xaxes(title_font=dict(size=16, color="black"))
    fig.update_yaxes(title_font=dict(size=16, color="black"))

    add_ubi_center_watermark(fig, x=logo_x, y=-0.17)

    fig.update_layout(plot_bgcolor="white")

    return fig
    
fig = ineq_scatter(x="household_taxes_concentration",
             xtitle="Household tax concentration index",
             title="Tax progressivity and inequality reduction in the OECD")
fig.show()
    </code>
  </pre>
</div>

<script>
function f4() {
  var x = document.getElementById("asset_code_4");
  var b = document.getElementById("button4");
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
      $("#asset4").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-4.html");
    });
  </script>
</div>
<div id = "asset4"></div>

A stronger correlate of inequality reduction is the generosity of public cash transfers.
The countries that distribute a higher share of household income as cash transfers generally cut inequality more.


<button class="code-button" id="button5" onclick="f5()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_5" style="display: none;">
  <pre>
    <code>
fig = ineq_scatter(x="public_cash_transfers_income_share",
             xtitle="Public cash transfers / household disposable income",
             title="Cash transfer generosity and inequality reduction in the OECD",
             logo_x=0.95)
fig.show()
    </code>
  </pre>
</div>

<script>
function f5() {
  var x = document.getElementById("asset_code_5");
  var b = document.getElementById("button5");
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
      $("#asset5").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-5.html");
    });
  </script>
</div>
<div id = "asset5"></div>

While overall tax levels also significantly correlate with inequality reduction, the effect vanishes when controlling for cash transfers, as shown in column 4 of the regression table below.
Cash transfers are consistently the dominant predictor of the extent to which governments reduce inequality.


<button class="code-button" id="button6" onclick="f6()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_6" style="display: none;">
  <pre>
    <code>
oecd = sm.add_constant(oecd)

def gini_reg(x, weighted=True):
    if weighted:
        m = sm.WLS(oecd.gini_diff, oecd[x + ["const"]], oecd.population)
    else:
        m = sm.WLS(oecd.gini_diff, oecd[x + ["const"]])
    return m.fit(cov_type="HC1")  # Robust standard errors.

cash_m = gini_reg(["public_cash_transfers_income_share"])
tax_prog_m = gini_reg(["household_taxes_concentration"])
tax_level_m = gini_reg(["household_taxes_income_share"])
combined_m = gini_reg(["household_taxes_concentration",
                       "household_taxes_income_share",
                       "public_cash_transfers_income_share"])

def starg(models, covariate_order=None):
    """ Creates formatted Stargazer object.
    """
    star = sg.Stargazer(models)
    if covariate_order is not None:
        star.covariate_order(covariate_order)
    star.rename_covariates(LABELS)
    star.show_adj_r2 = False
    star.show_residual_std_err = False
    star.show_f_statistic = False
    return star


star = starg([cash_m, tax_level_m, tax_prog_m, combined_m],
             ["public_cash_transfers_income_share",
              "household_taxes_income_share",
              "household_taxes_concentration",
              ])
star.add_custom_notes(["Weighted by population. Robust SEs."])
star.title("Inequality reduction and tax levels, tax progressivity, and cash "
           "transfers")
star
    </code>
  </pre>
</div>

<script>
function f6() {
  var x = document.getElementById("asset_code_6");
  var b = document.getElementById("button6");
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
      $("#asset6").load("{{site.baseurl}}assets/markdown_assets/us-flat-tax/2020-12-30-us-flat-tax-asset-6.html");
    });
  </script>
</div>
<div id = "asset6"></div>

This cross-country picture aligns with our simulations: larger UBIs cut inequality more, and even if the tax system that funds those larger UBIs isn't progressive, ability to fund the UBI is what matters.

## Conclusion

Beyond their simplicity, flat taxes have a number of theoretical advantages.
Progressive tax structures necessarily encourage shifting income from one year to the next as well as [marriage, divorce, or both](https://www.cbo.gov/sites/default/files/105th-congress-1997-1998/reports/marriage.pdf).[^marriage]
Flat taxes treat income neutrally, regardless of when it was earned, by whom, or earners' family choices.
And because they align marginal tax rates (which determine labor incentives) with effective tax rates (which determine revenue), they raise revenue with relatively little work disincentive.
For example, a [2020 paper](https://www.nber.org/papers/w27622) from the National Bureau of Economic Research found that "a uniform flat tax on capital and labor income combined with a lump-sum transfer is nearly optimal."

[^marriage]: Consider, for example, two couples: one with $30,000 earnings each, and another with one earning $60,000 and the spouse earning $0. And consider a progressive tax policy with two rates: 0% (a standard deduction) and 50%. If the standard deduction is $30,000, the first couple has a total tax liability of $15,000 if filing as a couple, but $0 if filing separately---a large marriage bonus (the second couple's tax liability is $15,000 whether married or separate). If the standard deduction instead varies with marital status, e.g. $15,000 for singles and $30,000 for couples, then the first couple will be treated neutrally, paying $15,000 whether filing separate or married. But now the second couple faces a marriage *bonus*, paying $22,500 in taxes if filing separately, but only $15,000  if married. This can be partly remedied by moving to an individualized tax system, as the United Kingdom does, where earnings are taxed independently of a spouse's earnings. But couples will still have joint assets, and therefore face marriage penalties or bonuses on their capital income if capital income is taxed progressively. Only a flat tax avoids marriage penalties or bonuses.

Our simulations and cross-country comparisons show that these advantages don't need to come at the cost of progressivity; if anything, they may enhance progressivity.
Even a 30 percent flat income tax, with excess revenue distributed as UBI, could cut poverty in half, reduce inequality by 10 percent, and leave most Americans better off.
To achieve the egalitarianism of other developed countries, the US should focus less on progressive taxation, and more on how to raise enough revenue to distribute it broadly, effectively, and generously.
