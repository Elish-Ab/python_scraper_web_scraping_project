# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass



class BookItem(scrapy.Item):
    url =  scrapy.field()
    title =  scrapy.field()
    upc =  scrapy.field()
    product_type =  scrapy.field()
    price_excl_tax =  scrapy.field()
    price_incl_tax =  scrapy.field()
    tax =  scrapy.field()
    availability =  scrapy.field()
    num_reviews =  scrapy.field()
    stars =  scrapy.field()
    category =  scrapy.field()
    description =  scrapy.field()
    price =  scrapy.field()
