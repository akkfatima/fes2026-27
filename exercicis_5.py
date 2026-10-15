###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom_tecnic = input("Introdueix el nom del tècnic: ")
nom_xarxa = input("Introdueix el nom de la xarxa: ")
print(f"El nom del tècnic és {nom_tecnic} i està instal·lant la xarxa {nom_xarxa}.")




# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud_enllaç, velocitat_transmissio = input("Introdueix la longitud de l'enllaç de fibra en quilòmetres i la velocitat de transmissió en Gbps\n").split()
longitud_enllaç = float(longitud_enllaç)
velocitat_transmissio = float(velocitat_transmissio)

segons = 8/velocitat_transmissio
print(f"Per transmetre 1 GB de dades, caldrien {segons} segons.")





# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores_de_feina, preu_per_hora, preu_material = input("Introdueix el nombre d'hores de feina, el preu per hora i el preu del material\n").split()
hores_de_feina = float(hores_de_feina)
preu_per_hora = float(preu_per_hora)
preu_material = float(preu_material)

cost_total = hores_de_feina * preu_per_hora + preu_material
print(f"El cost total de la instal·lació és de {cost_total} euros.")