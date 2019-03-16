import yaml
data = {
    'name': '王五',
    'age': '22',
    'tag': '學生'
}
'''
可以直接dump到文件或者檔案串流中，
default_flow_style=False 可將檔案中""去除 
allow_unicode=True 可輸出unicode
'''
with open('E1-3-3-2-output.yaml', 'w', encoding='UTF-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)