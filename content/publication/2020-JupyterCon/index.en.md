---
title: "A Jupyter sandbox environment coupled into the high-order Navier-Stokes solver Xcompact3d"
authors:
- admin
- F.D. Vianna
- A. Mombach
- J.H. Silvestrini
date: 2020-10-12
publishDate: 2020-09-02T17:46:50-03:00
doi:

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "JupyterCon 2020"
publication_short: "JupyterCon 2020"

abstract: 'Beginners may face many barriers to entry in a Navier-Stokes solver, for instance: The domain decomposition for parallel computation in a distributed-memory system; Coding, compiling and debugging in program languages like Fortran or C; The fear of breaking anything in the code; Stability of different numerical methods; Lack of documentation; and others. This work aims to break these barriers by coupling a sandbox environment into the solver. Due to this end, the high-order Navier-Stokes solver Xcompact3d was modified to accept the entire initial set-up from an external source, including physical and numerical parameters, initial and boundary conditions, and a solid geometry that can be inserted with Immersed Boundary Method (IBM). The initial set-up, in turn, is provided from a Jupyter Notebook, taking advantage of the built-in documentation with markdown cells (easily including figures and Latex equations), visualization and interactivity with widgets and plotting libraries, besides the versatility and readability of Python coding. Additionally, the input parameters can be checked for consistency and compatibility. Previous knowledge of NumPy and Matplotlib is enough to start with the exemplified flow configurations. However, there is no limitation to extended it to more advantaged tools like Pandas, Xarray, Dask, Numba, Holoview, Plotly and many others from the Jupyter ecosystem. The outcome of the presented framework benefits users from different levels. For students in computational fluid dynamics, it provides direct hands-on experience and a safe place for practising and learning. For advanced users and code developers, it works as a rapid prototyping tool to test concepts and then compare results to validate any future implementations at the numerical solver. Furthermore, it is a useful advance in terms of research reproducibility and can be ported to any other numerical solver.'

# Summary. An optional shortened abstract.
summary: This work aims to break many of the barriers to entry in a Navier-Stokes solver by coupling it to a Jupyter sandbox environment. For students in computational fluid dynamics, it provides direct hands-on experience and a safe place for practising and learning, while for advanced users and code developers, it works as a rapid prototyping tool.

tags:
- Python
- Xcompact3d
featured: false

# links:
# - name: ""
#   url: ""
url_pdf:
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ['xcompact3d-toolbox', 'xcompact3d']

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

{{% alert note %}}
To appear soon at [JupyterCon](https://jupytercon.com/talk-poster-cfp/).
{{% /alert %}}
