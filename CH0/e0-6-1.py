# e0-6-1 自然語言處理
# 載入 jieba 與 jieba.analyse
import jieba
import jieba.analyse

# 把 article.txt 檔案的內容讀出來
f = open('article.txt', 'r', encoding='UTF-8')
article = f.read()

# 透過 jieba 內建的 idf 頻率庫，我們可以計算文章中最重要的字詞
tags = jieba.analyse.extract_tags(article, 10)
print('最重要字詞', tags)