---
title: "SJCAB Epigenetics - About"
layout: textlay
excerpt: "SJCAB Epigenetics -- About"
sitemap: false
permalink: /about/
---

Our website is based on the open source templates forked from [Dr. Stephan Sanders](https://github.com/sanderslab/sanderslab.github.io), designed and shared by the labs of [D. Allan Drummond](http://www.allanlab.org/aboutwebsite.html) and [Trevor Bedford](http://bedford.io/misc/about/). We downloaded source codes from their repository and modified our contents based on shared templates. We greatly thank for Stephan, Allan and Trevor for allowing reuse of their codebase.

It's based on [jekyll](https://jekyllrb.com).
We added plugin [jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship) to improve table shown by markdown.

If you use conda, these will help you start build for your own
- Step1: Fork [https://github.com/stjudecab/stjudecab.github.io](https://github.com/stjudecab/stjudecab.github.io)
- Step2: on you forked git, click setting and get your own repository name
- Under linux
```
git clone https://github.com/yourid/stjudecab.github.io
conda create -n iobuild python=3.8 ruby=2.6.3
conda activate iobuild
gem install jekyll bundle jekyll-spaceship
bundle install
bundle exec jekyll build
git commit "update" && git push
#local debug, would rebuild automatically everytime you changed a file
bundle exec jekyll serve --host $yourip --port 5050 --livereload
```

The website is deployed using [GitHub Pages](https://stjudecab.github.io) and the source code is available on [GitHub](https://github.com/stjudecab/stjudecab.github.io). Please feel free to reuse this code (making sure to cite the Sanders, Bedford and Drummond lab as the original sources of the lab website template).
