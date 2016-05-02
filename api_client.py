import urllib.request, urllib.parse
def GET(url,username=None):
    return urllib.request.urlopen(url).read().decode()
          
def POST(url,data,username=None):
    data = bytes( urllib.parse.urlencode( data ).encode() )
    handler = urllib.request.urlopen( url, data )
    print("you send: ")
    print( handler.read().decode( 'utf-8' ) )
user_name = input("type in a username")
while True:
    response = input("type get to get messages or type send to send a message.")
    if response == 'get':
        print(GET(("http://localhost/message/"+user_name)))
    elif response == 'send':
        data = {}
        for i in ["to","from","msg"]:
            response = input(i)
            data[i] = response
        POST(("http://localhost/message/"+user_name))
