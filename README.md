# scrapy
Python3 爬虫模块。

## 环境准备
### 启动 Selenium Remote 容器
```bash
docker run -d \
  --name selenium \
  --restart=unless-stopped \
  --ulimit nofile=32768:32768 \
  -p 4444:4444 \
  -p 7900:7900 \
  -e SE_VNC_PASSWORD="TestForRabbirScrapy" \
  -e SE_NODE_SESSION_TIMEOUT=180 \
  -e SE_NODE_MAX_SESSIONS=2 \
  -e SE_SCREEN_WIDTH=1920 \
  -e SE_SCREEN_HEIGHT=1080 \
  --shm-size="2g" \
  selenium/standalone-chrome:latest
```
```bash
docker stop selenium && docker rm selenium
```

## 可选的方案
- `scrapy`
    > 可用 `requests` 代替。
- `selenium`（获取 `cookies`）+ `scrapy`
    > 适用于需要登录的网站。
- `scrapy` + <u>`selenium`</u>(Downloader Middleware)
    > 适用于反爬稍微严格的网站。
- `scrapy` + <u>`selenium` + `undetected-chromedriver`</u>(Downloader Middleware)
    > 适用于反爬严格的网站。
- `scrapy` + <u>`selenium` + AdsPower 指纹浏览器</u>(Downloader Middleware)
    > 适用于反爬非常严格的网站。

## 资源
### 浏览器信息检测
- [https://www.browserscan.net/bot-detection](https://www.browserscan.net/bot-detection)
- [https://bot.sannysoft.com](https://bot.sannysoft.com)
- [https://ipinfo.io/](https://ipinfo.io/)

### Selenium 官方仓库
- [https://github.com/SeleniumHQ/docker-selenium](https://github.com/SeleniumHQ/docker-selenium)

### Selenium 第三方增加
- [https://github.com/markmelnic/stealthenium](https://github.com/markmelnic/stealthenium)
- [https://github.com/diprajpatra/selenium-stealth](https://github.com/diprajpatra/selenium-stealth)

### Cloudflare R2 验证
- [https://2captcha.com/2captcha-api](https://2captcha.com/2captcha-api)

### 其他浏览器操作
- [https://github.com/ultrafunkamsterdam/undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

### 相关文章
- [如何防止 Selenium 被检测](https://blog.browserscan.net/zh/docs/how-to-avoid-selenium-detection?search=1)

### 相关问答
- [Python Selenium AWS Lambda 更改 WebGL 供应商/渲染器以获取无法检测到的无头刮刀](https://devpress.csdn.net/python/630110d67e66823466197826.html)
