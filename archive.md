---
layout: page
title: 文章归档
permalink: /archive/
keywords: 博客归档, 文章列表, 历史文章, 技术博客, 按年份归档
description: 浏览所有博客文章的归档，按年份整理的技术文章和心得分享。
---

## 按年份归档
{% assign posts_by_year = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
### {{ year.name }}
{% for post in year.items %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%m-%d" }}
{% endfor %}
{% endfor %}
