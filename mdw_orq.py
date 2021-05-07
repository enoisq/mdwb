from modules import *
import random
import time
import threading
import json
import sys
import schedule
from contextlib import suppress
import os                                                                       
from multiprocessing import Pool  

print ("\\\\Middleware em execução/////")

processos = ['controles.py', 'nuvem.py', 'dispositivos.py']                                    
                                                  
                                                                                
def roda_processo(processo):
    try:
            os.system('python {}'.format(processo))

    except Exception as e:
            print(e)
                                                                                
                                                                                
if __name__ == "__main__":
        pool = Pool(processes=3)                                                        
        pool.map(roda_processo, processos) 


