from http.server import BaseHTTPRequestHandler
import requests
import base64
import json
import random

class Rotation:
  def __init__(self):
    pass

  def $model(self):
    char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join([char[random.randint(0, len(char) - 1)] for _ in range(3)]) + str(random.randint(100, 999))

  def $build(self):
    char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join([char[random.randint(0, len(char) - 1)] for _ in range(2)]) + '.'.join([str(random.randint(1, 99999)) for _ in range(3)])

  def create(self):
    prod = f"Mozilla {random.randint(3, 5)}.0"
    andr = f"Android {random.randint(10, 13)}"
    mod = f"{self.$model()} Build/{self.$build()}"
    kit = f"AppleWebKit/{random.randint(500, 550)}"
    ver = f"Version/{random.randint(3, 5)}"
    chrom = f"Chrome/{self.$build()}"
    safar = f"Mobile Safari/{random.randint(500, 550)}"
    return f"{prod} (Linux; {andr} {mod}) {kit} (KHTML, like Gecko) {ver} {chrom} {safar}"

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
      prox1 = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&country=all&ssl=all&anonymity=all')
      prox2 = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
      proxy = { 'http': prox1.text.split('\n').extend(prox2.text.split('\n')) }
    except:
      self.end(500, '500 Internal Error: Failed to generate scraped proxies')
    
    # start the request
    try:
      h = {
        'Origin': path,
        'User-Agent': Rotation.create()
      }
      req = requests.get(path, proxies=proxy, headers=h)
      if req.status_code > 399:
        raise Exception(f'{req.status_code}: {req.text}')
      self.end(200, req.text, proxy['http'], req.headers)
    except BaseException as e:
      return self.end(400, f'400 Bad Request: The request raised an error\n{str(e)}')
  
  def end(self, status, text, proxy=None, headers=None):
    self.send_response(status)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Access-Control-Allow-Origin', '*')
    if proxy != None:
      proxy = json.dumps(proxy).encode('utf-8')
      proxy = base64.b64encode(proxy)
      self.send_header('X-Request-Proxy', proxy.decode('utf-8'))
      self.send_header('X-Request-Headers', json.dumps(dict(headers)))
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))