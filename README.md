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
* `except`: 用于指定排除的题目标号

##### Examples

* [`/user/memset0,zx2003,CMXRYNP`](https://uoj.memset0.cn//user/memset0,zx2003,CMXRYNP) 获取 memset0 、 zx2003 和 CMXRYNP 做题记录的比较结果
* [`/user/memset0,zx2003/begin/335/end/346`](https://uoj.memset0.cn/user/memset0,zx2003/begin/335/end/346) 获取 memset0 和 zx2003 关于「清华集训 2017」的做题记录的比较结果
* [`/user/memset0/begin/335/end/346/except/335,345`](https://uoj.memset0.cn/user/memset0/begin/335/end/346/except/335,345) 获取 memset0 的在「清华集训 2017」的做题记录中除了「榕树之心」和「生成树计数」的做题记录

### Demo 

在线 Demo：[uoj.memset0.cn](https://uoj.memset0.cn) 。

请勿滥用或恶意攻击此地址，否则可能会关闭此演示站点。

![](https://memset0.github.io/uoj-ac-compare/demo.png)

### License

GNU v3.