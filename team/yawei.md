---
layout: member
title: Yawei Hui
position: Manager (DevOps)
handle: yawei
email: yawei.hui@stjude.org
twitter:
github: bh007
googlescholar: uwON2rEAAAAJ&hl
photo: tm_yawei.jpg
stjude: h/yawei-hui
orcid: 0000-0001-6397-3086
linkedin: yaweihui
bibfile: tm_yawei.bib
years: [2021, 2020, 2019, 2018, 2017, 2016, 2015]
scholar_first_names_underline: Yawei
scholar_first_name_bold: Yawei
---

### Overview
Being an astrophysicist by training, Dr. Yawei Hui spent much of his early career in exploring the universe for special celestial objects that emit strong X-rays. With experiences accumulated in computing and analytical modeling, he took a significant turn to focus on designing and implementing HPC/Supercomputing workflow and data management system and algorithms development. Now he is taking on new challenges to apply all his data science expertise to understand biomedical data and develop efficient and powerful systems to accelerate scientific discoveries in childhood diseases.


### Education
- PhD, Astrophisics, The Johns Hopkins University, Baltimore, MD (2008)
- MS, Computer Science, University of Tennessee, Knoxville, TN (2015)
- BS, Theoretical Physics, Nanjing University, Nanjing, China (1997)

### Professional Experience

Time        | Position                   | PI/Supervisor   | Institution                           |
----------- | :-----------               | -----------     | -----------                           |
2020-2021   | Manager - DevOps           | Gang Wu         | St. Jude Children's Research Hospital |
2019-2020   | Bioinformatics Analyst III | Gang Wu         | St. Jude Children's Research Hospital |
2016-2019   | Postmaster Res. Associate  | Eric Lingerfelt | The Oak Ridge National Laboratory     |
2012-2012   | Res. Asst. Prof.           |                 | University of Tennessee, Knoxville    |
2008-2012   | Postdoc. Res. Associate    | David Schultz   | The Oak Ridge National Laboratory     |
2000-2008   | Grad. Res. Assistant       | Julian Krolik   | The Johns Hopkins University          |
1997-2000   | Grad. Res. Assistant       | Jinming Dong    | Nanjing University                    |
{:.custom-table}

<!--more-->

# Publications

For a [full list (GEO\|SRA\|Browser\|Code) see below](#full-list)
{% if page.googlescholar %}, or [Google Scholar](https://scholar.google.com/citations?user={{page.googlescholar}}){:target="_blank"}
{% endif %} {% if page.myncbi %}, or [Pubmed](https://www.ncbi.nlm.nih.gov/myncbi/{{page.myncbi}}/bibliography/public/){:target="_blank"}{% endif %}


<div class="row">
  {% capture npaper %}
    {% bibliography_count -f {{ page.bibfile }} -q @*[highlight] %}
  {% endcapture %}
  {% assign npaper = npaper | plus: 0 %}
  {% if npaper > 0 %}
## Featured

<div class="publications_highlight">
  {% bibliography -f {{ page.bibfile }} --template bib_highlight -q @*[highlight] %}
</div>
{% endif %}

</div>

## Full List

<nobr><em>*</em>denotes equal contribution</nobr>
<div class="publications">
{% for y in page.years %}
  {% capture npaper %}
    {% bibliography_count -f {{ page.bibfile }} -q @*[year={{y}}]* %}
  {% endcapture %}
  {% assign npaper = npaper | plus: 0 %}
  {% if npaper > 0 %}
  <h2 class="year">{{y}}:{{npaper}}</h2>
  {% bibliography -f {{ page.bibfile }} -q @*[year={{y}}]* %}
  {% endif %}
{% endfor %}
</div>
