---
title: "Transforme qualquer URL em QRcode usando Python"
summary: Mais sobre automação de tarefas, aqui vemos como transformar qualquer URL facilmente para QRcode. Experimente ler o código com seu smartphone.
date: 2020-03-07
projects: ['aprenda.py']
tags:
  - Python
aliases:
  - /aprenda.py/blog/qrcode
  - /aprenda.py/blog/qrcode.html
---

Uma das principais utilidades de qualquer ferramenta computacional é a possibilidade de automatizar tarefas. Aqui vemos como transformar qualquer URL facilmente para QRcode com Python.

O primeiro passo é instalar o pacote `qrcode`.

Isso pode ser feito por meio do seu gerenciador de pacotes preferido, como [Anaconda Python](https://www.anaconda.com/distribution/), por exemplo, ou com o comando no terminal:

```bash
pip install -q qrcode
```

Ou pode ser importado diretamente dentro do ambiente [Jupyter](https://jupyter.org/) com o comando mágico:

```python
!pip install -q qrcode
```

Independente da sua escolha para meio de instalação, agora importamos o módulo:

```python
import qrcode
```

E então estamos prontos para criar o primeiro qrcode com o comando `qrcode.make(<url>)`, como vemos a seguir:

```python
qrcode.make('https://www.instagram.com/aprenda.py/')
```

![png](output_6_0.png)

Experimente ler o código acima com o seu smartphone.

A opção anterior apenas mostrou o resultado na tela, mas pode ser muito mais interessante salvar o qrcode para um arquivo. Pode-se fazer isso com duas linhas de código:


```python
img = qrcode.make('www.instagram.com/aprenda.py')
img.save('aprenda.py.qrcode.png')
```

Para opções avançadas, como alteração das cores, borda ao tamanho da imagem, não deixe de conferir a [documentação oficial](https://pypi.org/project/qrcode/) do pacote em:


```python
qr = qrcode.QRCode()
qr.add_data('https://pypi.org/project/qrcode/')
qr.make(fit=True)

qr.make_image(fill_color="darkblue", back_color="orange")
```

![png](output_10_0.png)

Note que é sempre possível e bastante simples consultar a documentação com:

```python
help(qr.make_image)
```

```text
Help on method make_image in module qrcode.main:

make_image(image_factory=None, **kwargs) method of qrcode.main.QRCode instance
    Make an image from the QR Code data.

    If the data has not been compiled yet, make it first.
```



Por fim, lembre-se que estamos dentro de um ambiente de programação Python, e podemos aproveitar de todos os recursos disponíveis, como laços, testes lógicos, estruturas de dados e a combinação com outros pacotes para produzir resultados únicos e automatizados.
