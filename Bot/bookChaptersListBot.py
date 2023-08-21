from lxml import etree
import requests
import config


def getBookChaptersList(bookUrl):
    bookDetailUrl = config.bookHomepage + bookUrl
    response = requests.get(url=bookDetailUrl, headers=config.apiHeaders)
    htmlRoot = etree.HTML(response.text)
    bookChapters = htmlRoot.xpath('//dd/a')
    bookName = htmlRoot.xpath('//meta[@property="og:novel:book_name"]/@content')[0]
    chapterInfoMap = {}
    for chapter in bookChapters:
        chapterName = chapter.text
        chapterUrl = chapter.get('href')

        if bookUrl not in chapterUrl:
            continue

        chapterCount = chapterUrl.split('/')[-1].split('.html')[0]
        chapterInfoMap[chapterCount] = {
            "chapterName": chapterName,
            "chapterUrl": chapterUrl
        }
    return chapterInfoMap,bookName


def getBookChaptersListByBookId(bookId):
    bookDetailUrl = config.bookHomepage + '/txt/' + str(bookId)
    response = requests.get(url=bookDetailUrl, headers=config.apiHeaders)
    htmlRoot = etree.HTML(response.text)
    bookChapters = htmlRoot.xpath('//dd/a')
    bookName = htmlRoot.xpath('//meta[@property="og:novel:book_name"]/@content')[0]
    chapterInfoMap = {}
    for chapter in bookChapters:
        chapterName = chapter.text
        chapterUrl = chapter.get('href')

        if '/txt/' + str(bookId) not in chapterUrl:
            continue

        chapterCount = chapterUrl.split('/')[-1].split('.html')[0]
        chapterInfoMap[chapterCount] = {
            "chapterName": chapterName,
            "chapterUrl": chapterUrl
        }
    return chapterInfoMap,bookName

if __name__ == '__main__':
    # print(getBookChaptersListMap('/txt/25352/'))
    print(getBookChaptersListByBookId(25531))
