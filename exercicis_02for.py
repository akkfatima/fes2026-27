###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.


for i in range(2, 21):
    if i % 2 == 0:
        print(i)

print()
print("--------------------------------------------------------")
   
# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.

numeros = [10, 20, 30, 40, 50]
mitjana = 0 
for i in numeros:
    mitjana += i
mitjana /= len(numeros)

print(f"La mitjana dels números és: {mitjana}")

print()
print("--------------------------------------------------------")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.

numeros = [15, 5, 25, 10, 20]
max = numeros[0]
for i in numeros:
    if i > max:
        max = i
print(f"El número més gran de la llista és : {max}")

print()
print("--------------------------------------------------------")


# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.

paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
paraules_nova_llista = []
for i in paraules: 
    if len(i) > 5:
        paraules_nova_llista.append(i)

print(f"La nova llista és: {paraules_nova_llista}")

print()
print("--------------------------------------------------------")


# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).

paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("Introdueix una lletra : ")
comptador = 0
for i in paraules:
    if i.lower().startswith(lletra.lower()):
        comptador += 1
print(f"El nombre de paraules que comencen per la lletra '{lletra}' és: {comptador}")



print()
print("--------------------------------------------------------")
# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.

tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
mitja = 0
for i in tensions:
    mitja += i
mitja /= len(tensions)
print(f"La tensió mitjana és de : {mitja:.3f} volts")


print()
print("--------------------------------------------------------")
# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.

resistencies = [100, 220, 470, 1000]
for i in resistencies:
    corrent = 12 / i
    print(f"El corrent en aquesta resistencia {i}ohms és de : {corrent}") 



print()
print("--------------------------------------------------------")
# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.

nivells_soroll = [-92, -85, -78, -95, -81, -88]
comptador = 0
for i in nivells_soroll:
    if i > -80:
        comptador += 1

print(f"El nombre de mostres que superen el llindar és: {comptador}")



print()
print("--------------------------------------------------------")
# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).

bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
comptador = 0
for i in bits_transmesos:
    for j in bits_rebuts:
        if i != j:
            comptador += 1
taxa_error = comptador / len(bits_transmesos)
print(f"La taxa d'error és: {taxa_error:.2f}")


print()
print("--------------------------------------------------------")
# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.

frequencies = [50, 100, 500, 1000] 
for i in frequencies:
    periode = 1 / i
    print(f"La freqüència {i}Hz, el seu període és de {periode}s ")
    