# PyPDF2 是一個輕鬆處理 PDF 檔的套件，提供了讀取、分割、合併、檔案轉換等多種操作。
# PdfFileReader 用來初始化一個 PdfFileReader

from PyPDF2 import PdfFileReader, PdfFileWriter

# 設定讀取 PDF 檔案，獲取 PdfFileReader 物件
readFile = 'E1-1-2-1-input.pdf'
pdfFileReader = PdfFileReader(readFile)
# pdfFileReader = pdfFileReader(open(readFile, 'rd'))

# 獲取與列印 PDF 檔的檔案資訊
documentInfo = pdfFileReader.getDocumentInfo()
print('documentInfo = %s' % documentInfo)
# 獲取與列印頁面配置
pageLayout = pdfFileReader.getPageLayout()
print('pageLayout = %s' % pageLayout)
# 獲取與列印頁模式
pageMode = pdfFileReader.getPageMode()
print('pageMode = %s' % pageMode)
# 從 PDF 檔案根目錄中檢索 XMP 資料
xmpMetadata = pdfFileReader.getXmpMetadata()
print('xmpMetadata = %s' % xmpMetadata)
# 獲取 PDF 檔頁數
pageCount = pdfFileReader.getNumPages()
print('pageCount = %s' % pageCount)
# 返回指定頁編號的 pageObject 並獲取 pageObject 在 PDF 檔案中處於的頁碼
for index in range(0, pageCount):
    pageObj = pdfFileReader.getPage(index)
    print('index = %d, pageObj = %s' % (index, type(pageObj)))
    # <class 'PyPDF2.pdf.PageObject'>
    pageNumber = pdfFileReader.getPageNumber(pageObj)
    print('pageNumber = %s' % pageNumber)
