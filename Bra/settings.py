# -*- coding: utf-8 -*-

BOT_NAME = 'Bra'

SPIDER_MODULES = ['Bra.spiders']
NEWSPIDER_MODULE = 'Bra.spiders'


ROBOTSTXT_OBEY = False

#request 线程数量
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 10000
CONCURRENT_REQUESTS_PER_IP = 0

#retry
RETRY_ENABLED = True
RETRY_TIMES = 100
DOWNLOAD_TIMEOUT = 10 #下载超时时间

#输出文件路径
FEED_URI = 'ABCD.json'
#FEED_FORMAT = 'json'
FEED_EXPORT_ENCODING = 'utf-8'

