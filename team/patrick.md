---
layout: member
title: Patrick Schreiner
position: Bioinoformatics Research Scientist(Transcriptomics)
handle: patrick
email: patrick.schreiner@stjude.org
twitter: pschreins
github: stjudecab
googlescholar:
myncbi: 1ZmoCXANKssI1v
photo: tm_patrick.png
stjude: x/patrick-schreiner
orcid: 0000-0001-5391-2642
linkedin: patrick-schreiner-phd
bibfile: tm_patrick
years: [2021, 2020, 2019, 2018, 2017]
scholar_first_names_underline: Patrick
scholar_first_name_bold: Patrick
---

### Overview
Patrick's graduate research was focused on the origin and function of sRNA mainly in the yellow fever mosquito.  In addition to mosquito samples, Patrick also has experience in analyzing data from bacteria, yeast, ferret, mice, and human samples. He received his Ph.D. in Genetics, Genomics, and Bioinformatics from the University of California, Riverside in 2017 before coming to St. Jude as a Bioinformatics Research Scientist.  Patrick has led the execution of projects that mine and analyze big data from internal and external datasets. His particular research areas of interest include Transcriptomics, Immunology, and Single-Cell Omics.

NGS Data that Patrick knows how to analyze:

- RNA-Seq
- scRNA-Seq
- scATAC-Seq
- Microarray (Expression)
- WGBS/TEBS

### Education
- PhD, University of California, Riverside (2017)
- BS, Loyola University of Chicago (2012)

### Professional Experience

Time        | Position                   | PI/Supervisor    | Institution                                   |
----------- | :-----------               | -----------      | -----------                                   |
2017-       | Bioinformatics	         | Gang Wu /        | St. Jude Children's Research Hospital         |
            | Research Scientist         | Yiping Fan       |                                               |
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
