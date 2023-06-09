## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[1] Family checks</b></summary><div><details><summary>🔥 <b>FAIL:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** sTypoAscender is not the same across the family:
Mekorot Medium Italic: 759
Mekorot Medium: 900
Mekorot Bold Italic: 759
Mekorot SemiBold: 900
Mekorot: 900
Mekorot SemiBold Italic: 759
Mekorot Bold: 900
Mekorot ExtraBold: 900
Mekorot Italic: 759
Mekorot ExtraBold Italic: 759 [code: sTypoAscender-mismatch]
* 🔥 **FAIL** sTypoDescender is not the same across the family:
Mekorot Medium Italic: -241
Mekorot Medium: -300
Mekorot Bold Italic: -241
Mekorot SemiBold: -300
Mekorot: -300
Mekorot SemiBold Italic: -241
Mekorot Bold: -300
Mekorot ExtraBold: -300
Mekorot Italic: -241
Mekorot ExtraBold Italic: -241 [code: sTypoDescender-mismatch]
* 🔥 **FAIL** sTypoLineGap is not the same across the family:
Mekorot Medium Italic: 522
Mekorot Medium: 0
Mekorot Bold Italic: 522
Mekorot SemiBold: 0
Mekorot: 0
Mekorot SemiBold Italic: 522
Mekorot Bold: 0
Mekorot ExtraBold: 0
Mekorot Italic: 522
Mekorot ExtraBold Italic: 522 [code: sTypoLineGap-mismatch]
* 🔥 **FAIL** usWinAscent is not the same across the family:
Mekorot Medium Italic: 1059
Mekorot Medium: 1200
Mekorot Bold Italic: 1059
Mekorot SemiBold: 1200
Mekorot: 1200
Mekorot SemiBold Italic: 1059
Mekorot Bold: 1200
Mekorot ExtraBold: 1200
Mekorot Italic: 1059
Mekorot ExtraBold Italic: 1059 [code: usWinAscent-mismatch]
* 🔥 **FAIL** usWinDescent is not the same across the family:
Mekorot Medium Italic: 463
Mekorot Medium: 358
Mekorot Bold Italic: 463
Mekorot SemiBold: 358
Mekorot: 358
Mekorot SemiBold Italic: 463
Mekorot Bold: 358
Mekorot ExtraBold: 358
Mekorot Italic: 463
Mekorot ExtraBold Italic: 463 [code: usWinDescent-mismatch]
* 🔥 **FAIL** ascent is not the same across the family:
Mekorot Medium Italic: 917
Mekorot Medium: 900
Mekorot Bold Italic: 917
Mekorot SemiBold: 900
Mekorot: 900
Mekorot SemiBold Italic: 917
Mekorot Bold: 900
Mekorot ExtraBold: 900
Mekorot Italic: 917
Mekorot ExtraBold Italic: 917 [code: ascent-mismatch]
* 🔥 **FAIL** descent is not the same across the family:
Mekorot Medium Italic: -463
Mekorot Medium: -300
Mekorot Bold Italic: -463
Mekorot SemiBold: -300
Mekorot: -300
Mekorot SemiBold Italic: -463
Mekorot Bold: -300
Mekorot ExtraBold: -300
Mekorot Italic: -463
Mekorot ExtraBold Italic: -463 [code: descent-mismatch]
</div></details><br></div></details><details><summary><b>[18] Mekorot-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Mekorot Medium Italic | Mekorot Medium |
| Subfamily Name | Regular | Italic |
| Full Name | Mekorot Medium Italic | Mekorot Medium Italic |
| Poscript Name | Mekorot-MediumItalic | Mekorot-MediumItalic |
| Typographic Family Name | Mekorot | Mekorot |
| Typographic Subfamily Name | Medium Italic | Medium Italic | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "522" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (759) and hhea ascent (917) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/italic_names">com.google.fonts/check/name/italic_names</a>)</summary><div>


* 🔥 **FAIL** Name ID 1 (Family Name) must not contain 'Italic'. [code: bad-familyname]
* 🔥 **FAIL** Name ID 2 (Subfamily Name) does not conform to specs. Only R/I/B/BI are allowed.
Got: 'Regular'. [code: bad-subfamilyname]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)
 

	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)
 [code: missing-codepoints]
