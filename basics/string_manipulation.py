# # String manipulation

# # With "" is more easy manipulate strings than with '' cause of apostrophe -> "I'm Adam"
# # IMPORTANT!!!  name != NAME lets check it.
# # remember we declared name ="Jhon Doe"
# # and now... 

# NAME = "ADAM" # Variables are case sensitive that's why isnt the same value NAME as name
# #print(name)
# print(NAME)

# # Multiline

# multiLine="""
# Use the wireless SCSI system, then you can compress the wireless feed!
# bypassing the circuit won't do anything, we need to synthesize the cross-platform SCSI card!
# neural
# """

# # Concat string examples

# firstString = "auxiliary"
# secondString = "synthesizing"
# thirdString = firstString + ", SAS"

# print(firstString + ' ' + secondString)
# print(thirdString)

# # join() method for tuples, lists, dictionarys

# solfeo = ['do', 're', 'mi']
# separator = ' - '
# print(separator.join(solfeo))

# # str.format() In my opinion, more efficient

# months = "First three months of the year are {},{},{}".format('January','February', 'March')
# print(months)

# # we can change the position

# months = "Months of the year are {2},{0},{1}".format('January','February', 'March')
# print(months) # March - January - February

# # format string 'f' 

# numberTelephone = 855123452
# userTelephone = "Buford"
# print(f"User: {userTelephone} and Phone number: {numberTelephone}")

# # we can do operations too

# a = 5
# b = 5

# print(f"Addition {a} + {b} is {a+b}")

# # Some times we need convert int to string to concat data

# year = 2025
# bday_year = 1987

# #print("I'm too old, i was born on " + bday_year + " and we are actually at year " + year) # Error type int to string

# print("I'm too old, i was born on " + str(bday_year) + " and we are actually at year " + str(year))

# # Acces to chars
# # to acces a char we use [] with a combinations
# phrase = "cc,a,bc,b"

# print(phrase[0])  # first char -> c 
# print(phrase[3])  # fourth char -> a
# print(phrase[4:]) # fifth char from the start ->,bc,b 
# print(phrase[:-3]) # fourth char from the end ->cc,a,b
# print(phrase[1:5])# second char at the start and 5th at the end ->c,a
# print(phrase[:])  # all chars


# Exercises

# Write a program that prompts the user for two numbers and a phrase. The first number entered
# It will correspond to the start position of the substring that the program should display on the screen.
# The second number will indicate the length of said substring.
# • Example 1: Position=4, Length=8, Phrase=’Developing is my new hobby’
# • Result 1: “loping i”
# • Example 2: Position=8, Length=11, Phrase=’Welcome to programming class’
# • Result 2: “to programm”

# # input phrase
# phrase = str(input("insert phrase: "))

# # input position
# position = int(input("enter position: "))

# # input length
# lenght = int(input("enter lenght: "))

# # So, we must calculate the final position 
# finalPosition = position + lenght

# # now we extract the substring doing slicing

# result = phrase[position:finalPosition]

# #print result
# print(result)

# Escribe un programa que solicite al usuario una frase. A continuación le solicitará la letra que quiere
# reemplazar y por qué letra deberá reemplazarse. Por último el programa mostrará el número de veces
# que la letra está presente en la frase y el resultado final tras reemplazarla.
# • Ejemplo: ‘Desarrollar es mi nuevo pasatiempos’, ‘a’,’e’
# • Resultado: 4 apariciones. ‘Deserroller es mi nueve pesetiempos’

# # introducimos la frase
# frase = str(input("Introduce una frase: "))

# # solicitar caracter a reemplazar

# quieroReemplazar = str(input("inserta el caracter que quieras reemplazar: "))

# # solicitar letra que se debe reemplazar

# debeReemplazar = str(input("Inserta el caractar que debe reemplazarse: "))

# # debemos contar el caracter que queremos reemplazar en la frase (paso innecesario)

# paso1 = frase.count(quieroReemplazar) # cuenta el numero de caracteres

# # con el metodo replace, ahora podemos sustituir los caracteres

# paso2 = frase.replace(quieroReemplazar, debeReemplazar)

# # resultado

# print(paso2)