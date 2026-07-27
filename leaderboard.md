---
layout: default
title: 排行榜
description: AI模型综合性能排行榜，包含不同维度的评分和排名
permalink: /leaderboard/
---

<header class="page-header">
  <div class="container">
    <h1>AI模型排行榜</h1>
    <p>客观评测各大AI模型在不同任务上的表现，帮助您选择最适合的模型</p>
  </div>
</header>

<section class="leaderboard-section">
  <div class="container">
    <div class="tab-container">
      <button class="tab-btn active" data-tab="overall">综合排名</button>
      <button class="tab-btn" data-tab="chat">对话能力</button>
      <button class="tab-btn" data-tab="coding">编程能力</button>
      <button class="tab-btn" data-tab="reasoning">推理能力</button>
      <button class="tab-btn" data-tab="knowledge">知识水平</button>
    </div>
    
    <div class="tab-content" id="overall-tab">
      <div class="table-responsive">
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th>排名</th>
              <th>模型</th>
              <th>开发公司</th>
              <th>综合得分</th>
              <th>价格 (百万Tokens)</th>
              <th>上下文长度</th>
              <th>发布日期</th>
            </tr>
          </thead>
          <tbody>
            {% for model in site.models | sort: "score_overall" | reverse %}
            <tr>
              <td>{{ forloop.index }}</td>
              <td><a href="{{ model.url | relative_url }}">{{ model.name }}</a></td>
              <td>{{ model.company }}</td>
              <td><strong>{{ model.score_overall | round: 1 }}</strong></td>
              <td>${{ model.price_input }}/${{ model.price_output }}</td>
              <td>{{ model.context_window }}K</td>
              <td>{{ model.release_date | date: "%Y-%m-%d" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="tab-content" id="chat-tab">
      <div class="table-responsive">
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th>排名</th>
              <th>模型</th>
              <th>开发公司</th>
              <th>对话得分</th>
              <th>价格 (百万Tokens)</th>
              <th>上下文长度</th>
              <th>发布日期</th>
            </tr>
          </thead>
          <tbody>
            {% for model in site.models | sort: "score_chat" | reverse %}
            <tr>
              <td>{{ forloop.index }}</td>
              <td><a href="{{ model.url | relative_url }}">{{ model.name }}</a></td>
              <td>{{ model.company }}</td>
              <td><strong>{{ model.score_chat | round: 1 }}</strong></td>
              <td>${{ model.price_input }}/${{ model.price_output }}</td>
              <td>{{ model.context_window }}K</td>
              <td>{{ model.release_date | date: "%Y-%m-%d" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="tab-content" id="coding-tab">
      <div class="table-responsive">
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th>排名</th>
              <th>模型</th>
              <th>开发公司</th>
              <th>编程得分</th>
              <th>价格 (百万Tokens)</th>
              <th>上下文长度</th>
              <th>发布日期</th>
            </tr>
          </thead>
          <tbody>
            {% for model in site.models | sort: "score_coding" | reverse %}
            <tr>
              <td>{{ forloop.index }}</td>
              <td><a href="{{ model.url | relative_url }}">{{ model.name }}</a></td>
              <td>{{ model.company }}</td>
              <td><strong>{{ model.score_coding | round: 1 }}</strong></td>
              <td>${{ model.price_input }}/${{ model.price_output }}</td>
              <td>{{ model.context_window }}K</td>
              <td>{{ model.release_date | date: "%Y-%m-%d" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="tab-content" id="reasoning-tab">
      <div class="table-responsive">
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th>排名</th>
              <th>模型</th>
              <th>开发公司</th>
              <th>推理得分</th>
              <th>价格 (百万Tokens)</th>
              <th>上下文长度</th>
              <th>发布日期</th>
            </tr>
          </thead>
          <tbody>
            {% for model in site.models | sort: "score_reasoning" | reverse %}
            <tr>
              <td>{{ forloop.index }}</td>
              <td><a href="{{ model.url | relative_url }}">{{ model.name }}</a></td>
              <td>{{ model.company }}</td>
              <td><strong>{{ model.score_reasoning | round: 1 }}</strong></td>
              <td>${{ model.price_input }}/${{ model.price_output }}</td>
              <td>{{ model.context_window }}K</td>
              <td>{{ model.release_date | date: "%Y-%m-%d" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="tab-content" id="knowledge-tab">
      <div class="table-responsive">
        <table class="leaderboard-table">
          <thead>
            <tr>
              <th>排名</th>
              <th>模型</th>
              <th>开发公司</th>
              <th>知识得分</th>
              <th>价格 (百万Tokens)</th>
              <th>上下文长度</th>
              <th>发布日期</th>
            </tr>
          </thead>
          <tbody>
            {% for model in site.models | sort: "score_knowledge" | reverse %}
            <tr>
              <td>{{ forloop.index }}</td>
              <td><a href="{{ model.url | relative_url }}">{{ model.name }}</a></td>
              <td>{{ model.company }}</td>
              <td><strong>{{ model.score_knowledge | round: 1 }}</strong></td>
              <td>${{ model.price_input }}/${{ model.price_output }}</td>
              <td>{{ model.context_window }}K</td>
              <td>{{ model.release_date | date: "%Y-%m-%d" }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all buttons
        tabButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');
        
        // Hide all tab contents
        tabContents.forEach(content => {
          const id = button.getAttribute('data-tab') + '-tab';
          if (content.id === id) {
            content.style.display = 'block';
          } else {
            content.style.display = 'none';
          }
        });
      });
    });
  });
</script>