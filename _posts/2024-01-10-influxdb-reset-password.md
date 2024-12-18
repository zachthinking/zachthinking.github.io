---
layout: post
title: "InfluxDB v2 忘记密码重置方法"
date: 2024-01-10 14:32:33 +0800
categories: [Database, 教程]
tags: [influxdb, troubleshooting]
toc: true
---

在使用 InfluxDB v2 时，有时可能会遇到忘记管理员密码的情况。本文介绍一种重置 InfluxDB v2 密码的方法。

## Influxdb2 修改 admin 密码


可以通过恢复管理员令牌来重置InfluxDB2管理员的密码

1、在主机上找到influxd.bolt文件：/var/lib/influxdb2/influxd.bolt

2、在这个混合文本和二进制json文件中搜索已知的用户名或token之类的字符串。

例如：

```json
{"id":"1234567898000000",
"token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==",
"status":"active",
"description":"admins's Token",
```

3、借助管理员特权令牌，你可以使用Influx命令行界面命令 influx user password 来更新口令。

例如：

```bash
influx user password -n admin -t xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==
Please type your new password *********************
Please type your new password again *********************
Your password has been successfully updated.
```

修改密码成功！

