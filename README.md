# UOJ 通过题目比较器

### Usage

需要 Python3 及 Flask 和 requests 两个第三方库。运行

```
$ pip3 install flask
$ pip3 install requests
$ python3 server.py
```

### Route

##### Values

每个参数部分由参数名和参数值构成，在 URL 中依次给定参数名和参数值，之间用逗号分隔即可

* `user`：用于给定若干用户名，不同用户名之间用逗号分隔
* `begin`：用于指定起始比较的题目标号
* `end`：用于指定结束比较的题目标号

##### Examples

* `/user/memset0,zx2003,CMXRYNP` 获取 memset0 、 zx2003 和 CMXRYNP 做题记录的比较结果
* `/user/memset0,zx2003/begin/335/end/346` 获取 memset0 和 zx2003 关于清华集训 2017 的做题记录的比较结果

### Demo 

可以打开 [这个](https://memset0.github.io/uoj-ac-compare/demo.htm) 页面查看部署后的效果。这是一个静态的 Demo 页面，在功能进一步完善后 **将很快上线在线的 Demo 页面** 供大家浏览和使用。

![](https://memset0.github.io/uoj-ac-compare/demo.png)

### License

GNU v3.