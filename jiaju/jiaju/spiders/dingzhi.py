# -*- coding: utf-8 -*-

import scrapy,time
from jiaju.items import JiajuItem

class DingzhiSpider(scrapy.Spider):
    name = 'dingzhi'
    #allowed_domains = ['https://search.jd.com/']
    baseURL= 'https://search.jd.com/search?keyword=%E5%AE%9A%E5%88%B6%E5%AE%B6%E5%85%B7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E5%AE%9A%E5%88%B6%E5%AE%B6%E5%85%B7&stock=1&page='
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        # 没有用管道，用来存储所有的jj字段
        # jjs = []
        quanbu = response.xpath('//*[@id="J_goodsList"]/ul/li')
        a = 0
        print(len(quanbu))
        for fen in quanbu:
            a +=1
            print(a)
            jj = JiajuItem()
            try:
                if len(fen.xpath('./div/div[3]/strong/i/text()').extract()[0]):
                    jj['jg'] = fen.xpath('./div/div[3]/strong/i/text()').extract()[0]
                else:
                    jj['jg'] =''
                jj['name'] = fen.xpath('./div/div[4]/a/em/text()').extract()[0]
                jj['dz'] = fen.xpath('./div/div[1]/a/@href').extract()[0]
            except:
                print(1111)#这三个打印用了测试的
                time.sleep(5)
                print(fen.xpath('.').extract())
                if len(fen.xpath('./div/div[3]/strong/@data-price').extract()[0]):
                    jj['jg'] = fen.xpath('./div/div[3]/strong/@data-price').extract()[0]
                else:
                    jj['jg'] =''
                jj['name'] = fen.xpath('./div/div[7]/span/a/text()').extract()[0]
                jj['dz'] = fen.xpath('./div/div[7]/span/a/@href').extract()[0]



            # jj['jg'] = jg[0]
            # jj['name'] = name[0]
            # jj['dz'] = dz[0]
            # jjs.append(jj)

            # 返回提取到的每个jj数据，给管道文件处理，同时还会回来继续执行后面的代码（要把jjs注释掉）
            yield jj

        if self.offset < 199:
            self.offset += 2
            url = self.baseURL+str(self.offset)
            yield scrapy.Request(url,callback=self.parse)


