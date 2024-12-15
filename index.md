---
layout: home
title: 扎克爱思 - 技术博客 | 软件开发 | 个人成长
description: 分享软件开发心得、技术洞察和个人成长故事。专注于编程、职业发展和创新思考。
keywords: 软件开发, 技术博客, 程序员, 个人成长, 职业发展
---

# 欢迎来到扎克爱思的技术博客

## 🚀 关于本站

这是一个专注于分享**软件开发**、**技术趋势**和**个人成长**的技术博客。

### 我的技术栈
- 编程语言：Python, JavaScript, Java
- 框架：Django, Vue, Spring Boot
- 工具：Git, Docker

### 最新文章
{% for post in site.posts limit:3 %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

### 联系我
- GitHub: [@zachthinking](https://github.com/zachthinking)
- Email: zach.thinking@gmail.com
