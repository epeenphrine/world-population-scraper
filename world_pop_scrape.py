#%%
from proxy.proxy_rotate_api import proxy_rotate_api
import pandas as pd 
import requests
import json 
#get table quick through pandas
res = proxy_rotate_api('https://www.worldometers.info/world-population/population-by-country/')
df = pd.read_html(res.content)
df = df[0]
df = df.rename(columns={
    df.columns[0]: "index",
    df.columns[1]: "country", 
    df.columns[2]: "population",
    df.columns[3]: "yearly_change",
    df.columns[4]: "net_change",
    df.columns[5]: "density", 
    df.columns[6]: "land_area",
    df.columns[7]: "migrants",
    df.columns[8]: "fert_rate",
    df.columns[9]: "med_age",
    df.columns[10]: "urban_pop",
    df.columns[11]: "world_share"
})

df = df.astype(str)
# i don't need the index, my database indexes for me already
df = df.drop(columns=['index'])
## data is here converted to dictionary just interate through.
df_dict = df.to_dict('records')

##  send to data base like this as api request
#for item in df_dict:
    #payload = item
    #api = '' ## change to your api
    #res = requests.post(api, data=payload) 
    #print(payload)
    #print(res)