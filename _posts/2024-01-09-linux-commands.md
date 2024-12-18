---
layout: post
title: "Linux 常用命令大全：从入门到精通"
date: 2024-01-09 11:30:19 +0800
categories: [Linux, 教程]
tags: [linux, command, shell]
toc: true
---

Linux 命令是与 Linux 系统交互的基本方式。本文整理了最常用的 Linux 命令，从基础到进阶，帮助你更好地使用 Linux 系统。

## 文件和目录操作

### 基本操作

1. **ls - 列出目录内容**
```bash
ls              # 列出当前目录文件
ls -l           # 详细信息
ls -a           # 显示隐藏文件
ls -lh          # 以人类可读格式显示文件大小
ls -R           # 递归显示子目录
```

2. **cd - 切换目录**
```bash
cd /path        # 切换到指定目录
cd              # 切换到家目录
cd ..           # 切换到上级目录
cd -            # 切换到上次的目录
```

3. **pwd - 显示当前目录**
```bash
pwd             # 显示当前完整路径
```

4. **mkdir - 创建目录**
```bash
mkdir dir1                  # 创建单个目录
mkdir -p dir1/dir2/dir3    # 创建多级目录
```

5. **rm - 删除文件或目录**
```bash
rm file         # 删除文件
rm -r dir       # 递归删除目录
rm -f file      # 强制删除文件
rm -rf dir      # 强制递归删除目录
```

### 文件操作

1. **cp - 复制文件**
```bash
cp file1 file2          # 复制文件
cp -r dir1 dir2        # 复制目录
cp -p file1 file2      # 保留文件属性
```

2. **mv - 移动文件**
```bash
mv file1 file2         # 重命名文件
mv file1 dir/          # 移动文件到目录
mv dir1 dir2           # 移动目录
```

3. **touch - 创建空文件**
```bash
touch file            # 创建空文件或更新时间戳
```

4. **chmod - 修改权限**
```bash
chmod 755 file        # 使用数字设置权限
chmod u+x file        # 给所有者添加执行权限
chmod -R 644 dir      # 递归设置目录权限
```

## 文本处理

### 查看文件内容

1. **cat - 查看文件内容**
```bash
cat file            # 显示文件内容
cat -n file         # 显示行号
cat file1 file2     # 连接显示多个文件
```

2. **less - 分页查看**
```bash
less file           # 分页查看文件
# 常用快捷键：
# q - 退出
# 空格 - 下一页
# b - 上一页
# /pattern - 搜索
```

3. **head/tail - 查看文件头/尾**
```bash
head -n 10 file     # 查看前10行
tail -n 20 file     # 查看后20行
tail -f file        # 实时查看文件更新
```

### 文本搜索

1. **grep - 文本搜索**
```bash
grep pattern file           # 搜索文件
grep -r pattern dir        # 递归搜索目录
grep -i pattern file       # 忽略大小写
grep -v pattern file       # 显示不匹配的行
```

2. **find - 文件搜索**
```bash
find . -name "*.txt"       # 按名称搜索
find . -type f -size +100M # 搜索大文件
find . -mtime -7          # 最近7天修改的文件
```

## 系统管理

### 进程管理

1. **ps - 查看进程**
```bash
ps aux            # 显示所有进程
ps -ef            # 显示所有进程
ps aux | grep nginx  # 查找特定进程
```

2. **top - 动态进程监控**
```bash
top               # 实时显示进程信息
# 常用快捷键：
# M - 按内存排序
# P - 按CPU排序
# q - 退出
```

3. **kill - 终止进程**
```bash
kill PID          # 终止进程
kill -9 PID       # 强制终止进程
killall process   # 终止所有同名进程
```

### 系统信息

1. **df - 磁盘空间**
```bash
df -h             # 显示磁盘使用情况
```

2. **free - 内存使用**
```bash
free -h           # 显示内存使用情况
```

3. **uname - 系统信息**
```bash
uname -a          # 显示系统信息
```

## 网络操作

### 网络连接

1. **ping - 测试连接**
```bash
ping host         # 测试网络连接
ping -c 4 host    # 发送4个包后停止
```

2. **netstat - 网络统计**
```bash
netstat -an       # 显示所有连接
netstat -tulpn    # 显示监听端口
```

3. **curl - 网络请求**
```bash
curl URL          # 获取网页内容
curl -O URL       # 下载文件
curl -X POST URL  # 发送POST请求
```

### 远程操作

1. **ssh - 远程登录**
```bash
ssh user@host     # 远程登录
ssh -p 2222 host  # 指定端口
```

2. **scp - 远程复制**
```bash
scp file user@host:/path   # 上传文件
scp user@host:/path file   # 下载文件
scp -r dir user@host:/path # 复制目录
```

## 压缩和解压

1. **tar - 打包和解包**
```bash
tar -czf file.tar.gz dir   # 压缩目录
tar -xzf file.tar.gz       # 解压文件
tar -tvf file.tar.gz       # 查看内容
```

2. **zip/unzip - ZIP压缩**
```bash
zip -r file.zip dir        # 压缩目录
unzip file.zip            # 解压文件
```

## 用户管理

1. **useradd - 添加用户**
```bash
useradd username          # 创建用户
useradd -m username      # 创建用户并建立主目录
```

2. **passwd - 设置密码**
```bash
passwd username          # 设置用户密码
```

3. **su - 切换用户**
```bash
su username             # 切换用户
su -                   # 切换到root用户
```

## 权限管理

1. **sudo - 以管理员权限执行**
```bash
sudo command           # 以root权限执行命令
sudo -i               # 切换到root用户环境
```

2. **chown - 更改所有者**
```bash
chown user:group file  # 更改文件所有者和组
chown -R user dir     # 递归更改目录所有者
```

## 实用技巧

### 命令组合

1. **管道和重定向**
```bash
command1 | command2    # 管道：前一个命令的输出作为后一个命令的输入
command > file        # 输出重定向到文件
command >> file       # 追加输出到文件
```

2. **后台运行**
```bash
command &            # 在后台运行命令
nohup command &      # 在后台运行命令，并忽略挂起信号
```

### 命令历史

1. **history - 查看命令历史**
```bash
history             # 显示命令历史
!n                 # 执行历史命令中的第n条
!!                 # 执行上一条命令
```

## 总结

这些 Linux 命令是日常工作中最常用的命令。要点：

1. 多使用命令的帮助文档（man 或 --help）
2. 注意命令的权限要求
3. 谨慎使用删除和修改命令
4. 善用 Tab 补全和命令历史
5. 掌握基本的正则表达式

建议：
- 从基础命令开始，逐步掌握高级用法
- 多实践，建立自己的命令笔记
- 了解命令的危险性，特别是系统管理命令
- 学会查看命令的帮助文档和在线资源
