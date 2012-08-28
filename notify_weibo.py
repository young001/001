import webbrowser
import urllib
import os
import time
from weibo import APIClient

APP_KEY = '3699220472' # app key
APP_SECRET = '93ebbb2c2b46f388c8f3ac584ba28016' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url


if os.path.exists('token_file') and (int(open('token_file','r').readline().split()[1])>time.time()):
    token_data = open('token_file','r').readline()
    #print 'token_data',token_data
    access_token = token_data.split()[0]
    expires_in = token_data.split()[1]
    print 'expires_in is', expires_in
    #print 'now time is', time.time()
    #if time.time()<expires_in:
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
else:
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url
#print 'the url is',urllib.urlopen(url).read()
#print 'now the url is', urll
    webbrowser.open_new_tab(url)

    code = raw_input('ok,you got the code,then input it')
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
#to save the access_token in file
    token_file = open('token_file','w')
    token_file.write('%s\t%s' %(access_token,expires_in))

#print 'access_token is', access_token
#print 'expires_in is', expires_in

client.set_access_token(access_token, expires_in)
#client.get.statuses__user_timeline(uid=123)
print client.get.statuses__user_timeline()
#print client.get.remind__unread_count

#test shorten url
url_long1 = 'www.baidu.com'
print client.get.short_url__shorten(url_long='www.baidu.com')
print type(client.get.short_url__shorten(url_long='http://www.baidu.com'))
print client.get.short_url__shorten(url_long='http://www.baidu.com').get('urls')[0].get('url_short')



