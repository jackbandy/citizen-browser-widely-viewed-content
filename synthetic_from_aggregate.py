import pandas as pd

# read in aggregate data
df_hits = pd.read_csv('data/q2/impressions-top-1000-domains.csv')
df_users = pd.read_csv('data/q2/unique_users-top-1000-domains.csv')
df = df_users.merge(df_hits,on='url_domain')

# citizen browser had 1,917 panelists as of December 2020
user_ids = pd.Series(list(range(1,1919)))

domain_visitors = []
for index, row in df.iterrows():
    users_df = pd.DataFrame(user_ids.sample(row['unique_users']))
    users_df.columns = ['user_id']
    users_df['url_domain'] = row['url_domain']
    domain_visitors.append(users_df)

#TODO set up random date

# save output
synthetic = pd.concat(domain_visitors)
synthetic.to_csv('synthetic_visitors/visitors.csv',index=False)
synthetic.sample(1000).to_csv('synthetic_visitors/sample_visitors_1k.csv',index=False)
