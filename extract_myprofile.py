import requests
import facebook
import json
import mysql.connector as MySQLdb
from pprint import pprint 

graph = facebook.GraphAPI(access_token='EAABzvhV5PZBgBAKcq5gYS00mJdNHC0cfaCXU30E0RHYEPK0aNoeozj4wsGgB9yDuH6vws40twJCMqKGNJmJYXDAt1l6To6mv3jvrKcUJ2x9ZCBpDjANxyqVqw3JueaC3sq8jGcdmmZAyRCtvN6VTPSuTsaWfZAFwVALM2E6FAwZDZD',version='2.10')
posts = graph.get_connections(id='me',connection_name='posts')

fp1 = open('my_posts','w')
with fp1 as temp_file:
    json.dump(posts,temp_file,indent=4,separators=(',', ': '))

conn1 = MySQLdb.connect(host="localhost",user="root",passwd="shubhashree",database="first_database")
cur1 = conn1.cursor()
cur1.execute("CREATE TABLE IF NOT EXISTS my_table(ID VARCHAR(30) NOT NULL,MESSAGE VARCHAR(100000),STORY VARCHAR(100000),CREATED_TIME DATE, PRIMARY KEY(ID) )")

with open('my_posts') as data_file:    
    info1 = json.load(data_file)

myfb_posts = info1['data']
for obj in myfb_posts:
    try:
        insert_stmt = ("INSERT INTO my_table VALUES (%s,%s,%s,%s)")
        val = (obj["id"],obj["message"],obj["story"],obj["created_time"])
        cur1.execute(insert_stmt,val)
        conn1.commit()
    except:
        pass

