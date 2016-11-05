import tornado.httpclient

def callback(response):
    print(response.body)

client = tornado.httpclient.AsyncHTTPClient()
client.fetch(url, callback=callback)
