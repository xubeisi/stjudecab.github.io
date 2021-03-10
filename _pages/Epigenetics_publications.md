---
title: "Publications"
layout: gridlay
excerpt: "- Publications"
sitemap: false
permalink: /Epigenetics_publications/
years: [2021, 2020, 2019, 2018, 2017, 2016, 2015]
group: Epigenetics
groupcolor: "#D2B48C"
---

{% assign bibfile = page.group | append: ".clean.bib" %}

## Publications

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list), also [Google Scholar](https://scholar.google.com/citations?user=PIPGxWoAAAAJ){:target="_blank"}, [Pubmed](https://www.ncbi.nlm.nih.gov/myncbi/1zofdYmKS0FQg/bibliography/public/){:target="_blank"}

<div class="row">
### Featured

<div class="publications_highlight">
  {% bibliography -f {{ bibfile }} --template bib_highlight -q @*[highlight] %}
</div>
</div>

<p> &nbsp; </p>

### Full List

<nobr><em>*</em>denotes equal contribution</nobr>

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}:{% bibliography_count -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}</h2>
  {% bibliography -f {{ bibfile }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
