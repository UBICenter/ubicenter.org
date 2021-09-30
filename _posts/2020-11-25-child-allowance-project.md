---
layout: post
current: post
cover:
navigation: True
title: Our new child allowance project
date: 2020-11-25
cover: assets/images/2020-11-25-child-allowance-project/cover.webp
tags: [us, child allowance]
class: post-template
subclass: 'post'
author: [nate, john, matt, max]
excerpt: We're examining universal payments to parents across multiple angles.
useplotly: true
---

_See the full project at [child-allowance.ubicenter.org](https://child-allowance.ubicenter.org)._


1 in 7 children in the United States lives in poverty, [raising](https://heckmanequation.org/resource/invest-in-early-childhood-development-reduce-deficits-strengthen-the-economy/) stress and crime rates, [worsening](https://www.sciencedirect.com/science/article/abs/pii/S1876285915003836) educational outcomes, and [shrinking](https://www.nap.edu/catalog/25246/a-roadmap-to-reducing-child-poverty) the economy by up to $1 trillion annually. Research shows that giving money to families with children, as [most developed countries do](https://www.vox.com/future-perfect/2019/3/6/18249290/child-poverty-american-family-act-sherrod-brown-michael-bennet), reduces each of these issues. A child allowance is a policy that gives families an equal amount for each child.

This project examines child allowances through various lenses:
* [**Simulations**](2020-11-25-child-allowance-state-simulation) quantifying the effects of child allowance policies (deficit- and tax-funded) on poverty and inequality across US states.
* [**Research**](https://child-allowance.ubicenter.org/empirical) on the effects of child allowances and similar policies on children, based on randomized controlled trials and other empirical techniques.
* [**Policy context**](https://child-allowance.ubicenter.org/policies) of existing US child benefits and child allowances in other countries.

For example, this interactive map is one of several visualizations in our [simulations page](2020-11-25-child-allowance-state-simulation).


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
# TODO: Add tax reforms as a drop-down (mirrored from simulation.ipynb).

# Imports.
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data.
summary = pd.read_csv('https://github.com/ngpsu22/Child_Allowance_States/raw/main/poverty_gini_tax_child_allowance')

# General configs.
LABELS = {'monthly_ca': 'Monthly child allowance',
          'decile': 'Decile',
          'net_chg': 'Net change',
          'pct_chg': 'Net change',
          'child_allowance':'Monthly child allowance',
          'code': 'State',
          'state': 'State',
          'fed_tax_rate': 'Tax rate',
          'state_tax_rate': 'Tax rate',
          'non_funded_poverty_rate': 'Poverty rate',
          'fed_poverty_rate': 'Poverty rate',
          'state_poverty_rate': 'Poverty rate',
          'non_funded_gini': 'Gini index',
          'fed_gini': 'Gini index',
          'state_gini': 'Gini index'}

CONFIG = {'displayModeBar': False}

# Preprocess data.
summary.drop('Unnamed: 0', 1, inplace = True)
state_dict = summary[['code', 'state']].set_index('code').to_dict()['state']

# data labels
FUNDING = {'fed_poverty_rate': 'Federal tax',
           'state_poverty_rate': 'State tax',
           'non_funded_poverty_rate': 'No funding'}

ca_amts = summary.child_allowance.unique()
child_poverty = summary[(summary['age_group'] == 'child') &
                        (summary['race'] == 'All')]

# create figure dictionary
fig_dict = {
    'data': [],
    'layout': {},
    'frames': []
}

# fill in most of layout
fig_dict['layout'] = {
    'plot_bgcolor': 'white',
    'font': dict(family = 'Roboto'),
    'height': 600,
    'margin': dict(t=100, b=0, l=0, r=10)
}
fig_dict['layout']['title'] = {
    'text': ('Child poverty by state and child allowance amount'),
    'y': 0.97,
    'x': 0.05,
    'xanchor': 'left',
    'yanchor': 'top'
}

# add slider specifications
slidermenu =  {
    'buttons': [
        {
            'args': [None, {'frame': {'duration': 500, 'redraw': True},
                            'fromcurrent': True,
                            'transition': {'duration': 300,
                                           'easing': 'quadratic-in-out'}}],
            'label': '&#9654;',
            'method': 'animate'
        },
        {
            "args": [[None], {"frame": {"duration": 0, "redraw": True},
                              "mode": "immediate",
                              "transition": {"duration": 0}}],
            "label": "&#9724;",
            "method": "animate"
        }
    ],
    'direction': 'left',
    'pad': {'r': 15, 't': 75},
    'showactive': True,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top'
}
    
sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Monthly child allowance: ',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

steps = []
for ca in ca_amts:
    slider_step = {
        'args': [
            [ca],
            {'frame': {'duration': 300, 'redraw': True},
             'mode': 'immediate',
             'transition': {'duration': 300}}
        ],
        'label': '$' + str(ca),
        'method': 'animate'
    }
    steps.append(slider_step)
sliders_dict['steps'] = steps

# generate frames
frames = []
locations = child_poverty.code
zero_poverty = child_poverty[child_poverty.child_allowance == 0]
for ca in ca_amts:
    data_list = []
    ca_data = child_poverty[child_poverty.child_allowance == ca]
    for funding in FUNDING:
        data_list.append({
            'hovertemplate': 
                '<b>%{customdata[1]}</b>' + 
                '<br>Child poverty rate: %{z}%<br>' + 
                'Poverty reduction: %{customdata[0]}%' +
                '<extra></extra>',
            'locationmode': 'USA-states',
            'locations': child_poverty.code.unique(),
            'z': ca_data[funding].tolist(),
            'type': 'choropleth',
            'customdata': list(map(lambda x, y, z: (round(100 * (1 - y / x)), state_dict[z]),
                                   zero_poverty[funding], ca_data[funding], state_dict))
        })
    
    frame = {'data': data_list, 'name': str(ca), 'traces': [0,1,2]}
    frames.append(frame)
    
# add frames to figure dictionary
fig_dict['frames'] = frames

# add traces to figure dictionary
for i in (range(len(FUNDING))):
    fig_dict['data'].append(frames[0]['data'][0])

# generate figure
fig = go.Figure(fig_dict)

# generate dropdown menu buttons
buttons = []
for funding in FUNDING:
    new_button = {'method': 'update',
                  'label': FUNDING[funding],
                  'args': [{'visible': [f == funding for f in FUNDING.keys()]}
                          ]}
    buttons.append(new_button)
    
# construct button menu
updatemenu = {'buttons': buttons,
              'direction': 'down',
              'showactive': True,
              'pad':{"r": 10, 't': 20, 'l': 50},
              'xanchor': 'left',
              'yanchor': 'top',
              'x': 0,
              'y': 1.2
             }

# add slider, dropdown menu, and set geo scope
fig.update_layout(
    geo_scope='usa', # limite map scope to USA
    sliders=[sliders_dict],
    updatemenus=[slidermenu, updatemenu]
)

# update visual attributes
fig.update_traces(showscale=False, colorscale='Reds', zmin=0, zmax=22)
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font=dict(family='Roboto')
    ),
    title_font_size=20,
)
fig.update(layout_showlegend=False)

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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/index/2020-11-25-index-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

We also review the evidence around child allowances from the United States and Canada, and a special deep dive into research from sub-Saharan Africa, where randomized cash transfer rollouts produce particularly high-quality estimates. For example, cash transfer programs consistently reduced consumption poverty (below). See the [**full paper**](https://child-allowance.ubicenter.org/empirical) for evidence across other outcomes like education and health.


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
pov = pd.DataFrame({
    "effect_pp": [-2.1, -3.9, 3.8, -14.9, -8.3, -4.1, -0.5],
    "baseline_pp": [93, 88, 68, 82, 44, 94, 92],
    "stars": [2, 0, 0, 3, 1, 2, 0]
}, index=['Ghana LEAP', 'Kenya HSNP', 'Lesotho CGP', 'Malawi SCTP',
          'Uganda SAGE', 'Zambia CGP', 'Zimbabwe HSCT']
)
pov['pct_effect'] = 100 * pov.effect_pp / pov.baseline_pp
pov['significance'] = pov.stars.map({0: '>10%',
                                     1: '5-10%',
                                     2: '1-5%',
                                     3: '<1%'})
# Sort by stars for proper legend ordering.
pov.sort_values('stars', ascending=False, inplace=True)

DARK_BLUE = '#0D47A1'
BLUE = '#2196F3'
BARELY_BLUE = '#BBDEFB'
GRAY = '#E0E0E0'

fig = px.bar(pov, 'pct_effect', color='significance',
             labels={'pct_effect': 'Poverty change',
                     'index': 'Program',
                     'significance': 'Significance'},
             title='Poverty reductions across cash transfer RCTs in SSA',
             color_discrete_map={'>10%': GRAY,
                                 '5-10%': BARELY_BLUE,
                                 '1-5%': BLUE,
                                 '<1%': DARK_BLUE},
)

fig.update_layout(font=dict(family='Roboto'),
                  plot_bgcolor='white',
                  yaxis_title='Cash transfer program',
                  legend_title='Statistical significance',
                  xaxis_title='Percent change in poverty headcount rate',
                  xaxis_ticksuffix='%',
                  # Sort by effect size
                  # (since data is sorted by stars for legend order)
                  yaxis={'categoryorder':'total descending'},
                  title_font_size=20,
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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/index/2020-11-25-index-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

Finally, we consider the political state of child allowances, such as the [American Family Act](https://www.bennet.senate.gov/public/index.cfm/american-family-act), which would ensure all low-income children in the US receive the full benefits of the Child Tax Credit, and how such a policy would align US child benefits with those from other developed countries.

By efficiently reducing child poverty, child allowances provide kids with basic needs, improve access to opportunity, and invest in our future.
