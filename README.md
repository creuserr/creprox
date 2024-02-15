# creprox: rotating proxy
creprox is an open-source HTTP GET request proxy that utilizes rotating IP origins, useful and commonly used for web scraping purposes. [Try a demo](https://creprox.vercel.app/https:/httpbin.org/ip)

```http
GET https://creprox.vercel.app/https://httpbin.org/ip
```

*POST and other methods will be implemented soon.*

# Usage
To initiate an HTTP GET request, insert your complete URL after `creprox.vercel.app`.

```http
GET https://creprox.vercel.app/https://github.com/creuserr?tab=repositories
```

For details regarding request headers and the proxies used, refer to the response headers:

```http
X-Request-Headers: JSON
X-Request-Proxy: Base-64 JSON
```

*This service heavily utilizes and accredits `requests`, [proxyscrape.com](https://proxyscrape.com), and [proxy-list.download](https://proxy-list.download).*
