# PdfFileWriter 可以分割寫入 PDF 檔

from PyPDF2 import PdfFileReader, PdfFileWriter

# 設定讀取 PDF 檔案，獲取 PdfFileReader 物件，此處增加宣告 strict = False
# 是因為所讀取 PDF 混用了不同的編碼方式，因此直接讀取發生 error 而無法執行，
# 宣告此一參數將使 error 改為 warning 方式出現，使程式仍能繼續。
readFile = 'E1-1-2-2-input.pdf'
pdfFileReader = PdfFileReader(readFile, strict=False)
# pdfFileReader = PdfFileReader(open(readFile, 'rb'))

# 設定輸出檔案，並獲取 PdfFileWriter 物件。
outFile = 'E1-1-2-3-output.pdf'
pdfWriter = PdfFileWriter()
# 取得讀取檔案的頁數
numPages = pdfFileReader.getNumPages()
# 從第 3 頁之後的頁面，輸出到一個新的檔案中，即分割檔案。添加完每頁，再一起保存至檔案中。
if numPages > 3:
    for index in range(3, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfWriter.addPage(pageObj)
        pdfWriter.write(open(outFile, 'wb'))