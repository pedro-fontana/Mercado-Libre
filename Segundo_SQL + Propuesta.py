#Asumo que la  Carrier capacity es la maxima cantidad de envios que puede hacer un carrier en un solo viaje

#Primero Creo las clases Zona y Carrier

class Carrier:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity


class Zona:
    def __init__(self, nombre, cantidad_envios):
        self.nombre = nombre
        self.cantidad_envios = cantidad_envios


#Creo la conexion, podria haberla importada del ejercicio anterior, pero para estos ejercicios
#que no son muy engorrosos prefiero escribir la funcion que necesito aca

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


    def close(self):
        self.connection.close()


    #Busca todas los Carries que hay en la tabla Carrier
    def get_carriers(self):

        sql = "SELECT CarrierID, Name, Capacity FROM Carrier "
        try:

            self.cursor.execute(sql)

            carriers = self.cursor.fetchall()

        except Exception as e:
            raise


        return carriers
        #En la variable query  se guardo la consulta con todos los Carriers


        #Creo una lista de objetos Carrier
        carriers = []
        for carrier in query:
            carriers.append( Carrier(carrier[0], (carrier[1], (carrier[2]) )

    # Busca todas las zonas y su respectiva cantidad de envios  que hay en la tabla cantidad de envios

    def get_zonas(self):
        mes = 1
        sql = "SELECT Zona, Cantidad de envios FROM Cantidad de envios WHERE mes = " + mes


        try:

            self.cursor.execute(sql)

            zonas = self.cursor.fetchall()

        except Exception as e:
            raise

        return  zonas

    def get_costo_de_envio(self,carrier_id,zona_nombre):
        sql = "SELECT Costo, Tiempo de entrega FROM Costos " \
              "WHERE CarrierID = "  + str(carrier_id) +  \
               "AND Zona = " + zona_nombre

        try:

            self.cursor.execute(sql)

            costo = self.cursor.fetchone()

        except Exception as e:
            raise

        #Devuelve una tupla (costo de envio, Tiempo de entrega)
        return costo





# Defino una funcion para saber cuanto costaria enviar los envios de Cantidad de envios por cada carrier


def solve():
    database = DataBase()

    lista_carriers = database.get_carriers()
    lista_zonas = database.get_zonas()



    # Creo una lista de objetos Carrier
    carriers = []
    for carrier in lista_carriers:
                        #           ID    ,  Name    ,  Capacity
        carriers.append(Carrier(carrier[0], carrier[1], carrier[2]) )

        # Creo una lista de objetos Carrier
    zonas = []
    for zona in lista_zonas:
                        #nombre  ,cantidad de envios
        zonas.append( Zona(zona[0], zona[1]))


    # Calculo cuanto cuesta realizar todos los envios con cada carrier

    for carrier in carriers:

        #el Costo total es el coste de cada carrier para cubrir las 3 zonas (AMBA, Bs As y Resto)
        costo_total = 0
        #hago lo mismo para los dias
        dias_total = 0
        for zona in zonas:

            costo_de_envio , tiempo_de_entrega = database.get_costo_de_envio(carrier.id,zona.nombre)


            #para saber cuanto me cuesta cubrir la zona que se esta evaluando,
            # multiplico la cantidad de envios por el costo del envio del carrier

            costo_por_zona = zona.cantidad_envios * costo_de_envio

            #Para saber los dias que necesito para completar las entregas de la zona
            # multiplico la cantidad de viajes que tiene que hacer el carrier por el tiempo
            #que tarda el carrier en hacer el viaje

            #calculo la cantidad de viajes
            if zona.cantidad_envios % carrier.capacity == 0:
                cant_de_viajes = zona.cantidad_envios // carrier.capacity
            else:
                cant_de_viajes = (zona.cantidad_envios // carrier.capacity) + 1

            dias_para_cubrir_la_zona = cant_de_viajes * tiempo_de_entrega

            #ahora que ya tengo el costo y los dias que necesito para cubrir una zona las imprimo

            print( "Para cubrir la " + zona.nombre + "necesito" + dias_para_cubrir_la_zona )
            print( "Y tiene un costo de : " + costo_por_zona)
            costo_total += costo_por_zona
            dias_total += dias_para_cubrir_la_zona


        # ahora que recorri las 3 zonas informo lo que tarda y el coste del carrier que estoy evaluanto

        print("el Carrier " + carrier.name + "tarda " + dias_total + " en completar todas las entregas del mes ")
        print("Lo hace con un coste de " + costo_total)


#Nota: el programa me parece que funcionaria bien, tengo un problema con el ultimo carrier que solo hace envios al AMBA
# y no al resto de las zonas, creo que el programa seguiria funcionando pero habria que cubrir esos errores de otra manera



# ● ¿Que propuesta harías para el mes 1 considerando un presupuesto de
#     $3.000.000?

# Con ese presupuesto alcanza para cubrir las zonas de Bs As  (< $1.000.000 )  y Amba  ( < $800.000)
# En cuanto al resto tiene un costo minimo de $3.000.000 y tardarias 42 dias en completar todos los envios
# con lo cual te quedarian envios demorados en el mes
# Lo que yo haria en esta situacion seria consultar la gente correspondiente informandoles como son las condiciones
# y las posibles variaciones en el costo y los tiempos de entrega ya que con un presupuesto de
# $3.000.000 no alcanza para realizar todos los envios solicitados



● ¿Qué queries realizaste?

#Primero consulte las tablas de Carrier y Cantidad de envios para poder armar los objetos respectivamente
# y luego hice otras para consultar el costo de envio del carrier a la zona que estoy envaluenado