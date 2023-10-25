#!/usr/bin/env python
# coding: utf-8

# In[22]:


print("Hola Mundo")
print("Mi nombre es willy y hoy te enseñare python")


# In[ ]:





# #  Data Types

# In[1]:


type(1) #funcion para saber que clase de cod es el que esta entre
#el parentesis a lo cual me indica que es int (entero , refiriendose)
# a los numeros enteros.


# In[3]:


type(2.4) #float = decimal


# In[4]:


1+2


# In[5]:


4-1


# In[6]:


type(True)


# In[9]:


type(False)


# In[ ]:


#en pyton todo lo que este en comillas sea dobles o simples es str o texto


# In[10]:


type("Hello World")


# In[11]:


"Hello World".upper() #codigo para pasar todo a mayuscula


# In[12]:


"Hello World".lower() #codigo para poner todo en minuscula


# In[13]:


"Hello World".title() #codigo para poner solo mayuscula las primeras palabras


# In[16]:


"Hello World".count('l') #codigo para saber cuantos argemtinos se repiten en una cadena
#en este caso de texto puse l osea indica que tiene 3 L


# In[17]:


"Hello World".replace('o', 'u') #este codigo hara que cada letra o en este texto
#sea reemplazada por u


# In[ ]:





# # VARIABLES

# In[11]:


message_1 = ("Estoy Aprendiendo Python")


# In[12]:


message_1


# In[13]:


message_2 = ("Y es divertido")


# In[15]:


message_2


# In[16]:


message_2


# In[18]:


message_1 + message_2


# In[20]:


message_1 + " " + message_2


# In[27]:


f'{message_1}'


# In[35]:


f'{message_1 + " " + message_2}' #como separar bien la y ejemplo


# In[ ]:





# In[34]:


f'{message_1 +   message_2}' #muestra que por mas que separemos no lo entendera python
#f es mas poderoso porque puede tener tanto cadena de texto como variables


# # LISTAS
# 

# In[ ]:





# In[9]:


countries = ['peru', 'chile', 'india', 'canada']


# In[ ]:





# In[ ]:





# In[4]:


countries


# In[ ]:





# In[39]:


countries[1]


# In[40]:


countries[-4]


# In[42]:


countries[-2]


# In[44]:


countries


# In[ ]:





# # REBANADAS O SLICING!!!
# 

# In[ ]:


nombre_lista[start:stop] #no estara en nuestra lista, regla general
# debemos escribir siempre el ultimo index+1


# In[15]:


countries[0:3]


# In[ ]:





# In[47]:


countries[1:+4] # o borar el ultimo elemento ej [1:]


# In[49]:


countries[0:2] # aca solo queriamos los 2 primero


# # OPERACIONES Y METODOS
# CON LISTAS
# 
# 

# In[51]:


countries.append('brasil') #append para sumar algo a la lista


# In[ ]:





# In[10]:


countries


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


countries_2


# In[ ]:





# In[12]:


countries


# In[ ]:





# In[ ]:





# In[ ]:


# countries.insert(0, 'argentina') #ingresar nuevo pais 
#pero en un orden que queremos


# In[ ]:


#contantenando lista 1 y 2 de paises


# In[15]:


countries_2 = ['uruguay', 'paraguay', 'mexico']


# In[ ]:





# In[11]:


countries_2


# In[ ]:





# In[11]:


countries


# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


countries_2


# In[ ]:





# # CONCATENACION

# In[9]:


countries + countries_2


# In[12]:


Nueva_lista = [countries, countries_2]


# In[13]:


Nueva_lista


# In[ ]:


#ELIMINAR ELEMENTOS


# In[20]:


countries.remove('chile')


# In[12]:


countries


# In[ ]:





# In[ ]:





# In[22]:


countries.pop(2) #sirve para referencia y nos dice que elemento estamos eliminando


# In[23]:


countries


# In[24]:


del countries_2[2]


# In[25]:


countries_2


# In[ ]:





# # ORDENAR UNA LISTA

# In[26]:


numeros = [2,3,4,6,7,9]


# In[27]:


numeros


# In[28]:


numeros.sort() #ordenar de menor a mayor


# In[29]:


numeros


# In[31]:


