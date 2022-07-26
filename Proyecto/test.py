import codecs
from nltk.tokenize import word_tokenize as wt
def Tokeniza(doc,dicc):
    #print(dicc)
	docto=codecs.open(doc,'r')
	Salida=codecs.open("Documentos/tokenizacion.txt",'w')
	for x in docto.readlines():
		if len(x)>1:
			datos=x.split('\t')
			Texto=wt(datos[2].lower())
			CadFinal = " ".join(Texto)
            #if datos[0] in dicc:
			Salida.write(datos[0]+'\t'+CadFinal+"\t"+dicc[datos[0]])
	docto.close()
	Salida.close()
    

docclases=codecs.open('Documentos/Gold-Ingles.csv','r')
clasesdicc={}
for x in docclases.readlines():
    if len(x)>2:
        lane=x.split(',')
        clasesdicc[lane[0]]=lane[2]
docclases.close()
#print(clasesdicc)
Tokeniza("Documentos/English.txt",clasesdicc)