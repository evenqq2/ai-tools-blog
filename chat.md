---
layout: default
title: "AI对话助手"
permalink: /chat/
---
<div class="hero">
  <h1>AI对话助手</h1>
  <p>ChatGPT、Claude、文心一言、通义千问、Kimi、DeepSeek——最全最深横评</p>
</div>
<div class="post-grid">
{% for post in site.posts %}
{% if post.categories contains 'chat' %}
<div class="post-card"><div class="post-card-body">
<span class="tag">AI对话</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endif %}{% endfor %}
</div>