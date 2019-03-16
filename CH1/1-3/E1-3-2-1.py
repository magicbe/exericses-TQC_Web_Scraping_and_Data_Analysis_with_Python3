import json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}'
text = json.loads(jsonData) # 現在反過來使用loads()把JSON字串menu_json解析成Python的資料結構。
print(text)