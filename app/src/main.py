from fastapi import FastAPI, Request
from pydantic import BaseModel, AnyUrl
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from lib.common import resolve, saveurl, short_url, benchmark

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
     
app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates") 

@app.get("/{id}", response_class=HTMLResponse) 
async def index(request: Request, id: str): 
    return templates.TemplateResponse (
        request=request, name="item.html", context={"id":id}
    )

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
