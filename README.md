# creprox
`creprox` is an open-source HTTP GET and POST requesting tool that utilizes rotating IP origins, and user agents. useful and commonly used for web scraping purposes and unlimited public rest api access.

<p align="center"><a href="https://creprox.vercel.app/https:/api.github.com/users/creuserr"><kbd>Try a demo :large_blue_circle:</kbd></a></p>

```http
GET https://creprox.vercel.app/https://httpbin.org/get
POST https://creprox.vercel.app/https://httpbin.org/post
```

# Usage
To initiate an HTTP GET/POST request, insert your complete URL after `creprox.vercel.app`.

```http
GET https://creprox.vercel.app/<URL>
POST https://creprox.vercel.app/<URL>
```

For details regarding request headers, user agent, and proxies used, refer to the response headers:

```http
X-Response-Headers: JSON
X-Request-UA: String
```

# Troubleshooting

1. **Trouble on URL format** <br>
   This can be triggered due to the protocol of your URL. If your URL is like this:
   ```
   https://creprox.vercel.app/https://...
   ```
   Try replacing `https://` with `https:/`
   ```
   https://creprox.vercel.app/https:/...
   ```

# Third-party
Credits to [proxyscrape.com](https://proxyscrape.com) and [proxy-list.download](https://proxy-list.download) for providing proxy servers.
