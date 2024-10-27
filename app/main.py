from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl

from lib.common import resolve, saveurl, short_url

app = FastAPI() 
#### 
# hash value's duplicate check 
# when if dup of hash how we will resolve with shortest time
# 
####

class ModelSurl(BaseModel):
    surl: str
    origin: AnyUrl
    #origin: str

class ModelOrigin(BaseModel):
    origin: str
     

@app.get("/") 
def index():
    return {"hello world"} 

@app.post("/csurl/")
async def mkshort(csurl: ModelOrigin): 
    print(type(csurl.origin))
    s = short_url(csurl.origin)
    sObj = ModelSurl(surl=s, origin=csurl.origin) 
    saveurl(sObj)
    return sObj
    
@app.get("/{surl}")
def fetch_surl(surl: str): 
    rObj = resolve(surl)  
    return rObj