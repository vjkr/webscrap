# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class WebscrapPipeline(object):
    def process_item(self, item, spider):
      if item['title']:
        return item
      else:
        raise DropItem("Missing title in %s" % item)


from scrapy.contrib.exporter import JsonLinesItemExporter

class JsonWriterPipeline2(object):
  def _init_(self):
    self.fields_to_export = [
      'title',
      'link'
    ]
    dispatcher.connect(self.spider_opened, signals.spider_opened)
    dispatcher.connect(self.spider_closed, signals.spider_closed)
  
  def spider_opened(self,spider):
    self.jsonlines_exporter = JsonLinesItemExporter(open(spider.name+".linejson", "w"), fields_to_export=self.fields_to_export)
    self.jsonlines_exporter.start_exporting()

  def process_item(self,item,spider):
    self.jsonlines_exporter.export_item(item)
    return item
  def spider_closed(self, spider):
    self.jsonlines_exporter.finish_exporting()


import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
