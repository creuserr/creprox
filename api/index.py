from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path
    if 'http:/' in path:
      path = path.replace(r'http\:\/', 'http://')
    elif 'https:/' in path:
      path = path.replace(r'https\:\/', 'https://')
    else:
      return self.end(400, '400 Bad Request: Invalid URL')
    try:
      proxy = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&country=all&ssl=all&anonymity=all')
      proxy = proxy.text.split('\n')
    except:
      self.end(500, '500 Internal Error: Failed to sc')
  
  def end(self, status, text):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))

"""
class handler(BaseHTTPRequestHandler):
  def do_POST(self):
    # check for proxy
    if 'X-Request-Proxy' in self.headers:
      # use the given proxy if specified
      proxy = self.headers['X-Request-Proxy'].split('\n')
    else:
      # find proxy source online if not specified
      proxy = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&country=all&ssl=all&anonymity=all')
      proxy = proxy.text.split('\n')
    proxy = { 'http': proxy }
    
    # check for method
    if 'X-Request-Method' not in self.headers:
      return self.end(400, '400 Bad Request: X-Request-Method is not specified')
    method = self.headers['X-Request-Method']
    
    # check for url
    if 'X-Request-URL' not in self.headers:
      return self.end(400, '400 Bad Request: X-Request-URL is not specified')
    url = self.headers['X-Request-URL']
    
    # check for headers
    if 'X-Request-Headers' in self.headers:
      headers = json.loads(self.headers['X-Request-Headers'])
    else:
      headers = {}
    
    # start request for get
    if method == 'GET':
      req = requests.get(url, proxies=proxy, headers=headers)
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.send_header('X-Request-Proxy', json.dumps(proxy['http']))
      self.end_headers()
      wfile = {
        'status_code': req.status_code,
        'text': req.text,
        'headers': req.headers
      }
      self.wfile.write(json.dumps(wfile).encode('utf-8'))
      return
    
    # start request for post
    if method == 'POST':
      req = requests.get(url, proxies=proxy, headers=headers, data=self.rfile)
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.send_header('X-Request-Proxy', json.dumps(proxy['http']))
      self.end_headers()
      wfile = {
        'status_code': req.status_code,
        'text': req.text,
        'headers': req.headers
      }
      self.wfile.write(json.dumps(wfile).encode('utf-8'))
      return
    
    self.end('400 Bad Request: X-Request-Method specified an unsupported method')
    
  def do_GET(self):
    self.end(400, '400 Bad Request: Invalid method')
  
  def end(self, status, text):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))
"""