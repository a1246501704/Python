\五 属性选择器
#1、作用：根据指定的属性名称找到对应的标签，然后设置属性。
       该选择器，最常用于input标签
 
#2、格式与具体用法：
    [属性名]
    其他选择器[属性名]
    [属性名=值]  # 等于什么
    [属性名^=值] # 以什么开头
    [属性名$=值] # 以什么结尾
    [属性名*=值] # 包含什么


    例1：找到所有有id属性的标签
        [id]
    
    例2：找到所有有id属性的p标签
        p[id]
    
    例3：找到所有class属性值为part1的p标签
        p[class="part1"]
    
    例4：找到所有href属性值以https开头的a标签
        a[href^="https"]
        
    例5：找到所有src属性值以png结尾的img标签
        img[src$="png"]
        
    例6：找到所有class属性值中包含part2的标签
        [class*="part"]
    

# 示例
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>属性选择器</title>

        <style type="text/css">
            [id] {
                color: red;
            }
            p[id] {
                font-size: 30px;
            }
            p[class="part1"] {
                color: green;
            }
            a[href^="https"] {
                font-size: 50px;
            }
            img[src$="png"] {
                width: 100px;
            }
            [class*="part"] {
                text-decoration: line-through;
            }
        </style>
    </head>
    <body>
        <h1 id="id1">哈哈啊</h1>
        <p id="id2">我是段落111</p>
        <p class="part1">我是段落222</p>
        <p class="xxx part2 yyy">我是段落333</p>
        <a href="#">我是我</a>
        <a href="http://www.baidu.com">http://www.baidu.com</a>
        <a href="https://www.baidu.com">https://www.baidu.com</a>
        <img src="1.png" alt="">
        <img src="2.jpg" alt="">
        <p>我是段落444</p>
        <p>我是段落555</p>
    </body>
</html>