<!-- post.tpl -->
{% extends "base.tpl" %}
{% block content %}
<article class="post">
    <h1>{{ title }}</h1>
    <p class="date">{{ date }}</p>
    {{ body }}
</article>
{% endblock %}
