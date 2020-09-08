
import googleapiclient.discovery

import json 

def pretty_print(data): 
      
    data = data
    print(json.dumps(data, indent = 10) )

"""
INSERT YOUR OWN API KEY HERE
"""
api_key = ""



api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = api_key

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)

"""
INSERT VIDEO ID HERE
"""
request = youtube.commentThreads().list(part="snippet,replies",videoId="ZvpdN4VltKY")

response = request.execute()

# print(pretty_print(response["items"][0]))
for i in range(20):
    print(i+1,"->",response["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"])