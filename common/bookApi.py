import json
import time

import requests
import config


class bookApi:
    @staticmethod
    def queryBookByName(name: str):
        param = {
            'q': name,
        }
        bookInfoMap = {}
        jsonResponse = 1
        for _ in range(3):
            response = requests.get(url=config.queryBookByNameApi, params=param,headers=config.apiHeaders)
            # print(response.text)
            jsonResponse = json.loads(response.text)
            if jsonResponse == 1:
                time.sleep(1)
                continue
            else:
                break
        if jsonResponse == 1:
            return {}
        for bookInfo in jsonResponse:
            bookInfoMapKey = str(bookInfo["articlename"]) + " 作者:" + str(bookInfo["author"])
            bookInfoMap[bookInfoMapKey] = bookInfo
        return bookInfoMap


if __name__ == '__main__':
    print(bookApi.queryBookByName("凡人"))
