import requests
import facebook
import json
import mysql.connector as MySQLdb
from pprint import pprint 

#Getting the feeds of group
graph = facebook.GraphAPI(access_token='EAABzvhV5PZBgBAKcq5gYS00mJdNHC0cfaCXU30E0RHYEPK0aNoeozj4wsGgB9yDuH6vws40twJCMqKGNJmJYXDAt1l6To6mv3jvrKcUJ2x9ZCBpDjANxyqVqw3JueaC3sq8jGcdmmZAyRCtvN6VTPSuTsaWfZAFwVALM2E6FAwZDZD',version='2.10')
list_of_public_groups = ['Advertise Online business','Making Money Online Sales and Business Opportunity','Facebook page likers','Adsense Clickers','Exchange Facebook Likes','Making Money From Home','SEO JOBS','MONEY MAKER']
length = len(list_of_public_groups)
group_id = graph.search(type='group',q=list_of_public_groups[0])
group_identifier = []
for res in group_id['data']:
    group_identifier.append(res['id'])
group_feed = graph.get_connections(id=group_identifier[0],connection_name='feed')
fp2 = open('test_file','w')
fp2.write('\n')
with fp2 as temp_file:
    json.dump(group_feed,temp_file,indent=4,separators=(',',':'))
        #temp_file.write('\n')

conn2 = MySQLdb.connect(host="localhost",user="root",passwd="shubhashree",database="first_database")
cur2 = conn2.cursor()
cur2.execute("CREATE TABLE IF NOT EXISTS GROUP_DATA(ID VARCHAR(30) NOT NULL,MESSAGE VARCHAR(100000),STORY VARCHAR(100000),UPDATED_TIME VARCHAR(20),CREATED_TIME VARCHAR(20), PRIMARY KEY(ID) )")
#db.commit()

with open('test_file') as data_file:    
    info2 = json.load(data_file)
#pprint(info2)
for val in info2:
    pprint(val)
    fbgroup_posts = info2[val] 
    #pprint(fbgroup_posts)
    print("*********************************************************************")

    for obj in fbgroup_posts:
    #print(counter["id"])
        try:
            insert_stmt2 = ("INSERT INTO GROUP_DATA VALUES (%s,%s,%s,%s)")
            val2 = (obj["id"],obj["message"],obj["story"],obj["updated_time"],obj["created_time"])
            cur2.execute(insert_stmt2,val2)
            conn2.commit()
        except:
            pass
    
 
 
