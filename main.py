#Importar bibliotecas necessarias
import requests
import json
import pandas as pd #pip install pandas & openpyxl
import pprint

#Consultar API com as informacoes
data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data = json.loads(data.content)
#Variaveis
candidato = []
numero = []
partido = []
votos = []
porcentagem = []
situacao = []

#Buscar as informacoes
for informacoes in json_data['cand']:    
    if informacoes['seq']: # in ['1', '2', '3', '4']:
        candidato.append(informacoes['nm'])
        numero.append(informacoes['n'])
        partido.append(informacoes['cc'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
        situacao.append(informacoes['st'])        
resultado = pd.DataFrame(list(zip(candidato, numero, partido, votos, porcentagem, situacao)), columns = [
    'Candidato', 'numero', 'Partido', 'Nº de Votos', 'Percentual', 'Situacao'
])

#Salvar resultado na pasta .xlsx ou exibe em tela
resultado.to_excel('Resultado.xlsx')
#pprint.pprint(resultado)












