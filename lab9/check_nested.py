import urllib.request
urls = [
    'http://127.0.0.1:8000/nested/',
    'http://127.0.0.1:8000/nested/about',
    'http://127.0.0.1:8000/nested/contact',
]
for u in urls:
    try:
        r = urllib.request.urlopen(u, timeout=5)
        body = r.read(2000).decode('utf-8', 'replace')
        print('URL:', u)
        print('STATUS:', r.getcode())
        print('BODY:\n', body)
        print('---')
    except Exception as e:
        print('URL:', u, 'ERROR:', e)
        print('---')
