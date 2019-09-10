from flask import render_template
from app import app
from .request import get_sources,get_articles

# views
@app.route('/')
def index():
    '''
    root page that returns the index page
    '''

    # Getting news sources
    sources = get_sources()
    articles = get_articles()


    return render_template('index.html', source = sources, articles = get_articles)


@app.route('/sources/<int:sources_id>')
def sources(sources_id):
    '''
    news page function that returns news details page
    '''

    return render_template('sources.html')


@app.route('/articles/<int:articles_id')
def articles(articles_id):
    '''
    articles function that returns articles page
    '''

    return render_template('articles.html')
