---
title: 'Métodos Numéricos em Python'
event: 'Aula especial para as turmas de Métodos Numéricos e Turbulência'
event_url: 

location: PPGRHSA, IPH, UFRGS
address:
  city: Porto Alegre
  region: RS
  country: Brazil

abstract: "Aula como professor convidado, para as turmas de Métodos Numéricos e Turbulência do Programa de Pós-Graduação em Recursos Hídricos e Saneamento Ambiental do Instituto de Pesquisas Hidraulicas da Universidade Federal do Rio Grande do Sul. Essas disciplinas são ministradas no programa de pós-graduação pela professora Edith Beatriz Camano Schettini, que acompanhou as apresentações."

# Summary. An optional shortened abstract.
summary: Aula como professor convidado, ministrada para as turmas de Métodos Numéricos e Turbulência do Programa de Pós-Graduação em Recursos Hídricos e Saneamento Ambiental do Instituto de Pesquisas Hidraulicas da Universidade Federal do Rio Grande do Sul.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-05-04T15:30:00-03:00
date_end: 2021-05-04T17:30:00-03:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2021-05-04T09:00:00-03:00

tags:
  - Python
  - Métodos Numéricos
  - Matplotlib
  - NumPy
  - SciPy

# Is this a featured talk? (true/false)
featured: false

links:
- icon: github
  icon_pack: fab
  name: Veja no GitHub
  url: https://github.com/fschuch/metodos-numericos-com-python
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
  - aprenda.py

aliases:
  - /talk/2021-metodos-iph
---

Esta palestra tem por objetivo introduzir os principais conceitos de programação e Python, empregando a didática interativa da plataforma Jupyter Notebook. Além disso, demonstra-se como solucionar problemas em métodos numéricos por meio de propostas computacionais. Para tanto, o material é dividido em duas aulas:

1. [Ligeira Introdução à Python](http://nbviewer.jupyter.org/github/fschuch/metodos-numericos-com-python/blob/main/Aulas/01-Introdução-Python-Bibliotecas.ipynb), contemplando:

   - Introdução e revisão sobre conceitos de programação em Python;
   - Manipulação de tensores em Python com Numpy;
   - Produção de gráficos com o pacote Matplotlib;
   - Cálculo Diferencial e Integral com Python;
   - Resolvendo Equações Diferenciais;

2. Exemplos de aplicação em Fenômenos de Transporte (próxima semana).

## Configurando o Tutorial

Esse tutorial foi projetado para rodar no [Binder](https://mybinder.org/).
O serviço permite executar totalmente na nuvem, nenhuma instalação extra é necessária.
Para tanto, basta clicar [aqui](https://mybinder.org/v2/gh/fschuch/metodos-numericos-com-python/main?urlpath=lab):
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fschuch/metodos-numericos-com-python/main?urlpath=lab)

Se você prefere instalar o tutorial localmente, siga os seguintes passos:

1. Clone o repositório:

   ```bash
   git clone https://github.com/fschuch/metodos-numericos-com-python
   ```

1. Instale o ambiente. O repositório inclui um arquivo `environment.yaml` que contém uma lista de todos os pacotes necessários para executar esse tutorial.
   Para instalá-los usando conda, use o comando:

   ```bash
   conda env create -f environment.yml
   conda activate metodos-numericos-python
   ```

1. Inicie uma seção Jupyter:

   ```bash
   jupyter lab
   ```