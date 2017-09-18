import urllib.request
import urllib.error
import re
import os

class NAMES:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.pageIndex = 2
        self.baseUrl = "http://www.thebump.com/b/baby-boy-names-that-start-with-a?page="

    def getPage(self,pageIndex):
        try:
            url = self.baseUrl + str(self.pageIndex)
            request = urllib.request.Request(url = url, headers = self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            # if self.pageIndex == 14:
            #     f = open(str(pageIndex) + '.html', 'w')
            #     f.write(pageCode)
            #     f.close()
            # if self.pageIndex == 17:
            #     f = open(str(pageIndex) + '.html', 'w')
            #     f.write(pageCode)
            #     f.close()
            # print (pageCode)
            return pageCode
        except urllib.error.HTTPError as e:
            if hasattr(e,"reason"):
                print (u"连接失败,",e.reason)
                return None

    def getPageNames(self,pageIndex):
        pageCode = self.getPage(self.pageIndex)
        # <a.*?data-popularity=\"\d+\".*?href=\".*?-baby-name\".*?>(.*?)<\/a>
        pattern = re.compile('<a .*?href=\"\/b\/.*?-baby-name\".*?>(.*?)<\/a>',re.S)
        pageNames = re.findall(pattern,pageCode)
        return pageNames

    def savePageNames(self,pageIndex):
        pageNames = self.getPageNames(pageIndex)
        if pageNames:
            f = open('nameList.txt', 'a')
            for name in pageNames:
                name = name + '\n'
                f.write(name)
        # print (pageNames)
    def setup(self):
        while True:
            if self.pageIndex <= 56:
                print ("正在抓取第 %d 页的names" % (self.pageIndex))
                self.savePageNames(self.pageIndex)
                self.pageIndex += 1
            else:
                break
            

        
a = NAMES()
a.setup()
