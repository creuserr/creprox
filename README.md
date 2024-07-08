## creprox :ninja:
REST-ly perform an HTTP GET request with rotating proxy and user agents.

```http
GET https://creprox.vercel.app/httpbin.org/get
Origin: 34.231.247.92
User-Agent: Mozilla/5.0 (Linux; Android 13; EPA642) AppleWebKit/145 (KHTML, like Gecko) Version/4.0 Chrome/348.300.751 Mobile Safari/945.892.561
```

### Usage

Place the URL without the protocols after the `creprox.vercel.app`. For example:

```http
GET https://creprox.vercel.app/example.com
```

Which will be transformed into a URL with `https` protocol.

### User Agent

The user agent generator uses android mobile format:

> Mozilla/<kbd>1</kbd>.0 (Linux; Android <kbd>2</kbd>; <kbd>3</kbd>) AppleWebKit/<kbd>4</kbd> (KHTML, like Gecko) Version/<kbd>5</kbd>.0 Chrome/<kbd>6</kbd> Mobile Safari/<kbd>7</kbd>

### Proxy

Proxies are obtained from [geonode](geonode.com/free-proxy-list) with the following filters:

1. HTTPS protocol
2. Google passed
3. Low latency