numeros.sort(reverse=True) #ordenar de mayor a menor


# In[32]:


numeros


# In[33]:


numeros[0] = 1000 #actualizamos el valor de 10 x 1000 al poner 0 que era el primer elemento en la lista


# In[34]:


numeros


# In[ ]:





# # COPIAR UNA LISTA

# In[35]:


paises = countries.copy() #metodo copy para copiar la lista


# In[36]:


paises


# In[38]:


paises[:] #2da forma como hacer una lista


# In[39]:


paises_copia2 = paises[:] #asi terminamos de copiar la 2da lista y cambiandole nombre


# In[40]:


paises_copia2


# In[ ]:


#el tema es el siguiente que si modificamos la lista original con append etc , las otras tambien se modifican, como podriamos hacer
#para evitar esto y crear copias pero que sean independientes ? ... sencillo haciendo la copia con countries.copy() o paises[:]
#van a crearse listas independientes , Pero si hacemos algo como nueva_lista3 = countries y al parecer todo bien
#hicimos una copia, pero esta copia no sera independiente... asi que depende de lo que quieras usar copy o [:] o directamente 
#hacer los otros si queremos dependencia o independencia.


# In[ ]:





# # DICCIONARIOS
# 
# #los dicciones en python nos ayudan almacenar data en forma de item
#  un item es esto que vemos aca una llave + 1 valor : 'key1':'value1 , los diccionarios
# #al igual que las listas son mutables osea sus valores pueden cambiar sin embargo
# #en un diccionario no podemos tener llaves duplicadas, para acceder
# #para acceder a un valor de un diccionario haremos algo parecido a la indexacion con listas
# #solo q aca entraremos mediante las llaves, ahora veremos :

# In[41]:


mi_diccionario = {'key1':'value1', 'key2':'value2'}


# In[42]:


my_data = {'nombre':'willy', 'edad':26}


# In[45]:


my_data


# In[ ]:





# In[47]:


my_data['nombre'] #como vieron al poner my data pero con el nombre solo da esa info


# In[48]:


my_data.keys()


# In[49]:


my_data.values()


# In[50]:


my_data.items()


# In[ ]:





# # AGREGAR / ACTUALIZAR ELEMENTOS ,haremos alguna como una indexacion imaginaria en este caso quiero agregar estatura y mas datos, fijense:

# In[51]:


my_data = {'nombre':'willy', 'edad':26}


# In[52]:


my_data['estatura'] = 1.72


# In[53]:


my_data


# In[59]:


my_data.update({'estatura':195, 'lenguajes':['ingles','portugues']}) #-->y este es el otro metodo para agregarle mas items 
# a un diccionario, en mi caso agregue lenguajes pero correji estatura tambien.


# In[ ]:





# In[60]:


my_data


# In[ ]:





# # COPIAR UN DICCIONARIO

# In[57]:


nuevo_diccionario = my_data.copy()   #usando metodo copy tenemos listas independientes , es lo mismo que en listas, usando los metodos
#metodos para independencia se vuelven independientes, si no se vuelven dependientes del diccionario principal.


# In[58]:


nuevo_diccionario


# In[61]:


my_data.pop('estatura') #eliminando un item primer metodo


# In[62]:


my_data


# In[65]:


del my_data ['lenguajes'] #segundo metodo para eliminar


# In[66]:


my_data


# In[67]:


my_data.clear() #Ultimo metodo para eliminar todos los items de un diccionario


# In[68]:


my_data


# In[ ]:





# # CONDICIONAL IF : Es usado para decidir que cierto codigo sea ejecutado o no
# en base a cierta condicion empieza con if seguido de una condicion
# <condition>:  y luego escibremos el codigo que es el que se cumplira o no
#  <code>:
# Lo mismo seria con elif -->este se ejecuta solo si uf es falsa
# elif <condition>:
#      <code>
#  ....
# else:
#       <code>       ---> bloque de ultimo camino, pues este es el ultimo en 
#           ejecutarse si todos los bloques dieron como condicion falso
#           y fallaron entonces else se activara.
#           
#           
# Ahi vamos :
# 

# In[69]:


edad = 18             #en este ejemplo haremos si la edad es mayor o igual
                      #a 18 diremos que es mayor que edad,si esto no se cumple
                      #diremos eres muy joven aun, pero aca pusimos 18 somos mayores
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres muy joven aun")


