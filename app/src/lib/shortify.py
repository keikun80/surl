import os, sys
from common import decoding_url, encoding_url, short_url
 
class shortify: 
    _surl = None
    def __init__(self, origin):  
        if target:
            self._surl = encoding_url(origin)
   
        
if __name__ == "__main__": 
    target = "http://www.google.com"
    s = shortify(target)
    print(s._surl) 
    
    