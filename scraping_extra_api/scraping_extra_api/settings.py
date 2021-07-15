# Scrapy settings for scraping_extra_api project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scraping_extra_api'

SPIDER_MODULES = ['scraping_extra_api.spiders']
NEWSPIDER_MODULE = 'scraping_extra_api.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Database specification
# MONGODB_CONNECTION = 'mongodb+srv://m001-student:m001-stundet-basics@sandbox.jspgt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# MONGODB_DB = "db_scraping_extra"
# MONGODB_COLLECTION = "productsAndReviews"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 10
RETRY_TIMES = 0
RETRY_ENABLED = False
# REDIRECT_ENABLED = False
DOWNLOAD_TIMEOUT = 15
LOG_LEVEL = 'INFO'
AJAXCRAWL_ENABLED = True
# PROXY
# PROXY = 'http://127.0.0.1:8888/?noconnect'
# PROXY = 'http://127.0.0.1:8888/'

# SCRAPOXY
# API_SCRAPOXY = 'http://127.0.0.1:8889/api'
# API_SCRAPOXY_PASSWORD = 'scraping_extra'
# ROTATING_PROXY_LIST = [
# 	'123.200.20.242:58847',
# 	'52.251.88.114:80',
# 	'200.39.154.1:999'
# 	# '51.222.123.204:9300',
# 	# '51.222.123.205:9300',
# 	# '51.222.123.196:9300',
# 	# '51.222.123.201:9300',
# 	# '51.222.123.192:9300',
# 	# '51.222.17.143:9300',
# 	# '51.222.123.215:9300',
# 	# '51.222.17.170:9300',
# 	# '51.222.121.248:9300',
# 	# '167.172.132.136:9300',
# 	# '51.222.123.213:9300',
# 	# '157.65.167.24:3128'
# 	# '64.235.204.107:8080',
# 	# '51.222.123.217:9300',
# 	# '51.222.123.191:9300',
# 	# '149.56.47.194:3128',
# 	# '51.222.123.202:9300',
# 	# '51.161.81.69:9300',
# 	# '51.222.121.242:9300',
# 	# '51.222.123.209:9300',
# 	# '51.222.123.212:9300',
# 	# '51.222.121.243:9300',
# 	# '51.222.123.216:9300',
# 	# '51.222.123.198:9300',
# 	# '174.142.69.0:13636',
# 	# '51.222.123.210:9300',
# ]

# DOWNLOADER_MIDDLEWARES = {
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
# }

# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
#     'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
#     'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
# }

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scraping_extra_api.middlewares.ScrapingExtraApiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scraping_extra_api.middlewares.ScrapingExtraApiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'scraping_extra_api.pipelines.MongoDBPipeline': 0}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
