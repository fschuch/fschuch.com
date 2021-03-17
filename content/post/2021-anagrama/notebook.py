#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import os.path
from unidecode import unidecode
import time
from collections import Counter


# In[ ]:


def normalizar_palavra(palavra: str) -> str:
    return unidecode(palavra).replace(" ", "").lower()


# In[ ]:


normalizar_palavra("Canção da América")


# In[ ]:


def inspecionar_palavra(palavra: str) -> Counter:
    return Counter(normalizar_palavra(palavra))


# In[ ]:


sum(inspecionar_palavra("Aprenda Python").values())


# In[ ]:


len("Aprenda Python")


# In[ ]:


sorted(inspecionar_palavra("eugenie gut zaza"))


# In[ ]:


"'a', 'e', 'g', 'i', 'n', 't', 'u', 'z'".replace("'", "`")


# In[ ]:


def testa_se_anagrama(inspecionada_1: Counter, inspecionada_2: Counter) -> bool:
    return inspecionada_1 == inspecionada_2


# In[ ]:


testa_se_anagrama(
    inspecionar_palavra("Roma"), inspecionar_palavra("amor"),
)


# In[ ]:


testa_se_anagrama(
    inspecionar_palavra("Iracema"), inspecionar_palavra("América"),
)


# In[ ]:


testa_se_anagrama(
    inspecionar_palavra("Python"), inspecionar_palavra("Fortran"),
)


# In[ ]:


page = requests.get("https://www.dicio.com.br/palavras-comecam-z-com-14-letras/")


# In[ ]:


soup = BeautifulSoup(page.content, "html.parser")


# In[ ]:


soup.find_all("p")[1].get_text(separator=" ").strip()


# In[ ]:


soup.find_all("p")[1].get_text(separator=" ").strip().split()


# In[ ]:


def obtem_as_palavras_possiveis(primeira_letra: str, numero_de_letras: int) -> list:
    def verifica_se_arquivo_existe(nome_do_arquivo: str) -> bool:
        return os.path.isfile(nome_do_arquivo)

    def leia_o_arquivo(nome_do_arquivo: str) -> str:
        with open(nome_do_arquivo, "r") as file_in:
            texto = file_in.read()
        return texto

    def escreva_o_arquivo(nome_do_arquivo: str, conteudo: str) -> None:
        with open(nome_do_arquivo, "w") as file_out:
            file_out.write(conteudo)

    palavras_alvo = f"palavras-comecam-{primeira_letra}-com-{numero_de_letras}-letras"
    arquivo_backup = palavras_alvo + ".txt"

    # Se o arquivo existe, carregue do disco
    if verifica_se_arquivo_existe(arquivo_backup):
        lista_de_palavras = leia_o_arquivo(arquivo_backup)
    # Senão, obtenha as palavras e salve o arquivo para o disco
    # para que possa ser utilizado da próxima vez
    else:
        page = requests.get(f"https://www.dicio.com.br/{palavras_alvo}/")
        soup = BeautifulSoup(page.content, "html.parser")
        lista_de_palavras = soup.find_all("p")[1].get_text(separator=" ").strip()
        lista_de_palavras = normalizar_palavra(lista_de_palavras)
        escreva_o_arquivo(arquivo_backup, lista_de_palavras)
        time.sleep(2)

    return lista_de_palavras.split()


# In[ ]:


obtem_as_palavras_possiveis("z", 14)


# In[ ]:


def procurar_anagrama(palavra_referencia: str) -> list:
    def compara_contra_alvo(palavra_alvo):
        return testa_se_anagrama(
            referencia_inspecionada, inspecionar_palavra(palavra_alvo),
        )

    referencia_inspecionada = inspecionar_palavra(palavra_referencia)
    letras_na_referencia = referencia_inspecionada.keys()
    len_referencia = sum(referencia_inspecionada.values())

    lista_possibilidades = []
    for letra in letras_na_referencia:
        lista_possibilidades.extend(obtem_as_palavras_possiveis(letra, len_referencia))

    print(f"Testando anagrama contra {len(lista_possibilidades)} possibilidades")
    return list(filter(compara_contra_alvo, lista_possibilidades))


# In[ ]:


referencia = "eugenie gut zaza"


# In[ ]:


list(procurar_anagrama(referencia))


# In[ ]:


list(procurar_anagrama("Roma"))


# In[ ]:


list(procurar_anagrama("Aprenda"))


# In[ ]:


list(procurar_anagrama("Python"))


# In[ ]:




