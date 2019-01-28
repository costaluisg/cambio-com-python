import requests
import jsons
import pandas as pd

def main():
    dollar = cambio_dollar()
    euro = cambio_euro()
    exportar_csv(dollar, euro)

def cambio_dollar(url='http://data.fixer.io/api/latest?access_key=50bb4128f07968d9320247f6dedecf8b&format=1'):
    print('estabelecendo conexão com link...')
    response = requests.get(url)
    if response.status_code == 200:
        print('estabeleceu conexão')
        dados = response.json()
        data_hoje = dados['date']
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_usd
        print('Hoje a cotação do Dólar  é US$ %.2f' % real)
        print("hoje é", data_hoje)
        return real
    else:
        print('Site com algum problema!')


def cambio_euro(url='http://data.fixer.io/api/latest?access_key=50bb4128f07968d9320247f6dedecf8b&format=1'):
    print('estabelecendo conexão com link...')
    response = requests.get(url)
    if response.status_code == 200:
        print('estabeleceu conexão')
        dados = response.json()
        data_hoje = dados['date']
        taxa_eur = dados['rates']['EUR']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_eur
        return real
        print('Hoje a cotação do euro  é € %.2f' % real)
        print("hoje é", data_hoje)
    else:
        print('Site com algum problema!')

def exportar_csv(dollar,euro):
    linha = {'Dollar - USD': [dollar],'Euro - EUR':[euro]}
    frame = pd.DataFrame (linha, columns= ['Dollar -USD', 'Euro - EUR'])
    frame.to_csv('moeda.csv')
    print('Dados salvo na tabela')

#Pede para que o programa execute a nossa funcao main
if __name__=='__main__':
    main()
