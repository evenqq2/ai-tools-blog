---
layout: default
title: "进阶篇 - AI效率提升"
permalink: /tutorial/advanced/
---
<div class="hero">
  <h1>⚡ 进阶篇</h1>
  <p>掌握结构化Prompt、多工具组合、自动化工作流，效率翻倍</p>
</div>
<div class="post-grid">
{% assign tut_posts = site.posts | where: "categories", "tutorial-advanced" %}
{% for post in tut_posts %}
<div class="post-card"><div class="post-card-body">
<span class="tag">进阶</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endfor %}
</div>