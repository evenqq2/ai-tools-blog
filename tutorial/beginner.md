---
layout: default
title: "入门篇 - AI新手教学"
permalink: /tutorial/beginner/
---
<div class="hero">
  <h1>🌱 入门篇</h1>
  <p>零基础开始使用AI工具，每篇教程都配有完整步骤和示例</p>
</div>
<div class="post-grid">
{% assign tut_posts = site.posts | where: "categories", "tutorial-beginner" %}
{% for post in tut_posts %}
<div class="post-card"><div class="post-card-body">
<span class="tag">入门</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endfor %}
</div>