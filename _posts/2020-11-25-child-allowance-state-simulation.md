---
layout: post
current: post
navigation: True
title: The effect of child allowances across US states
date: 2020-11-25
tags: [us, child allowance]
cover: assets/images/2020-11-25-child-allowance-state-simulation/cover.webp
class: post-template
subclass: 'post'
author: [nate, matt, max]
excerpt: How different forms of cash grants to parents would affect poverty and inequality.
useplotly: true
---


Poverty has a lasting impact on children.  Growing up in poverty increases [stress](https://heckmanequation.org/resource/invest-in-early-childhood-development-reduce-deficits-strengthen-the-economy/) and [incarceration rates](https://heckmanequation.org/resource/invest-in-early-childhood-development-reduce-deficits-strengthen-the-economy/) and decreases [educational](https://www.sciencedirect.com/science/article/abs/pii/S1876285915003836) and [health](https://www.aeaweb.org/articles?id=10.1257/app.2.1.86) outcomes.  These negative consequences not only impact the nation’s poor, but the entire economy as well--child poverty shrinks GDP by more than [$1 trillion annually](https://www.nap.edu/read/25246/chapter/1).

Research has shown that giving money to families with children, as most developed countries do, can reduce each of these issues.  Programs that provide cash to families with children are called a _child allowance_, and are typically paid out on a monthly basis.  

Here you can explore the impact of a potential child allowance of various amounts in each state.
We show impacts across three funding mechanisms:

* **Federal tax** as a flat rate on taxable income. For each child allowance amount the total cost is calculated by multiplying the annual child allowance by the total number of children.  To calculate the revenue neutral tax rate, the total cost is divided by the nation’s total taxable income.  For example, a child allowance of $100 per month would cost about $88 billion annually and require a new flat tax of 1.1 percent.
* **State tax** as a flat rate on taxable income. The state tax is calculated in the same manner as the federal tax, but at the state level. This shows how states can fund their own child allowances. Because states vary in child population and income, different states have different tax rates. A $100 monthly child allowance in DC is offset by a 0.5 percent tax on taxable income while the same amount requires a 1.3 percent tax in Alabama.
* **No funding** does not impose any new taxes.

These static analyses (they do not consider labor supply effects) are based on data from the Current Population Survey March Supplement representing income from 2017 to 2019, and preserve existing benefits such as the Child Tax Credit.


<button class="code-button" id="button1" onclick="f1()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_1" style="display: none;">
  <pre>
    <code>
# Imports.
import pandas as pd
import numpy as np
import math
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import copy

# Load data.
summary = pd.read_csv('https://github.com/ngpsu22/Child_Allowance_States/raw/main/poverty_gini_tax_child_allowance')

deciles = pd.read_csv('data/deciles.csv')

deciles.funding = deciles.funding.map({'deficit': 'No funding',
                                       'fed': 'Federal tax',
                                       'state': 'State tax'})

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
tax = summary[(summary.race == 'All') & (summary.age_group == 'all')]

state_names = tax.state.unique()
state_names = np.insert(state_names[:-1], 0, 'US')
default_state = 'US'
state_dict = summary[['code', 'state']].set_index('code').to_dict()['state']

# Colors from https://material.io/design/color/the-color-system.html
DARK_BLUE = '#1565C0'
LIGHT_BLUE = '#42A5F5'
GRAY = '#BDBDBD'
GRAY_SHADOW = '#EEEEEE'
COLOR_MAP = {
    'Federal tax rate': DARK_BLUE,
    'State tax rate': LIGHT_BLUE,
    'Federal tax': DARK_BLUE,
    'State tax': LIGHT_BLUE,
    'No funding': GRAY,
    'No funding, out of poverty': GRAY_SHADOW
}

# data labels
REFORM = {'state_tax_rate': 'State tax rate', 
          'fed_tax_rate': 'Federal tax rate'}

# reformat data
data_list = []
for state in state_names:
    state_data = tax[tax.state == state]
    state_list = []
    for reform in REFORM:
        state_list.append(state_data[reform])
    data_list.append(state_list)

# generate first graph
data_columns = list(REFORM.keys())
data = pd.DataFrame(data_list, columns = data_columns)
data['State'] = state_names
data = data.set_index('State')

def getDataList(state):
    data_list = []
    for dc in data_columns:
        data_list.append(data.loc[state][dc])
    return data_list

# initialize figure
fig = go.Figure()

# add traces
x = tax.child_allowance.unique()
for reform in REFORM:
    fig.add_trace(go.Scatter(
        x=x, 
        y=data[reform][default_state],
        name=REFORM[reform],
        marker = dict(color = COLOR_MAP[REFORM[reform]]),
        hoverlabel = dict(namelength = -1)
#         hovertemplate=
#                 REFORM[reform] + ': %{y}' + 
#                 '<extra></extra>',
    ))

# generate buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'y': getDataList(state), 
                            'visible': ['legendonly' if state == 'US' 
                                        else True, True]}
                          ]}
    buttons.append(new_button)
    
