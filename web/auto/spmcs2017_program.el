(TeX-add-style-hook
 "spmcs2017_program"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "oneside" "A4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("xeCJK" "slantfont" "boldfont") ("xcolor" "table") ("fncychap" "Lenny") ("rotating" "figuresright") ("ulem" "normalem")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "xeCJK"
    "titlesec"
    "hyperref"
    "xcolor"
    "amsmath"
    "textcomp"
    "fancyhdr"
    "tikz"
    "longtable"
    "float"
    "geometry"
    "fncychap"
    "rotating"
    "capt-of"
    "amssymb"
    "ulem"
    "wrapfig"
    "grffile"
    "booktabs"
    "tabularx"
    "xunicode"
    "indentfirst"
    "fontspec"
    "listings")
   (LaTeX-add-labels
    "sec:org11c4816"
    "sec:org8069820"
    "sec:org56b02c5"
    "sec:org9d04bbf"
    "sec:org5b0b52f"
    "sec:orgc6153e5"
    "sec:org6b39fa7"
    "sec:org6e83465"
    "sec:org55875e6"
    "sec:org52a223a"
    "sec:orgc5617bf"
    "sec:orgebd7b08"
    "sec:org1a3e787"
    "sec:org7e70e15"
    "sec:orgfc3ff67"
    "sec:org42a67f9"
    "sec:org98e2734"
    "sec:orge0ae0ac"
    "sec:org0b20730"
    "sec:org9a330b7"
    "sec:orgee5bc1f")))

