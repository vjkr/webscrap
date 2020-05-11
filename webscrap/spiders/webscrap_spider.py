from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from webscrap.items import WebscrapItem
from webscrap.pipelines import WebscrapPipeline


class WebscrapSpider(CrawlSpider):
  name = "webscrap"
  allowed_domains = ["putlocker.bz"]
  start_urls = ["http://putlocker.bz/a-z/"]
  rules = (
    Rule(SgmlLinkExtractor(allow=('f.html', ), deny=('watch*.html', ))),
    Rule(SgmlLinkExtractor(allow=('watch*.html',)), callback='parse_movie'),
  )
  
  def parse_movie(self, response):
    self.log("Hi, this is an item page! %s" % response.url)
  
  def parse_item(self, response):
#    self.log("Hi, this is an item page! %s" % response.url)
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//tr/td')
    items = []
#    for test in sites.select('.//a[contains(@href,"watch")]/@href'):
#      print test.extract()
# http://doc.scrapy.org/en/0.14/topics/selectors.html#scrapy.selector.XPathSelector.re
# Using examples from the above link, extract the title and link to each required object
# 
    for site in sites:
      item = WebscrapItem()
      item['title'] = site.select('a[contains(@href,"watch")]/@title').extract()
      item['link']  = site.select('a[contains(@href,"watch")]/@href').extract()
      items.append(item) # Now, we have the title and link for each object!
#      print title, link
    return items



      
