---
title: "Obtenção da previsão do tempo com o pacote PyOWM"
summary: PyOWM é um invólucro em Python para a API web de previsão do tempo OpenWeatherMap.
date: 2020-04-23
projects: ['aprenda.py']
tags:
  - Python
aliases:
  - /aprenda.py/blog/pyowm
  - /aprenda.py/blog/pyowm.html
---

PyOWM é uma biblioteca Python, projetada como um invólucro cliente para a API web do OpenWeatherMap (OWM).
Permite o consumo rápido e fácil dos dados OWM para aplicações Python por meio de um modelo de objeto simples e de maneira amigável ao usuário humano.

A biblioteca está disponível no [GitHub](https://github.com/csparpa/pyowm), onde pode-se obter maiores informações.

O primeiro passo para sua utilização é a instalação, que pode ser feita no ambiente Jupyter Notebook (como esse post) com um comando mágico, com a seguinte linha de código:


```python
!pip install -q pyowm
```

A seguir, importamos a biblioteca:


```python
import pyowm
```

Note que o provedor de dados climáticos é grátis, mas requer uma chave de acesso. Para tanto, um rápido registro é necessário na [página do OWM](https://home.openweathermap.org/users/sign_up).

Uma vez que se tenha a chave, informamos ela ao programa:


```python
owm = pyowm.OWM('sua-chave-aqui')

# Tem uma assinatura Pro? Nesse caso use:
# owm = pyowm.OWM(API_key='sua-chave-aqui', subscription_type='pro')
```

Podemos fazer uma observação informando o local pretendido, por exemplo:


```python
observation = owm.weather_at_place('Porto Alegre,BR')
```

E então obtemos a previsão do tempo:


```python
w = observation.get_weather()
```

Para imprimir na tela:

```
w
```




    <pyowm.weatherapi25.weather.Weather - reference time=2020-04-23 20:57:39+00, status=clear, detailed status=clear sky>



O último passo do exemplo é observar os resultados obtidos:


```python
# Informação sobre o vento
w.get_wind()
```




    {'deg': 130, 'speed': 5.1}




```python
# Umidade relativa do ar
w.get_humidity()
```




    44




```python
# E temperatura
w.get_temperature('celsius')
```




    {'temp': 25.67, 'temp_kf': None, 'temp_max': 27.0, 'temp_min': 24.44}



Confira a [documentação oficial](https://pyowm.readthedocs.io/en/latest/) da biblioteca se precisar de qualquer informação adicional.
