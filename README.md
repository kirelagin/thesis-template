HOWTO
======

*   Install XeTeX, Pandoc and other stuff.
*   `./waf configure`
*   while `./waf` is not succeeding

    * install missing stuff

*   while not happy with your text

    * Edit `.pd` files
    * _(sometimes)_ Edit `.latex` files
    * _(sometimes)_ Update `sources` in `wscript`
    * `./waf`



Nice links
===========

* [The Waf Book](https://waf.io/book/)
* Always feel free to refer to the [real-life example](https://github.com/kirelagin/ninja-thesis/tree/master)



Structure
==========

* Everything starts with `main.latex`.
  Edit the first three lines of this file.
* `title.latex` describes the title page.
  Edit the university name if needed.
* `preamble.latex` has boring technical TeX stuff.
* `bib.bib` is the bibliography.
  Edit it with [KBibTeX](http://home.gna.org/kbibtex/) or something like that.
* `pseudo.latex` is the definition of a simple pseudocode programming language.
  You’ll probably want to extend it and/or define more languages (don’t forget
  to `\input` them in `preamble.latex`).
* `wscript` describes how to build everything and the `sources` variable
  is actually the only interesting thing there.
