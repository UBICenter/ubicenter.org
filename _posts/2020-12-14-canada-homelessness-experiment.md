---
layout: post
current: post
cover: 
navigation: True
title: What a Canadian experiment tells us about cash transfers and homelessness
date: 2020-12-14
tags: [canada, homelessness, pilots]
cover: assets/images/2020-12-14-canada-homelessness-experiment/cover.jpg
class: post-template
subclass: 'post'
author: [charles, max]
excerpt: Recipients spent mostly on their children and stable housing.
useplotly: true
---


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
        source="https://raw.githubusercontent.com/UBICenter/ubicenter.org/master/assets/images/logos/wide-blue.jpg",
        # See https://github.com/plotly/plotly.py/issues/2975.
        # source="../_static/logos/wide-blue.jpg",
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

Another way of quantifying the changes is as a share of spending. Alcohol, drugs, and cigarettes made up 9 percent of the cash group’s spending, a fifth less than the non-cash group’s 11.4 percent, while food and clothes for children made up 7.9 percent of the cash group’s spending, nearly double the 4.1 percent share in the non-cash group. The cash group also spent a larger share on clothes (for themselves) and transit, and a smaller share on rent and food.


### Transitions to stable housing

Cash recipients also spent less time homeless than the control group. The two groups started similarly, but in the month following the intervention, the cash group was only homeless for 49 percent of days, while the control group was homeless for 78 percent of those days. The effect diminished over time, and by the end of the year, the two groups converged at around a fifth of days homeless. Overall, people in the cash group spent an average of 88 fewer days homeless throughout the full year.


![Days homeless fell faster over the year for the cash group than the non-cash group](assets/images/days_homeless_chart.png "Change in days homeless for cash and non-cash groups")


Those extra 88 days in homelessness housing and services would have cost the government about $8,200, exceeding the $7,500 grant (NLP did not report total costs beyond the grant, which would factor into a comprehensive cost-effectiveness analysis).

In open-ended surveys, cash recipients reported that they did not have to depend on social services and could move into housing that better met their preferences. For instance, one participant said, “The impact it had on my life was huge. I was able to do a lot of things that I couldn't do before. It has changed my ability to make proper choices. If I had not received the cash transfer, I wouldn't be able to move out. Wouldn't be able to get my car back on the road. None of that.”


## Comparison with other studies

While NLP is the first randomized controlled trial giving unconditional cash transfers to people experiencing homelessness, it aligns with other studies on how cash transfers are spent.

