# Mekorot
A Hebrew/Latin typeface in the Rashi style. Originally this project was part of an attempt to create a free version of the Hebrew Talmud, as PDF files, while keeping the original page's shape (known as 'Tzurat Hadaf'). This repository has been adapted from a previous [Sourceforge archive](http://mekorot.sourceforge.net), based on the original work by Dr. Alan Hoenig [here](https://ctan.org/tex-archive/language/hebrew/makor/).

In 2023 this project was re-engineered by Eli Heuer for inclusion in the Google Fonts catalog.

# Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://eliheuer.github.io/hasubi-mono.

# License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

# Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.

# Changelog

**12 Jan 2023. Version 0.001**
- Updated repo to the new Google Fonts Project Template