* ⚠ **WARN** GF_TransLatin_Arabic is almost fulfilled. Missing codepoints:

	- 0x1E34 (LATIN CAPITAL LETTER K WITH LINE BELOW)


	- 0x1E35 (LATIN SMALL LETTER K WITH LINE BELOW)


	- 0x1E96 (LATIN SMALL LETTER H WITH LINE BELOW)
 

	- 0x02BD (MODIFIER LETTER REVERSED COMMA)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Mekorot Medium Italic' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- CR

	- Euro.LP

	- Euro.OP

	- T_h

	- a.superior

	- aacute.sc

	- abreve.sc

	- acircumflex.sc

	- acute.case

	- acutedotaccent

	- acutedotaccent.case

	- adieresis.sc

	- aeacute.sc

	- agrave.sc

	- amacron.sc

	- ampersand.sc

	- aogonek.sc

	- aring.sc

	- aringacute.sc

	- at.case

	- at.sc

	- atilde.sc

	- b.superior

	- backslash.case

	- blacktriangle

	- braceleft.case

	- braceright.case

	- bracketleft.case

	- bracketright.case

	- breve.case

	- breveacute

	- breveacute.case

	- brevegrave

	- brevegrave.case

	- brevehookabove

	- brevehookabove.case

	- brevetilde

	- brevetilde.case

	- c.superior

	- c_h

	- c_t

	- cacute.sc

	- caron.case

	- carondotaccent

	- carondotaccent.case

	- ccaron.sc

	- ccedilla.sc

	- ccircumflex.sc

	- cdotaccent.sc

	- cent.LP

	- cent.OP

	- circumflex.case

	- circumflexhookabove

	- circumflexhookabove.case

	- circumflextilde

	- circumflextilde.case

	- d.superior

	- dcaron.sc

	- dcroat.sc

	- dieresis.case

	- dieresisacute.case

	- dieresismacron

	- dieresismacron.case

	- dollar.LP

	- dollar.OP

	- dotaccent.case

	- dotaccentmacron

	- dotaccentmacron.case

	- dotbelowcomb.case

	- dotlessi.sc

	- e.superior

	- eacute.sc

	- ebreve.sc

	- ecaron.sc

	- ecircumflex.sc

	- edieresis.sc

	- edotaccent.sc

	- egrave.sc

	- eight.LP

	- eight.OP

	- eight.subs

	- eight.sups

	- emacron.sc

	- emdash.case

	- endash.case

	- eng.sc

	- eogonek.sc

	- eth.sc

	- exclam.sc

	- exclamdown.case

	- exclamdown.sc

	- f.sc

	- f.superior

	- f_b

	- f_f_b

	- f_f_h

	- f_f_j

	- f_f_k

	- f_f_t

	- f_h

	- f_j

	- f_k

	- f_t

	- five.LP

	- five.OP

	- five.subs

	- five.sups

	- florin.LP

	- florin.OP

	- four.LP

	- four.OP

	- four.subs

	- four.sups

	- g.superior

	- gbreve.sc

	- gcaron.sc

	- gcircumflex.sc

	- gdotaccent.sc

	- germandbls.sc

	- grave.case

	- guillemotleft.case

	- guillemotright.case

	- guilsinglleft.case

	- guilsinglright.case

	- h.superior

	- hbar.sc

	- hcircumflex.sc

	- hungarumlaut.case

	- hyphen.case

	- i.loclTRK

	- i.loclTRK.sc

	- iacute.sc

	- ibreve.sc

	- icircumflex.sc

	- idieresis.sc

	- igrave.sc

	- ij.sc

	- imacron.sc

	- iogonek.sc

	- itilde.sc

	- j.superior

	- jcircumflex.sc

	- k.superior

	- kgreenlandic.sc

	- l.superior

	- lacute.sc

	- lcaron.sc

	- ldot.sc

	- lslash.sc

	- m.superior

	- macron.case

	- macronacute

	- macronacute.case

	- macrondieresis

	- macrondieresis.case

	- macrongrave

	- macrongrave.case

	- nacute.sc

	- ncaron.sc

	- nine.LP

	- nine.OP

	- nine.subs

	- nine.sups

	- ntilde.sc

	- numbersign.LP

	- numbersign.OP

	- o.superior

	- oacute.sc

	- obreve.sc

	- ocircumflex.sc

	- odieresis.sc

	- oe.sc

	- ograve.sc

	- ohungarumlaut.sc

	- omacron.sc

	- one.LP

	- one.OP

	- one.OT

	- one.subs

	- one.sups

	- oslashacute.sc

	- otilde.sc

	- p.superior

	- parenleft.case

	- parenright.case

	- periodcentered.case

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- periodcentered.loclCAT.sc

	- periodcentered.sc

	- q.sc

	- q.superior

	- question.sc

	- questiondown.case

	- questiondown.sc

	- quotedbl.sc

	- quotedblleft.sc

	- quotedblright.sc

	- quoteleft.sc

	- quoteright.sc

	- quotesingle.sc

	- r.superior

	- racute.sc

	- rcaron.sc

	- ring.case

	- s.superior

	- s_p

	- sacute.sc

	- scaron.sc

	- scedilla.sc

	- scircumflex.sc

	- seven.LP

	- seven.OP

	- seven.subs

	- seven.sups

	- six.LP

	- six.OP

	- six.subs

	- six.sups

	- slash.case

	- sterling.LP

	- sterling.OP

	- t.superior

	- tbar.sc

	- tcaron.sc

	- thorn.sc

	- three.LP

	- three.OP

	- three.subs

	- three.sups

	- tilde.case

	- tildeacute

	- tildeacute.case

	- tildedieresis

	- tildedieresis.case

	- tildemacron

	- tildemacron.case

	- two.LP

	- two.OP

	- two.subs

	- two.sups

	- u.superior

	- uacute.sc

	- ubreve.sc

	- ucircumflex.sc

	- udieresis.sc

	- ugrave.sc

	- uhungarumlaut.sc

	- umacron.sc

	- uni004A0301

	- uni006A0301

	- uni006A0301.sc

	- uni0123.sc

	- uni0137.sc

	- uni013C.sc

	- uni0146.sc

	- uni0157.sc

	- uni0163.sc

	- uni01C6.sc

	- uni01C9.sc

	- uni01CC.sc

	- uni01EB.sc

	- uni0201.sc

	- uni0203.sc

	- uni0205.sc

	- uni0207.sc

	- uni0209.sc

	- uni020B.sc

	- uni020D.sc

	- uni020F.sc

	- uni0211.sc

	- uni0213.sc

	- uni0215.sc

	- uni0217.sc

	- uni0219.sc

	- uni021B.sc

	- uni022B.sc

	- uni022D.sc

	- uni0231.sc

	- uni0233.sc

	- uni031B.case

	- uni0324.case

	- uni0326.case

	- uni0327.case

	- uni0328.case

	- uni032E.case

	- uni0331.case

	- uni0414.bgr

	- uni0416.bgr

	- uni041A.bgr

	- uni041B.bgr

	- uni0430.sc

	- uni0431.locl

	- uni0431.locl.sc

	- uni0432.bgr

	- uni0432.bgr.sc

	- uni0432.sc

	- uni0433.bgr

	- uni0433.bgr.sc

	- uni0433.locl

	- uni0433.locl.sc

	- uni0434.bgr.sc

	- uni0434.locl

	- uni0434.locl.sc

	- uni0435.sc

	- uni0436.bgr

	- uni0436.bgr.sc

	- uni0437.bgr

	- uni0437.bgr.sc

	- uni0438.bgr

	- uni0438.bgr.sc

	- uni0439.bgr

	- uni0439.bgr.sc

	- uni0439.sc

	- uni043A.bgr

	- uni043A.bgr.sc

	- uni043A.sc

	- uni043B.bgr

	- uni043B.bgr.sc

	- uni043B.sc

	- uni043C.sc

	- uni043D.bgr

	- uni043D.bgr.sc

	- uni043D.sc

	- uni043E.sc

	- uni043F.bgr

	- uni043F.bgr.sc

	- uni043F.locl

	- uni043F.locl.sc

	- uni0440.sc

	- uni0441.sc

	- uni0442.bgr

	- uni0442.bgr.sc

	- uni0442.locl

	- uni0442.locl.sc

	- uni0442.sc

	- uni0444.sc

	- uni0445.sc

	- uni0446.bgr

	- uni0446.bgr.sc

	- uni0447.bgr

	- uni0447.bgr.sc

	- uni0448.bgr

	- uni0448.bgr.sc

	- uni0449.bgr

	- uni0449.bgr.sc

	- uni044A.bgr

	- uni044A.bgr.sc

	- uni044B.sc

	- uni044C.bgr

	- uni044C.bgr.sc

	- uni044D.sc

	- uni044E.bgr

	- uni044E.bgr.sc

	- uni044F.sc

	- uni0451.sc

	- uni0452.sc

	- uni0453.sc

	- uni0454.sc

	- uni0455.sc

	- uni0456.sc

	- uni0457.sc

	- uni0458.sc

	- uni0459.sc

	- uni045A.sc

	- uni045B.sc

	- uni045C.sc

	- uni045E.sc

	- uni045F.sc

	- uni0463.sc

	- uni0473.sc

	- uni0475.sc

	- uni0491.sc

	- uni0493.sc

	- uni0497.sc

	- uni049B.sc

	- uni04A3.sc

	- uni04AF.sc

	- uni04B1.sc

	- uni04B3.sc

	- uni04B7.sc

	- uni04BB.sc

	- uni04CF.sc

	- uni04D9.sc

	- uni04E3.sc

	- uni04E9.sc

	- uni04EF.sc

	- uni1E09.sc

	- uni1E0D.sc

	- uni1E0F.sc

	- uni1E15.sc

	- uni1E17.sc

	- uni1E1D.sc

	- uni1E21.sc

	- uni1E25.sc

	- uni1E2B.sc

	- uni1E2F.sc

	- uni1E37.sc

	- uni1E3B.sc

	- uni1E43.sc

	- uni1E45.sc

	- uni1E47.sc

	- uni1E49.sc

	- uni1E4D.sc

	- uni1E4F.sc

	- uni1E51.sc

	- uni1E53.sc

	- uni1E5B.sc

	- uni1E5F.sc

	- uni1E61.sc

	- uni1E63.sc

	- uni1E65.sc

	- uni1E67.sc

	- uni1E69.sc

	- uni1E6D.sc

	- uni1E6F.sc

	- uni1E79.sc

	- uni1E7B.sc

	- uni1E8F.sc

	- uni1E93.sc

	- uni1E97.sc

	- uni1EA1.sc

	- uni1EA3.sc

	- uni1EA5.sc

	- uni1EA7.sc

	- uni1EA9.sc

	- uni1EAB.sc

	- uni1EAD.sc

	- uni1EAF.sc

	- uni1EB1.sc

	- uni1EB3.sc

	- uni1EB5.sc

	- uni1EB7.sc

	- uni1EB9.sc

	- uni1EBB.sc

	- uni1EBD.sc

	- uni1EBF.sc

	- uni1EC1.sc

	- uni1EC3.sc

	- uni1EC5.sc

	- uni1EC7.sc

	- uni1EC9.sc

	- uni1ECB.sc

	- uni1ECD.sc

	- uni1ECF.sc

	- uni1ED1.sc

	- uni1ED3.sc

	- uni1ED5.sc

	- uni1ED7.sc

	- uni1ED9.sc

	- uni1EDB.sc

	- uni1EDD.sc

	- uni1EDF.sc

	- uni1EE1.sc

	- uni1EE3.sc

	- uni1EE5.sc

	- uni1EE7.sc

	- uni1EE9.sc

	- uni1EEB.sc

	- uni1EED.sc

	- uni1EEF.sc

	- uni1EF1.sc

	- uni1EF5.sc

	- uni1EF7.sc

	- uni1EF9.sc

	- uni20B4.LP

	- uni20B4.OP

	- uni20B8.LP

	- uni20B8.OP

	- uni20BD.LP

	- uni20BD.OP

	- uni2116

	- uni2116.LP

	- uni2116.OP

	- uni2116.OT

	- uogonek.sc

	- uring.sc

	- utilde.sc

	- v.sc

	- v.superior

	- w.superior

	- wacute.sc

	- wcircumflex.sc

	- wdieresis.sc

	- wgrave.sc

	- whitetriangle

	- x.superior

	- y.superior

	- yacute.sc

	- ycircumflex.sc

	- ydieresis.sc

	- yen.LP

	- yen.OP

	- ygrave.sc

	- z.superior

	- zacute.sc

	- zcaron.sc

	- zdotaccent.sc

	- zero.LP

	- zero.OP

	- zero.slashLP

	- zero.slashOP

	- zero.subs 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* m (U+006D): L<<458.0,319.0>--<457.0,315.0>> -> L<<457.0,315.0>--<401.0,0.0>>

	* uni0442 (U+0442): L<<458.0,319.0>--<457.0,315.0>> -> L<<457.0,315.0>--<401.0,0.0>>

	* uni0448 (U+0448): L<<318.0,133.0>--<319.0,138.0>> -> L<<319.0,138.0>--<363.0,386.0>>

	* uni0449 (U+0449): L<<318.0,133.0>--<319.0,138.0>> -> L<<319.0,138.0>--<363.0,386.0>>

	* uni04B1 (U+04B1): L<<270.0,0.0>--<270.0,0.0>> -> L<<270.0,0.0>--<385.0,0.0>> 

	* uni1E43 (U+1E43): L<<458.0,319.0>--<457.0,315.0>> -> L<<457.0,315.0>--<401.0,0.0>> [code: found-colinear-vectors]
</div></details><br></div></details><details><summary><b>[9] Mekorot-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- i.loclTRK

	- one.sups

	- three.sups 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<475.0,307.0>--<476.0,552.0>>

	* G (U+0047): L<<642.0,619.0>--<643.0,467.0>>

	* Gbreve (U+011E): L<<642.0,619.0>--<643.0,467.0>>

	* Gdotaccent (U+0120): L<<642.0,619.0>--<643.0,467.0>>

	* m (U+006D): L<<676.0,68.0>--<677.0,296.0>>

	* m (U+006D): L<<790.0,329.0>--<789.0,68.0>>

	* thorn (U+00FE): L<<218.0,734.0>--<217.0,419.0>>

	* uni00B5 (U+00B5): L<<78.0,-213.0>--<77.0,433.0>>

	* uni0122 (U+0122): L<<642.0,619.0>--<643.0,467.0>> 

	* uni03BC (U+03BC): L<<78.0,-213.0>--<77.0,433.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[14] Mekorot-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "522" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (759) and hhea ascent (917) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)
 

	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)
 [code: missing-codepoints]
