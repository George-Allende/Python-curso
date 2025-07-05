#Elaborar um programa que alerte sobre os riscos de animais em extinção. O usuário deve
#digitar o nome da espécie e a sua população (total de indivíduos)
#.Populações entre 0 e 500 indivíduos, são classificadas como "Espécie criticamente em perigo"
#,populações entre 501 e 1000 indivíduos, são classificadas como "Espécie em perigo" 
#e populações entre 1001 e 5000 indivíduos, são classificadas como "Espécie vulnerável!"

esp_animal = input("Nome da espécie: ")
num_animal = int(input("Total de indivíduos: "))

if num_animal < 0:
    print("Espécie criticamente em perigo")
elif num_animal <= 500:
    print("Espécie criticamente em perigo")
elif num_animal <= 1000:
    print("Espécie em perigo")
elif num_animal < 5000:
    print("Espécie vulnerável")
else:
    print("Espécie vulneravel")