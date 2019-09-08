from flask import render_template
from app import app

#views
@app.route('/')
def index():

    '''
    root page that returns the index page
    '''

    
    return render_template('index.html')