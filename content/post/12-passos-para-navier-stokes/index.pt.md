---
title: "CFD com Python: 12 Passos para Navier-Stokes"
summary: Este material lhe guiará, passo a passo, pelos fundamentos de Dinâmica dos Fluidos Computacional. Cada tarefa introduz tanto novos conceitos físicos sobre as equações de Navier-Stokes, quanto detalhes sobre a programação em Python que resolve as equações diferenciais parciais. Tudo isso de maneira interativa e online (nenhuma instalação é necessária).
date: 2020-01-12
projects: ['aprenda.py']
tags:
  - CFD
  - Python
aliases:
  - /blog/12-passos-para-navier-stokes/
  - /aprenda.py/blog/12-passos-para-navier-stokes.html
---

# Introdução

**CFD com Python**, também conhecido como os **12 passos para Navier-Stokes**, é um módulo prático para o aprendizado dos fundamentos de Dinâmica dos Fluidos Computacional (CFD, do Inglês *Computational Fluid Dynamics*) por meio de códigos que resolvem as equações diferenciais parciais que descrevem a física dos escoamentos.
Esta é uma adaptação e tradução para português por [Felipe N. Schuch](https://fschuch.com). Os textos e códigos originais foram parte do curso ministrado pela [Prof. Lorena Barba](http://lorenabarba.com) entre 2009 e 2013 no departamento de Engenharia Mecânica da Universidade de Boston (Prof. Barba então se mudou para Universidade George Washington).

*O curso é para iniciantes*. O módulo assume que o leitor tenha conhecimentos básicos sobre programação (qualquer linguagem) e alguma familiaridade com equações diferenciais e mecânica dos fluidos.
Guiando estudantes através destes passos (sem falhar nenhum!), podemos ensina-los lições valiosas. A constante evolução entre os exercícios proporciona um senso de recompensa ao final de cada atividade, e eles sentem que estão aprendendo com pouco esforço. Conforme avançam, eles naturalmente praticam como reutilizar trechos de código e progressivamente aprendem técnicas de programação e visualização. Enquanto eles analisam os resultados, aprendem sobre difusão, precisão e convergência.
Em todos os casos, o aluno é encorajado a seguir o trabalho de cada lição paralelamente ao reescrever em um Jupyter Notebook novo, mantendo anotações pessoais de seu progresso e de seus experimentos.

> We hope that the CFD Python series will help a new cohort of students and self-learners gain basic CFD skills. Let us know what you think!<br>
> <cite><a href="https://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/">Prof. Lorena Barba</a></cite>

# Como Acessar

Existem basicamente duas opções, descritas à seguir:

## Executar online

Execute uma seção interativa dessa versão do **CFD com Python** em seu navegador usando o serviço Binder. Esta opção não requer nenhuma instalação na sua máquina, apenas clique no botão:

[![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/fschuch/CFDPython-BR/master/)

* Espere a aplicação carregar tudo para você, isso pode levar algum tempo;
* O próximo passo é abrir os arquivos na pasta `tarefas`;
* Ao final do curso, não esqueça de salvar uma cópia do Notebook com suas anotações pessoais.

## Instalação

Se você gostaria de executar na sua própria máquina por meio da instalação de alguma distribuição Python, consulte os detalhes sobre o procedimento em nosso [repositório no GitHub](https://github.com/fschuch/CFDPython-BR).

# Conteúdo

Os passos 1 a 4 são em uma direção espacial (1D). Passos 5 a 10 são em duas dimensões (2D). Passos 11 e 12 resolvem as equações de Navier-Stokes em 2D. Três Notebooks "bônus" cobrem a condição CFL de estabilidade, operações de arranjos multi-dimensionais com NumPy e definição de funções em Python.

* [Ligeira Introdução à Python](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/00_Ligeira_Intro_Python_.ipynb)
-- Para novatos em Python, essa lição introduz bibliotecas numéricas (NumPy e Matplotlib), variáveis em Python, endentação e manipulação de arranjos.
* [Passo 1](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/01_Passo_1.ipynb)
-- Convecção linear com avanço à partir da condição inicial (CI) e condições de contorno (CC) apropriadas.
* [Passo 2](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/02_Passo_2.ipynb)
-- Com as mesmas CI/BCs, convecção _não linear_.
* [Condição CFL](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/03_Condicao_CFL.ipynb)
-- Explorando a estabilidade numérica e a condição de Courant-Friedrichs-Lewy (CFL).
* [Passo 3](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/04_Passo_3.ipynb)
-- Com as mesmas CI/BCs, apenas _difusão_.
* [Passo 4](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/05_Passo_4.ipynb)
-- Equação de Burgers, com CI _dente de serra_ e CC periódica (e uma introdução ao SymPy).
* [Operações com arranjos em NumPy](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/06_Operacoes_de_arranjos_com_NumPy.ipynb)
* [Passo 5](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/07_Passo_5.ipynb)
-- Convecção linear 2D com CI função quadrada e CC apropriadas.
* [Passo 6](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/08_Passo_6.ipynb)
-- Com as mesmas CI/BCs, convecção _não linear_ 2D.
* [Passo 7](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/09_Passo_7.ipynb)
-- Com as mesmas CI/BCs, _difusão_ 2D.
* [Passo 8](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/10_Passo_8.ipynb)
-- Equação de Burgers 2D.
* [Definindo Funções em Python](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/11_Definindo_Funcoes_em_Python.ipynb)
* [Passo 9](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/12_Passo_9.ipynb)
-- Equação de Laplace 2D com CI zero e CC ambas Neumann e Dirichlet.
* [Passo 10](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/13_Passo_10.ipynb)
-- Equação de Poisson 2D.
* [Passo 11](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/14_Passo_11.ipynb)
-- Resolve o escoamento em Cavidade com Navier-Stokes 2D.
* [Passo 12](http://nbviewer.jupyter.org/github/fschuch/CFDPython-BR/blob/master/tarefas/15_Passo_12.ipynb)
-- Resolve o escoamento em Canal com Navier–Stokes 2D.

{{% alert note %}}
Clicar nos links nessa seção irá abrir cada Notebook pelo serviço `nbviewer`, que os apresenta na tela, porem não em forma executável. Para isso, consulte [Executar online](#executar-online).
{{% /alert %}}

# Conteúdo complementar

Existem ainda duas outras versões do CFD com Python:

* [Versão original em Inglês](https://github.com/barbagroup/CFDPython), por [Prof. Lorena Barba](http://lorenabarba.com).
* [Tradução para Espanhol](https://github.com/franktoffel/CFDPython-ES), por F.J. Navarro-Brull para [CAChemE.org](http://www.cacheme.org/)

A versão original foi ainda publicada em:

* Barba, Lorena A., and Forsyth, Gilbert F. (2018). CFD Python: the 12 steps to Navier-Stokes equations. _Journal of Open Source Education_, **1**(9), 21, [doi.org/10.21105/jose.00021](https://doi.org/10.21105/jose.00021)
