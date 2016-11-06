#use HTTPBaseAuthHandler
#Greate an OpenerDirector with support for Basic HTTP Authentication

import urllib.request




auth_handler = urllib.request.HTTPBaseAuthHandler()
auth_handler.app_password(realm='PDQ Application',
                          uri='https://mahler:2342/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')

opener = urllib.request.build_opener(auth_handler)

urllib.request.install_opener(opener)
urllib.request.urlopen(url)


#use proxy

proxies = {'http': 'localhost'}
opener = urllib.request.FancyURLopener(proxies)
with opener.open(r'http://www.python.org') as f:
    content = f.read().decode('utf-8')
