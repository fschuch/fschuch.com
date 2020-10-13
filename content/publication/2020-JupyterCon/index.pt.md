---
title: "Um ambiente \"Jupyter Sandbox\"  acoplado ao Xcompact3d, um código acadêmico de alta ordem para Fluidodinâmica Computacional"
authors:
- admin
- F.D. Vianna
- A. Mombach
- J.H. Silvestrini
date: "2020-10-12"
publishDate: 2020-09-02T17:46:50-03:00
doi: 0.13140/RG.2.2.10886.60485

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["0"]

# Publication name and optional abbreviated publication name.
publication: "JupyterCon 2020"
publication_short: "JupyterCon 2020"

abstract: 'Este trabalho visa quebrar muitas das barreiras de entrada em um código acadêmico que resolva Navier-Stokes, acoplando-o a um ambiente *Jupyter sandbox*. Para alunos de fluidodinâmica computacional, ele fornece experiência prática direta e um local seguro para praticar e aprender, enquanto para usuários avançados e desenvolvedores de código, funciona como uma ferramenta de prototipagem rápida.'

# Summary. An optional shortened abstract.
summary: 'Este trabalho visa quebrar muitas das barreiras de entrada em um código acadêmico que resolva Navier-Stokes, acoplando-o a um ambiente *Jupyter sandbox*. Para alunos de fluidodinâmica computacional, ele fornece experiência prática direta e um local seguro para praticar e aprender, enquanto para usuários avançados e desenvolvedores de código, funciona como uma ferramenta de prototipagem rápida.'

tags:
- CFD
- Python
- Xcompact3d
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: 'https://www.researchgate.net/publication/344633987_A_Jupyter_Sandbox_Environment_Coupled_Into_the_High-Order_Navier-Stokes_Solver_Xcompact3d'
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/dObubiHnEBk?t=1335'

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

# Descrição

Iniciantes podem enfrentar muitas barreiras de entrada em um código acadêmico para Fluidodinâmica Computacional (CFD), por exemplo:

* A decomposição de domínio de cálculo para computação paralela em um sistema de memória distribuída;
* Programação, compilação, teste e depuração em linguagens de programação como Fortran ou C;
* O receio de estragar qualquer coisa no código fonte;
* Critérios de estabilidade de diferentes métodos numéricos;
* Falta de documentação e outros.

Esse trabalho visa quebrar essas barreiras ao construir uma camada Python, ou mais especificamente [Jupyter Notebook](https://jupyter.org/), sobre o código CFD, programado originalmente em Fortran.

Para tanto, o código CFD de alta ordem [Xcompact3d](https://github.com/fschuch/Xcompact3d) foi modificado para aceitar toda a configuração do escoamento sob investigação de uma fonte externa, incluindo parâmetros físicos e numéricos, condição inicial e condições de contorno, e uma geometria sólida que pode ser inserida no domínio cartesiano por meio do método das fronteiras imersas (IBM, do inglês *Immersed Boundary Method*). A configuração do escoamento, por sua vez, é fornecida a partir de um [Jupyter Notebook](https://jupyter.org/), aproveitando a documentação embutida com células *Markdown* (incluindo facilmente figuras, tabelas e equações $\LaTeX$), visualização e interatividade com *widgets* e bibliotecas de plotagem, além da versatilidade e legibilidade da programação em Python. Além disso, os parâmetros de entrada podem ser verificados quanto à consistência e compatibilidade. O conhecimento prévio de [NumPy](https://numpy.org/) e [Matplotlib](https://matplotlib.org/) é suficiente para começar com as configurações de escoamento exemplificadas. No entanto, não há limitação para estendê-lo para ferramentas mais avançadas como [Pandas](https://pandas.pydata.org/), [Xarray](http://xarray.pydata.org/), [Dask]( https://dask.org/), [Numba](http://numba.pydata.org/), [Holoview](https://holoviews.org/), [Plotly](https://plotly.com/python/) e muitos outros do ecossistema Jupyter. Na verdade, o *Jupyter CFD Sandbox* foi incorporado ao pacote Python [Xcompact3d-toolbox](https://github.com/fschuch/xcompact3d_toolbox).

O resultado da metodologia apresentada nesse trabalho pode beneficiar usuários de diferentes níveis:

Para alunos de fluidodinâmica computacional, oferece experiência prática direta e um local seguro para praticar e aprender;
* Para usuários avançados e desenvolvedores de código, ele funciona como uma ferramenta de prototipagem rápida, onde é possível testar conceitos e, em seguida, comparar os resultados para validar quaisquer implementações futuras no solucionador numérico.

Além disso, é um avanço importante em termos de reprodutibilidade de pesquisa, e pode ser portado para qualquer outro solucionador numérico, (avise-nos se você fizer isso).

Tutoriais e diversas configurações de escoamento estão disponíveis na [Documentação do Xcompact3d-toolbox](https://xcompact3d-toolbox.readthedocs.io/en/latest/).
