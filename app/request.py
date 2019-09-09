from app import app
import urllib.request
import json
from .models import sources

Sources = sources.Sources


# Getting api key
api_key = app.config['API_KEY']

# Getting the news sources base url
base_url = app.config['SOURCES_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function that processes the sources result and transform them to a list of Objects

    Args:
        news_list: a list of dictionaries that contain news sources details
    '''

    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        author = sources_item.get('author')
        description = sources_item.get('description')
        url = sources_item.get('url_path')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        sources_object = Sources(id, name, author, description,
                           url, category, language, country)
        sources_results.append(sources_object)