# In[71]:


edad = 12              #ahora agregaremos el elif donde nuestro codigo nos dice
                #si somos mayores a 13 pero menores que 18 somos seremos adolescentes menor a 13 niños mayor de 18 
                 #mayor de edad, y podemos cambiar el codigo de edad el primero y veremos

if edad>=18:
    print("Eres mayor de edad")
elif edad>=13:
    print("Eres un adolescente")
else:
    print("Eres un niño")


# In[ ]:


#vamos ahora a combinar nuestra condicional if con listas , usaremos
#la lista que estabamos usando hasta hace unos momentos con countries
# in es para decir en nuestro codigo quiere decir si china esta en la lista countires
#que imprima ese mensaje y si no esta imprimira lo de else


# In[13]:


countries


# In[ ]:





# In[ ]:





# In[73]:


if "china" in countries:
    print("pais esta en la lista")
else:
    print("no esta en la lista")


# In[ ]:





# # FOR LOOP (TAMBIEN CONOCIDO COMO BUCLE FOR) : nos permite iterar en cualquier objeto iterable y luego nos permite hacer la misma accion a cada objeto en la iteraccion ,traeremos unas listas con las que ya trabajamos para 
# hacerlo claro for <variable> in <list>:
#                   <code>
# basicamente tenemos que usar for luego in , ''variable'' es algo temporal no existe solo lo ponemos de ejemplo e iteraremos con alguna lista <list> basicamente iterar es una palabra de algo q tiene muchos elementos asi q traremos una lista hecha de ciudades etc ahi vamos...
# 

# In[1]:


for <variable> in <list>:
    <code>


# In[ ]:





# In[77]:


for pais in countries: #--> aca le estamos diciendo que por cada elemento que haya en countries
                          #imprima lo que contiene y lo imprima, ahora usaremos if
    print(pais)


# In[84]:


for pais in countries:
    if pais == "india":
        print(pais)


# In[85]:


for numero, pais in enumerate(countries_2): #--> enumerate te da 2 valores uno va para el numero y otro para el pais
                                             #por eso escribimos 2 variables uno para el numero y otro para el pais
                                            #nos sirve que num o iteraccion es nuestro elemento para eso usamos enumerate para grandes listas
    print(numero)
    print(pais)


# In[21]:


my_data = {'nombre,':'willy', 'edad':31}


# In[ ]:





# In[87]:


my_data


# In[88]:


my_data.items() #metodo items


# In[89]:


for key, value in my_data.items(): #esto sirve para imprimir llave+ valor de algun diccionario
    print(key)                     #y asi es como se hace una iteracion en un diccionaria.
    print(value)


# In[ ]:





# # FUNCIONES
# funciones pre-fabricadas : las funciones son un grupo de codigo el cual nos ayuda a resolver una tarea en especifica, Pero en Py tenemos muchas pre-fabricadas que usaremos a continuacion

# In[ ]:


#Esta funcion len nos va a decir el tamaño de un iterable (listas o diccionarios ejemplo)


# In[14]:


countries


# In[15]:


len(countries)


# In[16]:


#con la funcion max nos tirara el valor mas alto de la lista
max([16,83,32,1,10])


# In[17]:


#ahora usaremos algo que hace lo contrario que es min y nos dara el mas bajo
min([4,5,3,6,8,10])


# In[18]:


type(countries)


# In[22]:


type(my_data) #ver mas arriba para que vean porque dicen que es un diccionario


# In[23]:


round(2.333, 1) #Esto es para redondear un num y decirle con cuantos # lo queremos


# In[24]:


round(2.333,2) #en este le estamos pidiendo 2 decimales por ejemplo


# In[25]:


for i in range(1,10,2):  #le estamos diciendo que suba de 2 en 2 pero ya al llegar al 10 
    print(i)                        #excede y no suma mas


# In[ ]:





# # CREA TU PROPIA FUNCION

# In[ ]:


def function(<params>): #esta es la base del codigo, lo pondremos a practica
    <code>
    return <data>


# In[27]:


def sumar_numeros(a, b):
    suma_final = a + b
    return suma_final


# In[28]:


