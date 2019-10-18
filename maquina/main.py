import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


################ Função para redimensionar uma imagem #############################################
def redim(img, largura): 
    alt = int(img.shape[0]/img.shape[1]*largura)
    img = cv2.resize(img, (largura, alt), interpolation = cv2.INTER_AREA)
    return img
################ Lista arquivos do diretorio #######################################################
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
############################################################################################



def CL(locPaiArq,locFilhos,valSIME,qtdMax):
    
    sml = valSIME
    
    # Lê pasta que contem os filhos
    # Lendo todos os arquivos do diretorio
    for filename in files(locFilhos):
        
        # PAI
        pai = cv2.imread(locPaiArq)
        
        # Pega a extencao do arquivo atual
        extension = os.path.splitext(filename)[1][1:]
        
        # Parte de comparação
        if(extension == "png" or extension == "jpg" or extension == "jpeg"):
            # Lê um dos filhos
            #filhoAtual = cv2.imread(filename)
 
            
            caminhoFilho = os.getcwd()+'\\busca\\filhos\\'+filename
            
      
            filhoAtual = cv2.imread(caminhoFilho)
            
            ## IMPORTANTE para testes
            ##cv2.imshow("Teste", filhoAtual)
            ##cv2.waitKey(10000)

            #Aplicando o template Matching
            res = cv2.matchTemplate(pai,filhoAtual,cv2.TM_CCOEFF_NORMED)
        
            #Recupera a similaridade entre o template e o conteúdo da Imagem de busca
            min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
            #texto = 'Similaridade com {0} entre Imagens é {1}%'.format(cv2.TM_CCOEFF_NORMED,round(similaridade*100,2))
        
            if similaridade >= sml:
                cv2.imwrite("out/"+str(similaridade)+filename,filhoAtual)
            else:
                print('Similaridade do filho:'+str(similaridade))
            
        
        elif(extension == "mp4"):
            a = 10
            
            
    
    

############################################################################################
         








def main():

    print('--- Inicializando ---')
    CL('busca/pai/pai2.jpg','busca/filhos/',0.2,10)



# Chama A main
main()
