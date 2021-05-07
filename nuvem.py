from modules import *
import random
import time
import threading
import json
import sys
import schedule
import sqlite3
from contextlib import suppress

print ("\\\\Middleware em execução/////")


def recebe():
        dados.armazena_dados(comunicacao_dispositivos.envia_ger_dados())


def get_time():
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute("SELECT cloud_interval from api_cloud_initial_config order by id desc limit 1")
        dados = c.fetchall()
        time = dados
        if(time==[]):
                time = 60
        else:
                time = dados[0][0]
        return (time)

def update_time(current_interval):
        new_interval=get_time()
        if(new_interval != current_interval):
                schedule.clear('cloud')
                print("Update Interval")
                #print(schedule.jobs)
                inicio(new_interval)
        
        


def inicio(interval):
        try:                      
                print("Enviando com intervalo de " + str(interval))
                #schedule.every(3).seconds.do(recebe).tag('mdw')
                schedule.every(interval).seconds.do(comunicacao_aplicacao.envia_nuvem,2).tag('cloud')
                schedule.every(60).seconds.do(update_time,interval).tag('cloud')
                #schedule.every(15).seconds.do(comunicacao_aplicacao.reenviar_dados).tag('mdw')
                print(schedule.jobs)
                
        except KeyboardInterrupt:
            sys.exit()    
            print ( "Middleware encerrado" )
            
        while True:
                try:
                        schedule.run_pending()
                        time.sleep(0.5)
                        #print(schedule.jobs)
                

                except Exception as e:   
                        print ( "rodando ainda" + str(e) )
                        pass
                except KeyboardInterrupt:
                        sys.exit()    
                        print ( "Middleware encerrado" )            
            

inicio(get_time())
