from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier

def arbolesPoda50(doc):
    print(f'Arbol con el archivo {doc} con poda a 50 niveles maximos ')
    Archivo=open(doc,'r')
    clasesConjunto=[]
    valoresConjunto=[]
    clases=[]
    caracteristicas=[]
    step=1
    for x in Archivo.readlines():
        if len(x)>2:
            atrib=x.replace('\n','').split(',')
            if step!=1: 
                clasesConjunto.append(atrib[-1])
                if not atrib[-1] in clases:
                    clases.append(atrib[-1])
                valoresConjunto.append(list(map(float,atrib[1:-1])))
            else:
                caracteristicas=atrib[1:-1]
                step+=1
    Archivo.close()
    valoresTrain, valoresTest, clasesTrain, clasesTest =train_test_split(valoresConjunto, clasesConjunto, test_size=0.7)
    print(len(clasesTrain))
    print(len(clasesTest))

    #### Algoritmo ################

    clasificador = DecisionTreeClassifier(criterion="entropy", max_depth=50)

    #Modelo
    modelo = clasificador.fit(valoresTrain,clasesTrain)
    arbol=export_text(modelo, feature_names=caracteristicas)
    #print(arbol)

    ##### Clasificar ##############
    clasesRecuperadas=modelo.predict(valoresTest)
    ####### Evaluar ############
    exactitud=accuracy_score(clasesTest,clasesRecuperadas)#Exactitud
    print("Exactitud: ",exactitud)

    matrizConfusion=confusion_matrix(clasesTest,clasesRecuperadas)
    print(matrizConfusion)

    reporte=classification_report(clasesTest, clasesRecuperadas, target_names=clases)
    print(reporte)

def redNeuronal(doc):
    print(f'Red neuronal con el archivo {doc} ')
    Archivo=open(doc,'r')
    clasesConjunto=[]
    valoresConjunto=[]
    clases=[]
    caracteristicas=[]
    step=1
    for x in Archivo.readlines():
        if len(x)>2:
            atrib=x.replace('\n','').split(',')
            if step!=1: 
                clasesConjunto.append(atrib[-1])
                if not atrib[-1] in clases:
                    clases.append(atrib[-1])
                valoresConjunto.append(list(map(float,atrib[1:-1])))
            else:
                caracteristicas=atrib[1:-1]
                step+=1
    Archivo.close()
    valoresTrain, valoresTest, clasesTrain, clasesTest =train_test_split(valoresConjunto, clasesConjunto, test_size=0.7)
    print(len(clasesTrain))
    print(len(clasesTest))

    #### Algoritmo ################ logistic = sigmoid 
    clasificador = MLPClassifier(activation = 'logistic',alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
    #Modelo
    modelo = clasificador.fit(valoresTrain,clasesTrain)
    
    ##### Clasificar ##############
    clasesRecuperadas=modelo.predict(valoresTest)
    ####### Evaluar ############
    exactitud=accuracy_score(clasesTest,clasesRecuperadas)#Exactitud
    print("Exactitud: ",exactitud)

    matrizConfusion=confusion_matrix(clasesTest,clasesRecuperadas)
    print(matrizConfusion)

    reporte=classification_report(clasesTest, clasesRecuperadas, target_names=clases)
    print(reporte)

def correr(doc):
    print("------------------------------------------------")
    arbolesPoda50(doc)
    print("------------------------------------------------")
    redNeuronal(doc)
    print("------------------------------------------------")
    
#correr('Documentos/tokenizacion_Binario.csv')
#correr('Documentos/tokenizacion_Conteo.csv')
#correr('Documentos/Lemas_Binario.csv')
#correr('Documentos/Lemas_Conteo.csv')
#correr('Documentos/Sttemming_Binario.csv')
correr('Documentos/Sttemming_Conteo.csv')


#arbolesPoda50('Documentos/tokenizacion_Conteo.csv')
# arboles('Documentos/tokenizacion_Conteo.csv')
# arboles('Documentos/tokenizacion_Conteo.csv')
# arboles('Documentos/tokenizacion_Conteo.csv')
# arboles('Documentos/tokenizacion_Conteo.csv')
# arboles('Documentos/tokenizacion_Conteo.csv')