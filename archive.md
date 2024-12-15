---
layout: page
title: 文章归档
permalink: /archive/
---

## 按年份归档
{% assign posts_by_year = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
### {{ year.name }}
{% for post in year.items %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%m-%d" }}
{% endfor %}
{% endfor %}
