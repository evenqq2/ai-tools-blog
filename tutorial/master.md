---
layout: default
title: "大师篇 - AI精通之路"
permalink: /tutorial/master/
---
<div class="hero">
  <h1>🎯 大师篇</h1>
  <p>RAG、Agent、模型微调、自建工具链——成为AI领域专家</p>
</div>
<div class="post-grid">
{% assign tut_posts = site.posts | where: "categories", "tutorial-master" %}
{% for post in tut_posts %}
<div class="post-card"><div class="post-card-body">
<span class="tag">大师</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endfor %}
</div>