# 1-3 JSON 讀取與寫入
JSON(JavaScript Object Notation)是源於 JavaScript 的開放資料交換格式，它是 JavaScript 語言的一個子集，若以餐廳的菜單舉例，其形式如下：
```json
{
  "breakfast": {
    "hours": "7-11",
    "items": {
      "breakfastburritos": "$60,
      "pancakes":"$40"
    }
  },
  "lunch": {
    "hours": "11-3",
    "items":{
      "hamburger": "$50"
    }
  },
  "dinner": {
    "hours": "3-10",
    "items": {
      "spaghetti": "$80"
    }
  }
}
```

## 1-3-1 JSON 套件常用方法
通過標準庫中的 json 模組，使用函數 dumps() 與 loads() 進行 json 資料基本讀寫。json.dumps() 是將 Python 中的文件序列化為 json 格式的 str，而 json.loads() 是反向操作，將已編碼的 JSON 字串解碼為 Python 物件。
- Encoding basic Python object hierarchies:
- 範例程式 El-3-1-1.py
- 範例程式 El-3-1-2.py

## 1-3-2 JSON 讀取與寫入

### json.loads
json.loads 用於解碼JSON資料，回傳 Python 的資料類型，用於輸入資料。

#### 語法 

```python
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, panse_constant[, object_pairs_hook[, **kw]]]]]]]]) 
```

json 類型轉換到Python的類型對照表：

JSON | Python 
:---- | :----
object | diet 
array | list 
string | Unicode 
number(int) | int, long 
number(real) | float 
true | True 
false | False 
null | None 

- 範例程式 E1-3-2-1.py
- 範例程式 E1-3-2-2.py

### json.dumps 

jscm.dumps 用於將 Python 物件編碼成 JSON 字串，用於輸出資料。
```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw) 
```

Python | JSON
:---- | :----
diet | object
list, tuple | array
str, Unicode | string
int, long, float | number
True | true
False | false
None null 

- 範例程式 E1-3-2-3.py

## 1-3-3 YAML
YAML (YAML Ain't a Markup Language)是一個可讀性高，用來表達資料康列的格式，語法和其他高階語言類似，並且可以簡單表達清單、雜湊表，純量等資料形態，使用空白符號縮排和大量依賴外觀的特色，特別適合用來表達或編輯資料結構、各種設定檔、傾印除錯内容、檔案大綱。通過標準庫中的yaml模組，使用函數 dumps()與 loads()進行 YAML 資料基本讀寫。yaml.dumps()是將 Python 中的文件序列化為 YAML 格式的 str，而yaml.loads()是反向操作，將已編碼的 YAML 字串解碼為 Python 物件。

### yaml.load 
yaml.loads 用於解碼 YAML 資料，回傳 Python 的資料類型，用於輸入資料。語法與 json 非常類似。
- 範例程式 E1-3-3-1.py

### yaml.dump
yaml.dumps 用於將 Python 物件編碼成 JSON 字串。語法與 json 非常類似。
- 範例程式 E1-3-3-2.py



