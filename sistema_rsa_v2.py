from __future__ import print_function
import mysql.connector
import sys
import matplotlib.pyplot as plt
import networkx as nx
import os


def generar_grafo_pregunta1():
    #Genera los grafos a partir de los datos de la tabla mysql
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    cursor.execute("select id_alumnos, substring_index(substring_index(pregunta1, ',', n),  ',',   -1) as resultados from relaciones join numbers on char_length(pregunta1)  - char_length(replace(pregunta1, ',', '')) >= n - 1 ")       
    data = cursor.fetchall()
    g = nx.Graph()
    
 
    #crea el grafo segun mysql
    
    for row in data:
        g.add_edge(row[0],row[1])
        
     
       
     
        

    nx.draw_spring(g,with_labels=True)
    plt.draw()
    plt.show()
    cnx.commit()
     #Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
    
def generar_grafo_pregunta2():
    #Genera los grafos a partir de los datos de la tabla mysql
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    cursor.execute("select id_alumnos, substring_index(substring_index(pregunta2, ',', n),  ',',   -1) as resultados from relaciones join numbers on char_length(pregunta2)  - char_length(replace(pregunta2, ',', '')) >= n - 1 ")       
    data = cursor.fetchall()
    g = nx.DiGraph()
 
        
    #crea el grafo segun mysql
    
    for row in data:
        g.add_edge(row[0],row[1])
     
       
     

    nx.draw(g,with_labels=True)
    plt.draw()
    plt.show()
    cnx.commit()
     #Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
    
def generar_grafo_pregunta3():
    #Genera los grafos a partir de los datos de la tabla mysql
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    cursor.execute("select id_alumnos, substring_index(substring_index(pregunta3, ',', n),  ',',   -1) as resultados from relaciones join numbers on char_length(pregunta3)  - char_length(replace(pregunta3, ',', '')) >= n - 1 ")       
    data = cursor.fetchall()
    g = nx.DiGraph()
 
        
    #crea el grafo segun mysql
    
    for row in data:
        g.add_edge(row[0],row[1])
     
       
     

    nx.draw(g,with_labels=True)
    plt.draw()
    plt.show()
    cnx.commit()
     #Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
    
def generar_grafo_pregunta4():
    #Genera los grafos a partir de los datos de la tabla mysql
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    cursor.execute("select id_alumnos, substring_index(substring_index(pregunta4, ',', n),  ',',   -1) as resultados from relaciones join numbers on char_length(pregunta4)  - char_length(replace(pregunta4, ',', '')) >= n - 1 ")       
    data = cursor.fetchall()
    g = nx.DiGraph()
 
        
    #crea el grafo segun mysql
    
    for row in data:
        g.add_edge(row[0],row[1])
     
       
     

    nx.draw(g,with_labels=True)
    plt.draw()
    plt.show()
    cnx.commit()
     #Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
    
    
    
def estadisticas_alumno():
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    print('\n')
    print('** Estadisticas por Alumno **')
    a = input('Ingresa el ID del alumno a buscar: ')
    id_alumno = int(a)
    
    #Realiza el query de la busqueda del alumno solicitado

    cursor.execute("SELECT * FROM centralidades_alumno "
           "WHERE id_alumnos = %d" %id_alumno)
   
    data = cursor.fetchall()
    for row in data:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        
    
    
                   
    cnx.commit()
#Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
             
   
def estadisticas_grupo():
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
    print('\n')
    print('** Estadisticas por Alumno **')
    idgrupo = input ('Ingresa el id del grupo a buscar: ')
    a = int(idgrupo)
    #Realiza el query de la busqueda del alumno solicitado
    query = ("SELECT * FROM centralidades_grupo "
            "WHERE id_grupo = %d" %a)
    cursor.execute(query)
   
    data = cursor.fetchall()
    for row in data:
        print(row[0],row[1],row[2],row[3])
        
    
    
                   
    cnx.commit()
#Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
             
   
                  
    
 
   

        
def ingresar_amistades():
    # Conexion de la base de datos
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
# La siguiente variable es para mantener el ciclo while
    choice = 'Y'
# Mientras no se ingrese N, el programa seguira pidiendo datos
    while (choice != 'N'):  #corregir que tambien detecte N minuscula
