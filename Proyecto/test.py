import codecs
from nltk.tokenize import word_tokenize as wt
from nltk.stem import WordNetLemmatizer
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
    
#AGREGAR UNA VARIANTE QUE ELIMINE FRECUENCIA SIMPLE
def obtencionVoc(doc,minFreq=1):
	docto=codecs.open(doc,'r')
	Voc={}
	for x in docto.readlines():
		if len(x)>3:
			l=x.split("\t")
			Text=l[1].split(" ")
			for y in Text:
				if len(y)>0:
					if y in Voc:
						Voc[y]+=1
					else:
						Voc[y]=1
	docto.close()
	#print(Voc)
	DocVoc=codecs.open(doc+'Voc.csv','w')
	Frec1=0
	for x in Voc:
		if Voc[x] >= minFreq:
			DocVoc.write(x+","+str(Voc[x])+",\n")
		if Voc[x]==1:
			Frec1+=1
	DocVoc.close()
	print(doc+"--> "+str(Frec1))

#categorias y lemas 
def Lemas(doc,dicc):
    Lematizar=WordNetLemmatizer()
    docto=codecs.open(doc,'r')
    Salida = codecs.open('Documentos/Lemas.txt', "w")
    for x in docto.readlines():
        if len(x)>1:
            datos=x.split('\t')
            id = datos[0]#idioma= datos[1]
            Text=wt(datos[2].lower())
            # Text=Texto.split(' ')#todo cambiar a minusculas 
            lemas=""
            for y in range(len(Text)-1):
                lema = Lematizar.lemmatize(Text[y])
                lemas+=lema
                lemas+=" "
            Salida.write(f'{id}\t{lemas}\t{dicc[datos[0]]}')
    docto.close()
    Salida.close()


def destringifyTupleData(d):
    return [tuple(destringifyList(l)) for l in d]

def destringifyList(l):
    return map(float, l)

def ObtenListaAtrib(Atributos):
	a=[]
	cad=""
	for l in Atributos.readlines():
		t=l.split(',')
		if len(t[0])>0:
			cad=cad+','+t[0]
			a.append(t[0])
	#print(len(a))
	return a,cad[1:]

def ObtenDocto(docto):
    salida=codecs.open("Documentos/"+Entrada+'_Conteo.csv','w')
    salidaBi=codecs.open("Documentos/"+Entrada+'_Binario.csv','w')
    salida.write("Id,"+CadAtrib+",Clase\n")
    salidaBi.write("Id,"+CadAtrib+",Clase\n")
    for l in docto.readlines():
        if len(l)>5:
            x=l.split('\t')
            FinClas=x[2].replace('\n','')
            texto=x[1].split(' ')
            cad=str(x[0])+','#Frecuencia
            cad3=str(x[0])+','#Ocurrencia
            Id=x[0]
            vector=InicializaVector()
            for i in texto:
                if i in vector:
                    vector[i]+=1
            for i in range(len(Atrib)):
                cad=cad+str(vector[Atrib[i]])+','
                if vector[Atrib[i]]>=1:
                    cad3=cad3+'1,'
                else:
                    cad3=cad3+'0,'
            cad=cad+FinClas
            cad3=cad3+FinClas
            salida.write(cad+'\n')
            salidaBi.write(cad3+'\n')
    salida.close()
    salidaBi.close()

def InicializaVector():
    tmp={}
    for i in Atrib:
        tmp[i]=0
    return tmp

docclases=codecs.open('Documentos/Gold-Ingles.csv','r')
clasesdicc={}
for x in docclases.readlines():
    if len(x)>2:
        lane=x.split(',')
        clasesdicc[lane[0]]=lane[2]
docclases.close()
#print(clasesdicc)

#Tokeniza("Documentos/English.txt",clasesdicc)
obtencionVoc("Documentos/tokenizacion.txt",2)
#Lemas("Documentos/English.txt",clasesdicc)


Entrada="tokenizacion.txt"
Atrib=[]
CadAtrib=''
#Leer el vocabulario para obtener los atributos
"""
DocCar=codecs.open('Documentos/'+Entrada+'Voc.csv','r')
Atrib,CadAtrib=ObtenListaAtrib(DocCar)
print(str(len(Atrib)))
DocCar.close()


docToCSV=codecs.open("Documentos/tokenizacion.txt",'r')
ObtenDocto(docToCSV)
docToCSV.close()
"""