# construct menus
updatemenus = [{'buttons': buttons,
                'direction': 'down',
                'showactive': True,
                'pad':{'l': 10, 'r': 25},
               }]

# update layout with buttons, and show the figure
fig.update_layout(updatemenus=updatemenus)

fig.update_xaxes(title_text='Monthly child allowance')

tax_values = tax.state_tax_rate.tolist() + tax.fed_tax_rate.tolist() 
ymin = math.floor(min(tax_values) * 100) / 100 - 0.1
ymax = math.ceil(max(tax_values) * 100) / 100
fig.update_yaxes(title_text='Tax rate on taxable income', range=[ymin, ymax])

fig.update_layout(height=600, 
                  margin=dict(l=0, r=0, t=80, b=0),
                  yaxis_ticksuffix='%',
                  font=dict(family='Roboto'),
                  hovermode='x', 
                  xaxis_tickprefix='$',
                  xaxis_ticksuffix='',
                  plot_bgcolor='white',
                  legend_title_text='',
                  title={
                    'text': 'Income tax required to fund child allowances',
                    'y':0.95,
                    'x':0.01,
                    'xanchor': 'left',
                    'yanchor': 'top'},
                  title_font_size=20,
                 )

fig.update_layout(hovermode="x unified")

# hide state tax rate for US only
hide_line = ['State tax rate']
fig.for_each_trace(lambda trace: trace.update(visible="legendonly")
                   if trace.name in hide_line else ())

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
      $("#asset1").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-1.html");
    });
  </script>
</div>
<div id = "asset1"></div>

## Distributional effects

While the new tax would hit most Americans, save the very poorest who earn less than the standard deduction, the overall distributional consequences would be positive.
For instance, the bottom decile would see their average annual resources rise by about $3,700 per person with a federal $300 per month child allowance, while the top 10 percent would see their average resources per person fall by about double, $6,400.


<button class="code-button" id="button2" onclick="f2()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_2" style="display: none;">
  <pre>
    <code>
# make chart symmetric with boundary at the maximum.
boundary = deciles.net_chg.agg([min, max]).abs().max()

# initial data set-up 
x = deciles.decile.unique()
ca_amts = deciles.monthly_ca.unique()
state_names = deciles.state.unique()
state_names = np.insert(state_names[:-1], 0, 'US')
fundings = ['Federal tax', 'State tax', 'No funding']

# get list of bar colors
colors = [COLOR_MAP[i] for i in fundings]

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
    'showlegend': True,
    'height': 600,
    'margin': dict(t=100, b=0, l=0, r=0)
}
fig_dict['layout']['title'] = {
    'text': 'Average net change to household income by decile', 
    'y': 0.97,
    'x': 0.05,
    'xanchor': 'left',
    'yanchor': 'top'
}
fig_dict['layout']['xaxis'] = {
    'title': 'Decile of resources per person', 
    'dtick': 1,
    'type': 'category'
}
fig_dict['layout']['yaxis'] = {
    'title': 'Average annual net change per SPM unit', 
    'tickprefix': '$',
    'range': [-boundary, boundary]
}

# add slider specifications
slider_menu =  {
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
    'showactive': False,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top'
}

