---
title: "Publications"
layout: gridlay
excerpt: "- Publications"
sitemap: false
permalink: /publications/
years: [2021, 2020, 2019, 2018, 2017, 2016, 2015]
---


## Publications

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list), also [Google Scholar](https://scholar.google.com/citations?user=PIPGxWoAAAAJ), [Pubmed](https://www.ncbi.nlm.nih.gov/myncbi/1zofdYmKS0FQg/bibliography/public/)

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
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
