## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[8] Mekorot-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x02D9 (DOT ABOVE)


	- 0x0307 (COMBINING DOT ABOVE)


	- 0x030C (COMBINING CARON)


	- 0x0306 (COMBINING BREVE)


	- 0x0312 (COMBINING TURNED COMMA ABOVE)


	- 0x0326 (COMBINING COMMA BELOW)


	- 0x0328 (COMBINING OGONEK)


	- 0x02DD (DOUBLE ACUTE ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)
 

	- And 0x02DB (OGONEK)
 [code: missing-codepoints]
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

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- three.sups 

	- And zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2 

	- And Glyph name: zdotaccent	Contours detected: 0	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<475.0,307.0>--<476.0,552.0>>

	* m (U+006D): L<<676.0,68.0>--<677.0,296.0>>

	* m (U+006D): L<<790.0,329.0>--<789.0,68.0>>

	* thorn (U+00FE): L<<218.0,734.0>--<217.0,419.0>>

	* uni00B5 (U+00B5): L<<78.0,-213.0>--<77.0,433.0>> 

	* And uni03BC (U+03BC): L<<78.0,-213.0>--<77.0,433.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Mekorot-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x02D9 (DOT ABOVE)


	- 0x0307 (COMBINING DOT ABOVE)


	- 0x030C (COMBINING CARON)


	- 0x0306 (COMBINING BREVE)


	- 0x0312 (COMBINING TURNED COMMA ABOVE)


	- 0x0326 (COMBINING COMMA BELOW)


	- 0x0328 (COMBINING OGONEK)


	- 0x02DD (DOUBLE ACUTE ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)
 

	- And 0x02DB (OGONEK)
 [code: missing-codepoints]
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

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- three.sups 

	- And zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2 

	- And Glyph name: zdotaccent	Contours detected: 0	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* U (U+0055): L<<310.0,585.0>--<311.0,291.0>>

	* Uacute (U+00DA): L<<310.0,585.0>--<311.0,291.0>>

	* Ucircumflex (U+00DB): L<<310.0,585.0>--<311.0,291.0>>

	* Udieresis (U+00DC): L<<310.0,585.0>--<311.0,291.0>>

	* Ugrave (U+00D9): L<<310.0,585.0>--<311.0,291.0>>

	* m (U+006D): L<<669.0,68.0>--<670.0,296.0>>

	* m (U+006D): L<<850.0,329.0>--<849.0,68.0>>

	* uni00B5 (U+00B5): L<<49.0,-214.0>--<48.0,440.0>> 

	* And uni03BC (U+03BC): L<<49.0,-214.0>--<48.0,440.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Mekorot-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x02D9 (DOT ABOVE)


	- 0x0307 (COMBINING DOT ABOVE)


	- 0x030C (COMBINING CARON)


	- 0x0306 (COMBINING BREVE)


	- 0x0312 (COMBINING TURNED COMMA ABOVE)


	- 0x0326 (COMBINING COMMA BELOW)


	- 0x0328 (COMBINING OGONEK)


	- 0x02DD (DOUBLE ACUTE ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)
 

	- And 0x02DB (OGONEK)
 [code: missing-codepoints]
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

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- three.sups 

	- And zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2 

	- And Glyph name: zdotaccent	Contours detected: 0	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<475.0,305.0>--<477.0,549.0>>

	* U (U+0055): L<<285.0,585.0>--<286.0,284.0>>

	* Uacute (U+00DA): L<<285.0,585.0>--<286.0,284.0>>

	* Ucircumflex (U+00DB): L<<285.0,585.0>--<286.0,284.0>>

	* Udieresis (U+00DC): L<<285.0,585.0>--<286.0,284.0>>

	* Ugrave (U+00D9): L<<285.0,585.0>--<286.0,284.0>>

	* m (U+006D): L<<672.0,68.0>--<673.0,296.0>>

	* m (U+006D): L<<820.0,329.0>--<819.0,68.0>>

	* uni00B5 (U+00B5): L<<64.0,-213.0>--<62.0,437.0>> 

	* And uni03BC (U+03BC): L<<64.0,-213.0>--<62.0,437.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Mekorot-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x02D9 (DOT ABOVE)


	- 0x0307 (COMBINING DOT ABOVE)


	- 0x030C (COMBINING CARON)


	- 0x0306 (COMBINING BREVE)


	- 0x0312 (COMBINING TURNED COMMA ABOVE)


	- 0x0326 (COMBINING COMMA BELOW)


	- 0x0328 (COMBINING OGONEK)


	- 0x02DD (DOUBLE ACUTE ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)
 

	- And 0x02DB (OGONEK)
 [code: missing-codepoints]
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

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- three.sups 

	- And zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2 

	- And Glyph name: zdotaccent	Contours detected: 0	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* m (U+006D): L<<679.0,68.0>--<680.0,296.0>>

	* m (U+006D): L<<760.0,329.0>--<759.0,68.0>>

	* thorn (U+00FE): L<<192.0,734.0>--<191.0,414.0>>

	* uni00B5 (U+00B5): L<<93.0,-212.0>--<91.0,430.0>> 

	* And uni03BC (U+03BC): L<<93.0,-212.0>--<91.0,430.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[8] Mekorot-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


	- 0x02D9 (DOT ABOVE)


	- 0x0307 (COMBINING DOT ABOVE)


	- 0x030C (COMBINING CARON)


	- 0x0306 (COMBINING BREVE)


	- 0x0312 (COMBINING TURNED COMMA ABOVE)


	- 0x0326 (COMBINING COMMA BELOW)


	- 0x0328 (COMBINING OGONEK)


	- 0x02DD (DOUBLE ACUTE ACCENT)


	- 0x02C7 (CARON)


	- 0x02D8 (BREVE)
 

	- And 0x02DB (OGONEK)
 [code: missing-codepoints]
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

	- periodcentered.loclCAT

	- periodcentered.loclCAT.case

	- three.sups 

	- And zero.sups
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character (codepoint 0x00AD) which is supposed to be zero-width and invisible, and is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation. It is mostly an obsolete mechanism now, and the character is only included in fonts for legacy codepage coverage. [code: softhyphen]
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: scedilla	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: Abreve	Contours detected: 0	Expected: 3

	- Glyph name: Amacron	Contours detected: 0	Expected: 3

	- Glyph name: Aogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: Cacute	Contours detected: 0	Expected: 2

	- Glyph name: Ccaron	Contours detected: 0	Expected: 2

	- Glyph name: Cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Dcaron	Contours detected: 0	Expected: 3

	- Glyph name: Dcroat	Contours detected: 0	Expected: 2

	- Glyph name: Ecaron	Contours detected: 0	Expected: 2

	- Glyph name: Edotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Emacron	Contours detected: 0	Expected: 2

	- Glyph name: Eng	Contours detected: 0	Expected: 1

	- Glyph name: Eogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Gbreve	Contours detected: 0	Expected: 2

	- Glyph name: Gdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Hbar	Contours detected: 0	Expected: 2

	- Glyph name: IJ	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Idotaccent	Contours detected: 0	Expected: 2

	- Glyph name: Imacron	Contours detected: 0	Expected: 2

	- Glyph name: Iogonek	Contours detected: 0	Expected: 1 or 2

	- Glyph name: Lacute	Contours detected: 0	Expected: 2

	- Glyph name: Lcaron	Contours detected: 0	Expected: 2

	- Glyph name: Lslash	Contours detected: 0	Expected: 1

	- Glyph name: Nacute	Contours detected: 0	Expected: 2

	- Glyph name: Ncaron	Contours detected: 0	Expected: 2

	- Glyph name: Ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: Omacron	Contours detected: 0	Expected: 3

	- Glyph name: Racute	Contours detected: 0	Expected: 3

	- Glyph name: Rcaron	Contours detected: 0	Expected: 3

	- Glyph name: Sacute	Contours detected: 0	Expected: 2

	- Glyph name: Scaron	Contours detected: 0	Expected: 2

	- Glyph name: Tcaron	Contours detected: 0	Expected: 2

	- Glyph name: Ubreve	Contours detected: 0	Expected: 2

	- Glyph name: Uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: Umacron	Contours detected: 0	Expected: 2

	- Glyph name: Uogonek	Contours detected: 0	Expected: 1

	- Glyph name: Uring	Contours detected: 0	Expected: 3

	- Glyph name: Wacute	Contours detected: 0	Expected: 2

	- Glyph name: Wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: Wgrave	Contours detected: 0	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 0	Expected: 3

	- Glyph name: Ygrave	Contours detected: 0	Expected: 2

	- Glyph name: Zacute	Contours detected: 0	Expected: 2

	- Glyph name: Zcaron	Contours detected: 0	Expected: 2

	- Glyph name: Zdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: abreve	Contours detected: 0	Expected: 3

	- Glyph name: amacron	Contours detected: 0	Expected: 3

	- Glyph name: aogonek	Contours detected: 0	Expected: 2

	- Glyph name: cacute	Contours detected: 0	Expected: 2

	- Glyph name: ccaron	Contours detected: 0	Expected: 2

	- Glyph name: cdotaccent	Contours detected: 0	Expected: 2

	- Glyph name: dcaron	Contours detected: 0	Expected: 3

	- Glyph name: dcroat	Contours detected: 0	Expected: 2

	- Glyph name: ecaron	Contours detected: 0	Expected: 3

	- Glyph name: edotaccent	Contours detected: 0	Expected: 3

	- Glyph name: emacron	Contours detected: 0	Expected: 3

	- Glyph name: eng	Contours detected: 0	Expected: 1

	- Glyph name: eogonek	Contours detected: 0	Expected: 2

	- Glyph name: gbreve	Contours detected: 0	Expected: 3 or 4

	- Glyph name: gdotaccent	Contours detected: 0	Expected: 3 or 4

	- Glyph name: hbar	Contours detected: 0	Expected: 1

	- Glyph name: ij	Contours detected: 0	Expected: 3 or 4

	- Glyph name: imacron	Contours detected: 0	Expected: 2

	- Glyph name: iogonek	Contours detected: 0	Expected: 2 or 3

	- Glyph name: lacute	Contours detected: 0	Expected: 2

	- Glyph name: lcaron	Contours detected: 0	Expected: 2

	- Glyph name: lslash	Contours detected: 0	Expected: 1

	- Glyph name: nacute	Contours detected: 0	Expected: 2

	- Glyph name: ncaron	Contours detected: 0	Expected: 2

	- Glyph name: ohungarumlaut	Contours detected: 0	Expected: 4

	- Glyph name: omacron	Contours detected: 0	Expected: 3

	- Glyph name: racute	Contours detected: 0	Expected: 2

	- Glyph name: rcaron	Contours detected: 0	Expected: 2

	- Glyph name: sacute	Contours detected: 0	Expected: 2

	- Glyph name: scaron	Contours detected: 0	Expected: 2

	- Glyph name: tcaron	Contours detected: 0	Expected: 2

	- Glyph name: trademark	Contours detected: 0	Expected: 2

	- Glyph name: ubreve	Contours detected: 0	Expected: 2

	- Glyph name: uhungarumlaut	Contours detected: 0	Expected: 3

	- Glyph name: umacron	Contours detected: 0	Expected: 2

	- Glyph name: uni0122	Contours detected: 0	Expected: 2

	- Glyph name: uni0123	Contours detected: 0	Expected: 3 or 4

	- Glyph name: uni0136	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni0137	Contours detected: 0	Expected: 2 or 3

	- Glyph name: uni013B	Contours detected: 0	Expected: 2

	- Glyph name: uni013C	Contours detected: 0	Expected: 2

	- Glyph name: uni0145	Contours detected: 0	Expected: 2

	- Glyph name: uni0146	Contours detected: 0	Expected: 2

	- Glyph name: uni0156	Contours detected: 0	Expected: 3

	- Glyph name: uni0157	Contours detected: 0	Expected: 2

	- Glyph name: uni0218	Contours detected: 0	Expected: 2

	- Glyph name: uni0219	Contours detected: 0	Expected: 2

	- Glyph name: uni021A	Contours detected: 0	Expected: 2

	- Glyph name: uni021B	Contours detected: 0	Expected: 2

	- Glyph name: uni0237	Contours detected: 0	Expected: 1

	- Glyph name: uni1E9E	Contours detected: 0	Expected: 1

	- Glyph name: uogonek	Contours detected: 0	Expected: 1

	- Glyph name: uring	Contours detected: 0	Expected: 3

	- Glyph name: wacute	Contours detected: 0	Expected: 2

	- Glyph name: wcircumflex	Contours detected: 0	Expected: 2

	- Glyph name: wdieresis	Contours detected: 0	Expected: 3

	- Glyph name: wgrave	Contours detected: 0	Expected: 2

	- Glyph name: ycircumflex	Contours detected: 0	Expected: 2

	- Glyph name: ygrave	Contours detected: 0	Expected: 2

	- Glyph name: zacute	Contours detected: 0	Expected: 2

	- Glyph name: zcaron	Contours detected: 0	Expected: 2 

	- And Glyph name: zdotaccent	Contours detected: 0	Expected: 2
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* m (U+006D): L<<671.0,68.0>--<672.0,296.0>>

	* m (U+006D): L<<835.0,329.0>--<834.0,68.0>>

	* uni00B5 (U+00B5): L<<56.0,-214.0>--<55.0,438.0>> 

	* And uni03BC (U+03BC): L<<56.0,-214.0>--<55.0,438.0>> [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 5 | 35 | 557 | 31 | 447 | 0 |
| 0% | 0% | 3% | 52% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