sliders_dict = {
    'active': 20,
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

# create frames for a given state and funding method
def make_frames(state, funding):
    raw_data = deciles[(deciles.state == state) &
                       (deciles.funding == funding)].round()
    frames = {}
    for ca in ca_amts:
        frames[str(ca)] = list(raw_data[raw_data.monthly_ca == ca].net_chg)
    return frames

# create dataframe of booleans to determine trace visibility
# separating funding mechanisms is currently redundant but can 
#    in theory be used to add another dropdown menu
n = len(state_names) * len(fundings)
frames_list = []
count = 0
visible = []
for state in state_names:
    vis_list = []
    for funding in fundings:
        frames_list.append(make_frames(state, funding))
        v = np.array([False] * n)
        v[count] = True
        vis_list.append(v)
        count += 1
    visible.append(vis_list)
visible = pd.DataFrame(visible, columns = fundings, index = state_names)

# add traces to figure dictionary
for i in range(n):
    data_dict = {
        'x': x,
        'y': frames_list[i]['500'],
        'type': 'bar',
        # Only show the Federal tax line (index 0) when first loading chart.
        'visible': True if i == 0 else ('legendonly' if i < 3 else False),
        'name': fundings[i % 3],
        'marker_color':  colors[i % 3],
        'hovertemplate': 
                '<b>' + fundings[i % 3] + '</b>' + 
                '<br>Change in resources: %{y}<br>' + 
                '<extra></extra>'
    }
    fig_dict['data'].append(data_dict)

# reorder existing frames
frames = []
for ca in ca_amts:
    data_list = []
    for f in frames_list:
        data_list.append({'y': f[str(ca)], 'type': 'bar'})
    frame = {'data': data_list, 'name': str(ca), 'traces': list(range(n))}
    frames.append(frame)

# add additional features to figure dictionary
fig_dict['frames'] = frames
fig_dict['layout']['sliders'] = [sliders_dict]

# generate plotly figure
fig = go.Figure(fig_dict)

# generate dropdown menu buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'visible': (visible[fundings[0]][state] | 
                                        visible[fundings[1]][state] |
                                        visible[fundings[2]][state])}
                          ]}
    buttons.append(new_button)
    
# construct button menu
updatemenus = {'buttons': buttons,
               'direction': 'down',
               'showactive': True,
               'pad':{"r": 10, 't': 20},
               'xanchor': 'left',
               'yanchor': 'top',
               'x': 0,
               'y': 1.2
               }

# add slider and button menus
fig.update_layout(updatemenus=[slider_menu, updatemenus],
                  title_font_size=20,)

# display figure
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
      $("#asset2").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-2.html");
    });
  </script>
</div>
<div id = "asset2"></div>

This $300-per-month child allowance would raise the bottom decile's income by 33 percent, while lowering the top decile's income by 4 percent.


<button class="code-button" id="button3" onclick="f3()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_3" style="display: none;">
  <pre>
    <code>
# make chart symmetric with boundary at the maximum.
boundary = deciles.pct_chg.agg([min, max]).abs().max()

# initial data set-up 
x = deciles.decile.unique()
ca_amts = deciles.monthly_ca.unique()
state_names = deciles.state.unique()
state_names = np.insert(state_names[:-1], 0, 'US')
fundings = ['Federal tax', 'State tax', 'No funding']

# get list of bar colors
colors = [COLOR_MAP[i] for i in fundings]

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
    'showlegend': True,
    'height': 600,
    'margin': dict(t=100, b=0, l=0, r=0)
}
fig_dict['layout']['title'] = {
    'text': 'Average percent change to household income by decile', 
    'y': 0.97,
    'x': 0.05,
    'xanchor': 'left',
    'yanchor': 'top'
}
fig_dict['layout']['xaxis'] = {
    'title': 'Decile of resources per person', 
    'dtick': 1,
    'type': 'category'
}
fig_dict['layout']['yaxis'] = {
    'title': 'Average percent change to SPM unit resources', 
    'ticksuffix': '%',
    'range': [-boundary, boundary]
}

# add slider specifications
slider_menu =  {
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
    'showactive': False,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top'
}

sliders_dict = {
    'active': 20,
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

# create frames for a given state and funding method
def make_frames(state, funding):
    raw_data = deciles[(deciles.state == state) &
                       (deciles.funding == funding)].round()
    frames = {}
    for ca in ca_amts:
        frames[str(ca)] = list(raw_data[raw_data.monthly_ca == ca].pct_chg)
    return frames

# create dataframe of booleans to determine trace visibility
# separating funding mechanisms is currently redundant but can 
#    in theory be used to add another dropdown menu
n = len(state_names) * len(fundings)
frames_list = []
count = 0
visible = []
for state in state_names:
    vis_list = []
    for funding in fundings:
        frames_list.append(make_frames(state, funding))
        v = np.array([False] * n)
        v[count] = True
        vis_list.append(v)
        count += 1
    visible.append(vis_list)
visible = pd.DataFrame(visible, columns = fundings, index = state_names)

# add traces to figure dictionary
for i in range(n):
    data_dict = {
        'x': x,
        'y': frames_list[i]['500'],
        'type': 'bar',
        # Only show the Federal tax line (index 0) when first loading chart.
        'visible': True if i == 0 else ('legendonly' if i < 3 else False),
        'name': fundings[i % 3],
        'marker_color':  colors[i % 3],
        'hovertemplate': 
                '<b>' + fundings[i % 3] + '</b>' + 
                '<br>Change in resources: %{y}<br>' + 
                '<extra></extra>'
    }
    fig_dict['data'].append(data_dict)

# reorder existing frames
frames = []
for ca in ca_amts:
    data_list = []
    for f in frames_list:
        data_list.append({'y': f[str(ca)], 'type': 'bar'})
    frame = {'data': data_list, 'name': str(ca), 'traces': list(range(n))}
    frames.append(frame)

# add additional features to figure dictionary
fig_dict['frames'] = frames
fig_dict['layout']['sliders'] = [sliders_dict]

# generate plotly figure
fig = go.Figure(fig_dict)

# generate dropdown menu buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'visible': (visible[fundings[0]][state] | 
                                        visible[fundings[1]][state] |
                                        visible[fundings[2]][state])}
                          ]}
    buttons.append(new_button)
    
# construct button menu
updatemenus = {'buttons': buttons,
               'direction': 'down',
               'showactive': True,
               'pad':{"r": 10, 't': 20},
               'xanchor': 'left',
               'yanchor': 'top',
               'x': 0,
               'y': 1.2
               }

# add slider and button menus
fig.update_layout(updatemenus=[slider_menu, updatemenus],
                  title_font_size=20,)

# display figure
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
      $("#asset3").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-3.html");
    });
  </script>
</div>
<div id = "asset3"></div>

## Inequality

The progressive benefits by decile demonstrate that child allowances would reduce inequality.
Measures of inequality can formalize this result.
For example, the Gini index lies between 0 and 1, with 0 indicating that everyone has the exact same income, and 1 indicating that one person possesses all the income.

Across funding strategies, child allowances reduce inequality as measured by the Gini index, with larger child allowances producing larger inequality reductions.
Nationally, a $500 monthly child allowance shrinks the Gini index nine percent, from 0.446 to 0.406.
While states vary in their levels of current inequality, a $200 monthly child allowance cuts the measure of inequality consistently between 4 and 5 percent across them.


<button class="code-button" id="button4" onclick="f4()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_4" style="display: none;">
  <pre>
    <code>
# data labels
GINI = {'fed_gini': 'Federal tax',
        'state_gini': 'State tax',
        'non_funded_gini': 'No funding'}

# reformat data
data_list = []
for state in state_names:
    state_data = tax[tax.state == state]
    state_list = []
    for gini in GINI:
        state_list.append(state_data[gini])
    data_list.append(state_list)

data_columns = list(GINI.keys())
data = pd.DataFrame(data_list, columns = data_columns)
data['State'] = state_names
data = data.set_index('State')

def getDataList(state):
    data_list = []
    for dc in data_columns:
        data_list.append(data.loc[state][dc])
    return data_list

# initialize figure
fig = go.Figure()

# add traces
x = tax.child_allowance.unique()
for gini in GINI:
    fig.add_trace(go.Scatter(
        x=x, 
        y=tax[tax.state == default_state][gini],
        name=GINI[gini],
        marker = dict(color = COLOR_MAP[GINI[gini]]),
#         hovertemplate=
#                 GINI[gini] + ': %{y}' + 
#                 '<extra></extra>'
    ))

# generate buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'y': getDataList(state),
                           'visible': [True,
                                       'legendonly' if state == 'US' else True,
                                       True]},
                          ]}
    buttons.append(new_button)
    
# construct menus
updatemenus = [{'buttons': buttons,
                'direction': 'down',
                'showactive': True,
                'pad':{'l': 10, 'r': 25},
               }]

# update layout with buttons, and show the figure
fig.update_layout(updatemenus=updatemenus)

fig.update_xaxes(title_text='Monthly child allowance')

gini_values = tax.non_funded_gini.tolist() + tax.fed_gini.tolist() + tax.state_gini.tolist()
ymin = math.floor(min(gini_values) * 100) / 100
ymax = math.ceil(max(gini_values) * 100) / 100
fig.update_yaxes(title_text='Gini index of per-capita income, 2017-2019',
                 range=[ymin, ymax])

fig.update_layout(height=600, 
                  margin=dict(l=0, r=0, t=80, b=0),
                  font=dict(family='Roboto'),
                  hovermode='x', 
                  xaxis_tickprefix='$',
                  xaxis_ticksuffix='',
                  plot_bgcolor='white',
                  legend_title_text='',
                  title={
                    'text': 'Income inequality by child allowance amount',
                    'y':0.95,
                    'x':0.01,
                    'xanchor': 'left',
                    'yanchor': 'top'},
                  title_font_size=20,
                 )

fig.update_layout(hovermode="x unified")

# hide state tax rate for US only
hide_line = ['State tax']
fig.for_each_trace(lambda trace: trace.update(visible="legendonly")
                   if trace.name in hide_line else ())

fig.show(config=CONFIG)
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
      $("#asset4").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-4.html");
    });
  </script>
</div>
<div id = "asset4"></div>

## Poverty
A child allowance can also substantially cut poverty.  In this example, a person is said to be in poverty if their household's total post tax and transfer income is less than their poverty threshold.
Poverty thresholds are determined by the Census Bureau’s Supplemental Poverty Measure (SPM), which considers a medley of factors including household size, housing status, and local housing costs.


<button class="code-button" id="button5" onclick="f5()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_5" style="display: none;">
  <pre>
    <code>
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
      $("#asset5").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-5.html");
    });
  </script>
</div>
<div id = "asset5"></div>

A child allowance of $300 per month, funded by a federal income tax, would cut US child poverty by 52 percent, and also cut adult poverty by 13 percent.
Overall poverty would fall 22 percent.


<button class="code-button" id="button6" onclick="f6()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_6" style="display: none;">
  <pre>
    <code>
FUNDING = {'fed_poverty_rate': 'Federal tax',
           'state_poverty_rate': 'State tax',
           'non_funded_poverty_rate': 'No funding'}

# initial data set-up
age = summary[summary['race'] == 'All'].copy(deep=True)
age.age_group = age.age_group.str.capitalize()
x = ['Child', 'Adult', 'All']
ca_amts = age.child_allowance.unique()
state_names = age.state.unique()
state_names = np.insert(state_names[:-1], 0, 'US')

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
    'showlegend': True,
    'height': 600,
    'margin': dict(t=100, b=0, l=0, r=0)
}
fig_dict['layout']['title'] = {
    'text': 'Poverty by age and child allowance amount',
    'y': 0.97,
    'x': 0.05,
    'xanchor': 'left',
    'yanchor': 'top'
}
fig_dict['layout']['xaxis'] = {
    'type': 'category'
}
fig_dict['layout']['yaxis'] = {
    'title': 'SPM poverty rate, 2017-2019',
    'ticksuffix': '%',
    'range': [0, 25]
}

