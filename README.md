# ronfedata

## step 1 
注意区分脚本，有些需要在mongo shell里跑，有些需要在robomongo里跑
在每个文件开头第一行会标明

## step 2
在执行robomongo的脚本前，最好使用mongodump，筛选出需求范围的数据，points表真的很慢
筛选方法：

```
 mongodump --db yangcong-prod25 --collection points --query '{"createdBy": {"$gt": ISODate("2015-09-06T00:00:00.367Z"), "$lt": ISODate("2015-09-15T00:00:00.367Z") } }' --out ./dataRange
```

## step 3
筛选出来的数据，用mongorestore恢复到本地作为靶场, 最好先进入存放筛选后的文件夹重命名一下表名

```
 mongorestore --host localhost --port 27017 ./dataRange
```

## step 4

### 4.1 择取脚本landingPageCalc.js
分两部分，第一部分计算mobile端pv uv数据，需修改输入如下：

```
var input = [
    {
        startDate : ISODate("2015-09-07T00:00:00.367Z"),
        endDate : ISODate("2015-09-08T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
        from: "mobile"
    },
    {
        startDate : ISODate("2015-09-08T00:00:00.367Z"),
        endDate : ISODate("2015-09-09T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
        from: "mobile"
    },
    {
        startDate : ISODate("2015-09-09T00:00:00.367Z"),
        endDate : ISODate("2015-09-10T00:00:00.367Z"),
        qudao: ["twyxyandroid","twyxyios","bjxxt"],
        from: "mobile"
    }
    ...........
    ...........
    ...........
    ...........
]
```

第二部分计算pc端，修改输入数据如下：

```
var inputPc = [
    {
        startDate: ISODate("2015-09-07T00:00:00.367Z"),
        endDate: ISODate("2015-09-08T00:00:00.367Z"),
        qudao: ["lzx", "bjxxt", "fywk", "cyxt", "twsm", "twsmcce", "sem1", "sem2", "seo1"],
        from: "pc"
    },
    {
        startDate: ISODate("2015-09-08T00:00:00.367Z"),
        endDate: ISODate("2015-09-09T00:00:00.367Z"),
        qudao: ["lzx", "bjxxt", "fywk", "cyxt", "twsm", "twsmcce", "sem1", "sem2", "seo1"],
    ,    from: "pc"
    },
    {
        startDate: ISODate("2015-09-09T00:00:00.367Z"),
        endDate: ISODate("2015-09-10T00:00:00.367Z"),
        qudao: ["lzx", "bjxxt", "fywk", "cyxt", "twsm", "twsmcce", "sem1", "sem2", "seo1"],
        from: "pc"
    },
    ............
    ............
    ............
    ............
]
```

### 4.2 编码类型转换
粘贴修改好的脚本到robomongo执行，将计算结果(两段文本)贴入当前目录某一文本文件,比如`data.txt`
打开脚本`transferUrlSendMail.py`,找到邮件发信部分，修改发信设置。
```
    server = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    username = "xingze@guanghe.tv"
    password = "looploop"
    fromaddr = "xingze@guanghe.tv"
    toaddrs = "xingze@guanghe.tv"
```
修改完成后执行脚本：

```
    $ python transferUrlSendMail.py data.txt
```
邮箱查收数据即可。

## step 5
在robomongo执行`mobileHomePage.js`计算移动端首页PV

## step 6
在robomongo执行`calMobileHomeDownloadBtn.js`计算移动端首页下载按钮PV

## step 7
进入文件夹`pcHomePage`，计算带q进入首页的数据
首先修改`funnel_have_q.js`的dateRange数组限定时间范围

```
dateRange = [
    {
        startDate: ISODate("2015-09-07T00:00:00.007Z"),
        endDate: ISODate("2015-09-08T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-08T00:00:00.007Z"),
        endDate: ISODate("2015-09-09T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-09T00:00:00.007Z"),
        endDate: ISODate("2015-09-10T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-11T00:00:00.007Z"),
        endDate: ISODate("2015-09-12T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-12T00:00:00.007Z"),
        endDate: ISODate("2015-09-13T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-13T00:00:00.007Z"),
        endDate: ISODate("2015-09-14T00:00:00.007Z")
    },
    {
        startDate: ISODate("2015-09-07T00:00:00.007Z"),
        endDate: ISODate("2015-09-14T00:00:00.007Z")
    }
];
```

之后修改`funnel_have_q.sh`的渠道信息

```
    qList="sem1 sem2 seo1 lzx bjxxt fywk cyxt twsm twsmcce"
    
```

一切完成后执行这段脚本,各个渠道的计算结果会存入tmp文件夹内

```
    $ sh funnel_have_q.sh
```

