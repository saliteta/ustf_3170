from flask import Flask
from flask import render_template

app = Flask(__name__)

HTML_FILE_NAME = "style"

@app.route('/') 
def home_page():
    return render_template(HTML_FILE_NAME+".html") 
