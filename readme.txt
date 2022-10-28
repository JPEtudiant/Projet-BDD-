database.db sert d'intermédiaire pour intéragir avec les tables de la BD

tablesql.py sert à importer dans l'application les tables et les insertions de la BD

interface.py est l'application exécutable et son code source est directement visible 
depuis un IDE(j'ai utilisé Thonny avec Python 3.7.9 bundled)

La base de données est vide au départ, il vous faudra appuyer sur le bouton "Créer la base" pour la remplir.
Vous pouvez modifier la base à votre guise sans fermer la fenetre d'interface.
Des boutons retour sont prévus et la réalisation d'une fonction ne coupe pas la fenêtre.
A chaque relance du programme, la base sera vide, en réappuyant sur "Créer la base", la base initiale sera relancée.
Le bouton Terminer ferme le programme.

-Pour utiliser l'appication, lancez interface.py avec Thonny
-Cliquez sur la flèche verte (Run) ou F5
-L'interface graphique apparait avec 13 boutons
-Vous pouvez intéragir avec les différentes fonctions grâce aux boutons
-Par exemple, en cliquant sur nouveau client, vous pouvez ajouter à la BD un client en entrant
son nom et prénom, puis cliquer sur Ajouter, un retour au menu principal s'effectura
et le client sera dans la DB
-S'il y a un problème dans le nom, afficher les clients et double cliquez dessus pour modifier
-Supprimer un client supprime un client en entrant son nom de famille
-Supprimer une réservation avec son id client et la date de la réservation
-Afficher réservation pour visualiser les réservation et double cliquer pour modifier
-Afficher le stock pour visualiser les stocks et double cliquer pour modifier


4 Views :

-bouton pour afficher le client qui a le plus dépensé
-bouton pour afficher le plat qui est le plus stocké
-bouton pour afficher la table qui a le plus de place
-bouton pour afficher le plat le plus cher

Les 4 déclencheurs sont les suivants :

- (nom dans le code t1) Après avoir ajouté une réservation, les quantités de chaque plat dans le stock est augmenté de 100.
- (nom dans le code t2) Après avoir supprimé un client, sa réservation est également supprimée.
- (nom dans le code t3) Après avoir modifié un client, son id_table est augmenté de 1.
- (nom dans le code t4) Après avoir supprimé une réservation, le client est également supprimé.




