---
layout: default
title: "AI新手教学"
permalink: /tutorial/
---
<div class="hero">
  <h1>AI新手教学</h1>
  <p>从零到大师——系统化AI使用教程，循序渐进掌握AI工具</p>
</div>

<div class="tutorial-grid">
  <div class="tutorial-card">
    <div class="icon">🌱</div>
    <span class="level-badge beginner">入门篇</span>
    <h3>新手入门</h3>
    <p>零基础也能用AI：注册、选择工具、基础对话、写好第一个Prompt</p>
    <a href="{{ '/tutorial/beginner/' | relative_url }}" class="btn btn-outline">开始学习</a>
  </div>
  <div class="tutorial-card">
    <div class="icon">⚡</div>
    <span class="level-badge advanced">进阶篇</span>
    <h3>效率进阶</h3>
    <p>结构化Prompt、多模态组合、工作流自动化、团队协作</p>
    <a href="{{ '/tutorial/advanced/' | relative_url }}" class="btn btn-outline">提升技能</a>
  </div>
  <div class="tutorial-card">
    <div class="icon">🎯</div>
    <span class="level-badge master">大师篇</span>
    <h3>精通AI</h3>
    <p>RAG、Agent搭建、模型微调、自建AI工具链、Prompt工程体系化</p>
    <a href="{{ '/tutorial/master/' | relative_url }}" class="btn btn-outline">登峰造极</a>
  </div>
</div>

<div class="post-grid">
{% for post in site.posts %}{% if post.categories contains 'tutorial' %}
<div class="post-card"><div class="post-card-body">
<span class="tag">教学</span>
<h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
<div class="excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</div>
</div><div class="post-card-meta">{{ post.date | date: "%Y-%m-%d" }}</div></div>
{% endif %}{% endfor %}
</div>