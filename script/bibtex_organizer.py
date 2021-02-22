#!/usr/bin/env python
#!/usr/bin/env pypy
#########################################################################
# Copyright (c) 2020-~ Beisi Xu && St Jude
# This source code is released for free distribution under the terms of the
# Attribution-NonCommercial-ShareAlike 4.0 International (cc)
#*Author:       Beisi Xu < xubeisi [at] gmail DOT com >
# File Name: bibtex_organizer.py            Created Time: Mon Feb 22 00:43:52 CST 2021
#########################################################################

from __future__ import print_function
import re, os, sys, shutil
from string import *
import argparse
import time

dbtext = "@article{2019_NatNeurosci_yang,
  title = {Differentiation of Human Pluripotent Stem Cells into Neurons or Cortical Organoids Requires Transcriptional Co-Regulation by {{UTX}} and {{53BP1}} Cofi},
  author = {Yang, Xiaoyang and Xu, Beisi and Mulvey, Brett and Evans, Myron and Jordan, Samuel and Wang, Yong-Dong and Pagala, Vishwajeeth and Peng, Junmin and Fan, Yiping and Patel, Arishna and Peng, Jamy C.},
  year = {2019},
  month = mar,
  volume = {22},
  pages = {362--373},
  issn = {1546-1726},
  doi = {10.1038/s41593-018-0328-5},
  abstract = {An interaction between UTX and 53BP1, which occurs in humans but not mice, promotes neurogenic gene expression that underlies neuronal differentiation and cortical development, perhaps providing insight into human-specific neurodevelopment.},
  copyright = {2019 The Author(s), under exclusive licence to Springer Nature America, Inc.},
  file = {files/5226/Yang et al. - 2019 - Differentiation of human pluripotent stem cells in.pdf;files/5225/s41593-018-0328-5.html},
  journal = {Nat Neurosci},
  language = {en},
  number = {3},
  pmcid = {PMC6511450},
  pmid = {30718900}
}"


def getPMCFig1(ffin, ffout):
	import bibtexparser
	with open('bibtex.bib') as bibtex_file:
   		bibtex_database = bibtexparser.load(bibtex_file)

def main(argv):
    parser = argparse.ArgumentParser(description="%prog [options] -f filein -o fileout -m mode ",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--filein", action="store", type=str,
                      dest="fin", help="in file name,.gz would gzip, none|stdin|- means stdin", metavar="<file>")
    parser.add_argument("-o", "--fileout", action="store", type=str,
                      dest="fout", help="out file name,.gz would gzip, none|stdout|- means stdout", metavar="<string>")
    parser.add_argument("-m", "--mode", action="store", type=str,
                      dest="mode", help="mode ", metavar="<string>")
    opt = parser.parse_args()
    if len(argv) < 2:
        parser.print_help()
        sys.exit(0)

    GenomeData.logcmd(argv, '.run.log')
    ffin = GenomeData.checkstdinout(opt.fin,"in","--filein")
    ffout = GenomeData.checkstdinout(opt.fout,"out","--fileout")

if __name__ == "__main__":
    main(sys.argv)