* ⚠ **WARN** GF_TransLatin_Arabic is almost fulfilled. Missing codepoints:

	- 0x1E34 (LATIN CAPITAL LETTER K WITH LINE BELOW)


	- 0x1E35 (LATIN SMALL LETTER K WITH LINE BELOW)


	- 0x1E96 (LATIN SMALL LETTER H WITH LINE BELOW)
 

	- 0x02BD (MODIFIER LETTER REVERSED COMMA)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- CR

	- Euro.LP

	- Euro.OP

	- T_h

	- a.superior

	- aacute.sc

	- abreve.sc

	- acircumflex.sc

	- acute.case

	- acutedotaccent

	- acutedotaccent.case

	- adieresis.sc

	- aeacute.sc

	- agrave.sc

	- amacron.sc

	- ampersand.sc

	- aogonek.sc

	- aring.sc

	- aringacute.sc

	- at.case

	- at.sc

	- atilde.sc

	- b.superior

	- backslash.case

	- blacktriangle

	- braceleft.case

	- braceright.case

	- bracketleft.case

	- bracketright.case

	- breve.case

	- breveacute

	- breveacute.case

	- brevegrave

	- brevegrave.case

	- brevehookabove

	- brevehookabove.case

	- brevetilde

	- brevetilde.case

	- c.superior

	- c_h

	- c_t

	- cacute.sc

	- caron.case

	- carondotaccent

	- carondotaccent.case

	- ccaron.sc

	- ccedilla.sc

	- ccircumflex.sc

	- cdotaccent.sc

	- cent.LP

	- cent.OP

	- circumflex.case

	- circumflexhookabove

	- circumflexhookabove.case

	- circumflextilde

	- circumflextilde.case

	- d.superior

	- dcaron.sc

	- dcroat.sc

	- dieresis.case

	- dieresisacute.case

	- dieresismacron

	- dieresismacron.case

	- dollar.LP

	- dollar.OP

	- dotaccent.case

	- dotaccentmacron

	- dotaccentmacron.case

	- dotbelowcomb.case

	- dotlessi.sc

	- e.superior

	- eacute.sc

	- ebreve.sc

	- ecaron.sc

	- ecircumflex.sc

	- edieresis.sc

	- edotaccent.sc

	- egrave.sc

	- eight.LP

	- eight.OP

	- eight.subs

	- eight.sups

	- emacron.sc

	- emdash.case

	- endash.case

	- eng.sc

	- eogonek.sc

	- eth.sc

	- exclam.sc

	- exclamdown.case

	- exclamdown.sc

	- f.sc

	- f.superior

	- f_b

	- f_f_b

	- f_f_h

	- f_f_j

	- f_f_k

	- f_f_t

	- f_h

	- f_j

	- f_k

	- f_t

	- five.LP

	- five.OP

	- five.subs

	- five.sups

	- florin.LP

	- florin.OP

	- four.LP

	- four.OP

	- four.subs

	- four.sups

	- g.superior

	- gbreve.sc

	- gcaron.sc

	- gcircumflex.sc

	- gdotaccent.sc

	- germandbls.sc

	- grave.case

	- guillemotleft.case

	- guillemotright.case

	- guilsinglleft.case

	- guilsinglright.case

	- h.superior

	- hbar.sc

	- hcircumflex.sc

	- hungarumlaut.case

	- hyphen.case

	- i.loclTRK

	- i.loclTRK.sc

	- iacute.sc

	- ibreve.sc

	- icircumflex.sc

	- idieresis.sc

	- igrave.sc

	- ij.sc

	- imacron.sc

	- iogonek.sc

	- itilde.sc

	- j.superior

	- jcircumflex.sc

	- k.superior

	- kgreenlandic.sc

	- l.superior

	- lacute.sc

	- lcaron.sc

	- ldot.sc

	- lslash.sc

	- m.superior

	- macron.case

	- macronacute

	- macronacute.case

	- macrondieresis

	- macrondieresis.case

	- macrongrave

	- macrongrave.case

	- nacute.sc

	- ncaron.sc

	- nine.LP

	- nine.OP

	- nine.subs

	- nine.sups

	- ntilde.sc

	- numbersign.LP

	- numbersign.OP

	- o.superior

	- oacute.sc

	- obreve.sc

	- ocircumflex.sc

	- odieresis.sc

	- oe.sc

	- ograve.sc

	- ohungarumlaut.sc

	- omacron.sc

	- one.LP

	- one.OP

	- one.OT

	- one.subs

	- one.sups

	- oslashacute.sc

	- otilde.sc

	- p.superior

	- parenleft.case

	- parenright.case

	- periodcentered.case

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- periodcentered.loclCAT.sc

	- periodcentered.sc

	- q.sc

	- q.superior

	- question.sc

	- questiondown.case

	- questiondown.sc

	- quotedbl.sc

	- quotedblleft.sc

	- quotedblright.sc

	- quoteleft.sc

	- quoteright.sc

	- quotesingle.sc

	- r.superior

	- racute.sc

	- rcaron.sc

	- ring.case

	- s.superior

	- s_p

	- sacute.sc

	- scaron.sc

	- scedilla.sc

	- scircumflex.sc

	- seven.LP

	- seven.OP

	- seven.subs

	- seven.sups

	- six.LP

	- six.OP

	- six.subs

	- six.sups

	- slash.case

	- sterling.LP

	- sterling.OP

	- t.superior

	- tbar.sc

	- tcaron.sc

	- thorn.sc

	- three.LP

	- three.OP

	- three.subs

	- three.sups

	- tilde.case

	- tildeacute

	- tildeacute.case

	- tildedieresis

	- tildedieresis.case

	- tildemacron

	- tildemacron.case

	- two.LP

	- two.OP

	- two.subs

	- two.sups

	- u.superior

	- uacute.sc

	- ubreve.sc

	- ucircumflex.sc

	- udieresis.sc

	- ugrave.sc

	- uhungarumlaut.sc

	- umacron.sc

	- uni004A0301

	- uni006A0301

	- uni006A0301.sc

	- uni0123.sc

	- uni0137.sc

	- uni013C.sc

	- uni0146.sc

	- uni0157.sc

	- uni0163.sc

	- uni01C6.sc

	- uni01C9.sc

	- uni01CC.sc

	- uni01EB.sc

	- uni0201.sc

	- uni0203.sc

	- uni0205.sc

	- uni0207.sc

	- uni0209.sc

	- uni020B.sc

	- uni020D.sc

	- uni020F.sc

	- uni0211.sc

	- uni0213.sc

	- uni0215.sc

	- uni0217.sc

	- uni0219.sc

	- uni021B.sc

	- uni022B.sc

	- uni022D.sc

	- uni0231.sc

	- uni0233.sc

	- uni031B.case

	- uni0324.case

	- uni0326.case

	- uni0327.case

	- uni0328.case

	- uni032E.case

	- uni0331.case

	- uni0414.bgr

	- uni0416.bgr

	- uni041A.bgr

	- uni041B.bgr

	- uni0430.sc

	- uni0431.locl

	- uni0431.locl.sc

	- uni0432.bgr

	- uni0432.bgr.sc

	- uni0432.sc

	- uni0433.bgr

	- uni0433.bgr.sc

	- uni0433.locl

	- uni0433.locl.sc

	- uni0434.bgr.sc

	- uni0434.locl

	- uni0434.locl.sc

	- uni0435.sc

	- uni0436.bgr

	- uni0436.bgr.sc

	- uni0437.bgr

	- uni0437.bgr.sc

	- uni0438.bgr

	- uni0438.bgr.sc

	- uni0439.bgr

	- uni0439.bgr.sc

	- uni0439.sc

	- uni043A.bgr

	- uni043A.bgr.sc

	- uni043A.sc

	- uni043B.bgr

	- uni043B.bgr.sc

	- uni043B.sc

	- uni043C.sc

	- uni043D.bgr

	- uni043D.bgr.sc

	- uni043D.sc

	- uni043E.sc

	- uni043F.bgr

	- uni043F.bgr.sc

	- uni043F.locl

	- uni043F.locl.sc

	- uni0440.sc

	- uni0441.sc

	- uni0442.bgr

	- uni0442.bgr.sc

	- uni0442.locl

	- uni0442.locl.sc

	- uni0442.sc

	- uni0444.sc

	- uni0445.sc

	- uni0446.bgr

	- uni0446.bgr.sc

	- uni0447.bgr

	- uni0447.bgr.sc

	- uni0448.bgr

	- uni0448.bgr.sc

	- uni0449.bgr

	- uni0449.bgr.sc

	- uni044A.bgr

	- uni044A.bgr.sc

	- uni044B.sc

	- uni044C.bgr

	- uni044C.bgr.sc

	- uni044D.sc

	- uni044E.bgr

	- uni044E.bgr.sc

	- uni044F.sc

	- uni0451.sc

	- uni0452.sc

	- uni0453.sc

	- uni0454.sc

	- uni0455.sc

	- uni0456.sc

	- uni0457.sc

	- uni0458.sc

	- uni0459.sc

	- uni045A.sc

	- uni045B.sc

	- uni045C.sc

	- uni045E.sc

	- uni045F.sc

	- uni0463.sc

	- uni0473.sc

	- uni0475.sc

	- uni0491.sc

	- uni0493.sc

	- uni0497.sc

	- uni049B.sc

	- uni04A3.sc

	- uni04AF.sc

	- uni04B1.sc

	- uni04B3.sc

	- uni04B7.sc

	- uni04BB.sc

	- uni04CF.sc

	- uni04D9.sc

	- uni04E3.sc

	- uni04E9.sc

	- uni04EF.sc

	- uni1E09.sc

	- uni1E0D.sc

	- uni1E0F.sc

	- uni1E15.sc

	- uni1E17.sc

	- uni1E1D.sc

	- uni1E21.sc

	- uni1E25.sc

	- uni1E2B.sc

	- uni1E2F.sc

	- uni1E37.sc

	- uni1E3B.sc

	- uni1E43.sc

	- uni1E45.sc

	- uni1E47.sc

	- uni1E49.sc

	- uni1E4D.sc

	- uni1E4F.sc

	- uni1E51.sc

	- uni1E53.sc

	- uni1E5B.sc

	- uni1E5F.sc

	- uni1E61.sc

	- uni1E63.sc

	- uni1E65.sc

	- uni1E67.sc

	- uni1E69.sc

	- uni1E6D.sc

	- uni1E6F.sc

	- uni1E79.sc

	- uni1E7B.sc

	- uni1E8F.sc

	- uni1E93.sc

	- uni1E97.sc

	- uni1EA1.sc

	- uni1EA3.sc

	- uni1EA5.sc

	- uni1EA7.sc

	- uni1EA9.sc

	- uni1EAB.sc

	- uni1EAD.sc

	- uni1EAF.sc

	- uni1EB1.sc

	- uni1EB3.sc

	- uni1EB5.sc

	- uni1EB7.sc

	- uni1EB9.sc

	- uni1EBB.sc

	- uni1EBD.sc

	- uni1EBF.sc

	- uni1EC1.sc

	- uni1EC3.sc

	- uni1EC5.sc

	- uni1EC7.sc

	- uni1EC9.sc

	- uni1ECB.sc

	- uni1ECD.sc

	- uni1ECF.sc

	- uni1ED1.sc

	- uni1ED3.sc

	- uni1ED5.sc

	- uni1ED7.sc

	- uni1ED9.sc

	- uni1EDB.sc

	- uni1EDD.sc

	- uni1EDF.sc

	- uni1EE1.sc

	- uni1EE3.sc

	- uni1EE5.sc

	- uni1EE7.sc

	- uni1EE9.sc

	- uni1EEB.sc

	- uni1EED.sc

	- uni1EEF.sc

	- uni1EF1.sc

	- uni1EF5.sc

	- uni1EF7.sc

	- uni1EF9.sc

	- uni20B4.LP

	- uni20B4.OP

	- uni20B8.LP

	- uni20B8.OP

	- uni20BD.LP

	- uni20BD.OP

	- uni2116

	- uni2116.LP

	- uni2116.OP

	- uni2116.OT

	- uogonek.sc

	- uring.sc

	- utilde.sc

	- v.sc

	- v.superior

	- w.superior

	- wacute.sc

	- wcircumflex.sc

	- wdieresis.sc

	- wgrave.sc

	- whitetriangle

	- x.superior

	- y.superior

	- yacute.sc

	- ycircumflex.sc

	- ydieresis.sc

	- yen.LP

	- yen.OP

	- ygrave.sc

	- z.superior

	- zacute.sc

	- zcaron.sc

	- zdotaccent.sc

	- zero.LP

	- zero.OP

	- zero.slashLP

	- zero.slashOP

	- zero.subs 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni20B1 (U+20B1): L<<318.0,535.0>--<413.0,535.0>> -> L<<413.0,535.0>--<413.0,535.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* threeeighths (U+215C): B<<311.5,596.5>-<273.0,571.0>-<215.0,565.0>>/B<<215.0,565.0>-<279.0,560.0>-<308.5,537.0>> = 10.373300175159743

	* threequarters (U+00BE): B<<311.5,596.5>-<273.0,571.0>-<215.0,565.0>>/B<<215.0,565.0>-<279.0,560.0>-<308.5,537.0>> = 10.373300175159743

	* uni00B3 (U+00B3): B<<338.5,746.5>-<300.0,721.0>-<242.0,715.0>>/B<<242.0,715.0>-<306.0,710.0>-<335.5,687.0>> = 10.373300175159743

	* uni0417 (U+0417): B<<495.5,381.0>-<449.0,353.0>-<381.0,344.0>>/B<<381.0,344.0>-<471.0,335.0>-<519.0,297.5>> = 13.250038277008938

	* uni2083 (U+2083): B<<208.5,11.5>-<170.0,-14.0>-<112.0,-20.0>>/B<<112.0,-20.0>-<176.0,-25.0>-<205.5,-48.0>> = 10.373300175159743

	* uni2153 (U+2153): B<<680.5,241.5>-<642.0,216.0>-<584.0,210.0>>/B<<584.0,210.0>-<648.0,205.0>-<677.5,182.0>> = 10.373300175159743

	* uni2154 (U+2154): B<<704.5,241.5>-<666.0,216.0>-<608.0,210.0>>/B<<608.0,210.0>-<672.0,205.0>-<701.5,182.0>> = 10.373300175159743

	* uni2782 (U+2782): B<<557.5,421.5>-<518.0,396.0>-<460.0,390.0>>/B<<460.0,390.0>-<525.0,384.0>-<554.5,361.5>> = 11.180037071122237 

	* uni278C (U+278C): B<<554.5,361.5>-<525.0,384.0>-<460.0,390.0>>/B<<460.0,390.0>-<518.0,396.0>-<557.5,421.5>> = 11.180037071122237 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] Mekorot-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- i.loclTRK

	- one.sups

	- three.sups 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<475.0,305.0>--<477.0,549.0>>

	* U (U+0055): L<<285.0,585.0>--<286.0,284.0>>

	* Uacute (U+00DA): L<<285.0,585.0>--<286.0,284.0>>

	* Ubreve (U+016C): L<<285.0,585.0>--<286.0,284.0>>

	* Ucircumflex (U+00DB): L<<285.0,585.0>--<286.0,284.0>>

	* Udieresis (U+00DC): L<<285.0,585.0>--<286.0,284.0>>

	* Ugrave (U+00D9): L<<285.0,585.0>--<286.0,284.0>>

	* Uhungarumlaut (U+0170): L<<285.0,585.0>--<286.0,284.0>>

	* Umacron (U+016A): L<<285.0,585.0>--<286.0,284.0>>

	* Uogonek (U+0172): L<<285.0,585.0>--<286.0,284.0>>

	* Uring (U+016E): L<<285.0,585.0>--<286.0,284.0>>

	* m (U+006D): L<<672.0,68.0>--<673.0,296.0>>

	* m (U+006D): L<<820.0,329.0>--<819.0,68.0>>

	* uni00B5 (U+00B5): L<<64.0,-213.0>--<62.0,437.0>> 

	* uni03BC (U+03BC): L<<64.0,-213.0>--<62.0,437.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] Mekorot-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- i.loclTRK

	- one.sups

	- three.sups 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* G (U+0047): L<<639.0,631.0>--<640.0,474.0>>

	* Gbreve (U+011E): L<<639.0,631.0>--<640.0,474.0>>

	* Gdotaccent (U+0120): L<<639.0,631.0>--<640.0,474.0>>

	* m (U+006D): L<<679.0,68.0>--<680.0,296.0>>

	* m (U+006D): L<<760.0,329.0>--<759.0,68.0>>

	* thorn (U+00FE): L<<192.0,734.0>--<191.0,414.0>>

	* uni00B5 (U+00B5): L<<93.0,-212.0>--<91.0,430.0>>

	* uni0122 (U+0122): L<<639.0,631.0>--<640.0,474.0>> 

	* uni03BC (U+03BC): L<<93.0,-212.0>--<91.0,430.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] Mekorot-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Mekorot SemiBold Italic | Mekorot SemiBold |
