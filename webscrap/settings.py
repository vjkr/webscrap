# Scrapy settings for webscrap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'webscrap'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['webscrap.spiders']
NEWSPIDER_MODULE = 'webscrap.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = [
  'webscrap.pipelines.WebscrapPipeline',
  'webscrap.pipelines.JsonWriterPipeline'
]
