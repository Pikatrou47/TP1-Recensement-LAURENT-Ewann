#L'objectif initial du programme est de proposer à l'utilisateur de choisir la région ou le département qu'il souhaite étudier
import matplotlib.pyplot as plt
fic=open("donnees_2008.csv","r")            #On importe le fichier csv
liste=fic.readline() #On supprime la première ligne du csv
texte=""
temp=[]
dico={}
departement={}
nombre_d_habitants=[]
somme=0
evolution=[]                                          #On crée une liste qui servira d'axe des abscisses
annee=[2008,2016,2021,2022,2023]                      #On crée une liste qui servira d'axe des ordonnées
for ligne in fic:
	texte=str(ligne)
	texte=texte.strip()          # On enlève les "/n"
	temp=texte.split(",")      #On sépare le texte en une liste par les virgules
	code_region,nom_region,code_departement,code_arrondissement,code_canton,code_commune,nom_commune,pop_municipale,pop_comptee_a_part,pop_totale=temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9]

#on crée désormais un dictionnaire ayant pour clé le nom des régions et pour valeurs des dictionnaires ayant pour clé le numéro des départements et pour valeurs les listes comportant les informations pour chaque commune.
  
if nom_region in dico:
		dico[nom_region][code_departement]=[int(code_region),int(code_arrondissement),int(code_canton),int(code_commune),nom_commune,int(pop_municipale),int(pop_comptee_a_part),int(pop_totale)]	
else:
	dico[nom_region]={code_departement:[int(code_region),int(code_arrondissement),int(code_canton),int(code_commune),nom_commune,int(pop_municipale),int(pop_comptee_a_part),int(pop_totale)]}
#On propose à l'utilisateur de choisir s'il souhaite étudier une région ou un département particulier
if choix=="r":
	region=input("Veuillez rentrer le nom de région que vous souhaitez étudier, exemple : Bourgogne")
	for i in dico[region].values():
			somme+=i[7]									#On fait la somme de la population totale de chaque département de chaque région
evolution.append(somme)           #On ajoute la somme de la population totale de cette année à la liste évolution afin de pouvoir utiliser les données pour le graphique plus tard
print("Le nombre d'habitant en ",region," est de : ", somme)
if choix=="d":
	region=input("Veuillez rentrer le nom de région que vous souhaitez étudier, exemple : Bourgogne")
	departement=input("Veuillez rentrer le code de département que vous souhaitez étudier.")
plt.plot(evolution,annee)                             #On crée la courbe avec les listes correspondant à chaque axe.
plt.show()
