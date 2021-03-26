# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from pprint import pprint


class FlashbotSpider(scrapy.Spider):
    name = 'flashbot'
    allowed_domains = ['rss.jobsearch.monster.com']

    # Start the crawler at this URLs
    start_urls = ['file:///home/olivier/Documents/Briefes/20201112_Brief_Moteur_Recherche_Emploi/rssquery.ashx']
    #start_urls = ['http://rss.jobsearch.monster.com/rssquery.ashx?q={query}']

    #thesaurus = ["machine learning", "machine", "learning", "big data", "big", "data"]
    thesaurus = ["machine learning"]

    LOG_LEVEL = "INFO"

    def parse(self, response):

        # We stat with this url
        url = self.start_urls[0]

        # Build and send a request for each word of the thesaurus
        for query in self.thesaurus:
            target = url.format(query=query)
            print("fetching the URL: %s" % target)
            if target.startswith("file://"):
                r = Request(target, callback=self.scrapit, dont_filter=True)
            else:
                r = Request(target, callback=self.scrapit)
            r.meta['query'] = query
            yield r

    def scrapit(self, response):
        query = response.meta["query"]

        # Scrap the data
        for doc in response.xpath("//item"):
            # Base item with query used to this response
            item = {"query": query}

            item["title"] = doc.xpath("title/text()").extract()
            item["description"] = doc.xpath("description/text()").extract()
            item["link"] = doc.xpath("link/text()").extract()
            item["pubDate"] = doc.xpath("pubDate/text()").extract()
            item["guid"] = doc.xpath("guid/text()").extract()
            #pprint(item, indent=2)
            print("item scraped:", item["title"])
            yield item