sumar_numeros(10, 5)


# In[ ]:





# # MODULOS
# para usar algunos modelos habia que usar el comando pip para instalarlo en python en este caso este modulo ya viene con python como muchos otros
# ahi vamos... a usar el modulo OS

# In[ ]:


import #para importar un modulo hay que usar este comando posterior el modulo


# In[ ]:





# # MODULO OS

# In[30]:


import os


# In[ ]:





# In[31]:


os.getcwd() #con este codigo me indica la ruta de mi
              #archivo de jupyter notebook


# In[32]:


os.listdir() #modulo para ver todos mis archivos dentro de mi carpeta


# In[35]:


os.makedirs("Nueva Carpeta") #este codigo es para crear una carpeta dentro de tu ordenador
#en la ubicacion de usuario que nos dio anteriormente


# In[36]:


os.listdir() #pueden ver el nuevo elemento Nueva Carpeta creada recien


# In[ ]:





# # INTRODUCCION A PANDAS
# aqui aprenderemos que es pandas y compararemos pandas con excel, que es un dataframe tambien, Pandas es una herramienta importante para hacer analisis de datos en py, hacer transformaciones, limpiezas y mas, puedes pensar pandas como un super excel pero con muchas otras funcionalidades.

# BENEFICIOS PANDAS VS EXCEL : TAMAÑO , PANDAS PUEDE MANEJAR MUCHAS MAS FILAS , TRANSFORMACION DE DATA COMPLEJA EN COMPARACION A EXCEL, OTRA VENTAJA DE PYTHON SOBRE EXCEL ES POR SU AUTOMATIZACION , EXCEL NO FUE CREADO PARA AUTOMATIZAR, COMPATIBILIDAD EN DIFERENTES PLATAFORMAS.
# para mas info escribeme : alexander22618@gmail.com

# In[ ]:





# CONCEPTOS BASICOS :
# 
# Arrays : es algo parecido a una lista , hay de 1Dimension o 2D, en panda son series y dataframe, Principalmente trabajaremos con Dataframe (df) en 2d, en pandas 1 data frame viene a ser una hoja de calculo en excel que tiene filas , aca empezamos con el numero 0 , la intersecciona entre una columna y una fila es conocida como un valor de dato o simplemente una data, podemos almacenar distintos tipos de data 
# texto , enteros y mas.

# In[ ]:





# TERMINOLOGIA EXCEL             vs                   PANDA
#     Worksheet                                     Dataframe
#     Columna                                       Series
#     Row Heading                                   Index
#     Row                                           Row
#     Empty Cell                                     Nan

# In[ ]:





# # COMO CREAR UN DATAFRAME
# con Arrays, veremos un codigo ej : Numpy Array 
#                                    np.array([[1,4],[2,5],[3,6]])
#                                    #esta es una forma de crearlo con la 
#                                    libreria Numpy
# Pero tambien hay otra forma :
# usando listas :
# 
# List Arrays
# data = [[1,4]],[2,5],[3,6]]
# 
# Y usando diccionarios :
# 
# my_dict = {'key1':value1,'key2':value2} #key vendria a ser columna name y value data (Series 1D array)
# 
# y la mas sencilla usando un archivo CSV. , probaremos estas 3 formas
#                                              

# In[ ]:





# # Creando un dataFrame usando arrays

# # Opcion 1 importaremos pandas y numpy
# escribimos el codigo y ejecutamos con run(nosotros lo crearemos con una variable ''data'' , pero le aumentaremos unos argumentos osea nombres a nuestra dataframe

# In[ ]:





# In[7]:


import pandas as pd
import numpy as np
import os


# In[38]:


data = np.array([[1,4],[2,5],[3,4]])


# In[39]:


pd.DataFrame(data)


# In[41]:


df = pd.DataFrame(data, index=['row1','row2','row3'],columns=['col1','col2'])


# In[42]:


df #usamos df ya que es el nombre standart de un dataframe para ponerme nombre a todo nuestra dataframe de arriba


# In[ ]:





# # Opcion 2

# In[ ]:


#creando un array en forma de lista
data = [[1,4],[2,5],[3,4]]


# In[ ]:


#creando un dataframe
df = pd.DataFrame(data, index=['row1','row2','row3'],columns=['col1','col2'])


