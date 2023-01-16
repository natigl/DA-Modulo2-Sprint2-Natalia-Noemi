import pandas as pd
import numpy as np
import mysql.connector



class Cargar:
    
    def __init__(self, nombre_bbdd, brocoli):
       
        self.nombre_bbdd = nombre_bbdd
        self.brocoli = brocoli

   
    def crear_bbdd(self):

        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password=self.brocoli) 
        mycursor = mydb.cursor()
        print("Conexión realizada con éxito")

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nombre_bbdd};")
            
        except:
            print("La BBDD ya existe")
            
      
    def insertar_tabla_crear(self, query):
        
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       password=f'{self.brocoli}', 
                                       database=f"{self.nombre_bbdd}") 
        mycursor = mydb.cursor()
        
        try:
            mycursor.execute(query)
            mydb.commit()
          
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)                   