from http.server import BaseHTTPRequestHandler
import requests
import base64
import json

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    # format the provided url
    path = self.path[1:]
    if 'http:' in path:
      path = path.replace('http:', 'http:/')
    elif 'https:' in path:
      path = path.replace('https:', 'https:/')
    else:
      return self.end(400, '400 Bad Request: Invalid URL')
    
    # generate scraped proxies
    try:
      proxy = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&country=all&ssl=all&anonymity=all')
      proxy = { 'http': proxy.text.split('\n') }
    except:
      self.end(500, '500 Internal Error: Failed to generate scraped proxies')
    
    # start the request
    try:
      req = requests.get(path, proxies=proxy)
      if req.status_code > 399:
        raise Exception(f'{req.status_code}: {req.text}')
      self.end(200, req.text, proxy['http'], req.headers)
    except Exception as e:
      return self.end(400, f'400 Bad Request: The requested URL raised an error: {str(e)}')
  
  def end(self, status, text, proxy=None, headers=None):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    if proxy != None:
      proxy = dict(json.dumps(proxy)).encode('utf-8')
      proxy = base64.b64encode(proxy)
      self.send_header('X-Request-Proxy', proxy.decode('utf-8'))
      self.send_header('X-Request-Headers', json.dumps(headers))
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))