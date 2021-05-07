from modules import *
import random
import time
import threading
import json
import sys
import schedule
from contextlib import suppress

print ("\\\\Middleware em execução/////")


 
def inicio():
        try:                      
                
                #schedule.every(3).seconds.do(recebe).tag('mdw')
                #schedule.every(10).seconds.do(comunicacao_aplicacao.envia_nuvem,1).tag('mdw')
                schedule.every(4).minutes.do(comunicacao_aplicacao.reenviar_dados).tag('mdw')
                
                
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
