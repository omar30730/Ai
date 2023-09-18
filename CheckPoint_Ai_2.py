#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("Video games.csv")


# In[4]:


df.isnull().sum()


# In[5]:


df["Year"]


# In[6]:


df["Publisher"]


# In[7]:


df.dropna(inplace = True)


# In[8]:


df.isnull().sum()


# In[9]:


gb = df.groupby(df["Global_Sales"]).sum()
area_fig = px.area(gb,x = df["Year"],y = df["Global_Sales"])
gb.reset_index()


# In[10]:


area_fig.show()


# In[11]:


histo_fig = px.histogram(df,df["Global_Sales"],nbins = 10)


# In[12]:


histo_fig


# In[13]:


df.info()


# In[14]:


scatter_fig1 = px.scatter(df,x = "NA_Sales" ,y = "EU_Sales")


# In[15]:


scatter_fig1.show()


# In[16]:


scatter_fig2 = px.scatter(df,x = "JP_Sales" ,y = "Other_Sales")


# In[17]:


scatter_fig2.show()


# In[18]:


df.info()


# In[19]:


plt.stackplot(df["Year"],df["NA_Sales"],df["EU_Sales"],df["JP_Sales"],df["Other_Sales"],df["Global_Sales"])
plt.show()


# In[20]:


top10_recovered = pd.DataFrame(df.groupby('Publisher')['Global_Sales'].sum().nlargest(10).sort_values(ascending = False))


# In[21]:


top10_recovered.plot(kind = "bar")


# In[22]:


df.info()


# In[71]:


o = plt.pie(df["Global_Sales"],labels = df["Genre"])
print("oo")