# add slider specifications
slider_menu =  {
    'buttons': [
        {
            'args': [None, {'frame': {'duration': 500, 'redraw': True},
                            'fromcurrent': True, 
                            "mode": "immediate",
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
    'showactive': False,
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

# create frames for a given state and funding method
def make_frames(state, funding):
    raw_data = age[(age.state == state)]
    frames = {}
    for ca in ca_amts:
        frames[str(ca)] = list(raw_data[raw_data.child_allowance == ca].set_index(
            'age_group').loc[x][funding])
    return frames

# create dataframe of booleans to determine trace visibility
n = len(state_names) * len(FUNDING)
frames_list = []
count = 0
visible = {}
for state in state_names:
    v = [False] * n
    for funding in FUNDING:
        frames_list.append(make_frames(state, funding))
        v[count] = True
        count += 1
    visible[state] = v + v
v = [False] * n
v[0] = True
v[1] = 'legendonly'
v[2] = 'legendonly'
visible['US'] = v + v

# reorder existing frames
frames = []
for ca in ca_amts:
    data_list = []
    count = 0
    for f in frames_list:
        data_list.append({
            'y': f['0'], 
            'x': x,
            'type': 'bar', 
            'offsetgroup': count, 
            'showlegend': False,
            'legendgroup': count,
            'marker_color': GRAY_SHADOW,
            'name': 'No child allowance',
            'hovertemplate': 
                'Current poverty rate: %{y}' + 
                '<extra></extra>'
        })
        count += 1
    count = 0
    for f in frames_list:
        data_list.append({
            'y': f[str(ca)], 
            'x': x,
            'type': 'bar', 
            'offsetgroup': count,
            'legendgroup': count,
            'name': list(FUNDING.values())[count % 3],
            'marker_color': COLOR_MAP[list(FUNDING.values())[count % 3]],
            'hovertemplate': 
                '<b>' + list(FUNDING.values())[count % 3] + '</b>' + 
                '<br>Poverty rate: %{y}<br>' + 
                'Poverty reduction: %{customdata}%'
                '<extra></extra>',
            'customdata': list(map(lambda x, y: (round(100 * (1 - y / x))),
                                   f['0'], f[str(ca)]))
        })
        count += 1
    frame = {'data': data_list, 'name': str(ca), 'traces': list(range(n*2))}
    frames.append(frame)

# add additional features to figure dictionary
fig_dict['frames'] = frames
fig_dict['layout']['sliders'] = [sliders_dict]

for i in range(n):
    data_dict = copy.deepcopy(frames[0]['data'][i])
    if i == 0:
        data_dict['visible'] = True
    elif i < 3:
        data_dict['visible'] = 'legendonly'
    else:
        data_dict['visible'] = False
    fig_dict['data'].append(data_dict)
for i in range(n):
    data_dict = copy.deepcopy(frames[0]['data'][n + i])
    if i == 0:
        data_dict['visible'] = True
    elif i < 3:
        data_dict['visible'] = 'legendonly'
    else:
        data_dict['visible'] = False
    fig_dict['data'].append(data_dict)

# generate plotly figure
fig = go.Figure(fig_dict)

# generate dropdown menu buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'visible': (visible[state])},
                          ]}
    buttons.append(new_button)
    
# construct button menu
updatemenus = {'buttons': buttons,
               'direction': 'down',
               'showactive': True,
               'pad':{"r": 10, 't': 20},
               'xanchor': 'left',
               'yanchor': 'top',
               'x': 0,
               'y': 1.2
              }

# add slider and button menus
fig.update_layout(
    updatemenus=[slider_menu, updatemenus],
    hoverlabel=dict(
        font=dict(family='Roboto')
    ),
    title_font_size=20,)

# display figure
fig.show(config=CONFIG)
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
      $("#asset6").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-6.html");
    });
  </script>
</div>
<div id = "asset6"></div>

That same $300-per-month federally-funded child allowance would cut child poverty fairly consistently across races: 51 percent among White children and 54 percent among Black children.
But because Black children are currently about twice as likely to be in poverty, it also cuts the percentage-point racial gaps in half.


<button class="code-button" id="button7" onclick="f7()">&#9654; Click to show code</button>
<div class="code-cell" id="asset_code_7" style="display: none;">
  <pre>
    <code>
FUNDING = {'fed_poverty_rate': 'Federal tax',
           'state_poverty_rate': 'State tax',
           'non_funded_poverty_rate': 'No funding'}

# initial data set-up 
race = summary[summary['age_group'] == 'child']
x = ['Black', 'White', 'Other', 'All']
ca_amts = race.child_allowance.unique()
state_names = race.state.unique()
state_names = np.insert(state_names[:-1], 0, 'US')

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
    'showlegend': True,
    'height': 600,
    'margin': dict(t=100, b=0, l=0, r=0)
}
fig_dict['layout']['title'] = {
    'text': 'Child poverty by race and child allowance amount',
    'y': 0.97,
    'x': 0.05,
    'xanchor': 'left',
    'yanchor': 'top'
}
fig_dict['layout']['xaxis'] = {
    'type': 'category'
}
fig_dict['layout']['yaxis'] = {
    'title': 'Child SPM poverty rate, 2017-2019',
    'ticksuffix': '%',
    'range': [0, 25]
}

