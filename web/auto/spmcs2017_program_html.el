(TeX-add-style-hook
 "spmcs2017_program_html"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1") ("ulem" "normalem") ("fncychap" "Lenny") ("rotating" "figuresright")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "inputenc"
    "fontenc"
    "graphicx"
    "grffile"
    "longtable"
    "wrapfig"
    "rotating"
    "ulem"
    "amsmath"
    "textcomp"
    "amssymb"
    "capt-of"
    "hyperref"
    "fncychap"
    "booktabs"
    "tabularx"
    "fancyhdr"
    "tikz"
    "float"
    "geometry"
    "xunicode"
    "indentfirst"
    "fontspec"
    "xcolor"
    "listings")
   (LaTeX-add-labels
    "sec:orgd7ade9a"
    "sec:org5796bf6"
    "sec:org93872d5"
    "sec:org633757b"
    "sec:org001e2ae"
    "sec:org6070b63"
    "sec:orgcccf76d"
    "sec:org6a340ce"
    "sec:org8092f52"
    "sec:org2cd79bc"
    "sec:org026035e"
    "sec:orgda5a520"
    "sec:org53d2390"
    "sec:orgc20c8e9"
    "sec:orgd26fd09"
    "sec:org11e8363"
    "sec:orga1aa2b0"
    "sec:orgfe03dee")))

