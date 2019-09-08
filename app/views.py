from flask import render_template
from app import app

#views
@app.route('/')
def index():

    '''
    root page that returns the index page
    '''

    title = 'Home - The best news website.'
    return render_template('index.html')

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    movie page function that returns news details page
    '''

    return render_template('news.html')

