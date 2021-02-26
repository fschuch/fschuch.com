---
title: Xcompact3d Toolbox
summary: Pacote Python com uma série de utilidades para lidar com o pré e pós-processamento de dados de simulações numéricas do Xcompact3d.
tags:
- CFD
- Dask
- IPywidgets
- Jupyter
- Python
- Xarray
- Xcompact3d
date: "2020-08-14"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Image from [pypi.org](https://pypi.org/)
  focal_point: Smart

links:
- icon: github
  icon_pack: fab
  name: Veja no GitHub
  url: "https://github.com/fschuch/xcompact3d_toolbox"
- icon: python
  icon_pack: fab
  name: Veja no Pip
  url: "https://pypi.org/project/xcompact3d-toolbox/"
- icon: book
  icon_pack: fas
  name: Documentação
  url: "https://xcompact3d-toolbox.readthedocs.io/en/latest/"
---

## Sobre

Esse é um pacote Python projetado para lidar com o pré e pós-processamento dos dados
provenientes do código [Xcompact3d]({{< relref "/project/xcompact3d" >}}), uma solução acadêmica de código aberto e alta precisão,
empregada para solucionar problemas de fluidodinâmica computacional com transporte de escalares.
Tem como objetivo ajudar os usuários e desenvolvedores de código com um conjunto de ferramentas e processos automatizados.

Os parâmetros físicos e computacionais são construídos sobre [traitlets](https://traitlets.readthedocs.io/en/stable/index.html),
uma estrutura que permite que as classes em Python tenham seus atributos checados quanto ao tipo, definição de valores padrões,
e chamadas de métodos de verificação de atributos quando necessário. Isso visa manter todos os parâmetros em compatibilidade com o que
o simulador espera. Além disso, [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) são fornecidos para uma experiência amigável com o usuário (veja exemplos na [Documentação](https://xcompact3d-toolbox.readthedocs.io/en/latest/tutorial/parameters.html)).

A estrutura de dados empregada é [xarray](http://xarray.pydata.org/en/stable/) (veja [*Why xarray?*](http://xarray.pydata.org/en/stable/why-xarray.html)), que introduz mapeamentos na forma de dimensões, coordenadas e atributos sobre os arranjos puramente [NumPy](https://numpy.org/), permitindo uma experiência de desenvolvimento mais intuitiva, concisa e menos propensa à erros.
Xcompact3d Toolbox conta com métodos capazes de ler os dados binários brutos resultantes das simulações do [Xcompact3d]({{< relref "/project/xcompact3d" >}}), e empacota-los em um arranjo de dados Xarray, assim como o processo contrário, escrevendo-os para o disco em uma maneira compatível com a leitura de dados do [Xcompact3d]({{< relref "/project/xcompact3d" >}}).
Além disso, os arranjos de dados são compatíveis com [dask](https://dask.org/) para computação paralela.

Por fim, Xcompact3d Toolbox está perfeitamente integrado à nova *configuração de escoamento **Sandbox*** (veja [fschuch/Xcompact3d](https://github.com/fschuch/Xcompact3d/)). O plano é fornecer toda a informação que o [Xcompact3d]({{< relref "/project/xcompact3d" >}}) precisa para especificar uma simulação, como condição inicial, geometria sólida, condições de contorno e o arquivo de parâmetros ([veja os exemplos](https://xcompact3d-toolbox.readthedocs.io/en/latest/tutorial.html#sandbox-examples)). Desse modo, iniciantes podem executar qualquer configuração inédita sem ter que se preocupar com programar em Fortran e com o ambiente de paralelização [2decomp](http://www.2decomp.org/). Para desenvolvedores, isso funciona como uma ferramenta de prototipagem rápida, para testar hipóteses e conceitos, além de servir como base de comparação para validar qualquer implementação futura no código fonte do [Xcompact3d]({{< relref "/project/xcompact3d" >}}).