| Subfamily Name | Regular | Italic |
| Full Name | Mekorot SemiBold Italic | Mekorot SemiBold Italic |
| Poscript Name | Mekorot-SemiBoldItalic | Mekorot-SemiBoldItalic |
| Typographic Family Name | Mekorot | Mekorot |
| Typographic Subfamily Name | SemiBold Italic | SemiBold Italic | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "522" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (759) and hhea ascent (917) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/italic_names">com.google.fonts/check/name/italic_names</a>)</summary><div>


* 🔥 **FAIL** Name ID 1 (Family Name) must not contain 'Italic'. [code: bad-familyname]
* 🔥 **FAIL** Name ID 2 (Subfamily Name) does not conform to specs. Only R/I/B/BI are allowed.
Got: 'Regular'. [code: bad-subfamilyname]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)
 

	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)
 [code: missing-codepoints]
* ⚠ **WARN** GF_TransLatin_Arabic is almost fulfilled. Missing codepoints:

	- 0x1E34 (LATIN CAPITAL LETTER K WITH LINE BELOW)


	- 0x1E35 (LATIN SMALL LETTER K WITH LINE BELOW)


	- 0x1E96 (LATIN SMALL LETTER H WITH LINE BELOW)
 

	- 0x02BD (MODIFIER LETTER REVERSED COMMA)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Mekorot SemiBold Italic' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- CR

	- Euro.LP

	- Euro.OP

	- T_h

	- a.superior

	- aacute.sc

	- abreve.sc

	- acircumflex.sc

	- acute.case

	- acutedotaccent

	- acutedotaccent.case

	- adieresis.sc

	- aeacute.sc

	- agrave.sc

	- amacron.sc

	- ampersand.sc

	- aogonek.sc

	- aring.sc

	- aringacute.sc

	- at.case

	- at.sc

	- atilde.sc

	- b.superior

	- backslash.case

	- blacktriangle

	- braceleft.case

	- braceright.case

	- bracketleft.case

	- bracketright.case

	- breve.case

	- breveacute

	- breveacute.case

	- brevegrave

	- brevegrave.case

	- brevehookabove

	- brevehookabove.case

	- brevetilde

	- brevetilde.case

	- c.superior

	- c_h

	- c_t

	- cacute.sc

	- caron.case

	- carondotaccent

	- carondotaccent.case

	- ccaron.sc

	- ccedilla.sc

	- ccircumflex.sc

	- cdotaccent.sc

	- cent.LP

	- cent.OP

	- circumflex.case

	- circumflexhookabove

	- circumflexhookabove.case

	- circumflextilde

	- circumflextilde.case

	- d.superior

	- dcaron.sc

	- dcroat.sc

	- dieresis.case

	- dieresisacute.case

	- dieresismacron

	- dieresismacron.case

	- dollar.LP

	- dollar.OP

	- dotaccent.case

	- dotaccentmacron

	- dotaccentmacron.case

	- dotbelowcomb.case

	- dotlessi.sc

	- e.superior

	- eacute.sc

	- ebreve.sc

	- ecaron.sc

	- ecircumflex.sc

	- edieresis.sc

	- edotaccent.sc

	- egrave.sc

	- eight.LP

	- eight.OP

	- eight.subs

	- eight.sups

	- emacron.sc

	- emdash.case

	- endash.case

	- eng.sc

	- eogonek.sc

	- eth.sc

	- exclam.sc

	- exclamdown.case

	- exclamdown.sc

	- f.sc

	- f.superior

	- f_b

	- f_f_b

	- f_f_h

	- f_f_j

	- f_f_k

	- f_f_t

	- f_h

	- f_j

	- f_k

	- f_t

	- five.LP

	- five.OP

	- five.subs

	- five.sups

	- florin.LP

	- florin.OP

	- four.LP

	- four.OP

	- four.subs

	- four.sups

	- g.superior

	- gbreve.sc

	- gcaron.sc

	- gcircumflex.sc

	- gdotaccent.sc

	- germandbls.sc

	- grave.case

	- guillemotleft.case

	- guillemotright.case

	- guilsinglleft.case

	- guilsinglright.case

	- h.superior

	- hbar.sc

	- hcircumflex.sc

	- hungarumlaut.case

	- hyphen.case

	- i.loclTRK

	- i.loclTRK.sc

	- iacute.sc

	- ibreve.sc

	- icircumflex.sc

	- idieresis.sc

	- igrave.sc

	- ij.sc

	- imacron.sc

	- iogonek.sc

	- itilde.sc

	- j.superior

	- jcircumflex.sc

	- k.superior

	- kgreenlandic.sc

	- l.superior

	- lacute.sc

	- lcaron.sc

	- ldot.sc

	- lslash.sc

	- m.superior

	- macron.case

	- macronacute

	- macronacute.case

	- macrondieresis

	- macrondieresis.case

	- macrongrave

	- macrongrave.case

	- nacute.sc

	- ncaron.sc

	- nine.LP

	- nine.OP

	- nine.subs

	- nine.sups

	- ntilde.sc

	- numbersign.LP

	- numbersign.OP

	- o.superior

	- oacute.sc

	- obreve.sc

	- ocircumflex.sc

	- odieresis.sc

	- oe.sc

	- ograve.sc

	- ohungarumlaut.sc

	- omacron.sc

	- one.LP

	- one.OP

	- one.OT

	- one.subs

	- one.sups

	- oslashacute.sc

	- otilde.sc

	- p.superior

	- parenleft.case

	- parenright.case

	- periodcentered.case

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- periodcentered.loclCAT.sc

	- periodcentered.sc

	- q.sc

	- q.superior

	- question.sc

	- questiondown.case

	- questiondown.sc

	- quotedbl.sc

	- quotedblleft.sc

	- quotedblright.sc

	- quoteleft.sc

	- quoteright.sc

	- quotesingle.sc

	- r.superior

	- racute.sc

	- rcaron.sc

	- ring.case

	- s.superior

	- s_p

	- sacute.sc

	- scaron.sc

	- scedilla.sc

	- scircumflex.sc

	- seven.LP

	- seven.OP

	- seven.subs

	- seven.sups

	- six.LP

	- six.OP

	- six.subs

	- six.sups

	- slash.case

	- sterling.LP

	- sterling.OP

	- t.superior

	- tbar.sc

	- tcaron.sc

	- thorn.sc

	- three.LP

	- three.OP

	- three.subs

	- three.sups

	- tilde.case

	- tildeacute

	- tildeacute.case

	- tildedieresis

	- tildedieresis.case

	- tildemacron

	- tildemacron.case

	- two.LP

	- two.OP

	- two.subs

	- two.sups

	- u.superior

	- uacute.sc

	- ubreve.sc

	- ucircumflex.sc

	- udieresis.sc

	- ugrave.sc

	- uhungarumlaut.sc

	- umacron.sc

	- uni004A0301

	- uni006A0301

	- uni006A0301.sc

	- uni0123.sc

	- uni0137.sc

	- uni013C.sc

	- uni0146.sc

	- uni0157.sc

	- uni0163.sc

	- uni01C6.sc

	- uni01C9.sc

	- uni01CC.sc

	- uni01EB.sc

	- uni0201.sc

	- uni0203.sc

	- uni0205.sc

	- uni0207.sc

	- uni0209.sc

	- uni020B.sc

	- uni020D.sc

	- uni020F.sc

	- uni0211.sc

	- uni0213.sc

	- uni0215.sc

	- uni0217.sc

	- uni0219.sc

	- uni021B.sc

	- uni022B.sc

	- uni022D.sc

	- uni0231.sc

	- uni0233.sc

	- uni031B.case

	- uni0324.case

	- uni0326.case

	- uni0327.case

	- uni0328.case

	- uni032E.case

	- uni0331.case

	- uni0414.bgr

	- uni0416.bgr

	- uni041A.bgr

	- uni041B.bgr

	- uni0430.sc

	- uni0431.locl

	- uni0431.locl.sc

	- uni0432.bgr

	- uni0432.bgr.sc

	- uni0432.sc

	- uni0433.bgr

	- uni0433.bgr.sc

	- uni0433.locl

	- uni0433.locl.sc

	- uni0434.bgr.sc

	- uni0434.locl

	- uni0434.locl.sc

	- uni0435.sc

	- uni0436.bgr

	- uni0436.bgr.sc

	- uni0437.bgr

	- uni0437.bgr.sc

	- uni0438.bgr

	- uni0438.bgr.sc

	- uni0439.bgr

	- uni0439.bgr.sc

	- uni0439.sc

	- uni043A.bgr

	- uni043A.bgr.sc

	- uni043A.sc

	- uni043B.bgr

	- uni043B.bgr.sc

	- uni043B.sc

	- uni043C.sc

	- uni043D.bgr

	- uni043D.bgr.sc

	- uni043D.sc

	- uni043E.sc

	- uni043F.bgr

	- uni043F.bgr.sc

	- uni043F.locl

	- uni043F.locl.sc

	- uni0440.sc

	- uni0441.sc

	- uni0442.bgr

	- uni0442.bgr.sc

	- uni0442.locl

	- uni0442.locl.sc

	- uni0442.sc

	- uni0444.sc

	- uni0445.sc

	- uni0446.bgr

	- uni0446.bgr.sc

	- uni0447.bgr

	- uni0447.bgr.sc

	- uni0448.bgr

	- uni0448.bgr.sc

	- uni0449.bgr

	- uni0449.bgr.sc

	- uni044A.bgr

	- uni044A.bgr.sc

	- uni044B.sc

	- uni044C.bgr

	- uni044C.bgr.sc

	- uni044D.sc

	- uni044E.bgr

	- uni044E.bgr.sc

	- uni044F.sc

	- uni0451.sc

	- uni0452.sc

	- uni0453.sc

	- uni0454.sc

	- uni0455.sc

	- uni0456.sc

	- uni0457.sc

	- uni0458.sc

	- uni0459.sc

	- uni045A.sc

	- uni045B.sc

	- uni045C.sc

	- uni045E.sc

	- uni045F.sc

	- uni0463.sc

	- uni0473.sc

	- uni0475.sc

	- uni0491.sc

	- uni0493.sc

	- uni0497.sc

	- uni049B.sc

	- uni04A3.sc

	- uni04AF.sc

	- uni04B1.sc

	- uni04B3.sc

	- uni04B7.sc

	- uni04BB.sc

	- uni04CF.sc

	- uni04D9.sc

	- uni04E3.sc

	- uni04E9.sc

	- uni04EF.sc

	- uni1E09.sc

	- uni1E0D.sc

	- uni1E0F.sc

	- uni1E15.sc

	- uni1E17.sc

	- uni1E1D.sc

	- uni1E21.sc

	- uni1E25.sc

	- uni1E2B.sc

	- uni1E2F.sc

	- uni1E37.sc

	- uni1E3B.sc

	- uni1E43.sc

	- uni1E45.sc

	- uni1E47.sc

	- uni1E49.sc

	- uni1E4D.sc

	- uni1E4F.sc

	- uni1E51.sc

	- uni1E53.sc

	- uni1E5B.sc

	- uni1E5F.sc

	- uni1E61.sc

	- uni1E63.sc

	- uni1E65.sc

	- uni1E67.sc

	- uni1E69.sc

	- uni1E6D.sc

	- uni1E6F.sc

	- uni1E79.sc

	- uni1E7B.sc

	- uni1E8F.sc

	- uni1E93.sc

	- uni1E97.sc

	- uni1EA1.sc

	- uni1EA3.sc

	- uni1EA5.sc

	- uni1EA7.sc

	- uni1EA9.sc

	- uni1EAB.sc

	- uni1EAD.sc

	- uni1EAF.sc

	- uni1EB1.sc

	- uni1EB3.sc

	- uni1EB5.sc

	- uni1EB7.sc

	- uni1EB9.sc

	- uni1EBB.sc

	- uni1EBD.sc

	- uni1EBF.sc

	- uni1EC1.sc

	- uni1EC3.sc

	- uni1EC5.sc

	- uni1EC7.sc

	- uni1EC9.sc

	- uni1ECB.sc

	- uni1ECD.sc

	- uni1ECF.sc

	- uni1ED1.sc

	- uni1ED3.sc

	- uni1ED5.sc

	- uni1ED7.sc

	- uni1ED9.sc

	- uni1EDB.sc

	- uni1EDD.sc

	- uni1EDF.sc

	- uni1EE1.sc

	- uni1EE3.sc

	- uni1EE5.sc

	- uni1EE7.sc

	- uni1EE9.sc

	- uni1EEB.sc

	- uni1EED.sc

	- uni1EEF.sc

	- uni1EF1.sc

	- uni1EF5.sc

	- uni1EF7.sc

	- uni1EF9.sc

	- uni20B4.LP

	- uni20B4.OP

	- uni20B8.LP

	- uni20B8.OP

	- uni20BD.LP

	- uni20BD.OP

	- uni2116

	- uni2116.LP

	- uni2116.OP

	- uni2116.OT

	- uogonek.sc

	- uring.sc

	- utilde.sc

	- v.sc

	- v.superior

	- w.superior

	- wacute.sc

	- wcircumflex.sc

	- wdieresis.sc

	- wgrave.sc

	- whitetriangle

	- x.superior

	- y.superior

	- yacute.sc

	- ycircumflex.sc

	- ydieresis.sc

	- yen.LP

	- yen.OP

	- ygrave.sc

	- z.superior

	- zacute.sc

	- zcaron.sc

	- zdotaccent.sc

	- zero.LP

	- zero.OP

	- zero.slashLP

	- zero.slashOP

	- zero.subs 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* threeeighths (U+215C): B<<308.5,597.5>-<271.0,571.0>-<215.0,565.0>>/B<<215.0,565.0>-<276.0,559.0>-<305.0,536.0>> = 11.733084156412186

	* threequarters (U+00BE): B<<308.5,597.5>-<271.0,571.0>-<215.0,565.0>>/B<<215.0,565.0>-<276.0,559.0>-<305.0,536.0>> = 11.733084156412186

	* uni00B3 (U+00B3): B<<335.5,747.5>-<298.0,721.0>-<242.0,715.0>>/B<<242.0,715.0>-<303.0,709.0>-<332.0,686.0>> = 11.733084156412186

	* uni2083 (U+2083): B<<205.5,12.5>-<168.0,-14.0>-<112.0,-20.0>>/B<<112.0,-20.0>-<173.0,-26.0>-<202.0,-49.0>> = 11.733084156412186

	* uni2153 (U+2153): B<<674.5,242.5>-<637.0,216.0>-<581.0,210.0>>/B<<581.0,210.0>-<642.0,204.0>-<671.0,181.0>> = 11.733084156412186

	* uni2154 (U+2154): B<<699.5,242.5>-<662.0,216.0>-<606.0,210.0>>/B<<606.0,210.0>-<667.0,204.0>-<696.0,181.0>> = 11.733084156412186

	* uni2782 (U+2782): B<<555.5,422.5>-<518.0,396.0>-<462.0,390.0>>/B<<462.0,390.0>-<523.0,384.0>-<552.0,361.0>> = 11.733084156412186 

	* uni278C (U+278C): B<<552.0,361.0>-<523.0,384.0>-<462.0,390.0>>/B<<462.0,390.0>-<518.0,396.0>-<555.5,422.5>> = 11.733084156412186 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] Mekorot-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- i.loclTRK

	- one.sups

	- three.sups 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* m (U+006D): L<<671.0,68.0>--<672.0,296.0>>

	* m (U+006D): L<<835.0,329.0>--<834.0,68.0>>

	* uni00B5 (U+00B5): L<<56.0,-214.0>--<55.0,438.0>> 

	* uni03BC (U+03BC): L<<56.0,-214.0>--<55.0,438.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[9] Mekorot-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĩ ĭ i̇ ǐ i̒ ĩ̦ ĭ̦ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ ĩ̧ ĭ̧ i̧̇ i̧̊ i̧̋ ǐ̧ i̧̒ ĵ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>


