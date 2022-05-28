import time 
import hashlib 
from urllib.request import urlopen, Request 
url = Request('https://www.cnnbrasil.com.br/',  # Colocar o site aqui
              headers={'User-Agent': 'Mozilla/5.0'}) 
print("Rodando...") 
while True: 
    try: 
        resposta = urlopen(url).read() 
        hash = hashlib.sha224(resposta).hexdigest() 
        time.sleep(1) 
    
        resposta = urlopen(url).read() 
        Novo_Hash = hashlib.sha224(resposta).hexdigest() 
        
        if Novo_Hash == hash: 
            continue
        else: 
            print("---------------------Site Mudou-------------------------") 
            break
              
    except Exception as e: 
        print("error") 
        break