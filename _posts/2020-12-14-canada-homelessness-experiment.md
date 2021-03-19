---
layout: post
current: post
cover: 
navigation: True
title: What a Canadian experiment tells us about cash transfers and homelessness
date: 2020-12-14
tags: [blog, Canada, homelessness]
class: post-template
subclass: 'post'
author: [charles, max]
---

<head>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>


[35,000 Canadians](https://homelesshub.ca/sites/default/files/SOHC16_final_20Oct2016.pdf) experience homelessness each night, violating their [right to adequate housing](https://www.ohchr.org/EN/Issues/Housing/Pages/Homelessnessandhumanrights.aspx) and threatening their [health, safety](https://depts.washington.edu/triolive/quest/2007/TTQ07033/effects.html#:~:text=Their%20health%20gets%20worse%20from,Cardio%2DRespiratory%20diseases) and access to [education](https://journals.sagepub.com/doi/pdf/10.3102/0013189X12468210?casa_token=YsJRZhavl9EAAAAA:iKO6XaWu6oNbDgcRzw3Tml-_m6mHEYmRWGY48rzXTStFpmBEWzqa1L_euQoV8WXYkrwZ8vxj-KGMGQ). The Covid-19 pandemic exacerbates the issue, given [crowded living conditions and comorbidities](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7206983/), and the Canadian government has taken new steps to address it, such as [moving people experiencing homelessness into hotels](https://www.theglobeandmail.com/canada/article-could-shelter-hotels-be-a-model-for-addressing-homelessness/).

Prior to the pandemic, a Vancouver nonprofit, [Foundations for Social Change](https://forsocialchange.org/), worked with the University of British Columbia to test a novel homelessness intervention: [unconditional cash transfers](https://static1.squarespace.com/static/5f07a92f21d34b403c788e05/t/5f751297fcfe7968a6a957a8/1601507995038/2020_09_30_FSC_Statement_of_Impact_w_Expansion.pdf). In spring 2018, their [New Leaf Project](https://forsocialchange.org/new-leaf-project-overview) (NLP) granted a lump sum cash transfer to [Lower Mainland](https://www.britishcolumbia.ca/invest/communities/british-columbia/lower-mainland-southwest/) residents experiencing homelessness, and compared their outcomes to a control group. While some questions remain, the findings reveal that unconditional cash transfers, which are otherwise shown to improve [health](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD011135.pub2/full), [education](https://www.sciencedirect.com/science/article/pii/S1570677X18303575), and other outcomes, offer potential to reduce homelessness.


## Study overview

NLP selected 115 long-term residents or citizens of Canada aged 19 to 64 who had experienced homelessness within the previous six months. This group is fairly representative of Canada’s homeless population, given only about [10 percent](https://www.homelesshub.ca/about-homelessness/homelessness-101/how-many-people-are-homeless-canada) of people experiencing homelessness in a year were homeless for more than a month, and about [four percent](https://homelesshub.ca/sites/default/files/SOHC16_final_20Oct2016.pdf) are aged 65 or older. People with severe substance abuse or mental health disorders were ineligible for NLP.

At the beginning of the experiment, NLP deposited CAD 7,500[^cad] into the bank accounts of 50 participants, randomly selected from the full group of 115. Each cash recipient was also provided access to workshops, and 25 also had access to coaching. Of the 65 who did not receive cash, 19 were provided access to workshops and coaching, while the other 46 were not.[^unbalanced] Workshops focused on the development of a personal financial plan and self-affirmation exercises, and the coaching was offered for six months, aiming to develop and sustain life skills and strategies. Researchers tracked participants over twelve months, filling out questionnaires at one, three, six, nine and twelve months and open-ended qualitative interviews at six and twelve months. 

[^cad]: CAD 7,500 is equivalent to about USD 5,900 as of December 2020.

[^unbalanced]: Researchers did not explain their choice to have unbalanced treatment and control groups, or to give workshop access only to the cash group.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
import pandas as pd
import plotly.express as px

design = pd.DataFrame(
    {
        "Workshop": [25, 0],
        "Workshop + coaching": [25, 19],
        "Neither": [0, 46]
    },
    index=["Cash", "No cash"],
)
design
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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/canada-homelessness-experiment/2020-12-14-canada-homelessness-experiment-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

## Results


### Spending

The cash group spent an average of CAD 426 per month more than the non cash group over the course of the year. This amounts to 42 percent more than the non-cash group, or 6 percent of the total CAD 7,500 lump sum transfer. This extra spending covered a diverse range of categories: 54 percent more on transit, 113 percent more on clothing, 34 percent more on food, and so on. Of the treatment groups, the cash group increased its expenditure on alcohol, drugs, and cigarettes by the smallest proportion (11 percent).[^alcohol] It also increased its expenditure on food and clothing for the children of recipients by the largest proportion (171 percent).

[^alcohol]: The [study](https://static1.squarespace.com/static/5f07a92f21d34b403c788e05/t/5f751297fcfe7968a6a957a8/1601507995038/2020_09_30_FSC_Statement_of_Impact_w_Expansion.pdf) claims a "39% reduction in spending on alcohol, cigarettes and drugs." In email correspondence, Foundations for Social Change clarified that this is a comparison of pre-pilot spending with that at the end of 12 months for the cash group (i.e. not compared to the non-cash group).


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
# Construct data from report.
raw = pd.read_csv("new_leaf_homeless_expenditures.csv")
raw.set_index('spending_category', inplace=True)
# Sum food and clothing categories.
food_clothes_kids = raw.loc[['Food for kids', 'Clothes for kids']].sum()
food_clothes_self = raw.loc[['Food', 'Clothes']].sum()
spending = raw.drop(["Food", "Clothes", "Food for kids", "Clothes for kids"])
spending.loc["Food and clothes for self"] = food_clothes_self
spending.loc["Food and clothes for kids"] = food_clothes_kids

# Add total row and label total for graph.
spending.loc['TOTAL'] = spending.sum()
spending['is_total'] = spending.index == 'TOTAL'

spending.index.rename('Category', inplace=True)
spending['% difference'] = (
    100 * (spending.cash / spending.non_cash - 1)).round()


import plotly.graph_objects as go

# Plot % difference.
BLUE = '#1976D2'
DARK_BLUE = '#0D47A1'
COLOR_MAP = {True: DARK_BLUE, False: BLUE}  # Total vs non-total.
spending_order = spending.sort_values('% difference')
spending_order.rename({'cash': 'Cash', 'non_cash': 'Non-cash',
                       'is_total': 'Total'},
                      axis=1, inplace=True)
fig = px.bar(spending_order, y=spending_order.index, x='% difference',
             color='Total', color_discrete_map=COLOR_MAP,
             orientation='h', hover_data=['Cash', 'Non-cash'])

fig.update_layout(font=dict(family='Roboto'),
                  plot_bgcolor='white',
                  paper_bgcolor='white',
                  showlegend=False,
                  xaxis_title='Difference between cash and non-cash group',
                  yaxis_title='',
                  xaxis_ticksuffix='%',
                  yaxis={'categoryorder': 'array',
                         'categoryarray': spending_order.index},
                  title='Spending differences between cash and non-cash groups'
                  )
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/UBICenter/blog/master/jb/_static/ubi_center_logo_wide_blue.png",
        # See https://github.com/plotly/plotly.py/issues/2975.
        # source="../_static/ubi_center_logo_wide_blue.png",
        xref="paper", yref="paper",
        x=1.04, y=-0.13,
        sizex=0.12, sizey=0.12,
        xanchor="right", yanchor="bottom"
    )
)
fig.show(config={'displayModeBar': False})
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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/canada-homelessness-experiment/2020-12-14-canada-homelessness-experiment-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>
