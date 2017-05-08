{ nixpkgs ? import <nixpkgs> {} }:

let
  inherit (nixpkgs) pkgs;
in
pkgs.stdenv.mkDerivation {
  name = "thesis-template-0";
  buildInputs = [
    (pkgs.texlive.combine {
      inherit (pkgs.texlive)

        scheme-basic

        collection-langcyrillic
        collection-xetex

        caption
        enumitem
        euenc     # fontenc
        extsizes
        fontspec
        listings
        mathtools
        ms        # textpos
        multirow
        pgf       # pgfplots
        pgfplots
        setspace
        textpos
        titlesec
        tocloft
        xcolor
        zapfding  # hyperref?

      ;
    })
  ];
}
