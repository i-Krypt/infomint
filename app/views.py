from flask import render_template
from app import app
from .request import get_sources

# views
@app.route('/')
def index():
    '''
    root page that returns the index page
    '''

    # Getting news sources
    sources = get_sources()


    return render_template('index.html', source = sources)


@app.route('/sources/<int:sources_id>')
def sources(sources_id):
    '''
    movie page function that returns news details page
    '''

    return render_template('sources.html')


