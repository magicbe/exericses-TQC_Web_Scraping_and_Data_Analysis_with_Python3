from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
# 開始解析與獲取所需資訊。
def parse():
    fn = open('E1-1-2-2-input.pdf', 'rb') # 以二進位元讀取模式打開本機 PDF 檔案
    parser = PDFParser(fn) # 創建一個PDF檔案分析器。
    doc = PDFDocument() # 創建一個PDF檔案。
    parser.set_document(doc) # 連接分析器與檔案物件。
    doc.set_parser(parser)
    doc.initialize('') # 提供初始化密碼，如果沒有密碼就創建一個空的字串。
    # 檢測檔案是否提供txt 轉換，不提供就忽略。
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        resource = PDFResourceManager() # 創建PDF資源管理器。
        laparams = LAParams() # 創建一個PDF參數分析器。
        device = PDFPageAggregator(resource, laparams=laparams) # 創建聚合器，用於讀取檔案的物件。
        interpreter = PDFPageInterpreter(resource, device) # 創建解譯器，對檔案編碼，解釋成 Python能夠識別的格式。
        for page in doc.get_pages(): # doc.get_pages() 獲取 page 列表，然後用迴圈遍歷清單，每次處理一頁的内容。
            interpreter.process_page(page) # 利用解譯器的 process_page() 方法解析讀取單獨頁數。
            layout = device.get_result() # 使用聚合器的 get_result()方法獲取内容。
            for out in layout: # layout 是一個 LTPage 物件，裡面存放著這個 page 解析出的各種物件，利用迴圏來遍歷。
                if hasattr(out, 'get_text'): # 判斷是否含有 get_text() 方法，獲取我們想要的文字，然後採用附加方式寫入 txt 檔案。
                    with open('E1-1-3-output.txt', 'a', encoding='UTF-8') as f:
                        f.write(out.get_text()+'\n')
# 呼叫 parse()
if __name__ == '__main__':
    parse()

