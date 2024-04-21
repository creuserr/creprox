> [!NOTE]
> This repository will be upgraded and rationalized soon. <br>
>
> *Stamped at April 21, 2024*

# creprox: rotating proxy
creprox is an open-source HTTP GET request that utilizes rotating IP origins, proxies, and user agents. useful and commonly used for web scraping purposes. [Try a demo](https://creprox.vercel.app/https:/httpbin.org/get)

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

<br>

### Third-party libraries
*This service heavily utilizes and accredits [proxyscrape.com](https://proxyscrape.com) and [proxy-list.download](https://proxy-list.download).*
