
# coding: utf-8

# # Inian population data set exploring

# #### Importing pandas and matplotlib

# In[2]:

import pandas as pd, matplotlib as mpl


# #### Create a data frame from the xl sheet

# In[3]:

main_df = pd.read_excel("http://www.censusindia.gov.in/2011census/C-series/c-13/DDW-0000C-13.xls", header=None)
df = main_df


# #### Data check by showing head

# In[4]:

df.head()


# In[5]:

df.head(20)


# #### see what the axes are

# In[6]:

df.axes


# #### Now remove unnecessary rows from the top

# In[7]:

df = df.ix[7:]


# In[8]:

df.head()


# ### Drop columns 1,2,3 inplace without reassigning it to df

# In[9]:

columns_to_remove = df.columns[[0,1,2]]


# In[10]:

df.drop( columns_to_remove , axis = 1 , inplace = True )


# In[11]:

df.head()


# In[12]:

indiadf = df.ix[:108]


# In[13]:

indiadf.tail()


# ### Rename dataframe columns

# palce , age , total , mlaes , femlaes , rural_total , rural_males , rural_females , urb_total , urb_males , urb_females

# In[14]:

indiadf.columns = [ "palce" , "age" , "total" , "males" , "females" , "rural_total" , "rural_males" , "rural_females" , "urb_total" , "urb_males" , "urb_females" ]


# In[15]:

indiadf.axes


# ### set matplotlib to work inline and import pyplot

# In[16]:

# In[17]:

from matplotlib import pyplot as p, patches as pt


# # Start plotting the data

# In[18]:

df = indiadf


# In[19]:

df.reset_index(inplace=True, drop=True)


# In[20]:

# fix small data problem,s before proceeding

# all ages is removed
# 100+ is considered as  101

df = df.ix[1:] # remove first row
buffer = df.set_value(100, 1 , 101 , takeable = True) # buffer so that it doesnt print output into notebook


# In[21]:

df.head(2)


# In[22]:

df.tail(2)


# ## Population by age

# In[23]:

p.plot( df['age'] , df['total'] , df['age'] ,  df['rural_total'] , df['age'] ,  df['urb_total'] )

# set decorations
p.ylabel('population in 10 millions')
p.xlabel('age')

p.grid(True)
p.title('population by age')
p.legend(['total','rural','urban'])

p.show()


# ## Gender population differnce by age

# In[24]:

males = df['males']
females = df['females']

r_males = df['rural_males']
r_females = df['rural_females']

u_males = df['urb_males']
u_females = df['urb_females']


# In[25]:

diff = females - males
r_diff = r_females - r_males
u_diff = u_females - u_males


# In[26]:

p.plot( df['age'] , diff , df['age'] , r_diff , df['age'] , u_diff )

# set decorations
p.ylabel('population difference (F-M)')
p.xlabel('age')

p.grid(True)
p.title('gender population difference by age ')
p.legend(['total','rural','urban'])

p.show()


# ## Sex ratio by age

# #### ratio is in females to males (F:M)

# In[27]:

ratio = females / males
r_ratio = r_females / r_males
u_ratio = u_females / u_males

# normalize the data to be around 0
ratio -= 1
r_ratio -= 1
u_ratio -= 1


# In[28]:

p.plot( df['age'] , ratio , df['age'] , r_ratio , df['age'] , u_ratio )

# set decorations
p.ylabel('population ratio (F:M)')
p.xlabel('age')

p.grid(True)
p.title('Sex ratio by age')
p.legend(['total','rural','urban'])

p.show()


# ## Urban to Rural population ratios

# #### urban to rural total , male and female ratios

# In[30]:

r_total = df['rural_total']
u_total = df['urb_total']

# urban to rural ratio
ur_ratio = r_total / u_total

# urban to rural males ratio
ur_males_ratio = r_males / u_males

# urban to rural females ratio
ur_females_ratio = r_females / u_females


# #### plot the data

# In[62]:

p.figure(1)

p.grid(True)

# plot the total ratio
p.subplot(221)
p.title('Total population ratio' )
p.ylabel('ratio')
p.xlabel('age')
p.plot(df['age'] , ur_ratio, color='b')

# plot the male ratio
p.subplot(222)
p.title('Male population ratio')
p.ylabel('ratio')
p.xlabel('age')
p.plot(df['age'] , ur_males_ratio, color='g')

# plot the female ratio
p.subplot(223)
p.title('Female population ratio')
p.ylabel('ratio')
p.xlabel('age')
p.plot( df['age'] , ur_females_ratio, color='r')

# set layout mode to tight to prevent overlapping
p.tight_layout()

p.show()


# In[ ]:
