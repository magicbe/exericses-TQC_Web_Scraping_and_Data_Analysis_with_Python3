import yaml
with open('E1-3-3-1-input.yaml', encoding='UTF-8') as f:
    list_doc = yaml.load(f)
for sense in list_doc:
    if sense['name'] == 'sense3':
        sense['value'] = 1234
with open('E1-3-3-1-output.yaml', 'w', encoding='UTF-8') as f:
    yaml.dump(list_doc, f)