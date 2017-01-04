import pandas as pd, matplotlib as mpl

main_df = pd.read_excel("http://www.censusindia.gov.in/2011census/C-series/c-13/DDW-0000C-13.xls", header=None)
df = main_df

# #### Now remove unnecessary rows from the top

df = df.ix[7:]

# ### Drop columns 1,2,3 inplace without reassigning it to df

columns_to_remove = df.columns[[0,1,2]]
df.drop( columns_to_remove , axis = 1 , inplace = True )
indiadf = df.ix[:108]
indiadf.tail()


# ### Rename dataframe columns

indiadf.columns = [ "palce" , "age" , "total" , "males" , "females" , "rural_total" , "rural_males" , "rural_females" , "urb_total" , "urb_males" , "urb_females" ]
indiadf.axes


# ### set matplotlib to work inline and import pyplot
from matplotlib import pyplot as p, patches as pt


# # Start plotting the data

df = indiadf
df.reset_index(inplace=True, drop=True)

# fix small data problem,s before proceeding

# all ages is removed
# 100+ is considered as  101

df = df.ix[1:] # remove first row
buffer = df.set_value(100, 1 , 101 , takeable = True) # buffer so that it doesnt print output into notebook


# ## Population by age
p.plot( df['age'] , df['total'] , df['age'] ,  df['rural_total'] , df['age'] ,  df['urb_total'] )

# et decorations
p.ylabel('population in 10 millions')
p.xlabel('age')

p.grid(True)
p.title('population by age')
p.legend(['total','rural','urban'])

p.show()


# ## Gender population differnce by age
males = df['males']
females = df['females']

r_males = df['rural_males']
r_females = df['rural_females']

u_males = df['urb_males']
u_females = df['urb_females']

diff = females - males
r_diff = r_females - r_males
u_diff = u_females - u_males


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

ratio = females / males
r_ratio = r_females / r_males
u_ratio = u_females / u_males

# normalize the data to be around 0
ratio -= 1
r_ratio -= 1
u_ratio -= 1

p.plot( df['age'] , ratio , df['age'] , r_ratio , df['age'] , u_ratio )

# set decorations
p.ylabel('population ratio (F:M)')
p.xlabel('age')

p.grid(True)
p.title('Sex ratio by age')
p.legend(['total','rural','urban'])

p.show()



