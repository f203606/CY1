#!/usr/bin/env python
# coding: utf-8

# In[1]:


def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é {}. Como vai você?'.format(nome),
              'Olá!', 'Oi, tudo bem?']
    print(frases[random.randint(0,2)])
    
def recebeTexto(nome):
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibida = ['bocó']
    for p in palavraProibida:
        if p in texto:
            print('{}: Não vem não! Me respeite!'.format(nome))
            return recebeTexto(nome)
        return texto

def buscaResposta(nome, texto):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('Cliente: ','') == 'Tchau':
                    print('{}: volte sempre!'.format(nome))
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
            else:
                print('{}: Me desculpe, não sei o que falar'.format(nome))
                conhecimento.write('\n{}'.format(texto))
                resposta_user = input(('{}: O que esperava?\n'.format(nome)))
                conhecimento.write('\nChatbot: {}'.format(resposta_user))
                return 'Hum...'
                
def exibeResposta(resposta, nome):
    print(resposta.replace('Chatbot',nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'


# Novas Funções para Interface Gráfica GUI

def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace('Chatbot',nome)

def saudacao_GUI(nome):
    import random
    frases = ['Bom dia! Meu nome é {}. Como vai você?'.format(nome), 'Olá!', 'Oi, tudo bem?']
    return frases[random.randint(0,2)]

def salva_sugestao(sugestao):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.write('Chatbot: {}\n'.format(sugestao))
        
def buscaResposta_GUI(texto):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if jaccard(texto, viu) > 0.3:
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
                    
            else:
                conhecimento.write(texto)
                return 'Me desculpe, não sei o que falar'

def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase

