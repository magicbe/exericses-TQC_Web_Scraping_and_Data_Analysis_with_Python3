# pdfkit 是一個在 Python 中將 HTML 轉成 PDF 的套件，使用前，要先安裝 wkhtmltopdf，
# 以 Windows 環境為例，需先進入 https://wkhtmltopdf.org/downloads.html 下載安裝。

import pdfkit

# 指定 wkhtmltopdf.exe 的安裝路徑
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# 從網路抓取網頁轉換成 PDF
pdfkit.from_url('https://www.csf.org.tw/main/index.asp', 'E1-1-1-1-out0.pdf', configuration=config)
# 字串轉換成 PDF
pdfkit.from_string('Hello World!', 'E1-1-1-1-out1.pdf', configuration=config)
# 本地 Html 轉換成 PDF
pdfkit.from_file('電腦技能基金會.html', 'E1-1-1-1-out2.pdf', configuration=config)