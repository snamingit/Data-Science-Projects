import os
import fredapi as fa
import pandas as pd
from config import fred
fred = fa.Fred(fred['api_key'])
import datetime
from datetime import timedelta

q_series = [('gdp','GDP')] 
m_series = [('capacity_manuf','MCUMFN'),('cpi','CPIAUCSL'),('unemp','UNRATE'),('leadin_ind','USALOLITONOSTSAM')]
d_series = [('fed_funds_rate','DFF'),('tbill_3','DTB3'),('tbill_6','DTB6')]
all_series = [item for sublist in [q_series, m_series, d_series] for item in sublist]


#Get the starting and end of series
date_df =[]

for varname, var in all_series:
    x= fred.search(var).observation_start
    x= x[var].strftime("%Y-%m-%d")
    y= fred.search(var).observation_end
    y= y[var].strftime("%Y-%m-%d")
    #list=[varname,x,y]
    #date_df.append(list)
    date_df.append({'Variable': varname, 'Start': x, 'End': y})


date_df = pd.DataFrame(date_df)
date_df.sort_values(by='Start')

#Get all the quarterly series
q_df =[]

for varname, var in q_series:
    x = fred.get_series(var)
    x.name = varname
    x = pd.DataFrame(x)
    q_df.append(x)

q_df = pd.concat(q_df, axis=1)
q_df.index = q_df.index - timedelta(days=1)
q_df['quarter'] = q_df.index.quarter
q_df['year'] = q_df.index.year
q_df['q_year'] = q_df['quarter'].astype(str) +'_'+ q_df['year'].astype(str)
q_df.set_index('q_year', inplace=True)

q_df.tail()

#Get all the monthly series
m_df =[]

for varname, var in m_series:
    x = fred.get_series(var)
    x.name = varname
    x = pd.DataFrame(x)
    m_df.append(x)

m_df = pd.concat(m_df, axis=1)
m_df['quarter'] = m_df.index.quarter
m_df['year'] = m_df.index.year
m_df['q_year'] = m_df['quarter'].astype(str) +'_'+ m_df['year'].astype(str)


m_df
m_df_mean= m_df.groupby('q_year').mean()
m_df_mean.sort_values(by=['year','quarter'])
m_df_mean.sample()

d_df =[]

for varname, var in d_series:
    x = fred.get_series(var)
    x.name = varname
    x = pd.DataFrame(x)
    d_df.append(x)

d_df = pd.concat(d_df, axis=1)
d_df['quarter'] = d_df.index.quarter
d_df['year'] = d_df.index.year
d_df['q_year'] = d_df['quarter'].astype(str) +'_'+ d_df['year'].astype(str)

d_df_mean= d_df.groupby('q_year').mean()
d_df_mean.sort_values(by=['year','quarter'])
d_df_mean.sample()
d_df_mean.tail()

#merge datasets
df0 = q_df.merge(m_df_mean, left_index=True, right_index=True, how='inner')
df = df0.merge(d_df_mean, left_index=True, right_index=True, how='inner')

#clean data
df.drop(columns=['quarter_x', 'year_x'], inplace=True)

df['quarter']= df['quarter'].astype(int)
df['year']= df['year'].astype(int)

## only include data starting 1972 when all the fields have data.
df = df[df['year']>=1972]

df.head()
df.shape
df.to_csv("data.csv")
