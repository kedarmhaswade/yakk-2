<!-- index.tpl -->
{% extends "base.tpl" %}
{% block content %}
<h1>Blog</h1>
<ul class="post-list">
{% for post in posts %}
    <li>
        <a href="{{ post.filename }}">{{ post.title }}</a>
        <span class="date">{{ post.date }}</span>
    </li>
{% endfor %}
</ul>
{% endblock %}
