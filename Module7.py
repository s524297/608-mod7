#!/usr/bin/env python
# coding: utf-8

# In[1]:


c = lambda f: 5 / 9 * (f - 32)


# In[2]:


temps = [(f, c(f)) for f in range (0, 101, 10)]


# In[3]:


import pandas as pd 


# In[4]:


temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])


# In[7]:


axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_lable = axes.set_ylabel('Celsius')


# In[10]:


nyc = pd.read_csv('C:/Users/ES068454/44608-80/examples/IntroToPython-master/examples/ch10/ave_hi_nyc_jan_1895-2018.csv')


# In[11]:


nyc.head()


# In[12]:


nyc.tail()


# In[13]:


nyc.columns = ['Date', 'Temperature', 'Anomaly']


# In[14]:


nyc.head(3)


# In[15]:


nyc.Date.dtype


# In[16]:


nyc.Date = nyc.Date.floordiv(100)


# In[17]:


nyc.head()


# In[18]:


pd.set_option('precision', 2)


# In[19]:


nyc.Temperature.describe()


# In[20]:


from scipy import stats 


# In[21]:


linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)


# In[22]:


linear_regression.slope


# In[23]:


linear_regression.intercept


# In[24]:


linear_regression.slope * 2019 + linear_regression.intercept 


# In[25]:


linear_regression.slope * 1890 + linear_regression.intercept 


# In[26]:


import seaborn as sns


# In[27]:


sns.set_style('whitegrid')


# In[28]:


axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)


# In[29]:


axes.set_ylim(10,70)


# In[ ]:




