import tornado.httpclient

url = r'http://www.ucdrs.superlib.net'

def callback(response):
    print(response.body)

client = tornado.httpclient.AsyncHTTPClient()
result = client.fetch(url, callback=callback)