* ⚠ **WARN** Glyph '.notdef' should contain a drawing, but it is empty. [code: empty]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- NULL

	- i.loclTRK

	- one.sups

	- three.sups 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* U (U+0055): L<<310.0,585.0>--<311.0,291.0>>

	* Uacute (U+00DA): L<<310.0,585.0>--<311.0,291.0>>

	* Ubreve (U+016C): L<<310.0,585.0>--<311.0,291.0>>

	* Ucircumflex (U+00DB): L<<310.0,585.0>--<311.0,291.0>>

	* Udieresis (U+00DC): L<<310.0,585.0>--<311.0,291.0>>

	* Ugrave (U+00D9): L<<310.0,585.0>--<311.0,291.0>>

	* Uhungarumlaut (U+0170): L<<310.0,585.0>--<311.0,291.0>>

	* Umacron (U+016A): L<<310.0,585.0>--<311.0,291.0>>

	* Uogonek (U+0172): L<<310.0,585.0>--<311.0,291.0>>

	* Uring (U+016E): L<<310.0,585.0>--<311.0,291.0>>

	* m (U+006D): L<<669.0,68.0>--<670.0,296.0>>

	* m (U+006D): L<<850.0,329.0>--<849.0,68.0>>

	* uni00B5 (U+00B5): L<<49.0,-214.0>--<48.0,440.0>> 

	* uni03BC (U+03BC): L<<49.0,-214.0>--<48.0,440.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] Mekorot-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "522" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (759) and hhea ascent (917) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)
 

	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)
 [code: missing-codepoints]
