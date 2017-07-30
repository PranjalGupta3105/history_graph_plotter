import os
import sqlite3
import pprint
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt

def parse(url):
    try:
        parsed_url_components=url.split('//')
        sublevel_split = parsed_url_components[1].split('/',1)
        domain=sublevel_split[0].replace("www.",'')

        if domain=="fb.com" or domain=="facebook.com":
            domain="fb.com"
            return domain
        elif domain=="google.com" or domain=="google.co.in":
            domain="google.co.in"
            return domain
        else:
            return domain

    except IndexError:
        print "Inappropriate Error in the URL"+url

def analyze(results):
    plt.bar(range(len(results)), results.values(), align='edge')
    plt.xticks(rotation=45)
    plt.xticks(range(len(results)), results.keys())
    plt.show()



data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
#print data_path ==> C:\Users\Pranjal Gupta\AppData\Local\Google\Chrome\User Data\Default
files=os.listdir(data_path)
#print files ==> Prints all the available files in Default Folder
history_db = os.path.join(data_path, 'history1')

#print history_db
c = sqlite3.connect(history_db)
cursor = c.cursor()
stmt = "SELECT urls.url, urls.visit_count FROM urls, visits where urls.id=visits.url;"
#stmt1 = "SELECT url, last_visit_time FROM urls"
cursor.execute(stmt)
#cursor.execute(stmt)

results = cursor.fetchall()

sites_count={}

for url,count in results:
    url = parse(url)
    if url in sites_count:
        #if url=="fb.com" or url=="facebook.com":
        sites_count[url] +=1
    else:
        sites_count[url] = 1


sorted_sites_dict=OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))
#print sorted_sites_dict
analyze(sorted_sites_dict)



#result=dict(results)
#pprint.pprint(results)#This pprint makes the printing of the items in the dictionary easy in a new line....

#print result
#print(results.__sizeof__())

