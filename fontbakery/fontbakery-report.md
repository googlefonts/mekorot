## Fontbakery report

Fontbakery version: 0.8.4

<details>
<summary><b>[5] Mekorot-SemiBold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - NULL
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: uni00B2	Contours detected: 0	Expected: 1
 - Glyph name: uni00B3	Contours detected: 0	Expected: 1
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: uni00B9	Contours detected: 0	Expected: 1
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: uni2074	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2 
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 [code: contour-count]

</details>
<br>
</details>
<details>
<summary><b>[5] Mekorot-ExtraBold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - NULL
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: uni00B2	Contours detected: 0	Expected: 1
 - Glyph name: uni00B3	Contours detected: 0	Expected: 1
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: uni00B9	Contours detected: 0	Expected: 1
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: uni2074	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2 
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 [code: contour-count]

</details>
<br>
</details>
<details>
<summary><b>[5] Mekorot-Medium.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - NULL
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: uni00B2	Contours detected: 0	Expected: 1
 - Glyph name: uni00B3	Contours detected: 0	Expected: 1
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: uni00B9	Contours detected: 0	Expected: 1
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: uni2074	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2 
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 [code: contour-count]

</details>
<br>
</details>
<details>
<summary><b>[5] Mekorot-Regular.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - NULL
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: uni00B2	Contours detected: 0	Expected: 1
 - Glyph name: uni00B3	Contours detected: 0	Expected: 1
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: uni00B9	Contours detected: 0	Expected: 1
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: uni2074	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2 
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 [code: contour-count]

</details>
<br>
</details>
<details>
<summary><b>[5] Mekorot-Bold.ttf</b></summary>
<details>
<summary>⚠ <b>WARN:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/vendor_id](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id)
<pre>--- Rationale ---
Microsoft keeps a list of font vendors and their respective contact info. This
list is updated regularly and is indexed by a 4-char &quot;Vendor ID&quot; which is stored
in the achVendID field of the OS/2 table.
Registering your ID is not mandatory, but it is a good practice since some
applications may display the type designer / type foundry contact info on some
dialog and also because that info will be visible on Microsoft&#x27;s website:
https://docs.microsoft.com/en-us/typography/vendors/
This check verifies whether or not a given font&#x27;s vendor ID is registered in
that list or if it has some of the default values used by the most common font
editors.
Each new FontBakery release includes a cached copy of that list of vendor IDs.
If you registered recently, you&#x27;re safe to ignore warnings emitted by this
check, since your ID will soon be included in one of our upcoming releases.</pre>

* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]

</details>
<details>
<summary>⚠ <b>WARN:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/old_ttfautohint](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/old_ttfautohint)
<pre>--- Rationale ---
Check if font has been hinted with an outdated version of ttfautohint.</pre>

* ⚠ **WARN** ttfautohint used in font = 1.8.3; latest = 1.8.4; Need to re-run with the newer version! [code: old-ttfa]

</details>
<details>
<summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table.</summary>

* [com.google.fonts/check/meta/script_lang_tags](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags)
<pre>--- Rationale ---
The OpenType &#x27;meta&#x27; table originated at Apple. Microsoft added it to OT with
just two DataMap records:
- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font is designed for
- slng: comma-separated ScriptLangTags that indicate which scripts, or languages
and scripts, with possible variants, the font supports
The slng structure is intended to describe which languages and scripts the font
overall supports. For example, a Traditional Chinese font that also contains
Latin characters, can indicate Hant,Latn, showing that it supports Hant, the
Traditional Chinese variant of the Hani script, and it also supports the Latn
script
The dlng structure is far more interesting. A font may contain various glyphs,
but only a particular subset of the glyphs may be truly &quot;leading&quot; in the design,
while other glyphs may have been included for technical reasons. Such a
Traditional Chinese font could only list Hant there, showing that it’s designed
for Traditional Chinese, but the font would omit Latn, because the developers
don’t think the font is really recommended for purely Latin-script use.
The tags used in the structures can comprise just script, or also language and
script. For example, if a font has Bulgarian Cyrillic alternates in the locl
feature for the cyrl BGR OT languagesystem, it could also indicate in dlng
explicitly that it supports bul-Cyrl. (Note that the scripts and languages in
meta use the ISO language and script codes, not the OpenType ones).
This check ensures that the font has the meta table containing the slng and dlng
structures.
All families in the Google Fonts collection should contain the &#x27;meta&#x27; table.
Windows 10 already uses it when deciding on which fonts to fall back to. The
Google Fonts API and also other environments could use the data for smarter
filtering. Most importantly, those entries should be added to the Noto fonts.
In the font making process, some environments store this data in external files
already. But the meta table provides a convenient way to store this inside the
font file, so some tools may add the data, and unrelated tools may read this
data. This makes the solution much more portable and universal.</pre>

* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs</summary>

* [com.google.fonts/check/unreachable_glyphs](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs)
<pre>--- Rationale ---
Glyphs are either accessible directly through Unicode codepoints or through
substitution rules. Any glyphs not accessible by either of these means are
redundant and serve only to increase the font&#x27;s file size.</pre>

* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:
 - NULL
 [code: unreachable-glyphs]

</details>
<details>
<summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/contour_count](https://font-bakery.readthedocs.io/en/latest/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count)
<pre>--- Rationale ---
Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be
constructured in a handful of ways. This means a glyph&#x27;s contour count will only
differ slightly amongst different fonts, e.g a &#x27;g&#x27; could either be 2 or 3
contours, depending on whether its double story or single story.
However, a quotedbl should have 2 contours, unless the font belongs to a display
family.
This check currently does not cover variable fonts because there&#x27;s plenty of
alternative ways of constructing glyphs with multiple outlines for each feature
in a VarFont. The expected contour count data for this check is currently
optimized for the typical construction of glyphs in static fonts.</pre>

* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: uni00B2	Contours detected: 0	Expected: 1
 - Glyph name: uni00B3	Contours detected: 0	Expected: 1
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: uni00B9	Contours detected: 0	Expected: 1
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: uni2074	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: AE	Contours detected: 0	Expected: 2
 - Glyph name: Aacute	Contours detected: 0	Expected: 3
 - Glyph name: Acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Adieresis	Contours detected: 0	Expected: 4
 - Glyph name: Agrave	Contours detected: 0	Expected: 3
 - Glyph name: Aring	Contours detected: 0	Expected: 3 or 4
 - Glyph name: Atilde	Contours detected: 0	Expected: 3
 - Glyph name: Ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Eacute	Contours detected: 0	Expected: 2
 - Glyph name: Ecircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Edieresis	Contours detected: 0	Expected: 3
 - Glyph name: Egrave	Contours detected: 0	Expected: 2
 - Glyph name: Eth	Contours detected: 0	Expected: 2
 - Glyph name: Euro	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Iacute	Contours detected: 0	Expected: 2
 - Glyph name: Icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Idieresis	Contours detected: 0	Expected: 3
 - Glyph name: Igrave	Contours detected: 0	Expected: 2
 - Glyph name: Ntilde	Contours detected: 0	Expected: 2
 - Glyph name: OE	Contours detected: 0	Expected: 2
 - Glyph name: Oacute	Contours detected: 0	Expected: 3
 - Glyph name: Ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: Odieresis	Contours detected: 0	Expected: 4
 - Glyph name: Ograve	Contours detected: 0	Expected: 3
 - Glyph name: Oslash	Contours detected: 0	Expected: 2 or 3
 - Glyph name: Otilde	Contours detected: 0	Expected: 3
 - Glyph name: Thorn	Contours detected: 0	Expected: 1 or 2
 - Glyph name: Uacute	Contours detected: 0	Expected: 2
 - Glyph name: Ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: Udieresis	Contours detected: 0	Expected: 3
 - Glyph name: Ugrave	Contours detected: 0	Expected: 2
 - Glyph name: Yacute	Contours detected: 0	Expected: 2
 - Glyph name: aacute	Contours detected: 0	Expected: 3
 - Glyph name: acircumflex	Contours detected: 0	Expected: 3
 - Glyph name: acute	Contours detected: 0	Expected: 1
 - Glyph name: adieresis	Contours detected: 0	Expected: 4
 - Glyph name: ae	Contours detected: 0	Expected: 3
 - Glyph name: agrave	Contours detected: 0	Expected: 3
 - Glyph name: ampersand	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: aring	Contours detected: 0	Expected: 4
 - Glyph name: asciicircum	Contours detected: 0	Expected: 1
 - Glyph name: asciitilde	Contours detected: 0	Expected: 1
 - Glyph name: asterisk	Contours detected: 0	Expected: 1 or 4
 - Glyph name: at	Contours detected: 0	Expected: 2
 - Glyph name: atilde	Contours detected: 0	Expected: 3
 - Glyph name: backslash	Contours detected: 0	Expected: 1
 - Glyph name: bar	Contours detected: 0	Expected: 1
 - Glyph name: braceleft	Contours detected: 0	Expected: 1
 - Glyph name: braceright	Contours detected: 0	Expected: 1
 - Glyph name: bracketleft	Contours detected: 0	Expected: 1
 - Glyph name: bracketright	Contours detected: 0	Expected: 1
 - Glyph name: brokenbar	Contours detected: 0	Expected: 2
 - Glyph name: bullet	Contours detected: 0	Expected: 1
 - Glyph name: ccedilla	Contours detected: 0	Expected: 1 or 2
 - Glyph name: cedilla	Contours detected: 0	Expected: 1
 - Glyph name: cent	Contours detected: 0	Expected: 1 or 2
 - Glyph name: circumflex	Contours detected: 0	Expected: 1
 - Glyph name: colon	Contours detected: 0	Expected: 2
 - Glyph name: copyright	Contours detected: 0	Expected: 3
 - Glyph name: currency	Contours detected: 0	Expected: 2
 - Glyph name: degree	Contours detected: 0	Expected: 2
 - Glyph name: dieresis	Contours detected: 0	Expected: 2
 - Glyph name: divide	Contours detected: 0	Expected: 3
 - Glyph name: dollar	Contours detected: 0	Expected: 1 or 3
 - Glyph name: dotlessi	Contours detected: 0	Expected: 1
 - Glyph name: eacute	Contours detected: 0	Expected: 3
 - Glyph name: ecircumflex	Contours detected: 0	Expected: 3
 - Glyph name: edieresis	Contours detected: 0	Expected: 4
 - Glyph name: egrave	Contours detected: 0	Expected: 3
 - Glyph name: eight	Contours detected: 0	Expected: 3
 - Glyph name: ellipsis	Contours detected: 0	Expected: 3
 - Glyph name: emdash	Contours detected: 0	Expected: 1
 - Glyph name: endash	Contours detected: 0	Expected: 1
 - Glyph name: equal	Contours detected: 0	Expected: 2
 - Glyph name: eth	Contours detected: 0	Expected: 2
 - Glyph name: exclam	Contours detected: 0	Expected: 2
 - Glyph name: exclamdown	Contours detected: 0	Expected: 2
 - Glyph name: five	Contours detected: 0	Expected: 1
 - Glyph name: four	Contours detected: 0	Expected: 1 or 2
 - Glyph name: fraction	Contours detected: 0	Expected: 1
 - Glyph name: germandbls	Contours detected: 0	Expected: 1
 - Glyph name: grave	Contours detected: 0	Expected: 1
 - Glyph name: greater	Contours detected: 0	Expected: 1
 - Glyph name: guillemotleft	Contours detected: 0	Expected: 2
 - Glyph name: guillemotright	Contours detected: 0	Expected: 2
 - Glyph name: guilsinglleft	Contours detected: 0	Expected: 1
 - Glyph name: guilsinglright	Contours detected: 0	Expected: 1
 - Glyph name: hyphen	Contours detected: 0	Expected: 1
 - Glyph name: iacute	Contours detected: 0	Expected: 2
 - Glyph name: icircumflex	Contours detected: 0	Expected: 2
 - Glyph name: idieresis	Contours detected: 0	Expected: 3
 - Glyph name: igrave	Contours detected: 0	Expected: 2
 - Glyph name: less	Contours detected: 0	Expected: 1
 - Glyph name: logicalnot	Contours detected: 0	Expected: 1
 - Glyph name: macron	Contours detected: 0	Expected: 1
 - Glyph name: minus	Contours detected: 0	Expected: 1
 - Glyph name: multiply	Contours detected: 0	Expected: 1
 - Glyph name: nine	Contours detected: 0	Expected: 1 or 2
 - Glyph name: ntilde	Contours detected: 0	Expected: 2
 - Glyph name: numbersign	Contours detected: 0	Expected: 2
 - Glyph name: oacute	Contours detected: 0	Expected: 3
 - Glyph name: ocircumflex	Contours detected: 0	Expected: 3
 - Glyph name: odieresis	Contours detected: 0	Expected: 4
 - Glyph name: oe	Contours detected: 0	Expected: 3
 - Glyph name: ograve	Contours detected: 0	Expected: 3
 - Glyph name: one	Contours detected: 0	Expected: 1
 - Glyph name: onehalf	Contours detected: 0	Expected: 3
 - Glyph name: onequarter	Contours detected: 0	Expected: 3 or 4
 - Glyph name: oslash	Contours detected: 0	Expected: 3
 - Glyph name: otilde	Contours detected: 0	Expected: 3
 - Glyph name: paragraph	Contours detected: 0	Expected: 1, 2 or 3
 - Glyph name: parenleft	Contours detected: 0	Expected: 1
 - Glyph name: parenright	Contours detected: 0	Expected: 1
 - Glyph name: percent	Contours detected: 0	Expected: 5
 - Glyph name: period	Contours detected: 0	Expected: 1
 - Glyph name: periodcentered	Contours detected: 0	Expected: 1
 - Glyph name: plus	Contours detected: 0	Expected: 1
 - Glyph name: plusminus	Contours detected: 0	Expected: 1 or 2
 - Glyph name: question	Contours detected: 0	Expected: 2
 - Glyph name: questiondown	Contours detected: 0	Expected: 2
 - Glyph name: quotedbl	Contours detected: 0	Expected: 2
 - Glyph name: quotedblbase	Contours detected: 0	Expected: 2
 - Glyph name: quotedblleft	Contours detected: 0	Expected: 2
 - Glyph name: quotedblright	Contours detected: 0	Expected: 2
 - Glyph name: quoteleft	Contours detected: 0	Expected: 1
 - Glyph name: quoteright	Contours detected: 0	Expected: 1
 - Glyph name: quotesinglbase	Contours detected: 0	Expected: 1
 - Glyph name: quotesingle	Contours detected: 0	Expected: 1
 - Glyph name: registered	Contours detected: 0	Expected: 3 or 4
 - Glyph name: ring	Contours detected: 0	Expected: 2
 - Glyph name: section	Contours detected: 0	Expected: 2
 - Glyph name: semicolon	Contours detected: 0	Expected: 2
 - Glyph name: seven	Contours detected: 0	Expected: 1
 - Glyph name: six	Contours detected: 0	Expected: 1 or 2
 - Glyph name: slash	Contours detected: 0	Expected: 1
 - Glyph name: sterling	Contours detected: 0	Expected: 1 or 2
 - Glyph name: thorn	Contours detected: 0	Expected: 2
 - Glyph name: three	Contours detected: 0	Expected: 1
 - Glyph name: threequarters	Contours detected: 0	Expected: 3 or 4
 - Glyph name: tilde	Contours detected: 0	Expected: 1
 - Glyph name: two	Contours detected: 0	Expected: 1
 - Glyph name: uacute	Contours detected: 0	Expected: 2
 - Glyph name: ucircumflex	Contours detected: 0	Expected: 2
 - Glyph name: udieresis	Contours detected: 0	Expected: 3
 - Glyph name: ugrave	Contours detected: 0	Expected: 2
 - Glyph name: underscore	Contours detected: 0	Expected: 1
 - Glyph name: uni00B5	Contours detected: 0	Expected: 1
 - Glyph name: uni2215	Contours detected: 0	Expected: 1
 - Glyph name: yacute	Contours detected: 0	Expected: 2
 - Glyph name: ydieresis	Contours detected: 0	Expected: 3
 - Glyph name: yen	Contours detected: 0	Expected: 1 or 2 
 - Glyph name: zero	Contours detected: 0	Expected: 2 or 3
 [code: contour-count]

</details>
<br>
</details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 25 | 518 | 31 | 462 | 0 |
| 0% | 0% | 2% | 50% | 3% | 45% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