# In[43]:


#mostrando el dataframe
df


# In[ ]:





# # Creando un dataframe usando diccionarios

# In[62]:


#Listas usadas para el ejemplo
states = ['California','Texas','Florida','New York']
population = [39613493, 29730311, 21944577, 1929981]


# In[63]:


#Almacenando listas en un diccionario
dict_states = {'states':states,'population': population}


# In[64]:


#creando el dataframe
df_population = pd.DataFrame(dict_states)


# In[65]:


#Mostrando el dataframe
df_population


# In[ ]:





# # Creando un dataframe con archivos csv
# en este caso el metodo sera distinto el codigo cambia es pd.read_csv('archivo.csv') #algo mas para que pueda leer el archivo el jupiter tiene que estar guardado el archivo csv no dentro de la carpeta jupyter sino dentro de la misma carpeta donde esta guardada ejemplo en la carpeta X tenemos jupyter, anaconda, musica , en esa misma carpeta raiz debe estar el archivo .csv asi evitan perdidas de tiempo.

# In[8]:


# leyendo el archivo csv
df_exams = pd.read_csv('StudentsPerformance.csv')


# In[ ]:





# In[ ]:





# In[9]:


df_exams


# In[ ]:





# In[ ]:





# In[84]:


#comando para mostrar primeras 5 filas del dataframe
df_exams.head()


# In[85]:


#Comando para mostrar las ultimas 5 filas del df
df_exams.tail()


# In[86]:


#mostrar ultimas n filas del dataframe
df_exams.head(15)


# In[87]:


df_exams.tail(13)


# In[91]:


#accediendo al atributo shape
df_exams.shape #este comando sirve para el numero de filas y columnas


# In[ ]:





# In[10]:


#mostrar "n" filas #con este comando indico todas las filas que quiero que me muestre
pd.set_option('display.max_rows', 1000)
df_exams


# In[ ]:





# In[ ]:





# In[ ]:





# # Atributos basicos, Funciones y Metodos de Pandas :

# ATRIBUTOS : UN ATRIBUTO ES UN VALOR ASOCIADO A UN OBJETO Y ESTA REFERENCIA POR NOMBRE USANDO EL PUNTO "." ej: df.columns 

# FUNCION : UN GRUPO DE SENTENCIAS QUE HACEN UNA TAREA ESPECIFICA ejemplo : max(), min(), len() , maximo , minimo y el tamaño de una lista

# METODOS : UNA FUNCION QUE ES DEFINIDA DENTRO DEL CUERPO DE UNA CLASE Ejemplo df.head() seguimos....

# In[ ]:





# In[11]:


df_exams


# In[ ]:





# In[ ]:





# In[93]:


#ATRIBUTOS-------------------------------------------------------------
df_exams.index #indica en que numero empieza y en
               #cual acaba,step 1 indica que los datos van en ascenso
               #de en 1 en 1 ej 1,2,3,4,5,..


# In[94]:


df_exams.shape #atributo que muestra fila y columnas


# In[95]:


df_exams.columns #atributo util para cambiar el nombre de las columnas


# In[96]:


df_exams.dtypes #atributo para ver el tipo de datos que tiene cada columna


# In[ ]:





# # Ahora miremos Metodos de Pandas :

# In[97]:


#mostrando las 5 primeras filas parecido a tail para mostrar las 5 ultimas
df_exams.head()


# In[98]:


#mostrando informacion de dataframe
df_exams.info() #nos sirve para ver si tenemos data nula en nuestra DF


# In[99]:


#obteniendo valores estadisticos del dataframe
df_exams.describe() # sale valor minimo de score maximo , etc , la cantidad
                     # de con quienes se hizo el examen etc


# In[ ]:





# # Funciones
# 

# In[100]:


#obtener el tamaño del dataframe (filas)
len(df_exams)


# In[102]:


#obtener el maximo index
max(df_exams.index)


# In[103]:


#obtener el minimo index
min(df_exams.index)


# In[104]:


#obtener el tipo de dato
type(df_exams)


# In[105]:


#redondear valores del dataframe
round(df_exams, 2) #sirve para redondear los valores del dataframe
                   #no tiene ningun efecto pues tiene numeros enteros
                   #esto tendra mas efecto si su df tiene valores decimales
                   #asi los va a redondear.


