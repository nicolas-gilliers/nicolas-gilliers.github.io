---
layout: default
title: Blog
permalink: /blog/
---


<ul>
  {% for post in site.posts %}
    <li>
      <span>{{ post.date | date: "%d/%m/%Y" }}</span> - 
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>