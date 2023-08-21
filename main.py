import random
import time

from common.bookApi import bookApi
from Bot.bookChaptersListBot import getBookChaptersList, getBookChaptersListByBookId
from Bot.bookChapterContentBot import getBookChapterContent, saveBookChapterContent

while True:
    print('****************************')
    print('欢迎进入笔趣阁图书txt下载系统！')
    print('****************************')
    print('1.进行图书下载 2.退出系统')
    # 获取用户操作
    choose = input('请进行您的操作：')
    # 非法操作
    if choose not in ['1', '2']:
        print('输入错误！')

    # 用户进入指定图书下载
    elif choose == '1':
        while True:
            print('****************************')
            print('1.查询图书 2.下载指定图书 3.退出系统')
            # 获取用户操作
            choose = input('请进行您的操作：')
            # 非法操作
            if choose not in ['1', '2', '3']:
                print('输入错误！')
            elif choose == '1':
                name = input("请输入需要查询的图书名/作者名：")
                queryResult = bookApi.queryBookByName(name)
                if queryResult == {}:
                    print("查询结果为空,请重新输入")
                    continue
                topResult = list(queryResult.keys())[:10]
                print("查询结果如下")
                for index in range(len(topResult)):
                    print("{}  {}".format(index, topResult[index]))

                chooseNameIndex = int(input("请输入需要下载的图书序号："))
                chooseBookInfo = queryResult[topResult[chooseNameIndex]]
                bookChaptersListMap, bookName = getBookChaptersList(chooseBookInfo["url_list"])
                chooseNameIndex = int(input("总章节:{}, 请输入开始下载章节号:".format(len(bookChaptersListMap.keys()))))
                if chooseNameIndex > len(bookChaptersListMap.keys()):
                    break
                print("开始下载。。。")
                for chapterInfoKey in list(bookChaptersListMap.keys())[chooseNameIndex - 1:]:
                    startTime = time.time()
                    chapterValue = bookChaptersListMap[chapterInfoKey]
                    chapterContent = getBookChapterContent(chapterName=chapterValue["chapterName"],
                                                           chapterUrl=chapterValue["chapterUrl"])
                    saveBookChapterContent(bookName=bookName, chapterContent=chapterContent)
                    print("成功下载第:{}章 耗时:{}".format(chapterInfoKey, time.time() - startTime))
                    time.sleep(random.uniform(0.1, 1.0))
            elif choose == '2':
                chooseBookId = input("请输入图书的Id:")
                bookChaptersListMap, bookName = getBookChaptersListByBookId(chooseBookId)
                chooseNameIndex = int(input("总章节:{}, 请输入开始下载章节号:".format(len(bookChaptersListMap.keys()))))
                if chooseNameIndex > len(bookChaptersListMap.keys()):
                    break
                print("开始下载。。。")
                for chapterInfoKey in list(bookChaptersListMap.keys())[chooseNameIndex - 1:]:
                    startTime = time.time()
                    chapterValue = bookChaptersListMap[chapterInfoKey]
                    chapterContent = getBookChapterContent(chapterName=chapterValue["chapterName"],
                                                           chapterUrl=chapterValue["chapterUrl"])
                    saveBookChapterContent(bookName=bookName, chapterContent=chapterContent)
                    print("成功下载第:{}章 耗时:{}".format(chapterInfoKey, time.time() - startTime))
                    time.sleep(random.uniform(0.1, 1.0))
            elif choose == '3':
                break
    # 退出系统
    elif choose == '2':
        break
