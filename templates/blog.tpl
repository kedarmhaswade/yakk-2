{% extends 'classic/index.html.j2' %}

{% block header %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/light.css">
<!--<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/tuftsweb/tufts.css@main/tufts.min.css">-->
<link rel="stylesheet" href="style.css">

<nav class="blog-nav">
  <a href="index.html">Home</a>
  {% for post in resources.post_list %}
    <a href="{{ post.filename }}">{{ post.title }}</a>
  {% endfor %}
</nav>
<hr>
{% endblock header %}

{% block footer %}
<hr>
{% if resources.post_list|length > 1 %}
<div class="post-nav">
  {% set idx = resources.post_list | map(attribute='filename') | list | index(resources.current_filename) %}
  {% if idx > 0 %}
    <a href="{{ resources.post_list[idx-1].filename }}">← {{ resources.post_list[idx-1].title }}</a>
  {% else %}
    <span></span>
  {% endif %}
  {% if idx < resources.post_list|length - 1 %}
    <a href="{{ resources.post_list[idx+1].filename }}">{{ resources.post_list[idx+1].title }} →</a>
  {% else %}
    <span></span>
  {% endif %}
</div>
{% endif %}

<footer class="blog-footer">
  © {{ resources.build_year }} Yakk-2 Blog
</footer>
{% endblock footer %}

