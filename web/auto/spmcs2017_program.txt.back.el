(TeX-add-style-hook
 "spmcs2017_program.txt.back"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "oneside" "A4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("xeCJK" "slantfont" "boldfont") ("hyperref" "hidelinks") ("xcolor" "table") ("fncychap" "Lenny") ("rotating" "figuresright") ("ulem" "normalem")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "xeCJK"
    "titlesec"
    "hyperref"
    "xcolor"
    "fncychap"
    "rotating"
    "capt-of"
    "amssymb"
    "ulem"
    "wrapfig"
    "grffile"
    "booktabs"
    "tabularx"
    "amsmath"
    "textcomp"
    "fancyhdr"
    "tikz"
    "longtable"
    "float"
    "geometry"
    "xunicode"
    "indentfirst"
    "fontspec"
    "listings"
    "multirow")
   (LaTeX-add-labels
    "sec:org565174e"
    "sec:org0dc6616"
    "sec:org0d3f1cd"
    "sec:orgd63dfca"
    "sec:org67de4e4"
    "sec:org86c6356"
    "sec:org80ea109"
    "sec:org0fb918a"
    "sec:org9b73502"
    "sec:org75b9c08"
    "sec:org63fa7b7"
    "sec:orgd1cea20"
    "sec:org1d0d45d"
    "sec:org52ca5c8"
    "sec:org80694a1"
    "sec:org8036179")))