* ⚠ **WARN** GF_TransLatin_Arabic is almost fulfilled. Missing codepoints:

	- 0x1E34 (LATIN CAPITAL LETTER K WITH LINE BELOW)


	- 0x1E35 (LATIN SMALL LETTER K WITH LINE BELOW)


	- 0x1E96 (LATIN SMALL LETTER H WITH LINE BELOW)
 

	- 0x02BD (MODIFIER LETTER REVERSED COMMA)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- CR

	- Euro.LP

	- Euro.OP

	- T_h

	- a.superior

	- aacute.sc

	- abreve.sc

	- acircumflex.sc

	- acute.case

	- acutedotaccent

	- acutedotaccent.case

	- adieresis.sc

	- aeacute.sc

	- agrave.sc

	- amacron.sc

	- ampersand.sc

	- aogonek.sc

	- aring.sc

	- aringacute.sc

	- at.case

	- at.sc

	- atilde.sc

	- b.superior

	- backslash.case

	- blacktriangle

	- braceleft.case

	- braceright.case

	- bracketleft.case

	- bracketright.case

	- breve.case

	- breveacute

	- breveacute.case

	- brevegrave

	- brevegrave.case

	- brevehookabove

	- brevehookabove.case

	- brevetilde

	- brevetilde.case

	- c.superior

	- c_h

	- c_t

	- cacute.sc

	- caron.case

	- carondotaccent

	- carondotaccent.case

	- ccaron.sc

	- ccedilla.sc

	- ccircumflex.sc

	- cdotaccent.sc

	- cent.LP

	- cent.OP

	- circumflex.case

	- circumflexhookabove

	- circumflexhookabove.case

	- circumflextilde

	- circumflextilde.case

	- d.superior

	- dcaron.sc

	- dcroat.sc

	- dieresis.case

	- dieresisacute.case

	- dieresismacron

	- dieresismacron.case

	- dollar.LP

	- dollar.OP

	- dotaccent.case

	- dotaccentmacron

	- dotaccentmacron.case

	- dotbelowcomb.case

	- dotlessi.sc

	- e.superior

	- eacute.sc

	- ebreve.sc

	- ecaron.sc

	- ecircumflex.sc

	- edieresis.sc

	- edotaccent.sc

	- egrave.sc

	- eight.LP

	- eight.OP

	- eight.subs

	- eight.sups

	- emacron.sc

	- emdash.case

	- endash.case

	- eng.sc

	- eogonek.sc

	- eth.sc

	- exclam.sc

	- exclamdown.case

	- exclamdown.sc

	- f.sc

	- f.superior

	- f_b

	- f_f_b

	- f_f_h

	- f_f_j

	- f_f_k

	- f_f_t

	- f_h

	- f_j

	- f_k

	- f_t

	- five.LP

	- five.OP

	- five.subs

	- five.sups

	- florin.LP

	- florin.OP

	- four.LP

	- four.OP

	- four.subs

	- four.sups

	- g.superior

	- gbreve.sc

	- gcaron.sc

	- gcircumflex.sc

	- gdotaccent.sc

	- germandbls.sc

	- grave.case

	- guillemotleft.case

	- guillemotright.case

	- guilsinglleft.case

	- guilsinglright.case

	- h.superior

	- hbar.sc

	- hcircumflex.sc

	- hungarumlaut.case

	- hyphen.case

	- i.loclTRK

	- i.loclTRK.sc

	- iacute.sc

	- ibreve.sc

	- icircumflex.sc

	- idieresis.sc

	- igrave.sc

	- ij.sc

	- imacron.sc

	- iogonek.sc

	- itilde.sc

	- j.superior

	- jcircumflex.sc

	- k.superior

	- kgreenlandic.sc

	- l.superior

	- lacute.sc

	- lcaron.sc

	- ldot.sc

	- lslash.sc

	- m.superior

	- macron.case

	- macronacute

	- macronacute.case

	- macrondieresis

	- macrondieresis.case

	- macrongrave

	- macrongrave.case

	- nacute.sc

	- ncaron.sc

	- nine.LP

	- nine.OP

	- nine.subs

	- nine.sups

	- ntilde.sc

	- numbersign.LP

	- numbersign.OP

	- o.superior

	- oacute.sc

	- obreve.sc

	- ocircumflex.sc

	- odieresis.sc

	- oe.sc

	- ograve.sc

	- ohungarumlaut.sc

	- omacron.sc

	- one.LP

	- one.OP

	- one.OT

	- one.subs

	- one.sups

	- oslashacute.sc

	- otilde.sc

	- p.superior

	- parenleft.case

	- parenright.case

	- periodcentered.case

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- periodcentered.loclCAT.sc

	- periodcentered.sc

	- q.sc

	- q.superior

	- question.sc

	- questiondown.case

	- questiondown.sc

	- quotedbl.sc

	- quotedblleft.sc

	- quotedblright.sc

	- quoteleft.sc

	- quoteright.sc

	- quotesingle.sc

	- r.superior

	- racute.sc

	- rcaron.sc

	- ring.case

	- s.superior

	- s_p

	- sacute.sc

	- scaron.sc

	- scedilla.sc

	- scircumflex.sc

	- seven.LP

	- seven.OP

	- seven.subs

	- seven.sups

	- six.LP

	- six.OP

	- six.subs

	- six.sups

	- slash.case

	- sterling.LP

	- sterling.OP

	- t.superior

	- tbar.sc

	- tcaron.sc

	- thorn.sc

	- three.LP

	- three.OP

	- three.subs

	- three.sups

	- tilde.case

	- tildeacute

	- tildeacute.case

	- tildedieresis

	- tildedieresis.case

	- tildemacron

	- tildemacron.case

	- two.LP

	- two.OP

	- two.subs

	- two.sups

	- u.superior

	- uacute.sc

	- ubreve.sc

	- ucircumflex.sc

	- udieresis.sc

	- ugrave.sc

	- uhungarumlaut.sc

	- umacron.sc

	- uni004A0301

	- uni006A0301

	- uni006A0301.sc

	- uni0123.sc

	- uni0137.sc

	- uni013C.sc

	- uni0146.sc

	- uni0157.sc

	- uni0163.sc

	- uni01C6.sc

	- uni01C9.sc

	- uni01CC.sc

	- uni01EB.sc

	- uni0201.sc

	- uni0203.sc

	- uni0205.sc

	- uni0207.sc

	- uni0209.sc

	- uni020B.sc

	- uni020D.sc

	- uni020F.sc

	- uni0211.sc

	- uni0213.sc

	- uni0215.sc

	- uni0217.sc

	- uni0219.sc

	- uni021B.sc

	- uni022B.sc

	- uni022D.sc

	- uni0231.sc

	- uni0233.sc

	- uni031B.case

	- uni0324.case

	- uni0326.case

	- uni0327.case

	- uni0328.case

	- uni032E.case

	- uni0331.case

	- uni0414.bgr

	- uni0416.bgr

	- uni041A.bgr

	- uni041B.bgr

	- uni0430.sc

	- uni0431.locl

	- uni0431.locl.sc

	- uni0432.bgr

	- uni0432.bgr.sc

	- uni0432.sc

	- uni0433.bgr

	- uni0433.bgr.sc

	- uni0433.locl

	- uni0433.locl.sc

	- uni0434.bgr.sc

	- uni0434.locl

	- uni0434.locl.sc

	- uni0435.sc

	- uni0436.bgr

	- uni0436.bgr.sc

	- uni0437.bgr

	- uni0437.bgr.sc

	- uni0438.bgr

	- uni0438.bgr.sc

	- uni0439.bgr

	- uni0439.bgr.sc

	- uni0439.sc

	- uni043A.bgr

	- uni043A.bgr.sc

	- uni043A.sc

	- uni043B.bgr

	- uni043B.bgr.sc

	- uni043B.sc

	- uni043C.sc

	- uni043D.bgr

	- uni043D.bgr.sc

	- uni043D.sc

	- uni043E.sc

	- uni043F.bgr

	- uni043F.bgr.sc

	- uni043F.locl

	- uni043F.locl.sc

	- uni0440.sc

	- uni0441.sc

	- uni0442.bgr

	- uni0442.bgr.sc

	- uni0442.locl

	- uni0442.locl.sc

	- uni0442.sc

	- uni0444.sc

	- uni0445.sc

	- uni0446.bgr

	- uni0446.bgr.sc

	- uni0447.bgr

	- uni0447.bgr.sc

	- uni0448.bgr

	- uni0448.bgr.sc

	- uni0449.bgr

	- uni0449.bgr.sc

	- uni044A.bgr

	- uni044A.bgr.sc

	- uni044B.sc

	- uni044C.bgr

	- uni044C.bgr.sc

	- uni044D.sc

	- uni044E.bgr

	- uni044E.bgr.sc

	- uni044F.sc

	- uni0451.sc

	- uni0452.sc

	- uni0453.sc

	- uni0454.sc

	- uni0455.sc

	- uni0456.sc

	- uni0457.sc

	- uni0458.sc

	- uni0459.sc

	- uni045A.sc

	- uni045B.sc

	- uni045C.sc

	- uni045E.sc

	- uni045F.sc

	- uni0463.sc

	- uni0473.sc

	- uni0475.sc

	- uni0491.sc

	- uni0493.sc

	- uni0497.sc

	- uni049B.sc

	- uni04A3.sc

	- uni04AF.sc

	- uni04B1.sc

	- uni04B3.sc

	- uni04B7.sc

	- uni04BB.sc

	- uni04CF.sc

	- uni04D9.sc

	- uni04E3.sc

	- uni04E9.sc

	- uni04EF.sc

	- uni1E09.sc

	- uni1E0D.sc

	- uni1E0F.sc

	- uni1E15.sc

	- uni1E17.sc

	- uni1E1D.sc

	- uni1E21.sc

	- uni1E25.sc

	- uni1E2B.sc

	- uni1E2F.sc

	- uni1E37.sc

	- uni1E3B.sc

	- uni1E43.sc

	- uni1E45.sc

	- uni1E47.sc

	- uni1E49.sc

	- uni1E4D.sc

	- uni1E4F.sc

	- uni1E51.sc

	- uni1E53.sc

	- uni1E5B.sc

	- uni1E5F.sc

	- uni1E61.sc

	- uni1E63.sc

	- uni1E65.sc

	- uni1E67.sc

	- uni1E69.sc

	- uni1E6D.sc

	- uni1E6F.sc

	- uni1E79.sc

	- uni1E7B.sc

	- uni1E8F.sc

	- uni1E93.sc

	- uni1E97.sc

	- uni1EA1.sc

	- uni1EA3.sc

	- uni1EA5.sc

	- uni1EA7.sc

	- uni1EA9.sc

	- uni1EAB.sc

	- uni1EAD.sc

	- uni1EAF.sc

	- uni1EB1.sc

	- uni1EB3.sc

	- uni1EB5.sc

	- uni1EB7.sc

	- uni1EB9.sc

	- uni1EBB.sc

	- uni1EBD.sc

	- uni1EBF.sc

	- uni1EC1.sc

	- uni1EC3.sc

	- uni1EC5.sc

	- uni1EC7.sc

	- uni1EC9.sc

	- uni1ECB.sc

	- uni1ECD.sc

	- uni1ECF.sc

	- uni1ED1.sc

	- uni1ED3.sc

	- uni1ED5.sc

	- uni1ED7.sc

	- uni1ED9.sc

	- uni1EDB.sc

	- uni1EDD.sc

	- uni1EDF.sc

	- uni1EE1.sc

	- uni1EE3.sc

	- uni1EE5.sc

	- uni1EE7.sc

	- uni1EE9.sc

	- uni1EEB.sc

	- uni1EED.sc

	- uni1EEF.sc

	- uni1EF1.sc

	- uni1EF5.sc

	- uni1EF7.sc

	- uni1EF9.sc

	- uni20B4.LP

	- uni20B4.OP

	- uni20B8.LP

	- uni20B8.OP

	- uni20BD.LP

	- uni20BD.OP

	- uni2116

	- uni2116.LP

	- uni2116.OP

	- uni2116.OT

	- uogonek.sc

	- uring.sc

	- utilde.sc

	- v.sc

	- v.superior

	- w.superior

	- wacute.sc

	- wcircumflex.sc

	- wdieresis.sc

	- wgrave.sc

	- whitetriangle

	- x.superior

	- y.superior

	- yacute.sc

	- ycircumflex.sc

	- ydieresis.sc

	- yen.LP

	- yen.OP

	- ygrave.sc

	- z.superior

	- zacute.sc

	- zcaron.sc

	- zdotaccent.sc

	- zero.LP

	- zero.OP

	- zero.slashLP

	- zero.slashOP

	- zero.subs 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni045F (U+045F): B<<175.0,-80.5>-<198.0,-34.0>-<242.0,17.0>>/B<<242.0,17.0>-<205.0,-10.0>-<159.0,-10.0>> = 13.094837673254283 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] Mekorot-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Mekorot ExtraBold Italic | Mekorot ExtraBold |
