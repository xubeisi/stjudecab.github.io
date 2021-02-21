---
title: "{{ site.title }} - About"
layout: textlay
excerpt: "{{ site.titleshort }} -- About"
sitemap: false
permalink: /about/
---
# St. Jude Center for Applied Bioinformatics(CAB)

Our website is based on [jekyll](https://jekyllrb.com)
- The open source templates were forked from [Dr. Stephan Sanders](https://github.com/sanderslab/sanderslab.github.io),
- designed and shared by the labs of [D. Allan Drummond](http://www.allanlab.org/aboutwebsite.html) and [Trevor Bedford](http://bedford.io/misc/about/)
- We greatful thank them for sharing code and knowledge.
- We added plugin [jekyll-spaceship](https://github.com/jeffreytse/jekyll-spaceship) to improve table shown by markdown.
- We added plugin [flatify](http://acegik.net/blog/ruby/jekyll/plugins/howto-nest-liquid-template-variables-inside-yaml-front-matter-block.html) so new lab doesn't need change title for each .md file


If you use conda, these will help you start build for your own
- Step1: Fork [https://github.com/stjudecab/stjudecab.github.io](https://github.com/stjudecab/stjudecab.github.io)
- Step2: on you forked git, click setting and get your own repository name
- Step3: Under linux
```
git clone https://github.com/stjudecab/stjudecab.github.io
conda create -n iobuild python=3.8 ruby=2.6.3
conda activate iobuild
gem install bundle
bundle install
#local debug, would rebuild automatically everytime you changed a file
bundle exec jekyll serve --host $yourip --port 5050 --livereload
#after confirmation of the changes you want
bundle exec jekyll build
git commit "update" && git push
```

The website is deployed using [GitHub Pages](https://stjudecab.github.io) and the source code is available on [GitHub](https://github.com/stjudecab/stjudecab.github.io). Please feel free to reuse this code (making sure to cite the Sanders, Bedford and Drummond lab as the original sources of the lab website template).
