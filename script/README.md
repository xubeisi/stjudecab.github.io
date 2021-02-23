### bibtex_organizer.py

Script to Clean .bib from Zotero(bibtex)

```
usage: bibtex_organizer.py [-h] [-f <file>] [-o <string>] [-m <string>]

%prog [options] -f filein -o fileout -m mode

optional arguments:
  -h, --help            show this help message and exit
  -f <file>, --filein <file>
                        in file name,.gz would gzip, none|stdin|- means stdin (default: None)
  -o <string>, --fileout <string>
                        out file name,.gz would gzip, none|stdout|- means stdout (default: None)
  -m <string>, --mode <string>
                        abbr(get Journal Abbreviation),fig get 1st figure from PMC (default: abbr,fig)
```

#### I just want results!

1. Step1: Collect Manuscript using [Zotero](https://www.zotero.org/download/) along with [Chrome Extension](https://chrome.google.com/webstore/detail/zotero-connector/ekhagklcjbdpajgpjgmbionohlpdbjgc?hl=en)
- Option1: [Zotero Plugin PMCID Fetcher](https://github.com/retorquere/zotero-pmcid-fetcher) could help you get PMCID quickly.
- Option2: Manual fill in *Extra* region of Zotero
  such as
  ```
  PMCID: PMC6842117
  PMID: 31493975
  ```
- Option3: Other Tags would be automatically converted to links
  + Multiple Link Seperated by ';'
  + 'LINKID,Name' will show 'Name' as text of link, 'LINKID' will show defailt as text of linke (usually 'LINKID')
  + tex.cofirst:
    - 2 means first 2 authors equally contributed
    - 2,3 means 2nd and 3rd author equally contributed
    - 2;-1 means first 2 authors equally contributed, last author corresponding
    - 2;-2,-1 means first 2 authors equally contributed, last 2 authors corresponding
  ```
    tex.GEOID: GSE87064,Mouse;GSE87065,CHIP
    tex.SRAID: PRJNA473990,Human;PRJNA473991,Mouse
    tex.EGAID:  EGAS00001000514,Link1;EGAS00001000654
    tex.Browser: https://pecan.stjude.cloud/proteinpaint/study/retina_hic_2018,Mouse_mm9;https://viz.stjude.cloud/stjude/visualization/human-retina-wgbs-chipseq-chromhmmgene-fpkm-hg19,Human_hg19
    tex.Extralinks: https://platform.stjude.cloud/workflows/methylation-to-activity,STJUDE.CLOUD.workflow;https://github.com/chenlab-sj/M2A,Code
    tex.cofirst: 2
  ```

2. Step2: In Zotero, Select Items Export bibtex as .bib file

3. Step3:
```bash
conda env create -f .condaenv.xml
conda activate iobuild
cd _bibliography
python ../script/bibtex_organizer.py -f papers.bib -m abbr,fig
```

Details:
#### Used [bibtexparser](https://bibtexparser.readthedocs.io/en/master)

#### Only need get Abbreviations
- Recommend export using [Zotero Plugin](https://github.com/retorquere/zotero-better-bibtex/releases/tag/v5.2.121) [zotero-better-bibtex](https://retorque.re/zotero-better-bibtex)
- Using [jabref](https://abbrv.jabref.org/) [Database](https://github.com/JabRef/abbrv.jabref.org/tree/master/journals) [API](https://abbreviso.toolforge.org/)
- Alt: [CSL Abbreviations Data](https://github.com/citation-style-language/abbreviations)
- Alt: Canismarko's API using [CASSI and LTWA](https://github.com/canismarko/franklin/blob/master/franklin/journals.py)

```bash
cd _bibliography
python ../script/bibtex_organizer.py -f papers.bib -m abbr
#Results papers.clean.bib (with abbr property) will be used (defined in _config.yml -> scholar -> bibliography)
```

#### Only need get First Figure from PMC as potential highlights

```bash
cd _bibliography
python ../script/bibtex_organizer.py -f papers.bib -m fig
#Will automactially download first figure if it have PMCID
#Results papers.clean.bib (with fig1 property)
```
