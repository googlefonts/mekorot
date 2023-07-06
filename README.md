# Mekorot
A Hebrew typeface in the Rashi style. Originally this project was part of an attempt to create a free version of the Hebrew Talmud, as PDF files, while keeping the page shape known as Tzurat Hadaf.

This project has been adapted from a previous [SourceForge archive](https://sourceforge.net/projects/mekorot/), based on the [original work by Dr. Alan Hoenig](https://ctan.org/tex-archive/language/hebrew/makor/).

In 2023 this project was reengineered and redrawn by Eli Heuer for inclusion in the Google Fonts catalog. The Latin typeface included is a fork of [Spectral](https://fonts.google.com/specimen/Spectral).

# Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions. 

# License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

# Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the [Google Fonts](https://github.com/googlefonts/googlefonts-project-template) workflow.

# Changelog
**5 July 2023. Version 2.000**
- Version 2.000 release

**1 March 2023. Version 0.001**
- Removed all Spectral related source files
- Started a clean fork of Crimson Pro for Latian coverage

**12 Jan 2023. Version 0.001**
- Updated repo to the new Google Fonts Project Template
