import os

currentAbspath = os.path.abspath(__file__)
rootPath = os.path.abspath(os.path.join(currentAbspath, os.pardir))

bookHomepage = "https://www.bqg335.com"

apiHeaders = {
    'authority': 'www.bqg335.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Hm_lvt_5d5aa19afa19be9ba1b757fdac0b33df=1692584203; Hm_lpvt_5d5aa19afa19be9ba1b757fdac0b33df=1692584758; hm=9d7d0f2d286dc9e44bb6ca38189cbff9',
    'referer': 'https://www.bqg335.com/s?q=%E5%87%A1%E4%BA%BA',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

queryBookByNameApi = "https://www.bqg335.com/user/search.html"


