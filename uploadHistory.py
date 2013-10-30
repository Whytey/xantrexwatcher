'''
Created on 29/10/2013

@author: djwhyte
'''

from datetime import datetime, timedelta
import json
import time
import urllib2


def __requestJSON(data):
    '''Make a JSON request, to get a JSON response'''    
    req = urllib2.Request('http://192.168.0.100/zabbix/api_jsonrpc.php')
    req.add_header('Content-Type', 'application/json')

    return json.loads(urllib2.urlopen(req, json.dumps(data)).read())

def __authenticate(user, password):
    '''Using the provided login, authenticate and return the authentication key'''
    data = {"jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                       "user": user,
                       "password": password},
            "id": 1
            }
    
    response = __requestJSON(data)
    return response["result"]
    
def __getPowerForDate(authkey, date):
    '''Using the provided authentication key, get the maximum power out for
    the specified data'''
    epoch = datetime(1970, 1, 1, 0, 0, 0)
    timestamp = (date + timedelta(seconds=time.timezone) - epoch).total_seconds()
    data = {"jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                       "history": 0,
                       "itemids": ["22521"],
                       "time_from": timestamp,
                       "time_till": timestamp + 60,
                       "output": "extend"}, 
            
            "auth": authkey,
            "id": 2
            }

    response = __requestJSON(data)
    return response["result"][0]["value"]    
    
if __name__ == '__main__':
    # Authenticate
    user = raw_input("Zabbix Username: ")
    password = raw_input("Zabbix Password: ")
    authkey = __authenticate(user, password)
    
    # Get all history items for power.today
    date = datetime(2013, 10, 25, 23, 0, 0)
    end = datetime(2013, 02, 26, 00, 0, 0)
    
    # Get the data
    while True:

        # Get just 200 at a time so you can use the bulk CSV uploader 
        for count in range(200):
            try:
                power = float(__getPowerForDate(authkey, date))
            except:
                pass
            print "%s, %s" % (date.strftime("%Y%m%d"), power)
            date = date - timedelta(days=1)

        raw_input("Press enter for next 200...")