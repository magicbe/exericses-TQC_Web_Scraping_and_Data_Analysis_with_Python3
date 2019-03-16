# 開啓 data6.csv 檔案，將日期字串中的 '/' 改成 '-'，並另外儲存成 data6_out.csv
import csv
with open('data6.csv', 'r') as fin: # 以讀取模式開啓data6.csv指派給fin物件
    with open('data6_out.csv', 'w', newline='') as fout: # 以寫入模式開啓data6.csv指派給fout物件
        csvreader = csv.reader(fin, delimiter=',') # 將讀取檔案物件fin指派給閱讀器物件csvreader物件，分隔符號指定「,」
        csvwriter = csv.writer(fout, delimiter=',') # 將寫入檔案物件fout指派給寫入器物件csvwriter
        header = next(csvreader) # 迭代取出一行表頭，再印出表頭，與將表頭寫入檔案
        print(header)
        csvwriter.writerow(header)
        for row in csvreader: # 進迴圏逐行讀取資料，每一行曰期字串中的'/'改成'-'，印出資料，使用字串合併的方法join()印出字串，寫入器物件將row的行資料寫入
            row[6] = row[6].replace('/', '-')
            print(','.join(row))
            csvwriter.writerow(row)
