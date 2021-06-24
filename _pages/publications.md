---
title: "Publications"
layout: gridlay
excerpt: "- Publications"
sitemap: true
permalink: /publications/
years: [2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Beisi;Corey;Evadnie;Hongjian;Jason;Patrick;Ti-Cheng;Xun;Yawei;Yiping;Zhongshan;Wojciech;Nadhir;Gang
scholar_first_name_bold: Gang
---


## Publications

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list)

<div class="row">
### Featured

<div class="publications_highlight">
  {% bibliography -f {{ site.scholar.bibliography }} --template bib_highlight -q @*[highlight] %}
</div>
</div>

<p> &nbsp; </p>

### Full List

<nobr><em>*</em>denotes equal contribution</nobr>

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}:{% bibliography_count -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
