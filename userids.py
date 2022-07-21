from twython import Twython

# Paste your codes here
app_key = 'tr1RZR9F6Mo5Rdi9czzpMXUux'
app_secret ='vpbeNjAaah90FF7bYg91k54dgBDhop7H2koryCRIZXdetmvnoU'
oauth_token = '4113262402-Ih4QHi3Sc5uvzyoxnsbSWwU91FzQMVhlLwH3smm'
oauth_token_secret= 'FHNs7CYZuECtES57l8hvkk8IgBv5qOtxbDb384ddkb8Zw'

# Create twitter thing to query
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
# What to look up (Twitter screen_name:s)
ids = ["HafizSaeedLive"
,]# Create a comma separated string from the previous list
comma_separated_string = ",".join(ids)

# Query twitter with the comma separated list
output = twitter.lookup_user(screen_name=comma_separated_string)

username_list=[]

# Loop through the results (Twitter screen names)
outfile=open('twee.txt','a')
for user in output:
    print user["id_str"]
    usr_id=user["id_str"]
    outfile.write(usr_id)
    outfile.write("\n")
