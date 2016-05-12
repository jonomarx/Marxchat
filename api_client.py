import urllib.request, urllib.parse,sys,time
def GET(url,username=None):
    return urllib.request.urlopen(url).read().decode()
          
def POST(url,data,username=None):
    data = bytes( urllib.parse.urlencode( data ).encode() )
    handler = urllib.request.urlopen( url, data )
    print("you send: ")
    print( handler.read().decode( 'utf-8' ) )
def auto_get():
    one = True
    while True:
        try:
            if one:
                one = False
                current = GET(("http://localhost/message/"+user_name))
                time.sleep(1)
            new = GET(("http://localhost/message/"+user_name))
            if new != current:
                for i in new:
                    if i not in current:
                        print(i)
                current = new
        except Exception:
            sys.exit()
user_name = input("type in a username ")
while True:
    response = input("type get to get messages or type send to send a message.")
    if response == 'get':
        print(GET(("http://localhost/message/"+user_name)))
    elif response == 'send':
        data = {}
        for i in ["to","from","msg"]:
            response = input(i)
            data[i] = response
        POST(("http://localhost/message/"+user_name),data)
    else:
        response = input("do you want to auto-get messages? (y/quit)")
        if response == "y":
            pass
            auto_get()
        elif response == "quit":
            sys.exit()
