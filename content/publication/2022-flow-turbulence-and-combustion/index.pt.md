---
title: "A Cartesian Immersed Boundary Method Based on 1D Flow Reconstructions for High-Fidelity Simulations of Incompressible Turbulent Flows Around Moving Objects"
authors:
- A.E. Giannenas
- N. Bempedelis
- admin
- S. Laizet
date: "2022-09-05"
doi: 10.1007/s10494-022-00364-4

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Flow, Turbulence and Combustion"
publication_short: ""

abstract: "The aim of the present numerical study is to show that the recently developed Alternating Direction Reconstruction Immersed Boundary Method (ADR-IBM) (Giannenas and Laizet in Appl Math Model 99:606–627, 2021) can be used for Fluid–Structure Interaction (FSI) problems and can be combined with an Actuator Line Model (ALM) and a Computer-Aided Design (CAD) interface for high-fidelity simulations of fluid flow problems with rotors and geometrically complex immersed objects. The method relies on 1D cubic spline interpolations to reconstruct an artificial flow field inside the immersed object while imposing the appropriate boundary conditions on the boundaries of the object. The new capabilities of the method are demonstrated with the following flow configurations: a turbulent channel flow with the wall modelled as an immersed boundary, Vortex Induced Vibrations (VIVs) of one-degree-of-freedom (2D) and two-degree-of-freedom (3D) cylinders, a helicopter rotor and a multi-rotor unmanned aerial vehicle in hover and forward motion. These simulations are performed with the high-order fluid flow solver Incompact3d which is based on a 2D domain decomposition in order to exploit modern CPU-based supercomputers. It is shown that the ADR-IBM can be used for the study of FSI problems and for high-fidelity simulations of incompressible turbulent flows around moving complex objects with rotors."

# Summary. An optional shortened abstract.
summary:

tags:
- Xcompact3d
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: 'https://link.springer.com/content/pdf/10.1007/s10494-022-00364-4.pdf'
url_code: 'https://github.com/xcompact3d/Incompact3d'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Visualisation of vortical structures through Q-criterion = 6500 (a, c, d) and 19000 (b) iso-contours after ∼ 40 rotor rotations for a multi-rotor unmanned aerial vehicle in forward flight. The iso-contours are coloured by vertical velocity.'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ['xcompact3d']

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