# In[ ]:





# # Seleccionar una columna de un dataframe 

# # SYNTAX 1 lo que haremos es importar pandas y cargar el data frame o archivo csv dentro del dataframe, muy bien por las dudas ya corrimos el panda y el archivo de nuevo ahora a trabajar...

# In[25]:


df_exams.head()


# In[26]:


#seleccionar una columna con [] (forma preferida de seleccionar una columna)
df_exams['gender']


# In[27]:


#revisar el tipo de data de una columna
type(df_exams['gender'])


# In[28]:


#series : atributos y metodos
df_exams['gender'].index


# In[29]:


df_exams['gender'].head() #codigo para ver las primeras las 1eras 5 filas de una serie en este caso 
#estamos viendo de gender, anteriormente vimos algo parecido pero no habiamos especificado
#alguna serie como en este caso seleccionar gender.


# In[30]:


#seleccionar una columna con .
df_exams.gender #este metodo es sencillo pero tiene algunas debilidades, si quiero obtener una columna la de arriba que tiene 2 palabras
#miren lo que pasaria mas abajo


# In[31]:


df_exams.math score #python nos da error y esta es una de las debilidades de este codigo en panda
#python no entiende las palabras separadas tendria que ser en todo caso
#math_score , pero no es el caso


# In[32]:


#seleccionar la misma columna con []
df_exams['math score'] #sin embargo ahora con los corchetes y las comillas por mas que esten separados
#ahora python si reconoce porque sabe que es una cadena de texto y no le interesa
#que esten separados, pero esta es la forma correcta.


# In[33]:


df_exams.head()


# SELECCIONAR DOS O MAS COLUMNAS

# In[34]:


#seleccionar 2 columnas usando [[]]
df_exams[['gender','math score']] #como ve asi solo hemos elegido las 2 columnas seleccionadas
#pero las filas siguen intactas


# In[35]:


type(df_exams[['gender','math score']]) #traten de mirar los datos asi memorizan en pandas
#para cuando tenga que trabajar en pandas


# In[37]:


#seleccionar 2 o mas columnas usando [[]] por cierto la posicion en que hacen esto debe ser en el orden del dataframe
#por ejemplo si queremos que escritura este primero entonces lo podemos poner en el 2do por ejemplo
(df_exams[['gender','writing score','math score','reading score']])


# In[ ]:


#Cierto no podemos seleccionar 2 o mas columnas usando el "."
df_exams.'gender', 'math score' <--- codigo invalido


# In[ ]:





# # Como agregar nueva columna a nuestro DataFrame... ahi les enseñaremos varias formas

# In[12]:


#agregar una nueva columna al dataframe
df_exams['language score'] = 70 #ya esta el codigo df_Exams['lenguage score'] pero si lo ejecuto obvio no vere nada ya que esta columna
#no existe, entonces ahora tenemos que asignarle un valor, ahora veran el codigo completo


# In[ ]:


#HASTA AHORA TODO PERFECTO SOLO HAY UN PROBLEMA QUE EN LA NUEVA COLUMNA DE LENGUAGE SCORE... ES IMPOSIBLE QUE TODOS LOS ALUMNOS 
#SAQUEN LA MISMA NOTA... ENTONCES COMO HAREMOS PARA ARREGLAR DE PASO SIMULAMOS UN POCO COMO SE TRABAJARIA...
#BUENO USAREMOS ARRAY Y PARA USAR ARRAY O CREAR DEBERMOS USAR NUMPY... ASI QUE PASAREMOS A IMPORTAR Y A TRABAJAR.


# In[13]:


#importar numpy
import numpy as np


# In[3]:


#crear un array de 1000 elementos (usando metodo arange) y le agregaremos variable para no escribir todo el codigo a cada rato
np.arange(0,1000)


# In[14]:


language_score = np.arange(0,1000)


# In[15]:


#tamaño del array
len(language_score)


# In[16]:


#agregar una nueva columa al dataframe con un array :
#con este metodo estamos sobreescribiendo los valores que ya estan en la columna de language score, pues ya la habiamos creado esta columna
#si hubieramos empezamos con este metodo estariamos creando esta columna
df_exams['language score'] = language_score
df_exams


