
git push --debug
# Script foo.py

def soma(a, b):
    return a + b

if __name__ == "__main__":
    print("Testando a função soma:")
    print(soma(2, 3))
    

"none"
import math
print(math.pi)

from asyncio import taskgroups, tasks
from ctypes import LibraryLoader
from dbm.ndbm import library
from distutils.command import install
from distutils.errors import LibError
from gettext import npgettext
from multiprocessing.dummy import Pipe
from pickle import HIGHEST_PROTOCOL
from platform import libc_ver
from socket import IP_OPTIONS
from sqlite3 import apilevel
from sys import api_version



# Lotes
lotes = 3

# Limite de perda diária
limite_perda = 500

# Limite de ganho diário
limite_ganho = 500

# Stop loss em pontos
sl = 4

# Gain em pontos
gain = 5

# Stop loss em pontos para a vwap band
sl_vwap = [4, 5, 7]

# Gain em pontos para a vwap band
gain_vwap = [5, 10, 21]

# DEfiniçao de Media Movel
media_21 = media_movel=(21)

# Definiçao de vwap
vwap_diaria = vwap_diaria=()

# Definiçao de Prier Cote
prier_cote = Prier_Cote=()

# Definiçao de ifr
ifr = IFR=(14)

# Definição de variáveis para operação
compra = False
venda = False
preco_referencia = 0
preco_referencia_invertido = 0
stop_loss = 0
take_profit = 0
touched = False





# Declaração das variáveis de venda
# Definiçao de preço de venda

vendido = False
preco_venda = 0
stop_loss_venda = 0
take_profit_venda = 0

preço_maximo = 0

preço_minimo = 0

preço_abertura = 0

preço_atual = 0

preco_tocar_prier_cote_e_tendencia_de_alta = 0

preco_atinge_primeira_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70  = 0

preco_atinge_segunda_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70 = 0

preco_atinge_terceira_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70 = 0



# Declaração das variáveis de compra
# Definiçao de preço de compra

comprado = False
preco_compra = 0
stop_loss_compra = 0
take_profit_compra = 0


preço_abertura = 0

preco_atual = 0

preco_tocar_prier_cote_e_tendencia_de_baixa = 0

preco_atinge_primeira_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35 = 0

preco_atinge_segunda_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35 = 0

preco_atinge_terceira_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35 = 0


# Definição de variáveis para operação
compra = False
venda = False
preco_referencia = 0
preco_referencia_invertido = 0
stop_loss = 0
take_profit = 0
touched = False


# Definindo os níveis de suporte e resistência
# com base nos preços dos últimos 20 ajustes diários

prices = api.get_adjusted_close_prices('MINIDOLAR', 21)[:-1]

supports = []
resistances = []

for i in range(1, len(prices[0])):
    period = prices[:, i - 1:i + 4]
    max_price = np.max(period)
    min_price = np.min(period)
    pivot = prices[1, i - 1]

    if pivot > max_price:
        resistances.append(max_price)
        supports.append(min_price)
    elif pivot < min_price:
        resistances.append(max_price)
        supports.append(min_price)
    else:        resistances.append(np.nan)
        supports.append(npgettext.nan)

supports = supports[-20:]
resistances = resistances[-20:]






# Definiçoes de tempo

tempo_atual = 0

timestamp_ant = 0

tempo_espera = 20

atualizar_tempo = 0

tempo_toque_anterior = 20


encontrar_candle_maior_volume = 0


candle_maior_volume = 0






# Operação de venda quando o preço toca o Prier Cote pela primeira vez
if preco_tocar_prier_cote_e_tendencia_de_alta():
    venda(quantidade=1, preco=preco_atual, stop_loss=preco_atual-4, take_profit=preco_atual+5)

# Operação de venda quando o preço atinge a primeira linha da VWAP Band acima da VWAP diária
if preco_atinge_primeira_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70():
    candle_maior_volume = encontrar_candle_maior_volume[0] 
    venda(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-4, take_profit=candle_maior_volume.preco_abertura+5)

# Operação de venda quando o preço atinge a segunda linha da VWAP Band acima da VWAP diária
if preco_atinge_segunda_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70():
    candle_maior_volume = encontrar_candle_maior_volume()
    venda(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-5, take_profit=candle_maior_volume.preco_abertura+10)

# Operação de venda quando o preço atinge a terceira linha da VWAP Band acima da VWAP diária
if preco_atinge_terceira_linha_vwap_band_acima_da_vwap_diaria_e_ifr_acima_de_70():
    candle_maior_volume = encontrar_candle_maior_volume()
    venda(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-7, take_profit=media_21)




# Operação de compra quando o preço toca o Prier Cote pela primeira vez
if preco_tocar_prier_cote_e_tendencia_de_baixa():
    compra(quantidade=1, preco=preco_atual, stop_loss=preco_atual-4, take_profit=preco_atual+5)

# Operação de compra quando o preço atinge a primeira linha da VWAP Band abaixo da VWAP diária
if preco_atinge_primeira_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35():
    candle_maior_volume = encontrar_candle_maior_volume()
    compra(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-4, take_profit=candle_maior_volume.preco_abertura+5)

