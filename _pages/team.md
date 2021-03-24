---
title: "Team"
layout: gridlay
excerpt: "- Team members"
sitemap: false
permalink: /team/
---

## Team Members

---

### Directors

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == -1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

### Groups

            {% assign links = site.data.navigation %}
            {% for link in links %}
              {% if link.sublinks %}
                <li class="dropdown {{ class }}">
                  {% assign linkname = link.name %}
                  {% if page.group %}
                    {% assign linkname = page.group %}
                  {% endif %}
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownGroup" role="button" data-toggle="dropdown" title="Click to toggle dropmenu" aria-haspopup="true" aria-expanded="false">
                    <p style="text-decoration:underline;text-decoration-color:{{ page.groupcolor }};">
                    {{ linkname }}
                    <span class="caret"></span>
                    </p>
                  </a>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdownGroup">
                    {% for sublink in link.sublinks %}
                      {% if sublink.name == 'separator' %}
                        <li role="separator" class="divider"></li>
                      {% else %}
                        <li>
                          <a class="dropdown-item" href="{{ site.url }}{{ site.baseurl }}{{ sublink.link }}">{{ sublink.name }}</a>
                        </li>
                      {% endif %}
                    {% endfor %}
                  </ul>
                </li>


{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == -1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

### Scientist
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if member.group == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4><a href="{{ member.url }}" class="off">{{ member.name }}</a></h4>
  <i>{{ member.info }}</i>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

---

### Contact
Please contact our group lead, <a href="mailto:beisi.xu#stjude.org">Beisi Xu</a>.









