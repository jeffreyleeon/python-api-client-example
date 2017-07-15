import requests
import config

base_url = config.BASE_URL

def get_version():
    url = base_url
    return requests.get(url)

def search_package(text):
    # Maybe check whether text is a string?
    url = '{0}action/package_search?q={1}'.format(base_url, str(text))
    return requests.get(url)
