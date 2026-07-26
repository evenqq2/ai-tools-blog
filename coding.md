---
layout: default
title: "AI编程工具"
permalink: /coding/
---
<div class="hero">
  <h1>AI编程工具</h1>
  <p>GitHub Copilot、Cursor、通义灵码、CodeGeeX——编程提效神器</p>
</div>
<div class="post-grid">
{% for post in site.posts %}{% if post.categories contains 'coding' %}
<div class="post-card"><div class="post-card-body">
<span class="tag">AI编程</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endif %}{% endfor %}
</div>