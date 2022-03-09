import urequests, time, network
from machine import deepsleep
def connect_router(
    user_name1='user_name1', password1='password1',
    user_name2='user_name2', password2='password2'):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    print(station.scan())
    if '%s'%user_name1 in str(station.scan()):
        print(user_name1)
        ssid = '%s'%user_name1
        password = '%s'%password1
    else:
        print('%s'%user_name2)
        ssid = '%s'%user_name2
        password =  '%s'%password2
    ################
    if station.isconnected() == True:
        print("Already connected")
        return "Already connected"
    else: 
        station.connect(ssid, password)
    count = 0
    while station.isconnected() == False:
        while station.isconnected() == False and count < 300000:
            count += 1
        count = 0
        if station.isconnected() == False:
            deepsleep(10000)
        elif station.isconnected() == True:
            break
        else:
            print('error')
    print("Connection successful")
############################# read/write ####################
def http_post_request(url='myurl.com'):
    response = urequests.get('%s'%url)
    response.close()

def http_get_request(url='myurl.com'):
    response = urequests.get('%s'%url)
    return response.json()
