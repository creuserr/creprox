from http.server import BaseHTTPRequestHandler
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    # format the provided url
    path = self.path
    if 'http:/' in path:
      path = path.replace(r'http\:\/', 'http://')
    elif 'https:/' in path:
      path = path.replace(r'https\:\/', 'https://')
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
      self.end(200, req.text)
    except Exception as e:
      return self.end(400, f'400 Bad Request: The requested URL raised an error: {str(e)}')
  
  def end(self, status, text):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))