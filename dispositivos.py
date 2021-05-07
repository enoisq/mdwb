from modules import *
import random
import time
import threading
import json
import sys
import schedule
from contextlib import suppress

print ("\\\\Middleware em execução/////")


def recebe():
        comunicacao_dispositivos.recebe_dados()

   
def inicio():
        try:                      
                
                schedule.every(7).seconds.do(recebe).tag('mdw')
                #schedule.every(10).seconds.do(comunicacao_aplicacao.envia_nuvem,1).tag('mdw')
                #schedule.every(15).seconds.do(comunicacao_aplicacao.reenviar_dados).tag('mdw')
                
                
        except KeyboardInterrupt:
            sys.exit()    
            print ( "Middleware encerrado" )
            
        while True:
                try:
                        schedule.run_pending()
                        time.sleep(0.5)

                except Exception as e:   
                        print ( "rodando ainda" + str(e) )
                        pass
                except KeyboardInterrupt:
                        sys.exit()    
                        print ( "Middleware encerrado" )            
        
inicio()
