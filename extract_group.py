import requests
import facebook
import json
import mysql.connector as MySQLdb
from pprint import pprint 

#Getting the feeds of group
conn = MySQLdb.connect(host="localhost",user="root",passwd="shubhashree",database="first_database")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS NEW(ID VARCHAR(30) NOT NULL,MESSAGE TEXT(100000),STORY VARCHAR(100000),UPDATED_TIME VARCHAR(20),CREATED_TIME VARCHAR(20), PRIMARY KEY(ID) )")

graph = facebook.GraphAPI(access_token='EAABzvhV5PZBgBAKcq5gYS00mJdNHC0cfaCXU30E0RHYEPK0aNoeozj4wsGgB9yDuH6vws40twJCMqKGNJmJYXDAt1l6To6mv3jvrKcUJ2x9ZCBpDjANxyqVqw3JueaC3sq8jGcdmmZAyRCtvN6VTPSuTsaWfZAFwVALM2E6FAwZDZD',version='2.10')
#list_of_public_groups = ['Advertise Online business','Making Money Online Sales and Business Opportunity','Facebook page likers','Adsense Clickers','Exchange Facebook Likes','Making Money From Home','SEO JOBS','MONEY MAKER']
list_of_public_groups=['Advertise Online business']
length = len(list_of_public_groups)
for i in range(length):
    group_id = graph.search(type='group',q=list_of_public_groups[i])
    group_identifier = []
    for res in group_id['data']:
        group_identifier.append(res['id'])
    group_feed = graph.get_connections(id=group_identifier[0],connection_name='feed')
    
    with open('group_posts.json','w') as temp_file:
        json.dump(group_feed,temp_file,indent=4,separators=(',',':'))
        #temp_file.write('\n')

    with open('group_posts.json','r') as data_file:
        info = json.load(data_file)        

    for val in info:
        fbgroup_posts = info[val] 
    
        for obj in fbgroup_posts:
            try:
                print(obj.get('story','NULL'))
                insert_stmt2 = ("INSERT INTO NEW VALUES (%s,%s,%s,%s)")
                values = (obj.get('id','NULL'),obj.get('message','NULL'),obj.get('story','NULL'),obj.get('updated_time','NULL'),obj.get('created_time','NULL'))
                cur.execute(insert_stmt2,values)
                conn.commit()
            except:
                pass
