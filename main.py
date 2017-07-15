import catalog_client

print('Beginning of example')

# Request for catalog data version
version_response = catalog_client.get_version()
print('This is the version number {}'.format(version_response.json()['version']))

# Search for a package
search_spending_response = catalog_client.search_package('spending')
search_test_response = catalog_client.search_package('test')
print('This is the response of searching spending: {}'.format(search_spending_response.json()))
print('This is the response of searching test: {}'.format(search_test_response.json()))
