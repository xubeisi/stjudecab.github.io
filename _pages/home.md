---
title: "News"
layout: textlay
excerpt: "- News"
sitemap: true
permalink: /
---

## News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
