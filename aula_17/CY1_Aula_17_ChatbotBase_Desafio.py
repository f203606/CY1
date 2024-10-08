#!/usr/bin/env python
# coding: utf-8

# In[2]:


def saudacoes(nome_maquina, nome_cliente):
    import random
    from datetime import datetime, time
    #frases = ['Bom dia, {}! Meu nome é {}. Como vai você?'.format(nome_cliente, nome_maquina),
              #'Olá!', 'Oi, tudo bem?']
    #print(frases[random.randint(0,2)])
    hora_atual = datetime.now().time().hour
    if 0 <= hora_atual < 12:
        print('Bom dia, {}! Meu nome é {}.'.format(nome_cliente, nome_maquina))
    elif 12 <= hora_atual < 18:
        print('Boa tarde, {}! Meu nome é {}.'.format(nome_cliente, nome_maquina))
    else:
        print('Boa noite, {}! Meu nome é {}.'.format(nome_cliente, nome_maquina))
    
def recebeTexto(nome_maquina, nome_cliente):
    texto = 'Cliente: ' + input('{}: '.format(nome_cliente))
    palavraProibida = ['bocó','bobo']
    fraseProibida = ['você é horrível','que chatbot insuportável']
    tomMensagem = ['reclamação','elogio','sugestão']
    for p in palavraProibida:
        for frase in fraseProibida:
            if p in texto.strip().lower() or frase in texto.strip().lower():
                print('{}: Não vem não! Me respeite!'.format(nome_maquina))
                return recebeTexto(nome_maquina, nome_cliente)
    for tom in tomMensagem:
        if tom in texto.strip().lower():
            print('{}: Ok. Você está fazendo um(a) {}'.format(nome_maquina, tom))
            return recebeTexto(nome_maquina, nome_cliente)
    return texto

def buscaResposta(nome_maquina, texto):
    with open('CY1_Aula_17_BaseConhecimento.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('Cliente: ','').upper() == 'TCHAU':
                    print('{}: volte sempre!'.format(nome_maquina))
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
            else:
                print('{}: Me desculpe, não sei o que falar'.format(nome_maquina))
                conhecimento.write('\n{}'.format(texto))
                resposta_user = input(('{}: O que esperava?\n'.format(nome_maquina)))
                conhecimento.write('\nChatbot: {}'.format(resposta_user))
                return 'Hum...'
                
def exibeResposta(resposta, nome_maquina):
    print(resposta.replace('Chatbot', nome_maquina))
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

