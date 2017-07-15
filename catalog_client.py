import requests

base_url = "http://catalog.data.gov/api/3/"

def get_version():
    url = base_url
    return requests.get(url)

def search_package(text):
    # Maybe check whether text is a string?
    url = '{0}action/package_search?q={1}'.format(base_url, str(text))
    print('url is {}'.format(url))
    return requests.get(url)
