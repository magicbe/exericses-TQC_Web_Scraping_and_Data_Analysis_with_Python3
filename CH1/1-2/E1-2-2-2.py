'''
全國環境輻射偵測即時資訊
主要欄位說明：監測站，監測站(英文)，監測値(微西弗/時)，時間，GPS 經度
，GPS 緯度
'''
import csv
# 唯讀方式開啓'E1-2-2-2-input.csv'，編碼方式為'utf8',並設定為csvfile物件。
with open('E1-2-2-2-input.csv', 'r', encoding='UTF-8') as csvfile:
    # 呼叫csv模組的reader方法讀取csvfile物件，間隔符號為逗號，讀取内容設定給plots物件（此為串列物件）。
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0] + ' ' + row[2] + ' ' + row[3])