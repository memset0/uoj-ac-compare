# UOJ 通过题目比较器

### Usage

需要 Python3 及 Flask 和 requests 两个第三方库。运行

```
$ pip3 install flask
$ pip3 install requests
$ python3 server.py
```

打开 `localhost:5000/<你的用户名>/<对方的用户名>` 即可查看比较结果。

##### Values

* `begin`：表示开始比较的题目 ID
* `end`：表示结束比较的题目 ID

##### Examples

* `/memset0/zx2003` 获取 memset0 和 zx2003 做题记录的比较结果
* `/memset0/zx2003?begin=335&end=246` 获取 memset0 和 zx2003 关于清华集训 2017 的做题记录的比较结果

### Demo 

可以打开 [这个](https://memset0.github.io/uoj-ac-compare/demo.htm) 页面查看部署后的效果。这是一个静态的 Demo 页面，在功能进一步完善后 **将很快上线在线的 Demo 页面** 供大家浏览和使用。

![](https://memset0.github.io/uoj-ac-compare/demo.png)