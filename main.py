#kirjutada programm, mis küsib kasutajalt tema nime ja tervitab teda nimepidi.

#Algus
#Küsi kasutajalt eesnimi
#Salvesta väärtus muutujasse first_name
#Väljastab tervitust: "Hello, <eesnimi>!"
#Lõpp

first_name = input("Enter your first name:")
print("Hello, " + first_name + "!")


#f-string
print(f"Hello, {first_name}!")

#tehke nii, et programm küsib kasutajalt ka perekonnanime ja tervitaks teda nime ja perekonnanimega.
last_name = input("Enter your last name:")
print(f"Hello, {first_name} {last_name}!")