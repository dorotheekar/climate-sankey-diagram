## sankers-cout-climat

Script pour générer un diagramme de Sankers pour représenter les coûts de différentes offres.

### Fonctionnement

Le script génère un graphique svg à partir du fichier_input.csv pour lequel l'origine des coûts de chaque offre est affichée.
Il y a 7 coûts différents et un nombre quelconque d'offres différentes. La somme des coûts doit être égale à 100.

### Parameters :

#### Input :
	- fichier_input : nom du fichier .csv contenant les données

#### Script :
	- fichier.py : couleurs sont modifiables dans le dictionnaires des couleurs colorDict.

#### Output :
	- output : nom du fichier .svg affichant le diagramme de Sankers généré dans le repertoire

#### Librairies:
	- requirements.txt : permet d'installer les librairies pour le projet (pip install -r requirements.txt)

#### Polices d'écriture: il faut les installers sous Windows
	- FontFont - Daxline Offc Bold
	- FontFont - Daxline Offc Light
	- FontFont - Daxline SC Offc Bold
	- FontFont - Daxline SC Offc Light


