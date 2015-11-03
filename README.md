# TXT2MD(中文/[ENG](https://github.com/chenbotao828/txt2md#txt2mdenglish))

这是一个 Python 3 的脚本,将TXT文件,根据文本内容转换为Markdown格式.

### 如何运行

```
python cvt.py <type> <path>
```

例如 :

```
python cvt.py "GB" "C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\GB50096-2011"'
```

### 如何准备 

>+ 安装下载Python3.X,Windows可能需要设置Path 
> 
>+ Windows下,可能需要添加系统路径
> 
>+ 下载TXT2MD
> 
>+ 设置转换设定
> 
>+ 将需要转换的TXT文件放入一个文件夹. TXT可以是PDF经过ORC转换生成,中文推荐使用汉王ORC.
> 
>+ 运行!

### 如何设置配置 

`config`文件夹中是设置文件,其中一种为文档类型设置,例如`GB`,一种为单页类型设置,例如`GB_ZW`.可以根据样例来设置自己的配置文件.

# TXT2MD(English)

A Python 3 script converting TXT files to Markdown files .

###  How to run 

```
python cvt.py <type> <path>
```

For example :

```
python cvt.py "GB" "C:\\Users\\Administrator\\Documents\\GitHub\\txt2md\\test_sample\\GB50096-2011"
```

### How to prepare  

>+ Download and setup Python3.X
> 
>+ Set system Path , when using Windows platform.
> 
>+ Download TXT2MD to your computer
> 
>+ Set config file
> 
>+ Move TXT file to a folder.The TXT file may be converted by ORC from PDF
> 
>+ Run !

### How to set config

In `config` folder,there are two kinds of config file,one is document type file, another is single chapter type file, such as `GB` and `GB_ZW`. You can make your own config file according to examples .


# License

The MIT License (MIT)

Copyright (c) 2015 Chen Botao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

