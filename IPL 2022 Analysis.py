#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objects as go


# In[22]:


data= pd.read_csv('IPL 2022.csv')


# In[23]:


data.head()


# The dataset contains all the information needed to summarize the story of IPL 2022 so far. So let’s start by looking at the number of matches won by each team in IPL 2022:
# 
# 

# In[24]:


Figure =px.bar(data, x=['match_winner'],
              title = 'Number of Matches won in IPL 2022')
Figure.show()


# Now let’s see what most teams prefer (batting or fielding) after winning the toss:
# 
# 

# In[27]:


toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# Now let’s see the top scorers of most IPL 2022 matches:

# In[28]:


figure =px.bar(data, x=data['top_scorer'],
              title="Top Scorer in IPL 2022")
figure.show()


# In[34]:


figure = px.bar(data, x=data["top_scorer"], 
                y = data["highscore"], 
                color = data["highscore"],
            title="Top Scorers in IPL 2022")
figure.show()


#  Now let’s have a look at the most player of the match awards till now in IPL 2022:

# In[35]:


figure = px.bar(data, x=data["player_of_the_match"],
               title="Most Player of the Match Awards")
figure.show()


# Now let’s have a look at the bowlers with the best bowling figures in most of the matches:

# In[37]:


figure= px.bar(data, x=data['best_bowling'],
              title='Best Bowlers in IPL 2022')
figure.show()


# Now let’s have a look at whether most of the wickets fall while setting the target or while chasing the target:
# 
# 

# In[42]:


figure =go.Figure()
figure.add_trace(go.Bar(
                x=data['venue'],
                y=data['first_ings_wkts'],
                name="Fist Inning Wickets",
                marker_color='gold'
))
fig.add_trace(go.Bar(
    x=data['venue'],
    y=data['second_ings_wkts'],
    name ="Second Inning Wickets",
    marker_color='blue'
))


# In[43]:


figure.update_layout(barmode='group',xaxis_tickangle =-45)
figure.show()


# In[ ]:




