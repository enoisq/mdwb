import time
import threading
import json
import csv
import os
from os import listdir
from os.path import isfile, join
import sqlite3
from datetime import datetime


        





def envia_banco(dados,id_):


    
    try:

        if(len(dados)==7):
            d=datetime.strptime(dados[0], '%H:%M:%S-%d/%m/%Y')
            data = d.strftime('%Y-%m-%d %H:%M:%S')

            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()
            c.execute("INSERT INTO api_devices_data ('voltage','current','active_power','reactive_power','power_factor','dev_energy','time','dev_id') VALUES (?,?,?,?,?,?,?,?) ",(dados[1],dados[2],dados[4],dados[5],dados[3],dados[6],data,str(id_),))
            conn.commit()
            print("dev_id: "+str(id_))
            print("data: "+data)
            print("voltagem: "+dados[1])
            print("corrente: "+dados[2])
            print("fator potencia: "+dados[3])
            print("potencia ativa: "+dados[4])
            print("pot reativa: "+dados[5])
            print("pot aparente: "+dados[6])
    except Exception as erro:
        print(erro)
        pass

def busca_id(mac):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT id from api_app_outlet where mac_address = (?)",(mac,))
    #c.execute("SELECT * from valores")
    dados = c.fetchall()
    print (dados)
    if(dados==[]):
        print('nao existe')
        c.execute("INSERT INTO api_app_outlet ('mac_address') VALUES (?) ",(mac,))
        conn.commit()
        c.execute("SELECT id from api_app_outlet where mac_address = (?)",(mac,))
        dados = c.fetchall()
        print (dados[0][0])
        
    else:
        print(dados[0][0])

    id_tom = dados[0][0]
    return (id_tom)
   

def recebe_dados():
    print ("\\\*****Módulo de Gerenciamento de Comunicação com os Dispositivos******\\\\")
    try:
        #path = os.getcwd()+"\medidas"
        path = "/users/root/medidas"
        #path = '\'
        files = [f for f in listdir(path) if isfile(join(path, f))]
        print(files)
        for tom in files:
            if "swp" not in tom:
                x=busca_id(tom)
                #print(x)
                dados = open(path+"/"+tom,"r")
                #dados = open(path+"\\"+tom,"r")
                linhas = dados.readlines()
                dados.close()
                ultima = linhas[len(linhas)-1]
                #print (ultima)
                campos = ultima.split()
                envia_banco(campos,x)           
                os.remove(path+"/"+tom)

    except Exception as erro:
        print(str(erro))
        pass