The diversity of NLP participants’ spending is not unusual. The NGO GiveDirectly, which distributes unconditional cash transfers to extremely poor households in East Africa, [found](https://academic.oup.com/qje/article/131/4/1973/2468874?casa_token=r0_EGO-olVkAAAAA:D-gM7NEQ05yqBPV7qpwoDUZdQYeBkc0k0VD25VTBNDC9UAJbhM12Z45LDcGE3YRDELaGfBD7ktbJjA) in a randomized controlled trial that “With the exception of temptation goods (alcohol and tobacco), transfers increase expenditures in all categories, including food, medical and education expenditure, and social events.” GiveDirectly’s [GDLive tool](https://live.givedirectly.org/) shows unfiltered, unedited stories from recipients of their unconditional cash transfers and [universal basic income](https://www.givedirectly.org/ubi-study) payments; perusing the stories of UBI recipients reveals variety in spending, from [poultry](https://live.givedirectly.org/newsfeed/1b0ed686-5aef-4386-8fc3-0c00078d810d/199799?context=search-UBI#payment_26) and [tea seedlings](https://live.givedirectly.org/newsfeed/a048e9ee-4ee3-4af4-9a95-3e3a64b2d568/199175?context=search-UBI#payment_23) to [school fees](https://live.givedirectly.org/newsfeed/6e54ba92-ddde-4634-8c8e-f092303c56e6/199793?context=search-UBI#payment_26) and [dowries](https://live.givedirectly.org/newsfeed/65e70a79-f575-49e4-82e4-88bcf186e395/199033?context=search-UBI#payment_26) to [water tanks](https://live.givedirectly.org/newsfeed/cf2ec5ca-0fa8-4cab-98ed-3b8712ccf0e9/199064?context=search-UBI#payment_26) and [homebuilding materials](https://live.givedirectly.org/newsfeed/822e173e-d163-4472-a6ac-5124a59f44d1/199001?context=search-UBI#payment_26). A study of Australia’s Covid-19 economic support payment also found that recipients---mostly pensioners---increased spending across a [diverse range of categories](https://www.smh.com.au/business/the-economy/groceries-vs-video-games-how-women-and-men-spend-their-stimulus-payments-differently-20200419-p54l88.html). Given many in-kind assistance programs target just one or two categories each, such as food and rent, cash can fill in gaps for other needs that might be harder for policymakers to anticipate.

Spending on children is especially common, as evidenced by the robust evidence that cash transfers benefit children. As we summarize in [our child allowance paper](https://child-allowance.ubicenter.org/empirical.html), cash transfers consistently improve education and nutrition, as well as long-term outcomes like earnings and even lifespan, across both developing and developed countries. [One study](https://www.nber.org/system/files/working_papers/w14624/w14624.pdf) from Canada found that when Manitoba increased its child benefit in 2001, children ages 0 to 3 showed improved motor and social development, children ages 4-5 showed lower aggression and anxiety.

A common concern around giving money to poor people is that they will spend on temptation goods like alcohol, drugs, and cigarettes. This worry motivated San Francisco voters to [replace cash assistance](https://en.wikipedia.org/wiki/San_Francisco_Proposition_N_(2002)) for people experiencing homelessness with in-kind benefits like housing, in a 2002 program called [“Care Not Cash.”](https://www.latimes.com/politics/la-pol-ca-gavin-newsom-homelessness-san-francisco-20181023-story.html) A number of studies show such concerns to be misplaced. Data from San Francisco’s pre-Care-Not-Cash days indicates that homeless cash recipients were [less likely to use drugs](https://link.springer.com/article/10.1093/jurban/jti015) than those who didn’t receive cash (they were also less likely to receive income from selling drugs or be incarcerated, and more likely to find shelter). A [2015 Gallup poll](https://news.gallup.com/poll/184358/drinking-highest-among-educated-upper-income-americans.aspx) and a [2011 analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3185179/) of the Panel Study of Income Dynamics also found that low-income people consume less alcohol than higher-income people (though they’re more likely to drink heavy quantities and similarly likely to report that they drink more than they should). A [2014 World Bank meta-analysis](http://documents1.worldbank.org/curated/en/617631468001808739/pdf/WPS6886.pdf) demonstrates that these results are not mere correlations: data from 19 quantitative papers, including several randomized controlled trials, found that cash transfers most often _reduced_ or had no effect on temptation good consumption.[^temptation]

[^temptation]: Temptation goods are defined as: “goods that generate positive utility for the self that consumes them, but not for any previous self that anticipates that they will be consumed in the future.” But the meta study focuses principally on alcohol and tobacco. Similarly, the study suggests that temptation goods are synonymous with demerit goods or, "goods that were so demeritorious (either to the consumer or to others) that the government may be correct in regulating their use. That term is sometimes used in reference to alcohol and tobacco in cash transfer studies."


## Conclusion

Canada has long welcomed unconditional cash transfers, from the 1970s [“Mincome” program](https://www.bbc.com/worklife/article/20200624-canadas-forgotten-universal-basic-income-experiment) in Manitoba to its unusually generous [child benefit](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview.html) to its prematurely-cancelled [basic income pilot](https://www.pbs.org/newshour/economy/making-sense/ontario-is-canceling-its-basic-income-experiment) in Ontario. And as [developed](https://www.un.org/development/desa/dspd/wp-content/uploads/sites/22/2019/05/CASEY_Louise_Paper.pdf) and [developing](https://www.un.org/development/desa/dspd/wp-content/uploads/sites/22/2019/05/SPEAK_Suzanne_Paper.pdf) countries tackle homelessness, discussions inevitably include cash, whether it’s San Francisco [retracting cash assistance](https://en.wikipedia.org/wiki/San_Francisco_Proposition_N_(2002)) in 2002 or Manila introducing a [conditional cash transfer](https://link.springer.com/chapter/10.1007/978-81-322-2160-9_15) in 2012.

NLP unites Canadian interest in cash transfers with homelessness research. It shows that people experiencing homelessness spread lump-sum transfers over time and across spending categories---especially focusing on their children---and that cash transfers accelerate transitions into stable housing.

Some questions following this study remain. For example, how would cash transfers affect the [40 percent](https://canadiancentreforaddictions.org/addiction-in-the-homeless-population/) of Canadians experiencing homelessness who have substance abuse disorders? Or the [similar share](https://lop.parl.ca/staticfiles/PublicWebsite/Home/ResearchPublications/InBriefs/PDF/2014-11-e.pdf) with mental illness? NLP excluded both groups from this round, though a [recent Science meta-review](https://science.sciencemag.org/content/370/6522/eaay0214) found that "cash transfers and broader anti-poverty programs reduce depression and anxiety in randomized trials.” The long-term effects on children experiencing homelessness may be even starker, as the review also finds that “poverty experienced in childhood and in utero [results] in impaired cognitive development and adult mental illness."

Another question is: how do lump sum transfers, as used in the NLP experiment, compare to recurring payments for people experiencing homelessness? Research to date on this question has largely focused on developing countries. For example, a review of [post-emergency aid and development](https://www.odi.org/sites/odi.org.uk/files/odi-assets/publications-opinion-files/5745.pdf) contexts suggests that regular payments are less prone to corruption than lump sum transfers, and that they outperform on measures of social protection, while lump-sum transfers can more effectively spur investment if targeted to entrepreneurs. Similarly, a [GiveDirectly study](https://academic.oup.com/qje/article/131/4/1973/2468874?casa_token=r0_EGO-olVkAAAAA:D-gM7NEQ05yqBPV7qpwoDUZdQYeBkc0k0VD25VTBNDC9UAJbhM12Z45LDcGE3YRDELaGfBD7ktbJjA) among poor households in rural Kenya found: “Monthly transfers are more likely than lump-sum transfers to improve food security, whereas lump-sum transfers are more likely to be spent on durables,” and forthcoming results from its [basic income experiment](https://www.givedirectly.org/ubi-study/) will shed more light on the topic.

Beyond helping people currently experiencing homelessness, how can cash transfers prevent homelessness? Studies from [UCLA](https://www.latimes.com/business/la-fi-ucla-anderson-forecast-20180613-story.html) and [Zillow](https://www.zillow.com/research/homelessness-rent-affordability-22247/) link housing affordability and homelessness, suggesting that (along with reducing housing costs) raising incomes via cash transfers could keep people housed.

Finally: how much of these effects can be attributed to cash transfers compared to coaching, workshops, and other overhead, and how do these other costs affect cost-benefit analysis? This first experimental design makes it difficult to disentangle effects, but future experiments could omit other components to focus on the cash transfer, or test other components in a grid or hierarchical design. For example, a [recent study](https://www.nber.org/papers/w28106) on psychological well-being in rural Kenya employed a two-by-two experimental design to study the effect of cash transfers, a psychotherapy program, and the combination of the two. This revealed that, while the cash transfer improved well-being, psychotherapy did not---either by itself or in conjunction with the cash. A similar approach could quantify the effect of coaching or workshops, conditional on cash transfers.

Foundations for Social Change has committed to publishing a peer-reviewed paper on this round of results, and they are raising $10 million to enroll more participants across more Canadian cities and expand research capacity. Any follow-up research is likely to improve the precision of these estimates on expenditures and housing stability, and quantify the external validity to new contexts, even if only geographic. Open questions on cash and homelessness makes this fertile ground for further research, whether from NLP or other organizations. If nothing else, this study suggests that expanding cash assistance will increase spending on diverse needs---especially of children---and accelerate transitions to stable housing, thereby improving the range of outcomes associated with homelessness.
