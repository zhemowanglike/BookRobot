import os

import config
from lxml import etree
import requests


def getBookChapterContent(chapterName, chapterUrl):
    chapterDetailUrl = config.bookHomepage + chapterUrl
    response = requests.get(url=chapterDetailUrl, headers=config.apiHeaders)
    htmlRoot = etree.HTML(response.text)
    chapterContent = htmlRoot.xpath('//div[@id="chaptercontent"]/text()')
    for index in range(len(chapterContent)):
        chapterContent[index] = chapterContent[index].replace(u'\u3000', u'')

    chapterContent.insert(0, chapterName)
    return chapterContent


def saveBookChapterContent(bookName, chapterContent):
    with open(os.path.join(config.rootPath, "Download", bookName + ".txt"), "a+", encoding="utf-8") as saveContent:
        for content in chapterContent:
            saveContent.write(content)
            saveContent.write("\n")
        saveContent.write("\n")


if __name__ == '__main__':
    bookContent = getBookChapterContent("1", '/txt/25352/1663.html')
    saveBookChapterContent("test", bookContent)
