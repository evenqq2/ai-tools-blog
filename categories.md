---
layout: page
title: 分类
permalink: /categories/
---

# 文章分类

{% assign categories_list = site.categories | sort %}

{% for category in categories_list %}
  <h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2>
  <ul>
    {% for post in category[1] %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="post-meta">({{ post.date | date: "%Y-%m-%d" }})</span>
      </li>
    {% endfor %}
  </ul>
{% endfor %}