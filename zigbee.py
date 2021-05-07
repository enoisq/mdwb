import serial 
import time
from xbee import ZigBee


def coord_receive(porta, pan_id):
       
        while True:
                try:
                        
                        PORT = porta #change the port if you are not using Windows to whatever port you are using
                        BAUD_RATE = 9600
                        ser = serial.Serial(PORT, BAUD_RATE)

                        # Create API object

                        xbee = ZigBee(ser)
                        xbee.set_pan_id(utils.hex_string_to_bytes(pan_id))

                        # Continuously read and print packets
                        while True:
                            try:
                                response = xbee.wait_read_frame()

                                print("\nPacket received at %s : %s" %(time.time(), response))

                            except KeyboardInterrupt:
                                ser.close()
                                break
                except Exception as e:
                        #print (e)
                        pass
                        