# add slider specifications
slider_menu =  {
    'buttons': [
        {
            'args': [None, {'frame': {'duration': 500, 'redraw': True},
                            'fromcurrent': True, 
                            "mode": "immediate",
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
    'showactive': False,
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

# create frames for a given state and funding method
def make_frames(state, funding):
    raw_data = race[(race.state == state)]
    frames = {}
    for ca in ca_amts:
        frames[str(ca)] = list(raw_data[raw_data.child_allowance == ca].set_index('race').loc[x][funding])
    return frames

# create dataframe of booleans to determine trace visibility
n = len(state_names) * len(FUNDING)
frames_list = []
count = 0
visible = {}
for state in state_names:
    v = [False] * n
    for funding in FUNDING:
        frames_list.append(make_frames(state, funding))
        v[count] = True
        count += 1
    visible[state] = v + v
v = [False] * n
v[0] = True
v[1] = 'legendonly'
v[2] = 'legendonly'
visible['US'] = v + v

# reorder existing frames
frames = []
for ca in ca_amts:
    data_list = []
    count = 0
    for f in frames_list:
        data_list.append({
            'y': f['0'], 
            'x': x,
            'type': 'bar', 
            'offsetgroup': count, 
            'showlegend': False,
            'legendgroup': count,
            'marker_color': GRAY_SHADOW,
            'name': 'No child allowance',
            'hovertemplate': 
                'Current poverty rate: %{y}' + 
                '<extra></extra>'
        })
        count += 1
    count = 0
    for f in frames_list:
        data_list.append({
            'y': f[str(ca)], 
            'x': x,
            'type': 'bar', 
            'offsetgroup': count,
            'legendgroup': count,
            'name': list(FUNDING.values())[count % 3],
            'marker_color': COLOR_MAP[list(FUNDING.values())[count % 3]],
            'hovertemplate': 
                '<b>' + list(FUNDING.values())[count % 3] + '</b>' + 
                '<br>Child poverty rate: %{y}<br>' + 
                'Poverty reduction: %{customdata}%'
                '<extra></extra>',
            'customdata': list(map(lambda x, y: (round(100 * (1 - y / x))),
                                   f['0'], f[str(ca)]))
        })
        count += 1
    frame = {'data': data_list, 'name': str(ca), 'traces': list(range(n*2))}
    frames.append(frame)

# add additional features to figure dictionary
fig_dict['frames'] = frames
fig_dict['layout']['sliders'] = [sliders_dict]

for i in range(n):
    data_dict = copy.deepcopy(frames[0]['data'][i])
    if i == 0:
        data_dict['visible'] = True
    elif i < 3:
        data_dict['visible'] = 'legendonly'
    else:
        data_dict['visible'] = False
    fig_dict['data'].append(data_dict)
for i in range(n):
    data_dict = copy.deepcopy(frames[0]['data'][n + i])
    if i == 0:
        data_dict['visible'] = True
    elif i < 3:
        data_dict['visible'] = 'legendonly'
    else:
        data_dict['visible'] = False
    fig_dict['data'].append(data_dict)

# generate plotly figure
fig = go.Figure(fig_dict)

# generate dropdown menu buttons
buttons = []
for state in state_names:
    new_button = {'method': 'update',
                  'label': state,
                  'args': [{'visible': (visible[state])}]
                 }
    buttons.append(new_button)
    
# construct button menu
updatemenus = {'buttons': buttons,
               'direction': 'down',
               'showactive': True,
               'pad':{"r": 10, 't': 20},
               'xanchor': 'left',
               'yanchor': 'top',
               'x': 0,
               'y': 1.2
              }

# add slider and button menus
fig.update_layout(
    updatemenus=[slider_menu, updatemenus],
    hoverlabel=dict(
        font=dict(family='Roboto')
    ),
    title_font_size=20,)

# display figure
fig.show(config=CONFIG)
    </code>
  </pre>
</div>

<script>
function f7() {
  var x = document.getElementById("asset_code_7");
  var b = document.getElementById("button7");
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
      $("#asset7").load("{{site.baseurl}}assets/markdown_assets/simulation/2020-11-25-simulation-asset-7.html");
    });
  </script>
</div>
<div id = "asset7"></div>

Beyond reducing child poverty, child allowances would decrease adult poverty and abate inequality.
These effects are consistent across states, races, and the funding mechanisms.

Read on to our [Empirical studies](https://child-allowance.ubicenter.org/empirical) page for more research on the (often causal) links between child poverty and outcomes like health, education, and income.
For more information on how a child allowance would compare to existing policies like the Child Tax Credit, visit our [Policies](https://child-allowance.ubicenter.org/policies) page.
