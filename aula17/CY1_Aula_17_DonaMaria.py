#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import CY1_Aula_17_ChatbotBase as pc

nome_maquina = 'Maria'
pc.saudacoes(nome_maquina)
while True:
    texto = pc.recebeTexto()
    resposta = pc.buscaResposta(nome_maquina, texto)
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break

    

