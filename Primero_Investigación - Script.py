# 1ra parte
# Ejercicio - Investigación / Script


# #1. Recorrer todos los ítems publicados por el seller_id = 179571326 del
# site_id = "MLA"
# 2. Generar un archivo de LOG que contenga los siguientes datos de
# cada ítem:
# a. " id " del ítem, " title " del item, " category_id " donde está
# publicado, " name " de la categoría.


# Creo la conexion a la base de datos

import pymysql


class DataBase:

    def __init__(self):
        self.connection = pymysql.connect(

            # Yo utilize los parametros para conectarme a mi basede datos local de phpmyadmin
            host="localhost",
            user="root",
            password="",
            db="comercio"

        )
        self.cursor = self.connection.cursor()

        print('Conectado con exito')

    # Cierra la conexion
    def close(self):
        self.connection.close()

    def get_items_by_seller_id_in_MLA(self, seller_id):

        # seller_id es un String con 1 o mas vendedores
        # la convierto en una lista

        list_seller = seller_id.split()

        # Preparo la condicion WHERE para la consulta SQL
        condicion_query = ""
        for x in range(len(list_seller)):
            if x == 0:
                condicion_query += "seller_id = " + list_seller[x] + "\n"
            else:
                condicion_query += "OR seller_id = " + list_seller[x] + "\n"

        nombre_tabla = "items table"
        sql = "SELECT id, title, category_id, name " \
              "FROM " + nombre_tabla + \
              "WHERE " + condicion_query

        # realizo la consulta

        try:

            self.cursor.execute(sql)

            items = self.cursor.fetchall()

        except Exception as e:
            raise

        # Con los datos de la consulta ordeno el contenido del  .LOG

        log = ""

        for item in items:
            log += "id: " + item[0] + "\n" + \
                   "Title: " + item[1] + "\n" + \
                   "Category_id: " + item[2] + "\n" + \
                   "name : " + item[3] + "\n" + \
                   "----------------------------"

        # Creo el archivo LOG

        file = open("C:/users/Desktop/consulta.txt", "w") #la ruta depende de la PC
        file.write(".LOG \n")

        file.write(log)

#para conseguir los items publicados del seller_id = 179571326

database = DataBase()
database.get_items_by_seller_id_in_MLA(179571326)

# la funcion funciona con 1 o varios sellers_id
database.close()