# In[17]:


#crear numeros enteros aleatorios entre 1 y 100
np.random.randint(1,100,size=1000) #comando para asignar numeros randoms
#en este caso estamos pidiendo que cree 1000 notas con valores del 1 al 100
#para poder simular en nuestra nueva columna de language


# In[19]:


int_language_score = np.random.randint(1,100,size=1000) #creando la lista para no reescribir todo el codigo
#pero decidi ponerle el int y no lenguage por las dudas para no tener errores


# In[20]:


#el minimo valor es inclusivo y el maximo valor es exclusivo
min(int_language_score)
max(int_language_score)


# In[22]:


#agregar una nueva columna al dataframe con un array
df_exams['language score'] = int_language_score
df_exams #y a ejecutar y observemos.... ya tenemos valores mas 
#razonables PD : Termine creando una columna extra aleatoria.... con los
#tutoriales de arriba ya saben como pueden eliminarla se la dejo de ejercicio
#solo queria sobreescribir y bueno cosas que nos pasan a los humanos
#pero ahi se los dejo para que corrijan que asi aprenderan mas


# In[23]:


#crear numeros decimales aleatorios entre y 100
np.random.uniform(1,100,size=1000)


# In[ ]:





# # Operaciones en Dataframes
# operaciones como suma resta operacion division etc podemos hacer en los dataframes utilizando varios metodos, a continuacion paso a explicarle algunos

# OPERACIONES EN COLUMNAS

# In[24]:


#selecciona una columna y calcula la suma total
df_exams['math score'].sum()


# In[25]:


#contar,promedio, desv. estandar, maximo y minimo
df_exams['math score'].count()


# In[26]:


#suma del promedio
df_exams['math score'].mean()


# In[27]:


#division estandart
df_exams['math score'].std()


# In[28]:


#obteniendo el score minimo
df_exams['math score'].min()


# In[29]:


#obteniendo el score maximo
df_exams['math score'].max()


# In[30]:


#calcula mas rapido con .describe()
df_exams.describe()


# COMO PUDIERON VER CON LA OTRA FORMULA NO FUE NECESARIO YA ESCRIBIR VARIAS CON ESA NOS SACO EL PROMEDIO , ESTANDAR , MINIMO , MAXIMO ETC, ES MUY PRACTICO ESTE ULTIMO METODO.

# In[ ]:





# OERACIONES EN FILAS-------------------------------------

# In[31]:


#calcular la suma en una fila 
df_exams['math score'] + df_exams['reading score'] + df_exams['writing score']


# In[32]:


#calcular el score promedio y asignar los resultados a una
#nueva columna, solo tocara agregarle cerrar todo en parentesis y dividirlo entre 3 como muestra el codigo para dividir
(df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])/3


# In[33]:


#muy bien pasaremos todo colocarlo a una nueva columna llamada average que significa promedio para mostrarles el dataframe
df_exams['average'] = (df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])/3


# In[34]:


#mostrar el dataframe
df_exams


# In[ ]:


#bueno y aca esta el promedio de todos estos examenes sumados y divididos entre 3


# In[35]:


#haremos algo extra, es redondear todo el dataframe usando el comando round
df_exams.round(2) #dos es el numero de decimales que queremos


# 

# # Metodo Value Counts
# para ver mas a detalle algunas cosas como cuales son los promedios femeninos o masculinos etc

# In[36]:


#contar los elementos en la columna "gender"

#funcion len
len(df_exams['gender'])
#metodo .count()
df_exams['gender'].count()


# In[37]:


#contar elementos "gender" por categoria
df_exams['gender'].value_counts() #este codigo serviria por ejemplo
#te dan una lista con miles de personas hombre y mujer y asi sacarias facilmente
#cuanto % de hombre y mujeres tienes en esa lista y cosas asi


# In[38]:


#ahora queremos calcular el porcentaje mas que el numero entonces usaremos el mismo codigo
#pero agregando un pequeño argeumento
df_exams['gender'].value_counts(normalize=True)


# In[ ]:


# Y ASI VEMOS QUE HOMBRES SON 48% Y MUJERES 51% casi 52%


# In[39]:


