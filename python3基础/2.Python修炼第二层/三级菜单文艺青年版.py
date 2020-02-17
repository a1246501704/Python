menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}



#part1（初步实现）：能够一层一层进入
layers = [menu, ]

while True:
    current_layer = layers[-1]
    for key in current_layer:
        print(key)

    choice = input('>>: ').strip()
    if choice not in current_layer:
        continue
    layers.append(current_layer[choice])



#part2（改进）：加上退出机制
layers=[menu,]

while True:
    if len(layers) == 0:
        break
    current_layer=layers[-1]
    for key in current_layer:
        print(key)

    choice=input('>>: ').strip()

    if choice == 'b':
        layers.pop(-1)
        continue
    if choice == 'q':
        break
    if choice not in current_layer:
        continue
    layers.append(current_layer[choice])