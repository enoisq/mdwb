import sqlite3
import json
from time import gmtime, strftime



def armazena_dados(dados):
    print ("\\\\**********Módulo de Gerenciamento de Dados\\\\******")
    print ("Processando os dados")
    print ("Armazenando os Dados no BD")
    data=strftime("%Y-%m-%d %H:%M:%S")
    dados['time']=data
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    id_t="teste"
    tensao="teste"
    corrente="teste"
    potencia_ativa="teste"
    potencia_reativa="teste"
    dev_energy="teste"
    with open('modules\hems_mw.json', 'r') as searchfile:
        for line in searchfile:
            if '\"id\"' in line:
                string_teste = line.partition("\"id\": ")[2]
                string_teste = string_teste.replace("\"", "")
                id_t=string_teste[:-2]
            if '\"tensao\"' in line:
                string_teste = line.partition("\"tensao\":")[2]
                string_teste = string_teste.replace("\"", "")
                tensao=string_teste[:-3]
            if '\"corrente\"' in line:
                string_teste = line.partition("\"corrente\":")[2]
                string_teste = string_teste.replace("\"", "")
                corrente=string_teste[:-2]
            if '\"potencia_ativa\"' in line:
                string_teste = line.partition("\"potencia_ativa\":")[2]
                string_teste = string_teste.replace("\"", "")
                potencia_ativa=string_teste[:-2]
            if '\"potencia_reativa\"' in line:
                string_teste = line.partition("\"potencia_reativa\":")[2]
                string_teste = string_teste.replace("\"", "")
                potencia_reativa=string_teste[:-2]
            if '\"temperatura\"' in line:
                string_teste = line.partition("\"temperatura\":")[2]
                string_teste = string_teste.replace("\"", "")
                temperatura=string_teste[:-2]
            if '\"dev_energy\"' in line:
                string_teste = line.partition("\"dev_energy\": ")[2]
                string_teste = string_teste.replace("\"", "")
                dev_energy=string_teste[:-2]
            if '\"dev_onoff\"' in line:
                string_teste = line.partition("\"dev_onoff\": ")[2]
                string_teste = string_teste.replace("\"", "")
                dev_onoff=string_teste[:-1]   
    c.execute("INSERT INTO valores('time', 'dados','id_t','tensao','corrente','potencia_ativa','potencia_reativa','temperatura','dev_energy','dev_onoff','enviado') VALUES (?,?,?,?,?,?,?,?,?,?,?)",(data,str(dados),id_t,tensao,corrente,potencia_ativa,potencia_reativa,temperatura,dev_energy,dev_onoff,0))
    c.execute("SELECT id FROM valores WHERE id = (SELECT MAX(id) FROM valores)")
    dados=str(c.fetchall())
    teste=dados.partition("(")[2]
    idd=teste.partition(",")[0]
    c.execute("INSERT INTO api_devices_data('id','dev_id','voltage','current','active_power','reactive_power','temperature','dev_energy','time','sent') VALUES (?,?,?,?,?,?,?,?,?,?)",(idd,id_t,tensao,corrente,potencia_ativa,potencia_reativa,temperatura,dev_energy,data,0))
    conn.commit()











