---
layout: default
title: "AI绘图工具"
permalink: /image/
---
<div class="hero">
  <h1>AI绘图工具</h1>
  <p>Midjourney、Stable Diffusion、文心一格、通义万相——视觉创作新纪元</p>
</div>
<div class="post-grid">
{% for post in site.posts %}{% if post.categories contains 'image' %}
<div class="post-card"><div class="post-card-body">
<span class="tag">AI绘图</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endif %}{% endfor %}
</div>