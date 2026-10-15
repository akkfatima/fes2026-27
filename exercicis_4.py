###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom_encaminador = "RouterF"
ubicacio_encaminador = "Edifici Q"
nombre_de_ports = 9
esta_ences = False 
print(f"L'encaminador {nom_encaminador} està ubicat a {ubicacio_encaminador} i té {nombre_de_ports} ports. Està encès? {esta_ences}.")



# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

gb_inclosos_en_un_pla_de_dades_mobils = 50
gb_consumits = 20 

gb_restants = gb_inclosos_en_un_pla_de_dades_mobils - gb_consumits
print(f"Queden {gb_restants} GB del pla de dades mòbils.")

gb_consumits = 35
gb_restants = gb_inclosos_en_un_pla_de_dades_mobils - gb_consumits
print(f"Actualitzant el consum, queden {gb_restants} GB del pla de dades mòbils.")