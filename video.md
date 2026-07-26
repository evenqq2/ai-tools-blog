---
layout: default
title: "AI视频工具"
permalink: /video/
---
<div class="hero">
  <h1>AI视频工具</h1>
  <p>Sora、Runway、可灵、即梦——文字生视频的变革</p>
</div>
<div class="post-grid">
{% for post in site.posts %}{% if post.categories contains 'video' %}
<div class="post-card"><div class="post-card-body">
<span class="tag">AI视频</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endif %}{% endfor %}
</div>