# El maestro ingresa los datos de las relaciones

        no_lista = input('Ingresa el número de lista del alumno ')
        p1 = input('Ingresa la respuesta de pregunta 1: ')
        p2 = input('Ingresa la prespuesta de la pregunta 2: ')
        p3 = input('Ingresa la prespuesta de la pregunta 3: ')
        p4 = input('Ingresa la prespuesta de la pregunta 4: ')
        choice = input('Quieres ingresar otra vez datos S/N')
      
      
        
        

# Query para agregar datos a la tabla

    add_relaciones = ("INSERT INTO relaciones (id_alumnos, pregunta1, pregunta2, pregunta3, pregunta4)"
         
                    "VALUES (%s, %s, %s, %s, %s)")




    data_relacion = (no_lista, p1, p2, p3, p4 )

# Insert new employee



#Agrega los datos a la tabla
    cursor.execute(add_relaciones, data_relacion)
  



# Se asegura que los datos se agregaron a la tabla
    cnx.commit()
#Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()


def registro_grupo():
    # Conexion de la base de datos
    cnx = mysql.connector.connect(user='root', password='manzanillo20', database='sistema_rsa')
    cursor = cnx.cursor()
# La siguiente variable es para mantener el ciclo while
    choice = 'Y'
# Mientras no se ingrese N, el programa seguira pidiendo datos
    while (choice != 'N'):  #corregir que tambien detecte N minuscula
# El maestro ingresa los datos de las relaciones
        os.system("say Ingresa el nombre del alumno")
        nombre = input('Ingresa el nombre del alumno: ')
        os.system("say Ingresa el apellido paterno")
        apellido_p = input('Ingresa el apellido_paterno: ')
        os.system("say Ingresa el apellido materno")
        apellido_m = input('Ingresa el apellido materno: ')
        os.system("say Ingresa el ID del grupo: ")
        id_grupo =  input('Ingresa el ID del grupo: ')
        voz = '¿Quieres ingresar datos otra vez?'
        os.system("say %s" %voz)
        choice = input('Quieres ingresar otra vez datos S/N')
      
        if (choice == 'N'):
            despedida = 'Nos vemos luego'
            os.system("say %s" %despedida)
        
        

# Query para agregar datos a la tabla

    add_registro = ("INSERT INTO alumnos (nombre, apellido_p, apellido_m,id_grupo)"
         
                    "VALUES (%s, %s, %s)")




    data_registro = (nombre, apellido_p, apellido_m, id_grupo)

# Insert new employee



#Agrega los datos a la tabla
    cursor.execute(add_registro, data_registro)
  



# Se asegura que los datos se agregaron a la tabla
    cnx.commit()
#Se cierra la conexion de la base de datos
    cursor.close()
    cnx.close()
    #Menu de opciones 
def main():
 # os.system("say bienvenido al sistema de redes sociales en el aula version 1.0")
 # os.system("say selecciona una opcion del menu")
  print('\n\n')  
  print('***** SISTEMA RSA V 1.0 ******** \n \n')
  print('[1] Ingresar amistades de alumnos\n')
  print('[2] Ver análisis y estadisticas del grupo\n')
  print('[3] Ver análisis y estadísticas por alumno\n')
  print('[4] Subir datos a la nube\n')
  print('[5] Registrar grupo\n')
  print('[6] Generar grafo de la Pregunta 1\n')
  print('[7] Generar grafo de la Pregunta 2\n')
  print('[8] Generar grafo de la Pregunta 3\n')
  print('[9] Generar grafo de la Pregunta 4\n')
  print('[10] S A L I R\n')
  op = input("ELIGE UNA OPCION: ")
  if (op == '1'):
      ingresar_amistades()
  if (op == '2'):
      estadisticas_grupo()
  if (op == '3'):
      estadisticas_alumno()
  if (op == '5'):
     registro_grupo()
  if (op == '6'):
      generar_grafo_pregunta1()
  if (op == '7'):
      generar_grafo_pregunta2()
  if (op == '8'):
      generar_grafo_pregunta3()
  if (op == '9'):
      generar_grafo_pregunta4()
  if (op == '10'):
      exit
  if (op == '11'):
      temp()

     

    
main()