import yaml

def getlink():
    with open('config.yaml') as config:
        data = yaml.safe_load(config)
        return [data['link']['category'],data['link']['page']]

def getpath():
    with open('config.yaml') as config:
        data = yaml.safe_load(config)
        return data['storagepath']['path']

def update_category(category):
    config = open('config.yaml','r')
    data = yaml.safe_load(config)
    data['link']['category'] = category
    with open('config.yaml','w') as config:
        yaml.safe_dump(data,config)

def update_pageno(pageno):
    config = open('config.yaml', 'r')
    data = yaml.safe_load(config)
    data['link']['page'] = pageno
    with open('config.yaml', 'w') as config:
        yaml.safe_dump(data, config)

if __name__ == '__main__':

    update_pageno(10)
    print(getlink())