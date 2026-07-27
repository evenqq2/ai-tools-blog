---
layout: default
title: AI对话模型评测
description: ChatGPT、Claude、Gemini等对话模型的综合能力评测和排名
permalink: /chat/
---

<header class="page-header">
  <div class="container">
    <h1>AI对话模型评测</h1>
    <p>客观评测ChatGPT、Claude、Gemini、文心一言、通义千问等主流对话模型的综合能力</p>
  </div>
</header>

<section class="leaderboard-preview">
  <div class="container">
    <h2>最新排名</h2>
    <div class="table-responsive">
      <table class="leaderboard-table">
        <thead>
          <tr>
            <th>排名</th>
            <th>模型</th>
            <th>综合得分</th>
            <th>语言理解</th>
            <th>逻辑推理</th>
            <th>代码能力</th>
            <th>知识水平</th>
            <th>价格 (元/1M tokens)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><a href="/models/claude-3-5-sonnet/" class="model-link">Claude 3.5 Sonnet</a></td>
            <td><strong>85.2</strong></td>
            <td>88.5</td>
            <td>82.1</td>
            <td>83.7</td>
            <td>86.3</td>
            <td>$3.00 / $15.00</td>
          </tr>
          <tr>
            <td>2</td>
            <td><a href="/models/gpt-4o/" class="model-link">GPT-4o</a></td>
            <td><strong>84.7</strong></td>
            <td>86.2</td>
            <td>83.5</td>
            <td>85.1</td>
            <td>83.9</td>
            <td>$2.50 / $10.00</td>
          </tr>
          <tr>
            <td>3</td>
            <td><a href="/models/gemini-1-5-pro/" class="model-link">Gemini 1.5 Pro</a></td>
            <td><strong>83.9</strong></td>
            <td>84.8</td>
            <td>81.2</td>
            <td>84.5</td>
            <td>84.2</td>
            <td>$1.25 / $5.00</td>
          </tr>
          <tr>
            <td>4</td>
            <td><a href="/models/deepseek-v2/" class="model-link">DeepSeek V2</a></td>
            <td><strong>81.5</strong></td>
            <td>79.8</td>
            <td>82.3</td>
            <td>84.1</td>
            <td>80.2</td>
            <td>$0.14 / $0.28</td>
          </tr>
          <tr>
            <td>5</td>
            <td><a href="/models/qwen-2-5-72b/" class="model-link">通义千问2.5-72B</a></td>
            <td><strong>80.8</strong></td>
            <td>82.1</td>
            <td>79.5</td>
            <td>81.3</td>
            <td>80.7</td>
            <td>$0.30 / $0.60</td>
          </tr>
        </tbody>
      </table>
    </div>
    <a href="/benchmarks/chat/" class="btn btn-outline">查看完整基准测试</a>
  </div>
</section>

<section class="explanation">
  <div class="container">
    <h2>评测维度说明</h2>
    <div class="grid-2-cols">
      <div>
        <h3>语言理解</h3>
        <p>评估模型在中文语言理解、逻辑推理、常识推理等方面的能力，包括阅读理解、词义消歧、逻辑判断等子任务。</p>
      </div>
      <div>
        <h3>逻辑推理</h3>
        <p>测试模型进行复杂逻辑推理、数学推理、代码生成等任务的能力，评估其思维链构建和问题解决能力。</p>
      </div>
      <div>
        <h3>代码能力</h3>
        <p>评估模型在各种编程语言中的代码生成、代码理解、代码修复和算法实现能力。</p>
      </div>
      <div>
        <h3>知识水平</h3>
        <p>考察模型在各个领域的知识储备和应用能力，包括科学、技术、文化、历史等方面的事实准确性。</p>
      </div>
    </div>
  </div>
</section>

<section class="recent-reports">
  <div class="container">
    <h2>最新测评报告</h2>
    <div class="posts-grid">
      {%- for post in site.posts limit:4 -%}
        {%- if post.categories contains 'chat' -%}
        <article class="post-card">
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <div class="post-meta">
            <span>{{ post.date | date: "%Y-%m-%d" }}</span>
            <span class="category-tag">对话模型</span>
          </div>
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
        </article>
        {%- endif -%}
      {%- endfor -%}
    </div>
    <a href="/chat/blog/" class="btn btn-outline">查看所有对话模型报告</a>
  </div>
</section>