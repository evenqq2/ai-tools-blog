---
layout: default
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}

  {{ content }}

  {% if site.paginate %}
    {% assign posts = paginator.posts %}
  {% else %}
    {% assign posts = site.posts %}
  {% endif %}

  {%- if posts.size > 0 -%}
    <ul class="post-list">
      {%- for post in posts -%}
      <li>
        <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          <p class="post-excerpt {
            post.excerpt | strip_html | truncatewords: 50
          }
          </p>
        {%- endif -%}
      </li>
      {%- endfor -%}
    </ul>

    {% if pages.paginate %}
    </div>
    <div class="pagination" style="display: flex; gap: 1rem; margin: 2rem 0;">
      {% if pages.paginator.previous_page %}
        <a href="{{ pages.paginator.previous_page_path | relative_url }}">&laquo; 上一页</a>
      {% endif %}
      <span>第 {{ pages.paginator.page }} / {{ pages.paginator.total_pages }} 页</span>
      {% if pages.paginator.next_page %}
        <a href="{{ pages.paginator.next_page_path | relative_url }}">下一页 &raquo;</a>
      {% endif %}
    </div>
    {% endif %}
  {%- endif -%}

</div>