| Subfamily Name | Regular | Italic |
| Full Name | Mekorot ExtraBold Italic | Mekorot ExtraBold Italic |
| Poscript Name | Mekorot-ExtraBoldItalic | Mekorot-ExtraBoldItalic |
| Typographic Family Name | Mekorot | Mekorot |
| Typographic Subfamily Name | ExtraBold Italic | ExtraBold Italic | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* 🔥 **FAIL** OS/2.sTypoLineGap is "522" it should be 0 [code: bad-OS/2.sTypoLineGap]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>


* 🔥 **FAIL** OS/2 sTypoAscender (759) and hhea ascent (917) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̇ ǐ i̒ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ i̧̇ i̧̊ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection REGULAR bit should be unset. [code: bad-REGULAR]
* 🔥 **FAIL** OS/2 fsSelection ITALIC bit should be set. [code: bad-ITALIC]
</div></details><details><summary>🔥 <b>FAIL:</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/italic_names">com.google.fonts/check/name/italic_names</a>)</summary><div>


* 🔥 **FAIL** Name ID 1 (Family Name) must not contain 'Italic'. [code: bad-familyname]
* 🔥 **FAIL** Name ID 2 (Subfamily Name) does not conform to specs. Only R/I/B/BI are allowed.
Got: 'Regular'. [code: bad-subfamilyname]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Cyrillic_Core is almost fulfilled. Missing codepoints:

	- 0x0400 (CYRILLIC CAPITAL LETTER IE WITH GRAVE)


	- 0x040D (CYRILLIC CAPITAL LETTER I WITH GRAVE)


	- 0x0450 (CYRILLIC SMALL LETTER IE WITH GRAVE)
 

	- 0x045D (CYRILLIC SMALL LETTER I WITH GRAVE)
 [code: missing-codepoints]
