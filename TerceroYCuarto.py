# ● A tu entender, que se busca obtener como output del script?


# import me.*;
# def upsPullTrkService = ctx.getBean('upsPullTrkService')
# def s = Shipment.get(27528954729)
# def tn = s.trackingNumber
# def trackingData = upsPullTrkService.getTrkEvents([tn])
# trackingData.each { td ->
# println "------------------------------------------------"
# println "${td.sucursal} - ${td.eventDate} - ${td.description}"
# }
# "Done"
#
#
# Con este scrpit se obtienen los atributos td.sucursal , td.eventDate y td.description
# de todas las instancias de la clase upsPullTrkService que se encuentren en la pagina
#

# Script básico bash
# ● A tu entender, que se busca obtener como output del script?
# ● Podrías detallar que se hace en cada línea del script?
# ● Cuántas líneas se imprimen como output?
#
#
# #!/bin/bash
#
# #Lista de usuarios
# users_id=(71665538 66146765 132961968 15096445 172753273 54152646)
#
# #Se itinera por esta lista
# for users_id in ${users_id[*]}
# do
# 
# # Se solicita la informacion que esta en la url  ... user_id/shipping_preferences
# #y se espera como respuesta un Json
# curl=$(curl -s " api.mercadolibre.com/users/$users_id/shipping_preferences " | jq -c
# '.services')
# echo "$users_id: $curl"
# done
#
#
# # Con el script se busca obtener ciertos datos en forma de Json de los usuarios que estan en la lista de users_id
# Se imprimira un Json por cada usuario que este en la lista
# si el Json fuera de una linea, en este caso, se imprimirian 6 lineas en el outpur
#
