from http.server import BaseHTTPRequestHandler
import requests
import base64
import json
import random

class Rotation:
  def __init__(self):
    pass

  def _model(self):
    char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join([char[random.randint(0, len(char) - 1)] for _ in range(3)]) + str(random.randint(100, 999))

  def _build(self):
    char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join([char[random.randint(0, len(char) - 1)] for _ in range(2)]) + '.'.join([str(random.randint(1, 99999)) for _ in range(3)])

  def create(self):
    prod = f"Mozilla {random.randint(3, 5)}.0"
    andr = f"Android {random.randint(10, 13)}"
    mod = f"{self._model()} Build/{self._build()}"
    kit = f"AppleWebKit/{random.randint(500, 550)}"
    ver = f"Version/{random.randint(3, 5)}"
    chrom = f"Chrome/{self._build()}"
    safar = f"Mobile Safari/{random.randint(500, 550)}"
    return f"{prod} (Linux; {andr} {mod}) {kit} (KHTML, like Gecko) {ver} {chrom} {safar}"

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.url()
    proxy = self.proxy()
    try:
      h = {
        'Origin': path,
        'User-Agent': Rotation().create()
      }
      req = requests.get(path, proxies=proxy, headers=h)
      if req.status_code > 399:
        raise Exception(f'{req.status_code}: {req.text}')
      self.end(200, req.text, req.headers, h['User-Agent'])
    except BaseException as e:
      return self.end(400, f'400 Bad Request: The request raised an error\n{str(e)}')
  
  def do_POST(self):
    path = self.url()
    if path == None:
      return self.end(400, '204 No Content: ')
    proxy = self.proxy()
    try:
      h = {
        'Origin': path,
        'User-Agent': Rotation().create()
      }
      for header in dict(self.headers):
        h[header] = self.headers[header]
      d = None
      j = None
      if(h["Content-Type"] == "application/json"):
        j = json.loads(self.rfile.read(int(h["Content-Length"])))
      else:
        d = self.rfile.read()
      req = requests.post(path, proxies=proxy, headers=h, data=d, json=j)
      if req.status_code > 399:
        raise Exception(f'{req.status_code}: {req.text}')
      self.end(200, req.text, req.headers, h['User-Agent'])
    except BaseException as e:
      return self.end(400, f'400 Bad Request: The request raised an error\n{str(e)}')
  
  def end(self, status, text, headers=None, ua=None):
    self.send_response(status)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Access-Control-Allow-Origin', '*')
    if ua != None:
      self.send_header('X-Response-Headers', json.dumps(dict(headers)))
      self.send_header('X-Request-UA', ua)
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))
  
  def proxy(self):
    try:
      prox1 = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&country=all&ssl=all&anonymity=all')
      prox2 = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
      proxy = { 'http': prox1.text.split('\n').extend(prox2.text.split('\n')) }
      return proxy
    except:
      self.end(500, '500 Internal Error: Failed to generate scraped proxies')
  
  def url(self):
    path = self.path[1:]
    if 'http:' in path:
      return path.replace('http:', 'http:/')
    elif 'https:' in path:
      return path.replace('https:', 'https:/')
    else:
      return self.end(400, '400 Bad Request: Invalid URL')