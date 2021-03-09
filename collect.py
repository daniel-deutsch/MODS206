from requests_html import HTMLSession


session = HTMLSession()
r = session.get('http://python-requests.org')

r.html.render()

print(r.html.search('Python 2 will retire in only {months} months!')) # None