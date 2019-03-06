from urllib import request


class spider():
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(spider.url)
        htmls = r.read()

    def go(self):
        self.__fetch_content()


spider = spider()
spider.go()

#