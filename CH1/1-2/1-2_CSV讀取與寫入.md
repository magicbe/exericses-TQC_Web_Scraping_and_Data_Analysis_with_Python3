# 1-2 CSV 讀取與寫入

## 1-2-1 csv 套件常用方法
CSV 檔案格式是以逗號隔開欄位資料 (commaseparatedvalue，CSV) 的文字檔格式，
是資料庫與 excel 檔案之間資料匯入匯出最常用的檔案格式。csv 模組可以實現對
csv 檔案的存取，但目前已不限用逗號隔開，可依欄位分隔字元 (delimiter) 與識別
資料内容的引號 (quoting) 讀寫 csv 檔。常用的 csv 套件常用的方法見表1-2-1。

##### 表1-2-1 csv套件常用的方法
方法 | 功能說明
:---- | :----
csv.reader(csvfile, dialect = 'excel', **fmtparams) | 從csvfile讀取的每行都作為字串串列回傳給一個可迭代的閱讀器物件，dialect參數可用來定義採用其他分隔符號的方言，預設為excel。
csv.writer(csvlile, dialect = 'excer, **fmtparams) | 傳回一個寫入器物件，dialect參數用法同上。
next() | 取出閱讀器物件内下一列元素。
writerow(row) | 將row參數傳給寫入器物件，寫入csv檔案。

## 1-2-2 csv 讀取
CSV 檔的讀取，只要呼叫 CSV 模組的 reader 方法即可達成
- 範例程式 E1-2-2-1.py
- 範例程式 E1-2-2-2.py

## 1-2-3 csv 寫入
CSV 檔寫入只要呼叫 CSV 模組的 writer 方法即可達成
- 範例程式 E1-2-3-1.py