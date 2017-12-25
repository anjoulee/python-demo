# -*- coding: utf-8 -*-
from com.spider.baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    ###构造方法
    def __init__(self):
        self.urls = url_manager.UrlManger()  ###URL管理器
        self.downloader = html_downloader.HtmlDownloader()  ###下载器
        self.parser = html_parser.HtmlParser()  ###解析器
        self.outputer = html_outputer.HtmlOutputer()  ###输出搜集器

    ###爬取方法
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  ###URL管理器
        ###爬取循环
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  ###获取一个待爬虫的URL
                print 'craw %d : %s ' % (count, new_url)  ###记录当前爬取第几个URL，爬取的是哪个地址
                html_cont = self.downloader.download(new_url)  ###下载器：下载URL的内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)  ###解析器：解析新的URL和新的数据
                self.urls.add_new_urls(new_urls)  ###URL添加到URL管理器
                self.outputer.collect_data(new_data)  ###搜集数据

                if count == 1000:  ###爬取1000次结束
                    break
                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()

    obj_spider.craw(root_url)
