---
layout: default
---
<div class="hero">
  <h1>AI工具测评</h1>
  <p>深度横评海内外AI工具，教程指南、避坑宝典、场景推荐</p>
</div>

<div class="post-grid">
{%- for post in site.posts -%}
  <div class="post-card">
    <div class="post-card-body">
      {%- if post.categories[0] -%}<span class="tag">{{ post.categories[0] }}</span>{%- endif -%}
      <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
      <div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
    </div>
    <div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div>
  </div>
{%- endfor -%}
</div>