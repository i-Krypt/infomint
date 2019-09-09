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
    business_sources = get_sources('business')
    science_sources = get_sources('science')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    health_sources = get_sources('health')
    entertainment_sources = get_sources('entertainment')

    return render_template('index.html', business = business_sources,science = science_sources,sports = sports_sources,entertainment  = entertainment_sources,health = health_sources,technology = technology_sources)


@app.route('/sources/<int:sources_id>')
def sources(sources_id):
    '''
    movie page function that returns news details page
    '''

    return render_template('sources.html')