* ⚠ **WARN** GF_TransLatin_Arabic is almost fulfilled. Missing codepoints:

	- 0x1E34 (LATIN CAPITAL LETTER K WITH LINE BELOW)


	- 0x1E35 (LATIN SMALL LETTER K WITH LINE BELOW)


	- 0x1E96 (LATIN SMALL LETTER H WITH LINE BELOW)
 

	- 0x02BD (MODIFIER LETTER REVERSED COMMA)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Mekorot ExtraBold Italic' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- CR

	- Euro.LP

	- Euro.OP

	- T_h

	- a.superior

	- aacute.sc

	- abreve.sc

	- acircumflex.sc

	- acute.case

	- acutedotaccent

	- acutedotaccent.case

	- adieresis.sc

	- aeacute.sc

	- agrave.sc

	- amacron.sc

	- ampersand.sc

	- aogonek.sc

	- aring.sc

	- aringacute.sc

	- at.case

	- at.sc

	- atilde.sc

	- b.superior

	- backslash.case

	- blacktriangle

	- braceleft.case

	- braceright.case

	- bracketleft.case

	- bracketright.case

	- breve.case

	- breveacute

	- breveacute.case

	- brevegrave

	- brevegrave.case

	- brevehookabove

	- brevehookabove.case

	- brevetilde

	- brevetilde.case

	- c.superior

	- c_h

	- c_t

	- cacute.sc

	- caron.case

	- carondotaccent

	- carondotaccent.case

	- ccaron.sc

	- ccedilla.sc

	- ccircumflex.sc

	- cdotaccent.sc

	- cent.LP

	- cent.OP

	- circumflex.case

	- circumflexhookabove

	- circumflexhookabove.case

	- circumflextilde

	- circumflextilde.case

	- d.superior

	- dcaron.sc

	- dcroat.sc

	- dieresis.case

	- dieresisacute.case

	- dieresismacron

	- dieresismacron.case

	- dollar.LP

	- dollar.OP

	- dotaccent.case

	- dotaccentmacron

	- dotaccentmacron.case

	- dotbelowcomb.case

	- dotlessi.sc

	- e.superior

	- eacute.sc

	- ebreve.sc

	- ecaron.sc

	- ecircumflex.sc

	- edieresis.sc

	- edotaccent.sc

	- egrave.sc

	- eight.LP

	- eight.OP

	- eight.subs

	- eight.sups

	- emacron.sc

	- emdash.case

	- endash.case

	- eng.sc

	- eogonek.sc

	- eth.sc

	- exclam.sc

	- exclamdown.case

	- exclamdown.sc

	- f.sc

	- f.superior

	- f_b

	- f_f_b

	- f_f_h

	- f_f_j

	- f_f_k

	- f_f_t

	- f_h

	- f_j

	- f_k

	- f_t

	- five.LP

	- five.OP

	- five.subs

	- five.sups

	- florin.LP

	- florin.OP

	- four.LP

	- four.OP

	- four.subs

	- four.sups

	- g.superior

	- gbreve.sc

	- gcaron.sc

	- gcircumflex.sc

	- gdotaccent.sc

	- germandbls.sc

	- grave.case

	- guillemotleft.case

	- guillemotright.case

	- guilsinglleft.case

	- guilsinglright.case

	- h.superior

	- hbar.sc

	- hcircumflex.sc

	- hungarumlaut.case

	- hyphen.case

	- i.loclTRK

	- i.loclTRK.sc

	- iacute.sc

	- ibreve.sc

	- icircumflex.sc

	- idieresis.sc

	- igrave.sc

	- ij.sc

	- imacron.sc

	- iogonek.sc

	- itilde.sc

	- j.superior

	- jcircumflex.sc

	- k.superior

	- kgreenlandic.sc

	- l.superior

	- lacute.sc

	- lcaron.sc

	- ldot.sc

	- lslash.sc

	- m.superior

	- macron.case

	- macronacute

	- macronacute.case

	- macrondieresis

	- macrondieresis.case

	- macrongrave

	- macrongrave.case

	- nacute.sc

	- ncaron.sc

	- nine.LP

	- nine.OP

	- nine.subs

	- nine.sups

	- ntilde.sc

	- numbersign.LP

	- numbersign.OP

	- o.superior

	- oacute.sc

	- obreve.sc

	- ocircumflex.sc

	- odieresis.sc

	- oe.sc

	- ograve.sc

	- ohungarumlaut.sc

	- omacron.sc

	- one.LP

	- one.OP

	- one.OT

	- one.subs

	- one.sups

	- oslashacute.sc

	- otilde.sc

	- p.superior

	- parenleft.case

	- parenright.case

	- periodcentered.case

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- periodcentered.loclCAT.sc

	- periodcentered.sc

	- q.sc

	- q.superior

	- question.sc

	- questiondown.case

	- questiondown.sc

	- quotedbl.sc

	- quotedblleft.sc

	- quotedblright.sc

	- quoteleft.sc

	- quoteright.sc

	- quotesingle.sc

	- r.superior

	- racute.sc

	- rcaron.sc

	- ring.case

	- s.superior

	- s_p

	- sacute.sc

	- scaron.sc

	- scedilla.sc

	- scircumflex.sc

	- seven.LP

	- seven.OP

	- seven.subs

	- seven.sups

	- six.LP

	- six.OP

	- six.subs

	- six.sups

	- slash.case

	- sterling.LP

	- sterling.OP

	- t.superior

	- tbar.sc

	- tcaron.sc

	- thorn.sc

	- three.LP

	- three.OP

	- three.subs

	- three.sups

	- tilde.case

	- tildeacute

	- tildeacute.case

	- tildedieresis

	- tildedieresis.case

	- tildemacron

	- tildemacron.case

	- two.LP

	- two.OP

	- two.subs

	- two.sups

	- u.superior

	- uacute.sc

	- ubreve.sc

	- ucircumflex.sc

	- udieresis.sc

	- ugrave.sc

	- uhungarumlaut.sc

	- umacron.sc

	- uni004A0301

	- uni006A0301

	- uni006A0301.sc

	- uni0123.sc

	- uni0137.sc

	- uni013C.sc

	- uni0146.sc

	- uni0157.sc

	- uni0163.sc

	- uni01C6.sc

	- uni01C9.sc

	- uni01CC.sc

	- uni01EB.sc

	- uni0201.sc

	- uni0203.sc

	- uni0205.sc

	- uni0207.sc

	- uni0209.sc

	- uni020B.sc

	- uni020D.sc

	- uni020F.sc

	- uni0211.sc

	- uni0213.sc

	- uni0215.sc

	- uni0217.sc

	- uni0219.sc

	- uni021B.sc

	- uni022B.sc

	- uni022D.sc

	- uni0231.sc

	- uni0233.sc

	- uni031B.case

	- uni0324.case

	- uni0326.case

	- uni0327.case

	- uni0328.case

	- uni032E.case

	- uni0331.case

	- uni0414.bgr

	- uni0416.bgr

	- uni041A.bgr

	- uni041B.bgr

	- uni0430.sc

	- uni0431.locl

	- uni0431.locl.sc

	- uni0432.bgr

	- uni0432.bgr.sc

	- uni0432.sc

	- uni0433.bgr

	- uni0433.bgr.sc

	- uni0433.locl

	- uni0433.locl.sc

	- uni0434.bgr.sc

	- uni0434.locl

	- uni0434.locl.sc

	- uni0435.sc

	- uni0436.bgr

	- uni0436.bgr.sc

	- uni0437.bgr

	- uni0437.bgr.sc

	- uni0438.bgr

	- uni0438.bgr.sc

	- uni0439.bgr

	- uni0439.bgr.sc

	- uni0439.sc

	- uni043A.bgr

	- uni043A.bgr.sc

	- uni043A.sc

	- uni043B.bgr

	- uni043B.bgr.sc

	- uni043B.sc

	- uni043C.sc

	- uni043D.bgr

	- uni043D.bgr.sc

	- uni043D.sc

	- uni043E.sc

	- uni043F.bgr

	- uni043F.bgr.sc

	- uni043F.locl

	- uni043F.locl.sc

	- uni0440.sc

	- uni0441.sc

	- uni0442.bgr

	- uni0442.bgr.sc

	- uni0442.locl

	- uni0442.locl.sc

	- uni0442.sc

	- uni0444.sc

	- uni0445.sc

	- uni0446.bgr

	- uni0446.bgr.sc

	- uni0447.bgr

	- uni0447.bgr.sc

	- uni0448.bgr

	- uni0448.bgr.sc

	- uni0449.bgr

	- uni0449.bgr.sc

	- uni044A.bgr

	- uni044A.bgr.sc

	- uni044B.sc

	- uni044C.bgr

	- uni044C.bgr.sc

	- uni044D.sc

	- uni044E.bgr

	- uni044E.bgr.sc

	- uni044F.sc

	- uni0451.sc

	- uni0452.sc

	- uni0453.sc

	- uni0454.sc

	- uni0455.sc

	- uni0456.sc

	- uni0457.sc

	- uni0458.sc

	- uni0459.sc

	- uni045A.sc

	- uni045B.sc

	- uni045C.sc

	- uni045E.sc

	- uni045F.sc

	- uni0463.sc

	- uni0473.sc

	- uni0475.sc

	- uni0491.sc

	- uni0493.sc

	- uni0497.sc

	- uni049B.sc

	- uni04A3.sc

	- uni04AF.sc

	- uni04B1.sc

	- uni04B3.sc

	- uni04B7.sc

	- uni04BB.sc

	- uni04CF.sc

	- uni04D9.sc

	- uni04E3.sc

	- uni04E9.sc

	- uni04EF.sc

	- uni1E09.sc

	- uni1E0D.sc

	- uni1E0F.sc

	- uni1E15.sc

	- uni1E17.sc

	- uni1E1D.sc

	- uni1E21.sc

	- uni1E25.sc

	- uni1E2B.sc

	- uni1E2F.sc

	- uni1E37.sc

	- uni1E3B.sc

	- uni1E43.sc

	- uni1E45.sc

	- uni1E47.sc

	- uni1E49.sc

	- uni1E4D.sc

	- uni1E4F.sc

	- uni1E51.sc

	- uni1E53.sc

	- uni1E5B.sc

	- uni1E5F.sc

	- uni1E61.sc

	- uni1E63.sc

	- uni1E65.sc

	- uni1E67.sc

	- uni1E69.sc

	- uni1E6D.sc

	- uni1E6F.sc

	- uni1E79.sc

	- uni1E7B.sc

	- uni1E8F.sc

	- uni1E93.sc

	- uni1E97.sc

	- uni1EA1.sc

	- uni1EA3.sc

	- uni1EA5.sc

	- uni1EA7.sc

	- uni1EA9.sc

	- uni1EAB.sc

	- uni1EAD.sc

	- uni1EAF.sc

	- uni1EB1.sc

	- uni1EB3.sc

	- uni1EB5.sc

	- uni1EB7.sc

	- uni1EB9.sc

	- uni1EBB.sc

	- uni1EBD.sc

	- uni1EBF.sc

	- uni1EC1.sc

	- uni1EC3.sc

	- uni1EC5.sc

	- uni1EC7.sc

	- uni1EC9.sc

	- uni1ECB.sc

	- uni1ECD.sc

	- uni1ECF.sc

	- uni1ED1.sc

	- uni1ED3.sc

	- uni1ED5.sc

	- uni1ED7.sc

	- uni1ED9.sc

	- uni1EDB.sc

	- uni1EDD.sc

	- uni1EDF.sc

	- uni1EE1.sc

	- uni1EE3.sc

	- uni1EE5.sc

	- uni1EE7.sc

	- uni1EE9.sc

	- uni1EEB.sc

	- uni1EED.sc

	- uni1EEF.sc

	- uni1EF1.sc

	- uni1EF5.sc

	- uni1EF7.sc

	- uni1EF9.sc

	- uni20B4.LP

	- uni20B4.OP

	- uni20B8.LP

	- uni20B8.OP

	- uni20BD.LP

	- uni20BD.OP

	- uni2116

	- uni2116.LP

	- uni2116.OP

	- uni2116.OT

	- uogonek.sc

	- uring.sc

	- utilde.sc

	- v.sc

	- v.superior

	- w.superior

	- wacute.sc

	- wcircumflex.sc

	- wdieresis.sc

	- wgrave.sc

	- whitetriangle

	- x.superior

	- y.superior

	- yacute.sc

	- ycircumflex.sc

	- ydieresis.sc

	- yen.LP

	- yen.OP

	- ygrave.sc

	- z.superior

	- zacute.sc

	- zcaron.sc

	- zdotaccent.sc

	- zero.LP

	- zero.OP

	- zero.slashLP

	- zero.slashOP

	- zero.subs 

	- zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: uni01C6	Contours detected: 5	Expected: 4

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0F	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: d	Contours detected: 3	Expected: 2

	- Glyph name: dcaron	Contours detected: 4	Expected: 3

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni01C6	Contours detected: 5	Expected: 4

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni0496	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E0F	Contours detected: 4	Expected: 3 

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* ⚠ **WARN** OS/2 sTypoLineGap is not equal to 0. [code: OS/2]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* X (U+0058): L<<306.0,261.0>--<117.0,59.0>> -> L<<117.0,59.0>--<113.0,55.0>>

	* uni0425 (U+0425): L<<306.0,261.0>--<117.0,59.0>> -> L<<117.0,59.0>--<113.0,55.0>> 

	* uni04B2 (U+04B2): L<<306.0,261.0>--<117.0,59.0>> -> L<<117.0,59.0>--<113.0,55.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* d (U+0064): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* d (U+0064): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* dcaron (U+010F): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* dcaron (U+010F): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* dcroat (U+0111): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* dcroat (U+0111): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* dong (U+20AB): B<<322.0,351.0>-<320.0,355.0>-<317.0,358.0>>/L<<317.0,358.0>--<322.0,351.0>> = 9.462322208025574

	* dong (U+20AB): L<<317.0,358.0>--<322.0,351.0>>/B<<322.0,351.0>-<320.0,355.0>-<317.0,358.0>> = 8.972626614896358

	* three (U+0033): B<<427.5,389.0>-<379.0,367.0>-<318.0,360.0>>/B<<318.0,360.0>-<416.0,349.0>-<463.5,310.0>> = 12.950643509678146

	* threeeighths (U+215C): B<<314.5,595.5>-<274.0,570.0>-<214.0,565.0>>/B<<214.0,565.0>-<282.0,560.0>-<312.5,537.5>> = 8.968998692434685

	* threequarters (U+00BE): B<<314.5,595.5>-<274.0,570.0>-<214.0,565.0>>/B<<214.0,565.0>-<282.0,560.0>-<312.5,537.5>> = 8.968998692434685

	* uni00B3 (U+00B3): B<<341.5,745.5>-<301.0,720.0>-<241.0,715.0>>/B<<241.0,715.0>-<309.0,710.0>-<339.5,687.5>> = 8.968998692434685

	* uni01C6 (U+01C6): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* uni01C6 (U+01C6): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* uni0417 (U+0417): B<<497.0,380.5>-<448.0,353.0>-<377.0,344.0>>/B<<377.0,344.0>-<471.0,335.0>-<521.0,298.0>> = 12.693410664157241

	* uni1E0D (U+1E0D): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* uni1E0D (U+1E0D): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* uni1E0F (U+1E0F): B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>>/L<<354.0,401.0>--<359.0,394.0>> = 9.462322208025574

	* uni1E0F (U+1E0F): L<<354.0,401.0>--<359.0,394.0>>/B<<359.0,394.0>-<357.0,398.0>-<354.0,401.0>> = 8.972626614896358

	* uni2083 (U+2083): B<<211.5,10.5>-<171.0,-15.0>-<111.0,-20.0>>/B<<111.0,-20.0>-<179.0,-25.0>-<209.5,-47.5>> = 8.968998692434685

	* uni2153 (U+2153): B<<687.5,240.5>-<647.0,215.0>-<587.0,210.0>>/B<<587.0,210.0>-<655.0,205.0>-<685.5,182.5>> = 8.968998692434685

	* uni2154 (U+2154): B<<709.5,240.5>-<669.0,215.0>-<609.0,210.0>>/B<<609.0,210.0>-<677.0,205.0>-<707.5,182.5>> = 8.968998692434685

	* uni2782 (U+2782): B<<559.5,420.5>-<519.0,395.0>-<459.0,390.0>>/B<<459.0,390.0>-<527.0,385.0>-<557.5,362.5>> = 8.968998692434685 

	* uni278C (U+278C): B<<557.5,362.5>-<527.0,385.0>-<459.0,390.0>>/B<<459.0,390.0>-<519.0,395.0>-<559.5,420.5>> = 8.968998692434685 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 33 | 95 | 1192 | 61 | 926 | 0 |
| 0% | 1% | 4% | 52% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
