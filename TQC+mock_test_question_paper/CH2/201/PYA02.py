# 載入模組
import requests
import re

url = 'http://tqc.codejudger.com:3000/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == requests.codes.OK:
    # 欲搜尋的字串
    pattern = input("請輸入欲搜尋的字串 : ")
    name = re.findall(pattern, htmlfile.text)
    if pattern in htmlfile.text:
        print(pattern, "搜尋成功")
        print(pattern, "出現 %d 次" % len(name))
    else:
        print(pattern, "搜尋失敗")
        print(pattern, "出現 0 次")
else:
    print("網頁下載失敗")
