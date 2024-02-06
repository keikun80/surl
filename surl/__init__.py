from flask import Flask, url_for 
import zlib

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':  
    app.debug=True
    app.run()