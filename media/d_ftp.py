from ftplib import FTP
from datetime import datetime
from contextlib import suppress
import os                                                                       
from multiprocessing import Pool

def roda_arquivo(processo):
    try:
        os.system('python {}'.format(processo))

    except Exception as e:
        print(e)


start = datetime.now()
ftp = FTP('ftpupload.net')
ftp.login('epiz_24056272','ca126623')

# Get All Files
#files = ftp.nlst('\htdocs')
ftp.cwd('htdocs')
files = ftp.nlst()

# Print out the files
for file in files:
    #print (file)
    if(file=="controles_novo.py"):
        print (file)
        with open(file, 'wb') as f:        
           ftp.retrbinary('RETR %s' % file, f.write)

        break
        #fhandle = open('mailteste.php' , 'wb')
        #ftp.retrbinary('RETR '+ file, fhandle.write)

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')

#print (file)

processos = (file)
#if __name__ == "__main__":
#    pool = Pool(processes=1)                                                        
#    pool.map(roda_arquivo, processos) 


