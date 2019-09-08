from flask import render_template
from app import app
from .request import get_news

# views
@app.route('/')
def index():
    '''
    root page that returns the index page
    '''

    # Getting news sources
    news_headlines = get_news('headlines')
    trending_news = get_news('trending')
    title = 'Home - The best news website.'
    return render_template('index.html', title=title, headline=news_headlines, trending = trending_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    movie page function that returns news details page
    '''

    return render_template('news.html')


