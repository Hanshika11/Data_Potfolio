#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install plotly')


# In[2]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go



# In[3]:


pio.templates.default = "plotly_white"


# In[4]:


data = pd.read_csv("t20-world-cup-22.csv")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


figure = px.bar(data,
               x=data['winner'],
               title='Number of Matches won by teams in T20 world Cup 2022')
figure.show()


# As England won the t20 world cup 2022, England won five matches. And Both Pakistan and India won 4 matches.
# 
# 

# # Now let’s have a look at the number of matches won by batting first or second in the t20 world cup 2022:
# 
# 

# In[8]:


won_by = data["won by"].value_counts()
label = won_by.index
counts= won_by.values
color =['gold','lightgreen']


fig = go.Figure(data=[go.Pie(labels= label , values = counts)])
fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# So in the t20 world cup 2022, 16 matches were won by batting first, and 13 matches were won by chasing. Now, let’s have a look at the toss decisions by teams in the world cup:
# 
# 

# In[ ]:


toss = data["toss decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decisions in t20 World Cup 2022')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# So in 17 matches, the teams decided to bat first, and in 13 matches, the teams chose to field first. Now let’s have a look at the top scorers in the t20 world cup 2022:
# 
# 

# In[ ]:


figure = px.bar(data,
               x=data['top scorer'],
               y=data ['highest score'],
               color=data['highest score'],
               title= 'Top Scorer in T20 World Cup 2022')
figure.show()


# So, Virat Kohli scored the highest in 3 matches. Undoubtedly, he was the best batsman in the t20 world cup 2022. Now let’s have a look at the number of player of the match awards in the world cup:
# 
# 

# In[ ]:


figure = px.bar(data,
               x=data["player of the match"],
               title="players of the match Awards in T20 world Cup 2022")
figure.show()


# Now let’s have a look at the bowlers with the best bowling figures at the end of the matches:
# 
# 

# In[ ]:


figure =px.bar(data,
              x=data["best bowler"],
              title="Best bowlers in T20 world cup 20220")
figure.show()


# Now let’s compare the runs scored in the first innings and second innings in every stadium of the t20 world cup 20

# In[ ]:


fig = go.Figure()
fig.add_trace(go.Bar(
    x = data["venue"],
    y= data["first innings score"],
    name ='First Inining Runs',
    marker_color='blue'
))

fig.add_trace(go.Bar(
             x= data['venue'],
            y= data['second innings score'],
            name = 'Second Inning Score',
             marker_color= 'red'
))

fig.update_layout(barmode = 'group',
                 xaxis_tickangle =45,
                 title= "Best Stadium to Bat First to Chase")
fig.show()


# So SCG was the only stadium in the world cup that was best for batting first. Other stadiums didn’t make much difference while batting first or chasing.

# Now let’s compare the number of wickets lost in the first innings and second innings in every stadium of the t20 world cup 2022:
# 
# 
# 

# In[15]:


fig = go.Figure()
fig.add_trace(go.Bar(
             x=data['venue'],
             y=data['first innings wickets'],
             name='First Inning Wickets',
             marker_color= 'blue'
))

fig.add_trace(go.Bar(
              x=data['venue'],
              y=data['second innings wickets'],
              name ='Second Inning Wickets',
              marker_color='red'
                   
))

fig.update_layout(barmode ='group',
                 xaxis_tickangle =-45,
                 title='Best Statiums to Bowl First or Defend')
fig.show()
        
              


# SCG was the best stadium to bowl while defending the target. While the Optus Stadium was the best stadium to bowl first.
# 
# 

# In[ ]:




