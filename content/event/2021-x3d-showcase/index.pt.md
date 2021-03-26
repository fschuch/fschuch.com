---
title: "Sandbox flow configuration: A rapid prototyping tool inside XCompact3d"
event: XCompact3d 2021 Online Showcase Event
event_url: https://www.incompact3d.com/events

location: Online

abstract: "Uma ferramenta de prototipagem rápida incorporada ao XCompact3d, um código acadêmico para fluidodinâmica computacional. Isso visa aumentar a capacidade de trabalho dos desenvolvedores do código, ao mesmo tempo em que cria um ambiente mais amigável para estudantes em CDF."

# Summary. An optional shortened abstract.
summary: 

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.

date: 2021-03-12T15:55:00+00:00
date_end: 2021-03-12T16:12:00+00:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2021-03-09T15:00:00-03:00

tags:
  - CFD
  - HPC
  - Python
  - STEM
  - Xcompact3d

# Is this a featured talk? (true/false)
featured: false

# links:
# - icon: twitter
#   icon_pack: fab
#   name: Slides
#   url: https://twitter.com/incompact3d
url_code: ""
url_pdf: ""
url_slides: "https://www.fschuch.com/en/slides/2021-x3d-showcase/"
url_video: "https://youtu.be/W-TFZo4Qnhk"

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides:

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ['xcompact3d-toolbox', 'xcompact3d']
---

XCompact3d é uma ferramenta acadêmica de alta precisão, voltado para a resolução de problemas em fuidodinâmica computacioanl (CFD), incluindo capacidade para resolver transporte de calor e/ou massa, bem como escoamentos ao redor de obstáculos. Ele é programado em Fortran, com código aberto, e projetado para rodar em super-computadores por meio da interface por troca de mensagens (MPI).

A pesquisa na fronteira do conhecimento geralmente envolve extender as capacidades do código original, visando simular configurações de escoamento inéditas. Com isso, se faz necessário editar diretamente o código fonte, e todas as tarefas derivadas desse ato, como compilar o código, testar, corrigir possiveis falhas, executar e talvez repetir o ciclo. Essa atividade demanda conhecimentos especializados e tempo de deselvolvimento. Nesse contexto surge a motivação para esse trabalho:

- Como podemos acelerar o trabalho de desenvolvimentos de casos inéditos em nosso código?
- E também, como podemos acelerar o processo de aprendizagem para os que estão começando a estudar o código, ou mesmo tornar ele acessível para estudantes de CFD?

A solução para ambos os problemas acima foi proposta, confira mais detalhes abaixo:

- [Veja a palestra no YouTube](https://youtu.be/W-TFZo4Qnhk);
- [Veja os Slides Online](https://www.fschuch.com/en/slides/2021-x3d-showcase/);
- Por fim, [alguns exemplos](https://xcompact3d-toolbox.readthedocs.io/en/latest/tutorial.html#sandbox-examples) da ferramenta que desenvolvemos.