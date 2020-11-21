import requests

domain = 'neuralnine.com'

file = open('test.txt', 'r')

content = file.read()
subdomains = content.splitlines()

for subdomains in subdomains:
    url = f'http://{subdomains}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("Discovered Subdomain: ", url)