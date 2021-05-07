
import random
import time
import json
import sqlite3
import os
from datetime import datetime

from azure.iot.device import IoTHubDeviceClient, Message
import paho.mqtt.client as mqtt
from datetime import datetime, date, time, timedelta


def busca_dados():
    print ("\\\**********Módulo de Gerenciamento de Comunicação com Aplicações********\\\\")
    print ("Buscando dados no banco de dados")

    
    data_a= datetime.now()
    data_i = data_a - timedelta(seconds=75)
    data_atual=data_a.strftime('%Y-%m-%d %H:%M:%S')
    data_inicio = data_i.strftime('%Y-%m-%d %H:%M:%S')
    

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT api_devices_data.id,api_devices_data.time,api_devices_data.voltage,api_devices_data.current,api_devices_data.active_power,api_devices_data.reactive_power, api_devices_data.power_factor, api_devices_data.dev_energy, api_app_outlet.mac_address from api_devices_data inner join api_app_outlet on api_devices_data.dev_id=api_app_outlet.id where api_devices_data.time between (?) and (?) and (sent=0) order by api_devices_data.id",(data_inicio,data_atual))
    #c.execute("SELECT * from api_devices_data where time between (?) and (?) and (sent=0) order by id",(data_inicio,data_atual))
    #c.execute("SELECT * from api_devices_data where sent = 0 order by id limit 10")
    dados = c.fetchall()
    #conn.commit()
    #print(dados)
    return dados
    '''
    
    for dados in c.fetchall():
        #print (dados)
        ndado = str(dados).replace("'","\"")
        djson = (str(ndado)[2:-3])
        #print (djson)
        #print(djson)
        jsonpronto = json.loads(djson)
        #if(envia_iothub(jsonpronto)==1):
         #   print ("nao enviou")
          #  reenviar(jsonpronto)
        
    return djson'''

def reenviar_dados():
    print ("\\\**********Módulo de Gerenciamento de Comunicação com Aplicações********\\\\")
    print ("Reenviando Dados")

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT api_devices_data.id,api_devices_data.time,api_devices_data.voltage,api_devices_data.current,api_devices_data.active_power,api_devices_data.reactive_power, api_devices_data.power_factor, api_devices_data.dev_energy, api_app_outlet.mac_address from api_devices_data inner join api_app_outlet on api_devices_data.dev_id=api_app_outlet.id where sent=2 order by api_devices_data.id limit 100")
    #c.execute("SELECT * from api_devices_data where sent = 2 order by id limit 100")
    dados = c.fetchall()
    if (dados != []):
        envia_mqtt(dados)
    else:
        print("nada a reenviar")
        
    #dados = c.fetchall()
    #conn.commit()
    #print(dados)
    #print (c.fetchall())
    
    

def reenviar(dados):
    try:
        print("Gravando informações de dados não enviados")
        timestamp=dados['time']
        dataenvio = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect('json.db')
        c = conn.cursor()
        c.execute("UPDATE valores SET enviado=2 WHERE time=?",(dataenvio,))
        #c.execute("INSERT INTO reenvios(time) VALUES(?)",(dataenvio,))
        conn.commit()
        s1=("log_comunicacao_aplicacao.txt")
        S = open(s1, 'a')
        S.write(str(timestamp)+"\n")
        S.close()

    except Exception as e:
        
        print (e)

    #dadosj = json.dumps(dados)
    #print(dadosj[0]['time'])
    #print(time)
    #print (str(dados))
    #s1=("log_comunicacao_aplicacao.json")
    #S = open(s1, 'w')
    #S.write(str(j)[3:-4])
    #S.close()

    #d = open('log_comunicacao_aplicacao.json','r') #abre arquivo json para leitura
    #js = json.load(d)
    #print (js['time'])
    #print (js['outlets'])
    #d.close()
    
def envia_iothub(dados):
    flag= 1
    #CONNECTION_STRING = "HostName=mdwcopel.azure-devices.net;DeviceId=pythondevice;SharedAccessKey=PzCUFs423r12S9qGKOu74hqwRYR+2LlOCGAssUYv9Fo="

    try:
        client.connect()
    #client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
       
       #print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        # Send the message.
        print( "Enviando mensagem para IoTHub: "+str(dados) )
        client.send_message(str(dados))
        #print ( "Enviada com sucesso!" )
        time.sleep(0.5)
        client.disconnect()
        timestamp=dados['time']
        dataenvio = datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
        print(dataenvio)
        conn = sqlite3.connect('json.db')
        c = conn.cursor()
        c.execute("UPDATE valores SET enviado=1 WHERE time=?",(dataenvio,))
        #c.execute("INSERT INTO reenvios(time) VALUES(?)",(dataenvio,))
        conn.commit()

        flag=2
        

        

    except Exception as e:
        
        print ( "IoTHubClient sample stopped" )
        #reenviar(dados)
        return flag
        
    

    return flag

def on_connect(client, userdata, flags, rc):
    print("Connected flags ",str(flags),"result code ",str(rc))

def envia_mqtt(dados):
    MQTT_ADDRESS = '143.106.17.28'
    # descomente esta linha para usar o servidor da Fundação Eclipse.
    # MQTT_ADDRESS = 'iot.eclipse.org'
    MQTT_PORT = 1883
    # descomente esta linha caso seu servidor possua autenticação.
    # MQTT_AUTH = Auth('login', 'senha')
    MQTT_TIMEOUT = 60

    data=[]
    for i in dados:
        temp=list(i)
        del temp[0]
        data.append(temp)

    #if sys.version_info[0] == 3:
     #   input_func = input
    #else:
     #   input_func = raw_input
    try:
        
        client = mqtt.Client(client_id="hems_mdw_cloud")
        
        # descomente esta linha caso seu servidor possua autenticação.
        #client.username_pw_set(username="teste", password="hem")
        #client.on_connect=on_connect
        client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)
        #result, mid = client.publish('Hems', dados)
        rc = client.publish('hems/data', str(data),retain=True)
        print("RC = ",rc[0])
        if(rc[0]==0):
            for a in dados:
                print (a[0])
                conn = sqlite3.connect('db.sqlite3')
                c = conn.cursor()
                c.execute("UPDATE api_devices_data SET sent=1 WHERE id=?",(a[0],))
        #c.execute("INSERT INTO reenvios(time) VALUES(?)",(dataenvio,))
                conn.commit()
            
        client.loop_start()
        #print (mid)
        print('Mensagem enviada ao canal:')
        print(data)
        
        client.loop_stop()
        client.disconnect()

    except Exception as erro:
        print (erro)
        for a in dados:
                print (a[0])
                conn = sqlite3.connect('db.sqlite3')
                c = conn.cursor()
                c.execute("UPDATE api_devices_data SET sent=2 WHERE id=?",(a[0],))
        #c.execute("INSERT INTO reenvios(time) VALUES(?)",(dataenvio,))
                conn.commit()

def envia_nuvem (metodo):
    
    if (metodo==1):
        if(envia_iothub(busca_dados()))==2:
            print ("Enviando dados para a Nuvem: IoTHub")

    elif(metodo==2):
        envia_mqtt(busca_dados())
        
        
            
    
    

try:
    CONNECTION_STRING = "HostName=mdwcopel.azure-devices.net;DeviceId=pythondevice;SharedAccessKey=PzCUFs423r12S9qGKOu74hqwRYR+2LlOCGAssUYv9Fo="
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

except Exception:
    print ('ignoring failed address lookup')
    pass

    