#contar elementos de la columna ''parental level of education por categoria''
df_exams['parental level of education'].value_counts()


# In[42]:


#obtener la frecuencia relativa y redondear a 2 decimales
df_exams['parental level of education'].value_counts(normalize=True).round(2)


# In[ ]:





# # Ordenar un dataframe
# 

# In[43]:


df_exams


# In[44]:


#ordenar por una columna
df_exams.sort_values('math score')


# In[45]:


#orden descendiente por una columna
df_exams.sort_values('math score',ascending=False)


# In[46]:


#orden descendiente por multiples columnas
df_exams.sort_values(['math score','reading score'] , ascending=False)


# In[47]:


df_exams


# COMO PUEDEN VER HASTA AHORA EN EL DATAFRAMA ORIGINAL TODO SIGUE IGUAL... ESO QUIERE DECIR QUE EL METODO SORT VALUE NO NOS MODIFICO NADA, PARA QUE REALMENTE NOS MODIFIQUE EL DATAFRAMA ORIGINAL SE USA OTRO METODO COMO EL ''INPLACE=TRUE Y EN BREVE Y POCO MAS YA LO VEREMOS

# In[48]:


#orden descendiente por multiples columnas y actualizar dataframa
df_exams.sort_values(['math score','reading score'] , ascending=False, inplace=True)


# In[49]:


df_exams


# In[52]:


#orden descendiente con una funcion key en este caso usando la funciona lambda y nombrando col(que significa columna y diciendo que queremos que haga)
#le estamos diciendo con este codigo ordena esta columna pero antes estandariza todos los valores, ponlos en minusculas y ahi podremos compararlos y ordenarlos correctamente. 
df_exams.sort_values('race/ethnicity', ascending=True,key=lambda col:col.str.lower())


# 

# # Revision al DataSet

# # La Data

# In[6]:


import pandas as pd


# In[9]:


df_boston


# In[8]:


df_boston = pd.read_csv('Boston House Prices.csv')


# In[6]:


df_boston.describe()


# In[22]:


pip install matplot


# ## Regresion lineal con Statsmodels

# In[4]:


import statsmodels.api as sm


# In[ ]:


## 1.1 Regresion Lineal Simple


# ## 1.1.1 Definir las variables dependientes e independientes

# In[18]:


y = df_boston ['Value']
x = df_boston ['Rooms']


# ## 1.1.2 Explorar el dataset

# In[23]:


df_boston.plot(kind='scatter',
               x='Rooms',
               y='Value')


# In[ ]:





# ## 1.1.3 Crear la regresion : agregar constante y ajustar modelo

# In[12]:


x = sm.add_constant(x) #usando el metodo OLS y sm.add y modelo fit
lm = sm.OLS(y,x).fit() #ajustar el modelo


# In[13]:


lm.predict(x)


# ## 1.1.4 La Tabla de Regresion

# In[27]:


lm.summary()


# ## 1.1.5 Ecuacion de la regresion Lineal 

# In[28]:


#Coef Rooms : 9.1012
#Coef Constant: 34.6706

#Ecuacion lineal : y = ax + b
y_pred = 9.1021*x['Rooms'] - 34.6706


# ## 1.1.6 Graficar la regresion lineal

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


#graficar los puntos
plt.figure(figsize=(6, 4), tight_layout=True)
sns.scatterplot(x=x['Rooms'], y=y)
           
#graficar la linea
sns.lineplot(x=x['Rooms'],y=y_pred, color= 'red')

#axis
plt.xlim(0)
plt.ylim(0)
plt.savefig('linear_regression')
plt.show()


# # 1 Regresion Lineal con Scikit-Learn

# In[1]:


from sklearn import linear_model


# ## 1.1 Definir las variables dependientes e independientes

# In[10]:


y = df_boston['Value']
x = df_boston[['Rooms', 'Distance']]


# # 1.2 Ajustar el modelo

# In[15]:


lm = linear_model.LinearRegression()
lm.fit(x, y)


# ## 1.3 Predecir Valores

# In[18]:


lm.predict(x)[:5]


# In[19]:


# r2 score
lm.score(x,y)


# In[20]:


# coeficiente 
lm.coef_


# In[21]:


#intercepto
lm.intercept_


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 
