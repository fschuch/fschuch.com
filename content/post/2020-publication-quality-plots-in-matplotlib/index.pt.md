---
title: "Gráficos com qualidade de publicação em Python com Matplotlib"
date: "2020-10-14"
summary: "Independente do tipo de conteúdo que você está trabalhando, seja técnico, científico, educacional, ou voltado para divulgação em mídias sociais, existem quatro tópicos que influenciam diretamente na qualidade dos gráficos que se estão produzindo: Localização, dimensões, estilo e formato. Todos são abordados em detalhes neste post."
projects: ['aprenda.py']
tags:
  - Matplotlib
  - LaTeX
  - Python
aliases:
---

{{% toc %}}

## Introdução

A síntese e análises de dados e resultados na forma gráfica é um tópico de interesse para profissionais das mais diversas áreas, seja na produção de conteúdo técnico/científico, educacional, ou para divulgação em meios digitais. Uma boa figura vai atrair a atenção do seu público alvo.

Existem quatro tópicos que, na minha opinião, influenciam diretamente no resultado final dos gráficos que serão produzidos, especialmente quando falamos em qualidade de publicação. São eles:

1. **[Localização](#localização):** A formatação numérica deve estar de acordo com o idioma para o qual se está produzindo, seja na formatação de datas, moeda, ou mesmo o separador decimal;
1. **[Estilo](#estilo):** Aqui se definem diversos aspectos visuais, como o esquema de cores do gráfico, eixos e plano de fundo, fonte, e outros elementos. É importante manter a consistência para os diversos gráficos que vão constituir o mesmo documento;
1. **[Dimensões](#dimensões):** A definição da largura e altura da figura, bem como o tamanho da fonte, devem ser condizentes com o tipo de conteúdo onde o gráfico será inserido, seja em slides, pôster, relatório, artigo, postagem nas redes sociais e muitos outros;
1. **[Formato](#formato):** O formato no qual as figuras serão salvas. Opções vetoriais são preferíveis, porque mantém uma boa apresentação visual mesmo em telas ou impressões de alta resolução, ou quando as figuras são ampliadas.

<!--adsense-->

## Metodologia

Os pontos acima serão abordados em Python, ou mais especificamente, no pacote [Matplotlib](https://matplotlib.org/), que é uma biblioteca de plotagem 2D, que produz figuras de qualidade de publicação em uma variedade de formatos impressos e ambientes interativos para múltiplas plataformas. Matplotlib pode ser usada em scripts Python, nos shells do Python e do [IPython](https://ipython.org/), no [Jupyter Notebook](https://jupyter.org/), nos servidores de aplicativos da web e em quatro kits de ferramentas de interface gráfica do usuário. **Matplotlib tenta tornar as coisas fáceis simples e as coisas difíceis possíveis**. Você pode gerar gráficos, histogramas, espectros de potência, gráficos de barras, gráficos de erros, diagramas de dispersão, etc., com apenas algumas linhas de código.

Além disso, funções de plotagem Matplotlib são integradas às principais soluções para gerenciamento de dados em Python, como [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Xarray](http://xarray.pydata.org/en/stable/), [Dask](https://dask.org/) e muitos outros.

Matplotlib acompanha as principais distribuições de Python, de modo que podemos importar para nosso código com:

```python
import matplotlib.pyplot as plt
```

Agora vamos abordar especificamente cada tópico listado para a produção de figuras com qualidade de publicação.

### Localização

Se seu interesse é produzir conteúdo em lingua inglesa, indico que pule para o [próximo tópico](#estilo). Caso contrário, podemos usar o pacote [locale](https://docs.python.org/3.8/library/locale.html) para garantir a consistência de nossas figuras com os padrões da lingua portuguesa, por exemplo, ou realmente qualquer outra. Para tanto, podemos importar o pacote e definir a linguagem padrão como português:

```python
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")
```

Todos os parâmetros personalizáveis são armazenados no [dicionário](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#dictionaries) `plt.rcParams`, uma visão completa está disponível na página de sua [Documentação](https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html), mas não se preocupe, os principais pontos serão demonstrados aqui.

O passo a seguir é informar que queremos utilizar outro idioma para a notação nos eixos dos gráficos, por exemplo, usar `,` como separador decimal, fazemos isso com o seguinte código:

```python
plt.rcParams.update({
    'axes.formatter.use_locale' : True,
})
```

Não faz sentido confundir o público com diferentes separadores de decimal se podemos resolver isso facilmente com três linhas de código, não é mesmo?

Perceba que essa definição só é válida para os eixos das figuras, não modificando o comportamento do próprio núcleo Python, por exemplo:

```python
value = 0.67
print(value)
```

```text
    0.67
```

Note que a impressão ainda usa o ponto como separador decimal. Para impressões, anotações ou legendas nas figuras, podemos usar o método `locale.str()` para formatar automaticamente os números em ponto flutuante:

```python
print(locale.str(value))
```

```text
    0,67
```

O que pode ser uma boa prática, uma vez que basta retornar uma linha de código para o inglês (`locale.setlocale(locale.LC_ALL, "en_US.utf8")`), que todo o restante do código irá se comportar adequadamente.

Também é possível formatar facilmente dados monetários:

```python
print(locale.currency(value))
```

```text
    'R$ 0,67'
```

E o formato das datas, com o pacote [time](https://docs.python.org/3.8/library/time.html), veja:

```python
from time import gmtime, strftime
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
```

```text
    'qua, 14 out 2020 22:31:50 +0000'
```

### Estilo

Agora vamos falar sobre o estilo das figuras, incluindo sequencia de cores, estilo dos eixos, cor do fundo, presença ou não da grade, bem como seu próprio estilo, formatação das anotações e muitos outros detalhes.

Uma série de estilos já estão preparados e inclusos na biblioteca, e todos eles estão disponíveis em [Documentação - Matplotlib](https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html).
De lá, retirei alguns para exemplificar o leque de possibilidades que temos a nossa disposição:

{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_001.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_002.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_005.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_006.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_008.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_009.png" >}}
{{< figure src="https://matplotlib.org/3.1.0/_images/sphx_glr_style_sheets_reference_011.png" >}}

Indicamos o uso de um estilo pelo seu nome, e o seguinte comando:
```python
plt.style.use('ggplot')
```

É possível ainda combinar diversos estilos em uma lista, para a produção de resultados únicos:

```python
plt.style.use(['ggplot', 'dark_background'])
```

Note que os estilos mais à direita irão sobrescrever parâmetros definidos previamente pelos estilos à esquerda, então a ordem com que são fornecidos pode mudar o resultado do final.

Pode-se ainda personalizar cada um dos aspectos dos gráficos individualmente, para mais detalhes, sugiro consultar a [Documentação - Matplotlib](https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html).
Caso queira retomar os parâmetros originais, use:
```python
plt.rcdefaults()
```

### Dimensões

Outro ponto essencial, a relação entre o tamanho da figura e o tamanho da fonte. Quando falamos em qualidade de publicação, os textos e números dos gráficos devem ser exatamente do mesmo tamanho que o restante do documento onde eles são inseridos.

O ideal aqui é a precisa definição da largura e da altura que se deseja a figura, para que ela possa ser inserida no documento final em uma escala 1:1, sem nenhuma distorção.

Temos uma função preparada para isso:

```
def get_figsize(
    columnwidth=4, wf=1.0, hf_rel=(5.0 ** 0.5 - 1.0) / 2.0, hf_abs=None, unit="inch"
):
    """A função aceita uma série de argumentos para a precisa customização da
    largura e altura de uma figura que será produzida com Matplotlib.
    
    Maiores detalhes em:
    www.fschuch/blog/2020/10/14/graficos-com-qualidade-de-publicacao-em-python-com-matplotlib
    
    © 2020 Felipe N. Schuch, sob os termos da CC BY SA 4.0.
    (www.creativecommons.org/licenses/by-sa/4.0)
    
    Parâmetros
    ----------
    columnwidth : float
        Largura da página ou da coluna de texto (o padrão é 4)
        Obtenha isso em LaTeX usando \the\columnwidth
    wf : float
        A fração da largura que será utilizada pela figura (o padrão é 1.0)
    hf_rel : float
        Altura da figura, valor relativo em relação à largura (o padrão é a proporção áurea)
    hf_abs : float
        Altura da figura em termos absolutos, caso desejado (o padrão é None)
        Obtenha isso em LaTeX usando \the\textheight
    unit : float
        Unidade de comprimento utilizada para `columnwidth` e `hf_abs`,
        as opções suportadas são "inch" (polegada), "mm", "cm" e "pt" (Pontos tipográfico)
        (o padrão é "inch")
    Retorno
    -------
    set
        Retorna um set contendo a largura e a altura especificada para a figura.
    Apura
    -------
    ValueError
        Caso a unidade não seja suportada pela função.
    Exemplos
    -------
    
    >>> import matplotlib.pyplot as plt
    
    >>> get_figsize()
    (4.0, 2.4721359549995796)
    >>> get_figsize(columnwidth=16, unit='cm', hf_abs=9)
    (6.299212598425196, 3.543307086614173)
    >>> get_figsize(columnwidth=4, unit='inch', hf_rel = 1.0)
    (4.0, 4.0)

    >>> plt.rcParams.update({
    ... 'figure.figsize' : get_figsize(columnwidth=160, wf=0.75, unit='mm', hf_rel=1)
    ... })
    """

    # Dessa maneira, unit não será sensível a letras maiúsculas e minúsculas
    unit = unit.lower()

    # Converte unidades para polegadas, conforme esperado por Matplotlib
    conversion = dict(inch=1.0, mm=25.4, cm=2.54, pt=72.0,)

    if unit in conversion.keys():
        fig_width = columnwidth / conversion[unit]
        if hf_abs is not None:
            fig_height = hf_abs / conversion[unit]
    else:
        raise ValueError(f"unit deve ser: {conversion.keys()}")

    # A figura será apenas uma fração da largura útil da página
    fig_width *= wf

    # Caso hf_abs não seja definido, a altura será uma fração da largura
    if hf_abs is None:
        fig_height = fig_width * hf_rel

    # Retorna a largura e altura especificada para a figura
    return (fig_width, fig_height)
```

Vamos detalhar cada um dos parâmetros:

* `columnwidth` é a largura útil da página, isso é, a largura da página menos ambas margens. Ou a largura da coluna, para os casos em que isso se aplicar. Em documentos [$\LaTeX$](https://www.latex-project.org/), esse valor pode ser obtido com o comando `\the\columnwidth`;
* `wf` é a fração da largura que será utilizada para a figura, porque nem sempre queremos todo o espaço. Isso é, `wf=0.5` criará um gráfico que ocupa a metade da largura útil da página;
* `hf_rel` define a altura da figura em valor relativo em relação à largura. Por exemplo, `hf_rel=1.0` criará uma figura quadrada, enquanto `hf_rel=9.0/16.0` criará a proporção certa para telas wide-screen;
* `hf_abs` pode ser usado para o ajuste da altura em termos absolutos, caso o ajuste fino seja desejado. Em documentos [$\LaTeX$](https://www.latex-project.org/), esse valor pode ser obtido com o comando `\the\textheight`. Note que esse argumento desabilita o argumento anterior (`hf_rel`);
* `unit` representa a unidade de comprimento para `columnwidth` e `hf_abs`, as opções suportadas são "inch" (polegada), "mm", "cm" e "pt" (pontos tipográfico, é a utilizada em $\LaTeX$). Assim, a função realiza a devida conversão de unidades, uma vez que Matplotlib espera essa definição em polegadas.

A função retorna uma [tupla](https://docs.python.org/pt-br/3.8/tutorial/datastructures.html#tuples-and-sequences) contendo a largura e altura, que é exatamente o que precisamos. Veja como agora podemos definir com precisão o padrão de desejamos para dimensões e tamanho da fonte:

```python
plt.rcParams.update({
    #
    'figure.figsize' : get_figsize(columnwidth=160, unit='mm', hf_rel=1),
    #
    "axes.labelsize": 12,
    "font.size": 12,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
})
```

É possível realizar posteriormente um ajuste personalizado para cada figura, por exemplo:

```python
fig, axes = plt.subplots(figsize=get_figsize(columnwidth=16, unit='cm', hf_rel=0.5))
```

Toda minha produção técnica/científica tem sido feita em [$\LaTeX$](https://www.latex-project.org/), o que eu certamente recomendo. De fato, esse pode ser um tópico para outro post no futuro próximo.
Se esse não é o seu caso, pode ser o momento de prosseguir para o [próximo tópico](#formato).
De qualquer maneira, vou compartilhar alguns outros ajustes para referência:

* Artigo com o [template de duas colunas da Elsevier](https://www.ctan.org/pkg/els-cas-templates/):

    ```python
    ptl.rcParams.update({
        'figure.figsize' : get_figsize(columnwidth=238.25444, unit='pt'),
        #
        "axes.labelsize": 8,
        "font.size": 8,
        "legend.fontsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8
    })
    ```

* Relatório técnico, Dissertação ou Tese com [abnTeX2](https://www.abntex.net.br/):

    ```python
    ptl.rcParams.update({
        'figure.figsize' : get_figsize(columnwidth=455.0, unit='pt'),
        #
        "axes.labelsize": 12,
        "font.size": 12,
        "legend.fontsize": 12,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
    })
    ```

* Pôster em tamanho A0 com [beamer](https://ctan.org/pkg/beamer) (e [esse template](https://www.overleaf.com/latex/templates/landscape-beamer-poster-template/vjpmsxxdvtqk)):

    ```python
    ptl.rcParams.update({
        'figure.figsize' : get_figsize(columnwidth=2376.3973*.75, unit='pt'),
        #
        "axes.labelsize": 24,
        "font.size": 24,
        "legend.fontsize": 24,
        "xtick.labelsize": 24,
        "ytick.labelsize": 24,
    })
    ```

* Apresentação de slides com [beamer](https://ctan.org/pkg/beamer) (e o tema [Focus v2.6](https://github.com/elauksap/focus-beamertheme)):

    ```python
    ptl.rcParams.update({
        'figure.figsize' : get_figsize(columnwidth=412.56497, unit='pt'),
    })
    ```
Em $\LaTeX$, você tem a certeza de que deu tudo certo quando a figura é incluída com `scale=1`, e as dimensões e tamanho de fonte tem a aparência adequada, por exemplo:

```latex
\includegraphics[scale=1]{<nome_da_figura>}
```

<!--adsense-->

### Formato

Por fim, temos o formato no qual serão salvos os gráficos.
Eles podem ser divididos basicamente em dois grandes grupos, e temos um bloco de código para exemplificar:

```python
import numpy as np

x = np.linspace(0.0, 2.0 * np.pi)
y = np.sin(x)

for f in ['jpg', 'svg']:

    plt.plot(x,y, label = 'Label')
    plt.legend()
    plt.savefig('example_line.'+f, format=f)
```

1. **Formato de matriz**: A figura é constituída por um arranjo de pixels (ou matriz), que possuí um tamanho definido, por exemplo 240 x 120 pixels. Se quisermos amplia-la, veremos cada pequeno pixel, em um efeito meio quadriculado. Nesse grupo temos por exemplo os formatos JPG e PNG, veja o resultado:

    {{< figure src="example_line.jpg" title="Figura em formato de matriz 768 x 576 pixels (jpg).">}}

    A qualidade da figura é controlada pelo número de pixels, ou o parâmetro **dpi** (pontos por polegada, do inglês *dots per inch*). Aumentar o dpi aumenta a qualidade da imagem, mas também aumenta seu espaço em disco;

1. **Formato Vetorial**: Aqui, a figura é composta por vetores, utilizando elementos matemáticos para compor a figura completa. Ao contrário do grupo anterior, ela não perde qualidade quando ampliada. Como exemplo temos os formatos SVG e PDF, veja a figura:

    {{< figure src="example_line.svg" title="Figura em formato vetorial (svg).">}}

Mas afinal, qual escolher? A resposta é: isso depende.

Eu diria que opções vetoriais são preferíveis (svg para web, PDF para produção técnica), porque mantém uma boa apresentação visual mesmo em telas ou impressões de alta resolução, ou quando as figuras são ampliadas.
Existem entretanto aplicações que simplesmente não aceitam formatos vetoriais (como algumas redes sociais), então podemos mudar para formato matricial (jpg ou png).
Outro desafio para o formato vetorial é quando temos um elevado número de artefatos vetoriais. Independente do tipo de gráfico, à medida que a quantidade de dados vai aumentando de centenas, para milhares e milhões de pontos, pode ser que o espaço que a figura vetorial ocupa em disco seja, afinal, impraticável.

Note entretanto que existe uma abordagem intermediária, métodos em Matplotlib que permitem converter elementos vetoriais para representação matricial, chamados `rasterization`.
Para exemplificar isso, temos um bloco de código modificado da [Documentação - Matplotlib](https://matplotlib.org/3.1.3/gallery/misc/rasterization_demo.html), veja o código e a figura resultante:

```python
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)
yy = x*np.sin(theta) + y*np.cos(theta)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax1.transAxes)
ax1.set_title("No Rasterization")

ax2.set_aspect(1)
ax2.pcolormesh(xx, yy, d, zorder=-15)
ax2.text(0.5, 0.5, "Text", alpha=0.2, zorder=5,
         va="center", ha="center", size=50, transform=ax2.transAxes)
ax2.set_title("Rasterization z$<-10$")
ax2.set_rasterization_zorder(-10)

ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("Rasterization")
ax3.set_rasterized(True)

plt.savefig("test_rasterization.pdf", dpi=150)
plt.savefig("test_rasterization.eps", dpi=150)

if not plt.rcParams["text.usetex"]:
    plt.savefig("test_rasterization.svg")
```

{{< figure src="test_rasterization.svg" >}}

Vemos acima uma figura vetorial com três sub-gráficos:

* No elemento à esquerda, temos a figura puramente vetorial (*No Rasterization*), perceba a boa qualidade visual mesmo quando ampliada;
* A figura à direita foi convertida para o formato matricial (*Rasterization*) com a linha `ax3.set_rasterized(True)`, incluindo título, coordenadas, anotação e o `pcolormesh`, mesmo que a figura tenha sido salva em svg. Perceba como ela foi totalmente representada pixel por pixel;
* No centro temos uma solução intermediária. Nesse caso, apenas elementos com `zorder`[^1] menor que `-10` foram transformados com a linha `ax2.set_rasterization_zorder(-10)`, nesse caso temos o `pcolormesh`. Título, coordenadas e a anotação permaneceram vetoriais, e assim, podemos obter o melhor de dois mundos.

[^1]: O parâmetro `zorder` controla a ordem na qual cada elemento do gráfico será exibido, isso é, o texto com `zorder=5` será exibido sobre a figura `pcolormesh` com `zorder=-15`. Para maiores informações, consulte a [Documentação - Matplotlib](https://matplotlib.org/3.1.1/gallery/misc/zorder_demo.html).

A efetiva escolha sobre quais elementos converter é novamente um compromisso entre a qualidade da imagem e o seu tamanho em disco, e isso certamente depende de cada aplicação, ou mesmo da preferência pessoal. Note que dpi ainda é um parâmetro válido para os elementos convertidos para pixels.

Finalmente, podemos definir esses parâmetros para serem aplicados como padrão em nosso código da seguinte maneira:

```python
plt.rcParams.update({
    'figure.dpi' : 240,
    'savefig.format' : 'pdf',
    #
    'text.usetex' : True,
    'text.latex.preamble' : "\\usepackage{icomma}",
})
```

A opção `text.usetex` é particularmente útil para quem usa $\LaTeX$, permitindo incluir equações como anotações, título ou como rótulo para as coordenadas. A opção `'text.latex.preamble' : "\\usepackage{icomma}"` é um bônus, isso elimina o espaço inserido em modo matemático após cada vírgula, que certamente não são bem-vindos quando falamos em qualidade de publicação.

## Conclusão

A apresentação de resultados em alta qualidade é um ponto fundamental para atrair engajamento e atenção do seu público.
Aqui demonstrou-se como a atenção nos detalhes e algumas poucas linhas de código podem ter um enorme impacto na apresentação dos resultados em formato gráfico.
Por fim, espero que esse meu relato sobre a produção de figuras em Python e Matplotlib lhe seja útil como um ponto de partida e motivação para seguir estudando o tema.
