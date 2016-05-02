import urllib.request, urllib.parse
def GET(url,username=None):
    return urllib.request.urlopen(url).read().decode()
          
def POST(url,data,username=None):
    data = bytes( urllib.parse.urlencode( data ).encode() )
    handler = urllib.request.urlopen( url, data )
    print("you send: ")
    print( handler.read().decode( 'utf-8' ) )
