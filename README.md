Why
====

* This template automatically follows GOST to the letter
  (well, almost, there are _minor_ deviations where GOST is particularly ugly).
* `waf` magically reruns XeTeX as many times as needed to properly
  generate the table of contents (yes, XeTeX, just as LaTeX, is stupid
  and has to be run multiple times).



HOWTO
======

*   Install XeTeX and Pandoc.
*   `./waf configure`
*   while `./waf` is not succeeding

    * install missing stuff (see [Dependencies](#dependencies))

*   while not happy with your text

    * Edit `.pd` files
    * _(sometimes)_ Edit `.latex` files
    * _(sometimes)_ Update `sources` in `wscript`
    * `./waf`



Dependencies
=============

There is a list of required TeX Live packages in [`shell.nix`](shell.nix) but in case you could not care less you are always free to just install Tex Live Full.



Nice links
===========

* [The Waf Book](https://waf.io/book/)
* Always feel free to refer to the [real-life example](https://github.com/kirelagin/masters/tree/master) (or [a little bit obsolete one](https://github.com/kirelagin/ninja-thesis/tree/master)).



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
