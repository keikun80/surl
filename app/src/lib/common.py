import hashlib
import base64 
import pickle
from pydantic import BaseModel
from pathlib import Path 

DOCUMENT_ROOT="/Users/Jason/project/surl/app/data"

class ModelSurl(BaseModel):
    origin: str 
    surl: str    
    
def encoding_url(targetURL):  
    '''  
    encode plain text url with base64
    return : encoded url 
    '''
    encodeurl= ""
    try:
        encodeurl = base64.urlsafe_b64encode(bytes(targetURL, 'UTF-8')).decode('UTF-8')  
    except (TypeError, UnicodeEncodeError) as e:
        print(e)
    return encodeurl

def decoding_url(encodeURL):
    ''' 
    decode encoded url with base64
    return : decoded url
    '''
    decodeurl = ""
    try:
        decodeurl = base64.urlsafe_b64decode(bytes(encodeURL, 'UTF-8')).decode('UTF-8') 
    except (TypeError, UnicodeDecodeError) as e:
        print(e)
    return decodeurl

def short_url(targetURL):
    '''
    make short url 
    return : shorted url
    ''' 
    _hash = hashlib.md5()
    try:
        _hash.update(targetURL.encode("UTF-8"))
        return (_hash.hexdigest()[:6])
    except (TypeError,UnicodeEncodeError) as e:
        print(e) 
        return None

def resolve(surl): 
    filepath = DOCUMENT_ROOT+'/'+surl  
    result = None
    try:
        with open (filepath, 'rb') as f:
            result = pickle.load(f) 
    except Exception as e: 
        result = e
    return result 

def saveurl(saveObj): 
    Path(DOCUMENT_ROOT).mkdir(parents=True, exist_ok=True) 
    filepath = DOCUMENT_ROOT+'/'+saveObj.surl
    try:
        with open (filepath, 'wb+') as f:
            pickle.dump(saveObj, f) 
    except Exception as e:
        print(e) 
        
if __name__ == "__main__":
    url = ['https://stackoverflow.com/questions/8247792/python-how-to-cut-a-string-in-python',
           'https://stackoverflow.com/questions/58663300/cut-string-in-python-from-specific-word-words-to-the-end-of-the-string',
           'https://stackoverflow.com/questions/1010961/ways-to-slice-a-string'
           ] 
    for u in url: 
        s = short_url(u) 
        sObj = ModelSurl(surl=s, origin=u)
        saveurl(sObj)
        resolve(s) 