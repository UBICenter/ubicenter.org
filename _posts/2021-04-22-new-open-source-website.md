---
layout: post
current: post
navigation: True
title: Welcome to our new open-source website
date: 2021-04-22
tags: [open source, website]
class: post-template
cover: assets/images/2021-04-22-new-open-source-website/cover.webp
subclass: 'post'
author: [matt,yuri]
excerpt: Bringing together all our research in one GitHub-served platform.
useplotly: true
---

The UBI Center's mission is to produce open-source research that informs a robust policy debate around universal basic income. We emphasize "open-source" because we believe that the public deserves full transparency into research that influences economic policy, and because we know that feedback and contributions improve our work, whether or not it comes from our staff. As our friends at the [Policy Simulation Library](https://pslmodels.org/) say, "Open Models == Better Policy."

The UBI Center has been dedicated to open-source research since its inception. In our [first](https://www.ubicenter.org/distributional-analysis-of-andrew-yangs-freedom-dividend) [studies](https://www.ubicenter.org/budgetneutral-version-of-andrew-yangs-freedom-dividend) of Andrew Yang's Freedom Dividend, we just cited Jupyter [notebooks](https://github.com/UBICenter/ubi-center/tree/master/notebooks/yang) stored on GitHub. Later, we moved to the [Jupyter Book](https://jupyterbook.org/) platform for our [blog](https://blog.ubicenter.org) and [child allowance](https://child-allowance.ubicenter.org) website; we published Jupyter notebooks directly as webpages using GitHub Pages and GitHub Actions. We've also been developing open-source software with the Policy Simulation Library like [openfisca-uk](https://github.com/pslmodels/openfisca-uk), a microsimulation model of the UK tax and benefit system, and [microdf](https://github.com/pslmodels/microdf), a data analysis package for weighted survey microdata.

This week, we're taking the open-source part of our mission to a new level: we're re-launching [ubicenter.org](https://ubicenter.org) as a new website hosted entirely on GitHub. We've moved all our posts from [Medium](https://medium.com/ubicenter) and [blog.ubicenter.org](https://blog.ubicenter.org) (which was hosted with [JupyterBook](https://jupyterbook.org/)) to the format you're seeing here, as well as content from our old Google Sites website. We're using the [Jekyll](https://jekyllrb.com/) blogging platform, the [Jasper2](https://github.com/jekyller/jasper2) theme (based on [Ghost](https://ghost.org/)'s [Casper](https://github.com/TryGhost/Casper) theme), [GitHub Pages](https://pages.github.com/), and [GitHub Actions](https://github.com/features/actions), plus a [utility](github.com/UBICenter/plotly-converter) we built for turning Jupyter notebooks into Markdown files with interactive graphics. All the code is at [github.com/ubicenter/ubicenter.org](https://github.com/ubicenter/ubicenter.org).

Beyond the advantages of open-source, our new website provides a cleaner look, more immediate access to our new research, a unified view of our projects, and organization by author and topic. For example, you can see all our research on UBI and race at [ubicenter.org/tag/race](https://ubicenter.org/tag/race).


![Posts with the "race" tag](assets/images/2021-04-22-new-open-source-website/race-tag.webp "image_tooltip")


And just like our previous JupyterBook sites like [blog.ubicenter.org](https://blog.ubicenter.org/), we still have interactive visualizations and a toggle to see the Python code that generates them, like this chart from our [Women's Day 2021 post](https://www.ubicenter.org/womens-day-2021):


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
import microdf as mdf
import numpy as np
import pandas as pd
import plotly.express as px
import ubicenter

df = pd.read_csv(
    "https://github.com/MaxGhenis/datarepo/raw/master/pppub20.csv.gz",
    usecols=[
        "MARSUPWT",
        "SPM_RESOURCES",
        "SPM_POVTHRESHOLD",
        "SPM_WEIGHT",
        "SPM_NUMPER",
        "A_SEX",
        "A_AGE",
        "SPM_ID",
        "AGI",
    ],
)
df.columns = df.columns.str.lower()
df["weight"] = df.marsupwt / 100
df["spm_weight"] = df.spm_weight / 100
df["female"] = df.a_sex == 2
df["poverty"] = df.spm_resources < df.spm_povthreshold
df["deep_poverty"] = df.spm_resources < (df.spm_povthreshold / 2)
df["sex"] = np.where(df.female, "Female", "Male")

spm = df.groupby(
    ["spm_id", "spm_resources", "spm_weight", "spm_povthreshold", "spm_numper"]
)[["agi"]].sum()
spm["agi_pos"] = np.maximum(spm.agi, 0)
spm.reset_index(inplace=True)

total_population = df.weight.sum()
total_agi_pos = mdf.weighted_sum(spm, "agi_pos", "spm_weight")

# Bin into ages aligning with 18 year old threshold.
DARK_PURPLE = "#46296E"  # Official Intl Womens Day Color.
LIGHT_PURPLE = "#907EA8"  # Lightened version.
DARK_GREY = "#9E9E9E"  # Gray 500 from Material Design.
LIGHT_GREY = "#BDBDBD"  # Gray 400.

COLOR_MAP = {
    "Female": DARK_PURPLE,
    "Male": LIGHT_GREY,
    "Female poverty": DARK_PURPLE,
    "Female deep poverty": LIGHT_PURPLE,
    "Male poverty": DARK_GREY,
    "Male deep poverty": LIGHT_GREY,
    "Poverty": DARK_PURPLE,
    "Deep poverty": LIGHT_PURPLE,
}

df["age_group"] = pd.cut(df.a_age + 1, np.arange(0, 91, 5), labels=np.arange(0, 86, 5))
pov_age = mdf.weighted_mean(
    df, ["poverty", "deep_poverty"], "marsupwt", groupby=["age_group", "sex"]
)
pov_age = pov_age.round(3)
pov_age.reset_index(inplace=True)
pov_age = pov_age.melt(["age_group", "sex"], ["poverty", "deep_poverty"])
pov_age["label"] = (
    pov_age.sex
    + " "
    + np.where(pov_age.variable == "poverty", "poverty", "deep poverty")
)

fig = px.line(
    pov_age, x="age_group", y="value", color="label", color_discrete_map=COLOR_MAP
)
fig.update_layout(
    title="Poverty by gender and age",
    xaxis_title="Age (in 5-year bins)",
    yaxis_title="SPM poverty rate (2019)",
    legend_title="",
    yaxis_tickformat="%",
    yaxis_range=[0, pov_age.value.max() * 1.1] #fig.update_xaxes(range=[1.5, 4.5])
)

fig.update_traces(mode="markers+lines", hovertemplate=None)

fig = ubicenter.format_fig(fig, show = False)
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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/womens-day-2021/2020-03-08-womens-day-2021-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>


We have much more to do, as we've listed on [github.com/UBICenter/ubicenter.org/issues](https://github.com/UBICenter/ubicenter.org/issues). From completing the [migration](https://github.com/UBICenter/ubicenter.org/issues/161) [from JupyterBook](https://github.com/UBICenter/ubicenter.org/issues/162) to [adding a search bar](https://github.com/UBICenter/ubicenter.org/issues/3) to [embedding our Twitter feed](https://github.com/UBICenter/ubicenter.org/issues/149), we're prioritizing openness in our future development. If you see something off, or if there's something you'd like to see, feel free to [submit an issue](https://github.com/UBICenter/ubicenter.org/issues/new). And if you'd like to contribute, check out our open [research assistantships and internships](https://ubicenter.org/about/join/).
