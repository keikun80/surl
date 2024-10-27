import requests
import string
import random 
import json 
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

def random_string(size=10, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_url(s):
    prefix = ['http','https','file','smb','s3'] 
    prefix2 = ['www','web','data','links','img']
    suffix = ['com','co.kr','org','li','io','tk']
    return random.choice(prefix)+'://'+random.choice(prefix2)+'.'+random_string(size=10)+'.'+random.choice(suffix)+'/'+random_string(size=s) 
    
if __name__ == "__main__":  
    headers = {
    "Content-type": "application/json",
    "accept": "application/json"
    }
    for _ in range(100):  
        origin = random_url(random.randrange(100))  
        body = {"origin": origin}    
        print(body)
        tic = time.perf_counter()
        r1 = requests.post("http://127.0.0.1:8000/csurl/", data=json.dumps(body), headers=headers)
        toc = time.perf_counter() 
        elapsed = toc - tic   
        print(r1) 
        try:
            response = r1.json() 
            print(f"surl : {response['surl']}, duration: {toc - tic:0.4f}")  
        except Exception as e:
            print(e)