# Operação de compra quando o preço atinge a segunda linha da VWAP Band abaixo da VWAP diária
if preco_atinge_segunda_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35():
    candle_maior_volume = encontrar_candle_maior_volume()
    compra(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-5, take_profit=candle_maior_volume.preco_abertura+10)

# Operação de compra quando o preço atinge a terceira linha da VWAP Band abaixo da VWAP diária
if preco_atinge_terceira_linha_vwap_band_abaixo_da_vwap_diaria_e_ifr_abaixo_de_35():
    candle_maior_volume = encontrar_candle_maior_volume()
    compra(quantidade=1, preco=candle_maior_volume.preco_abertura, stop_loss=candle_maior_volume.preco_abertura-7, take_profit=media_21)






def new_func1():
    return "python.analysis.extraPaths"

import new_func1() : ["/sources]"]





import datetime

#verificando se ja passou o tempo de espera para uma nova operaçao no mesmo nivel de preço

if  tempo_atual : tempo_toque_anterior = 20 > tempo_espera *60

    # definindo o tempo de espera
    

tempo_espera = (20) # em minutos
    
    
    # armazenando tempo do ultimo toque no preço anterior
    tempo_toque_anterior = (20)

    #atualizar o tempo do ultimo toque no preço anterior
    tempo_toque_anterior  = tempo_atual 



def atualizar_tempo():
    global tempo_atual
    tempo_atual = datetime.datetime.now()
    print("O tempo atual é:", tempo_atual)
def new_func7(tempo_toque_anterior):
    return tempo_toque_anterior


    # definindo o tempo de espera
    tempo_espera = 20  # em minutos

    # armazenando tempo do ultimo toque no preço anterior
    tempo_toque_anterios = 0

    #atualizar o tempo do ultimo toque no preço anterior
    tempo_toque_anterior = tempo_atual









import talib


# Obter tempo do toque no preço anterior
timestamp = 0

new_var = close
new_var1 = open
cdl_shooting_star = talib.CDLSHOOTINGSTAR(HIGHEST_PROTOCOL, new_var1, open, new_var)
if cdl_shooting_star[-2] == 100:
    timestamp = timestamp_ant

import time
# definiçao de variaveis:
#armazenando o tempo atual em segundos
def new_func(tempo_atual):
    new_var = tempo_atual - time.time()
   






# Conexão com IQ Option
API = IP_OPTIONS.IQ_Option("email", "senha")
API.connect()

# Loop infinito para operação
while True:
    # Checagem do horário
    hora_atual = int(datetime.datetime.now().strftime("%H%M%S"))
    if hora_atual < 60000 or hora_atual > 220000:
        continue
    
if tempo_atual - tempo_toque_anterior > tempo_espera*60:

    # definindo o tempo de espera
    tempo_espera = 20  # em minutos

    # armazenando tempo do ultimo toque no preço anterior
    tempo_toque_anterios = 0

    #atualizar o tempo do ultimo toque no preço anterior
    tempo_toque_anterior = tempo_atual

    # definindo o tempo de espera
    tempo_espera = 20  # em minuto


    # Obtenção do preço atual
    preco_atual = API.get_best_candles("WDOJ23", 60)[-1]["close"]

    # Checagem da primeira vez que o preço tocou o preço de referência
    if not touched:
        if preco_atual <= preco_referencia:
            touched = True
            stop_loss = preco_referencia + 0.002
            take_profit = preco_referencia - 0.001
            compra = True
        elif preco_atual >= preco_referencia:
            touched = True
            stop_loss = preco_referencia - 0.002
            take_profit = preco_referencia + 0.001
            venda = True

    # Checagem para inverter a operação caso o preço rompa o preço de referência
    if touched:
        if compra and preco_atual > preco_referencia_invertido:
            compra = False
            venda = True
            preco_referencia = preco_referencia_invertido
            stop_loss = preco_referencia - 0.002
            take_profit = preco_referencia + 0.001
        elif venda and preco_atual < preco_referencia_invertido:
            compra = True
            venda = False
            preco_referencia = preco_referencia_invertido
            stop_loss = preco_referencia + 0.002
            take_profit = preco_referencia - 0.001

    # Execução da operação de compra ou venda
    if compra:
        if API.buy(3, "WDOJ23", "call", 1):
            print("Compra executada")
            preco_referencia_invertido = preco_referencia
            preco_referencia = preco_atual
            touched = False
    elif venda:
        if API.buy(3, "WDOJ23", "put", 1):
            print("Venda executada")
            preco_referencia_invertido = preco_referencia
            preco_referencia = preco_atual
            touched = False

    # Checagem de limite de perda diária
     if API.get_balance() - limite_perda <= API.get_balance_changes():
        break
    # Checagem de limite de ganho diário
    if API.get_balance_changes() >= limite_ganho:
        break

    # Intervalo de tempo para próxima iteração
    time.sleep(0.5)









