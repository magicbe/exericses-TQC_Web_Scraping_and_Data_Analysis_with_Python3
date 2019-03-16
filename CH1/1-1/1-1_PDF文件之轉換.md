# 1-1 PDF 文件之轉換
Python 處理 PDF 的套件非常多，最常用的 pdfkit、PyPDF2、pdfminer。

## 1-1-1 pdfkit
Python 中將 HTML 轉成 PDF 的套件。使用前，要先安裝 wkhimltopdf，
以 Windows 環境為例，需先進入 [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html) 下載並安裝。
```python
pip install pdfkit
```
[https://pypi.org/project/pdfkit/](https://pypi.org/project/pdfkit/)

## 1-1-2 PyPDF2 

PyPDF2 是一個輕鬆處理 PDF 檔的套件，提供了讀取、分割、合併、檔案轉換等多種操作。 
```python
pip install PyPDF2
```
[https://pypi.org/project/PyPDF2/](https://pypi.org/project/PyPDF2/)

## 1-1-3 pdfminer 
PDFMiner 是一個可以從PDF檔案中提取資訊的工具，注重的是獲取和分析文字資料，允許獲取某一頁中文字的準確位置和一些諸如字體、行數的資訊。包括可以把 PDF 檔轉換成 HTML 等格式（但不能直接看）的 PDF 轉換器、可以用於除文字分析以外其他用途的 PDFParser（檔案分析器）、PDFDocument（檔案物件）、PDFResourceManager（資源管理器）、PDFPagelnterpreter（解譯器）、PDFPageAggregator（聚合器）與 LAParams（參數分析器）。轉換的整體思維是先建構檔案物件，接著利用 PDFParser 解析檔案物件，然後提取所需内容。
```python
pip install pdfminer3k
```
[hhttps://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/591510/](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/591510/)

## 1-1-4 txt 檔案讀取 
Python 有關檔案類別的定義在内置模組中，可直接使用内置函式完成檔案的操作。
##### A .打開文件 
使用 open 函式打開一個檔案，回傳一個檔案物件，函式格式為
```python
open(file, mode = 'r', ...） 
```
參數 file 表示打開檔案的檔案名，參數 mode 表示打開檔案的方式，可用的控制字元如表所示。 

mode|解釋 
----|:----
r|以唯讀方式打開 
w|以寫入方式開檔，當這個檔案存在時，覆蓋原來的内容：當這個檔案不存在時，建立這個檔案
X|建立一個新檔案，以寫入方式開檔，當檔案已存在，回報錯誤 FileExistsError
a|以寫入方式開檔，寫入内容追加在檔案的末尾
b|表示二進位檔案，添加在其他控制字元後
t|表示文字檔案，預設値
+|以修改方式打開，支援讀寫

mode 預設為 r 表示唯讀，w/x/a 則表示可以寫入，b/t/+ 是修飾符號，添加在 r/w/x/a 之後，例如：
- rb 表示以唯讀方式打開一個二進位檔案
- sr+ 表示以修改方式打開一個文字檔案
- rb+表示以修改方式打開一個二進位檔案

例如建立一個在 C 槽 sample 目錄下的 test.txt 檔案，回傳由程式師命名的使用者識別項檔案物件 f，之後就可以使用 f 呼叫方法操作檔案。 
```python
f = open ("c:\\sample\test.txt","w") 
```
其中第一個參數是檔案名稱，其中路徑的分隔符號\需要轉義，用兩個 \\ 表示。如在當前程式目錄下打開，只需寫 "test.txt"。第二個參數是開檔模式 mode，上面例子中是以寫入方式打開文字檔，如果檔案不存在，則自動建立檔案。

##### B .關閉檔案 
檔案操作完畢關閉檔案，可釋放分配給檔案的系統資源，供其他檔案使用。可以呼叫檔案物件的 close 方法來關閉檔案，呼叫格式為
```python
<檔案物件>.close()
```
例如，打開一個檔案的檔案物件為 f，使用結束後關閉檔案。
```python
f.close()
```

## 1-1-5 txt 檔案寫入
文字檔讀取與寫入