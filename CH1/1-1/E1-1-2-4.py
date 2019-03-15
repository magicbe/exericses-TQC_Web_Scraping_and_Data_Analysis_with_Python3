import PyPDF2
# 設定需要合併的 PDF 檔案
pdfFiles = ['E1-1-1-1-out0.pdf', 'E1-1-1-1-out1.pdf', 'E1-1-1-1-out2.pdf']
# 獲取 pdfWriter 物件
pdfWriter = PyPDF2.PdfFileWriter()
# 設定合併後寫入的 PDF 檔案
pdfOutput = open('E1-1-2-4-comb.pdf', 'wb')
# 逐一讀取需要合併的 PDF 檔案
for fileName in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(fileName, 'rb'))
    # 取得檔案中每一頁頁面，並加入 pdfWriter 物件
    for pageNum in range(pdfReader.numPages):
        print(pdfReader.getPage(pageNum))
        pdfWriter.addPage(pdfReader.getPage(pageNum))
# 全部保存至檔案中
pdfWriter.write(pdfOutput)
pdfOutput.close()