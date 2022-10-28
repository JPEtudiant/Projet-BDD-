#Projet BD Coquet Jean-Philippe

from random import *
from tkinter import *
from tkinter.ttk import *
import sqlite3
from tablesql import *
connection = sqlite3.connect("database.db")
curseur = connection.cursor()
connection.commit()


creer_base_vide()



class stock:
    def __init__(self,nom_plat,quantite_plat):
        self.nom_plat = nom_plat
        self.quantite_plat = quantite_plat
    '''    
    def affiche_stock():
        curseur.execute('Select * from Stock')
        affiche_stck = curseur.fetchall()
        for i in affiche_stck:
            print(i)
        print()
    '''
class client:
    def __init__(self,nom,prenom,argent_depense):
        self.nom = nom
        self.prenom=prenom
        self.argent_depense = 0
    
    '''
    def ajout_client():
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prenom : ")
        argent_depense = 0
        curseur.execute("INSERT INTO Client (nom,prenom,argent_depense) VALUES (?, ?, ?)",(nom,prenom,argent_depense))
        connection.commit()
        print("Le client "+nom+" "+prenom+" a été ajouté")
     '''
    '''
    def affiche_client():
        curseur.execute("SELECT * FROM client")
        affiche_clt = curseur.fetchall()
        print(affiche_clt)
    
    def modif_client():
        client = input("Entrez le nom du client à modifier : ")
        curseur.execute("SELECT * FROM client where nom = ?",(client,))
        if (curseur.fetchall() == []):
            print("Erreur, veuillez recommencer l'opération")
        else:
            print("Que voulez vous modifier ?")
            print("Nom ? (Tapez 1)")
            print("Prénom ? (Tapez 2)")
            modif = int(input())
            if (modif == 1):
                nom = input("Entrez le nouveau nom : ")
                curseur.execute("UPDATE Client set nom = (?) where nom = (?)",(nom,client))
                connection.commit()
            elif(modif == 2):
                prenom = input("Entrez le nouveau prénom : ")
                curseur.execute("UPDATE Client set prenom = (?) where prenom = (?)",(prenom,client))
                connection.commit()
            else:
                print("Erreur, veuillez recommencer l'opération")
        
    def supprime_client():
        nom_client = input("Entrez le nom du client à supprimer : ")
        curseur.execute("DELETE from Client where nom = ?",(nom_client,))
        connection.commit()
        print("Le client "+nom_client+" a été supprimé")
    '''

class reservation:
    def __init__(self,id_client, id_table, date,heure_debut,heure_fin):
        self.id_client = id_client
        self.id_table = id_table
        self.date=date
        self.heure_debut=heure_debut
        self.heure_fin=heure_fin
    '''
    def ajout_reservation():
         id_client = int(input("Entrez l'id du client : "))
         id_table = int(input("Entrez le numéro de table :"))
         date = input("Entrez une date (format YYYY-MM-DD) : ")
         heure_debut = input("Entrez une heure de début (format HH:MM) : ")
         heure_fin = input("Entrez une heure de fin (format HH:MM) : ")
         curseur.execute("INSERT INTO Reservation (id_client, id_table, date, heure_debut, heure_fin) VALUES (?, ?, ?, ?, ?)",(id_client, id_table, date, heure_debut, heure_fin))
         connection.commit()
         
    def affiche_reservation():
        curseur.execute("SELECT * from Reservation")
        affiche_reserv = curseur.fetchall()
        for i in affiche_reserv:
            print(i)
        print()
        
    def supprime_reservation():
        id_client = int(input("Entrez l'id client de la réservation à supprimer : "))
        date = input("Entrez la date de sa réservation (format YYYY-MM-DD) : ")
        curseur.execute("DELETE from reservation where id_client = ? and date = ?",(id_client,date))
        connection.commit()
        print("La réservation a bien été supprimée")
    '''
        
class tables:
    def __init__(self,numero_table,nb_places):
        self.numero_table = numero_table
        self.nb_places = nb_places
        


class graphique(Frame):
    
    def __init__(self):
        self.menu_principal()
        
    def menu_principal(self):    
        self.fen = Tk()
        Frame(self.fen).grid(row=0,column=0)
        self.fen.title("Steve-concept restauration")
        
        self.title_frame = Frame(self.fen)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        self.fen.geometry('800x900')
        
        self.creation_base_button = Button(self.fen, text = "Créer la base", command = self.creation_base_remplie)
        self.creation_base_button.grid(row=0, column= 70, pady = 10, ipady= 10)

        self.nv_client_button = Button(self.fen, text = "Nouveau client", command = self.menu_nouveau_client)
        self.nv_client_button.grid(row = 1, column = 70, pady = 10, ipady = 10)

        self.modif_infos_button = Button(self.fen, text = "Afficher les clients", command = self.menu_affiche_client)
        self.modif_infos_button.grid(row = 2, column = 70, pady = 10, ipady = 10)
        
        self.supp_client_button = Button(self.fen, text = "Supprimer un client", command = self.menu_supp_client)
        self.supp_client_button.grid(row = 3, column = 70, pady = 10, ipady = 10)

        self.nv_reservation_button = Button(self.fen, text = "Nouvelle réservation", command = self.menu_new_reservation)
        self.nv_reservation_button.grid(row = 4, column = 70, pady = 10, ipady = 10)
        
        self.supp_reserv_button = Button(self.fen, text = "Supprimer une réservation", command = self.menu_supp_reservation)
        self.supp_reserv_button.grid(row = 5, column = 70, pady = 10, ipady = 10)

        #self.affiche_client_button = Button(self.fen, text = "Afficher les clients", command = client.affiche_client)
        #self.affiche_client_button.grid(row = 5, column = 70, pady = 10, ipady = 10)
        
        self.affiche_reserv_button = Button(self.fen, text = "Afficher les réservations", command = self.menu_affiche_reservation)
        self.affiche_reserv_button.grid(row = 6, column = 70, pady = 10, ipady = 10)
             
        
        self.affiche_stck_button = Button(self.fen, text = "Afficher le stock", command = self.menu_affiche_stock)
        self.affiche_stck_button.grid(row = 7, column = 70, pady = 10, ipady = 10)
        
        self.plus_haute_depense_button = Button(self.fen, text = "Afficher le client qui a le plus dépensé", command = self.plus_haute_depense)
        self.plus_haute_depense_button.grid(row = 8, column = 70, pady = 10, ipady = 10)
        
        self.plat_plus_commande_button = Button(self.fen, text ="Afficher le plat qui a été le plus stocké", command = self.plat_plus_stocke)
        self.plat_plus_commande_button.grid(row = 9, column = 70, pady = 10, ipady=10)
        
        self.table_plus_de_place_button = Button(self.fen, text ="Afficher la table qui a le plus de place", command = self.table_plus_de_place)
        self.table_plus_de_place_button.grid(row = 10, column = 70, pady = 10, ipady=10)
        
        self.table_plus_de_place_button = Button(self.fen, text ="Afficher le plat le plus cher", command = self.prix_plat_plus_cher)
        self.table_plus_de_place_button.grid(row = 11, column = 70, pady = 10, ipady=10)
        
        

        self.bouton_terminer = Button(self.fen, text='Terminer', command=self.fen.destroy)
        self.bouton_terminer.grid(row = 8, sticky = E, pady = 10, ipady = 3)

        self.bouton_terminer.grid(row = 12, padx=10, pady=10)
        self.fen.mainloop()
    
    def menu_nouveau_client(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Nouveau client")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Nom").grid(row = 0, padx = 10)
        Label(self.menu, text="Prénom").grid(row = 1, padx = 10)
    
        
        nom = Entry(self.menu)
        prenom = Entry(self.menu)
        
        
        nom.grid(row =0, column = 1, padx = 10, pady = 5)
        prenom.grid(row =1, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4) 
        Button(self.menu, text = "Ajouter", command = lambda: [curseur.execute("INSERT INTO Client (nom,prenom,argent_depense) VALUES (?, ?, ?)",(nom.get(),prenom.get(),0)),connection.commit(),self.menu.destroy(),self.menu_principal()]).grid(row = 2, column = 1, pady = 4)

    
        
    def menu_affiche_client(self):
        self.fen.destroy()
        
        self.menu_afficher = Tk()
        Frame(self.menu_afficher).grid(row = 0, column = 0)
        self.menu_afficher.title("Afficher clients")
        self.title_frame = Frame(self.menu_afficher)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        self.tableau = Treeview(self.menu_afficher, columns=("id_client","nom", "prénom", "argent depense"))
        self.tableau.heading("id_client", text="id_client")
        self.tableau.heading("nom", text="nom")
        self.tableau.heading("prénom", text="prénom")
        self.tableau.heading("argent depense", text="argent depense")
        self.tableau["show"] = "headings"
        self.tableau.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.tableau.bind("<Double-Button-1>", self.selectItem)
        
        curseur.execute("SELECT * FROM Client")
        resultat = curseur.fetchall()
        
        for valeurs in resultat:
            self.tableau.insert("", "end", iid=valeurs[0], values=(valeurs[0],valeurs[1], valeurs[2], valeurs[3]))
        
        Button(self.menu_afficher, text = "Retour", command = lambda: [self.menu_afficher.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
    
    def selectItem(self,a):
        valeurs = self.tableau.item(self.tableau.focus()).get("values")
        self.menu_modif_client(valeurs[1],valeurs[2],valeurs[3])
     
    def menu_modif_client(self,a,b,c):
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Modifier client")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Nom").grid(row = 0, padx = 10)
        Label(self.menu, text="Prénom").grid(row = 1, padx = 10)
        Label(self.menu, text="Argent depensé").grid(row = 2, padx = 10)
    
        
        nom = Entry(self.menu)
        nom.insert(0,a)
        prenom = Entry(self.menu)
        prenom.insert(0,b)
        argent_depense = Entry(self.menu)
        argent_depense.insert(0,c)
        
        nom.grid(row =0, column = 1, padx = 10, pady = 5)
        prenom.grid(row =1, column = 1, padx = 10, pady = 5)
        argent_depense.grid(row =2, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy()]).grid(row = 3, column = 0, pady = 4) 
        Button(self.menu, text = "Modifier", command = lambda: [curseur.execute("UPDATE Client SET nom = ? , prenom = ? , argent_depense = ? WHERE nom = ? AND prenom = ? AND argent_depense = ?", (nom.get(),prenom.get(),argent_depense.get(),a,b,c)),connection.commit(),self.actualiser_liste(nom.get(),prenom.get(),argent_depense.get()),self.menu.destroy()]).grid(row = 3, column = 1, pady = 4)
    
    def actualiser_liste(self,a,b,c):
        resultat = curseur.execute("SELECT * FROM Client WHERE nom = ? AND prenom = ? AND argent_depense = ?", (a,b,c)).fetchall()        
        for valeurs in resultat:
            self.tableau.item(valeurs[0], values=(valeurs[1], valeurs[2], valeurs[3]))
            
    def menu_supp_client(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Supprimer client")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Nom du client").grid(row = 0, padx = 10)
        
        nom = Entry(self.menu)
        
        nom.grid(row =0, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 5, column = 0, pady = 4)
        Button(self.menu, text = "Supprimer", command = lambda: [curseur.execute("DELETE from Client where nom = ?",(nom.get(),)),connection.commit(),self.menu.destroy(),self.menu_principal()]).grid(row = 2, column = 1, pady = 4)
        
        
    def menu_new_reservation(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Nouvelle réservation")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Id Client").grid(row = 0, padx = 10)
        Label(self.menu, text="Numéro table attribuée").grid(row = 1, padx = 10)
        Label(self.menu, text="Date (format YYYY-MM-DD)").grid(row = 2, padx = 10)
        Label(self.menu, text="Heure début (format HH:MM)").grid(row = 3, padx = 10)
        Label(self.menu, text="Heure fin (format HH:MM)").grid(row = 4, padx = 10)

        
        id_client = Entry(self.menu)
        id_table = Entry(self.menu)
        date = Entry(self.menu)
        heure_debut = Entry(self.menu)
        heure_fin = Entry(self.menu)
        
        id_client.grid(row =0, column = 1, padx = 10, pady = 5)
        id_table.grid(row =1, column = 1, padx = 10, pady = 5)
        date.grid(row =2, column = 1, padx = 10, pady = 5)
        heure_debut.grid(row =3, column = 1, padx = 10, pady = 5)
        heure_fin.grid(row =4, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 5, column = 0, pady = 4)
        Button(self.menu, text = "Ajouter", command = lambda: [curseur.execute("INSERT INTO Reservation (id_client, id_table, date, heure_debut, heure_fin) VALUES (?, ?, ?, ?, ?)",(id_client.get(), id_table.get(), date.get(), heure_debut.get(), heure_fin.get())),connection.commit(),self.menu.destroy(),self.menu_principal()]).grid(row = 5, column = 1, pady = 4)


    def menu_supp_reservation(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Supprimer réservation")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Id Client").grid(row = 0, padx = 10)
        Label(self.menu, text="Date de la réservation").grid(row = 1, padx = 10)
        
        id_client = Entry(self.menu)
        date = Entry(self.menu)
        
        id_client.grid(row =0, column = 1, padx = 10, pady = 5)
        date.grid(row =1, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        Button(self.menu, text = "Supprimer", command = lambda: [curseur.execute("DELETE from reservation where id_client = (?) and date = (?)",(id_client.get(),date.get())),connection.commit(),self.menu.destroy(),self.menu_principal()]).grid(row = 2, column = 1, pady = 4)


    def menu_affiche_stock(self):
        self.fen.destroy()
        
        self.menu_afficher = Tk()
        Frame(self.menu_afficher).grid(row = 0, column = 0)
        self.menu_afficher.title("Afficher stock")
        self.title_frame = Frame(self.menu_afficher)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        self.tableau = Treeview(self.menu_afficher, columns=("nom_plat", "quantité_plat"))
        self.tableau.heading("nom_plat", text="nom_plat")
        self.tableau.heading("quantité_plat", text="quantité_plat")
        self.tableau["show"] = "headings"
        self.tableau.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.tableau.bind("<Double-Button-1>", self.selectItem_stock)
        
        curseur.execute("SELECT * FROM Stock")
        resultat = curseur.fetchall()
        
        for valeurs in resultat:
            self.tableau.insert("", "end", iid=valeurs[0], values=(valeurs[1], valeurs[2]))
        
        Button(self.menu_afficher, text = "Retour", command = lambda: [self.menu_afficher.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
    def selectItem_stock(self,a):
        valeurs = self.tableau.item(self.tableau.focus()).get("values")
        self.menu_modif_stock(valeurs[0],valeurs[1])
        
    def menu_modif_stock(self,a,b):
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Modifier stock")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Nom plat").grid(row = 0, padx = 10)
        Label(self.menu, text="Quantité plat").grid(row = 1, padx = 10)
    
        nom_plat = Entry(self.menu)
        nom_plat.insert(0,a)
        
        quantite_plat = Entry(self.menu)
        quantite_plat.insert(0,b)
        
        nom_plat.grid(row =0, column = 1, padx = 10, pady = 5)
        quantite_plat.grid(row =1, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy()]).grid(row = 2, column = 0, pady = 4) 
        Button(self.menu, text = "Modifier", command = lambda: [curseur.execute("UPDATE Stock SET nom_plat = ? , quantite_plat = ? WHERE nom_plat = ? AND quantite_plat = ? ", (nom_plat.get(),quantite_plat.get(),a,b)),connection.commit(),self.actualiser_liste_stock(nom_plat.get(),quantite_plat.get()),self.menu.destroy()]).grid(row = 2, column = 1, pady = 4)
    
    def actualiser_liste_stock(self,a,b):
        resultat = curseur.execute("SELECT * FROM Stock WHERE nom_plat = ? AND quantite_plat = ?", (a,b)).fetchall()        
        for valeurs in resultat:
            self.tableau.item(valeurs[0], values=(valeurs[1], valeurs[2]))    
    
    def menu_affiche_reservation(self):
        self.fen.destroy()
        
        self.menu_afficher = Tk()
        Frame(self.menu_afficher).grid(row = 0, column = 0)
        self.menu_afficher.title("Afficher les réservations")
        self.title_frame = Frame(self.menu_afficher)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        self.tableau = Treeview(self.menu_afficher, columns=("id_client", "id_table", "date", "heure_debut", "heure_fin"))
        self.tableau.heading("id_client", text="id_client")
        self.tableau.heading("id_table", text="numéro_table")
        self.tableau.heading("date", text="date")
        self.tableau.heading("heure_debut", text="heure_debut")
        self.tableau.heading("heure_fin", text="heure_fin")
        self.tableau["show"] = "headings"
        self.tableau.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.tableau.bind("<Double-Button-1>", self.selectItem_reservation)
        
        curseur.execute("SELECT * FROM reservation")
        resultat = curseur.fetchall()
        
        for valeurs in resultat:
            self.tableau.insert("", "end", iid=valeurs[0], values=(valeurs[0],valeurs[1], valeurs[2],valeurs[3],valeurs[4]))
        
        Button(self.menu_afficher, text = "Retour", command = lambda: [self.menu_afficher.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
    def selectItem_reservation(self,a):
        valeurs = self.tableau.item(self.tableau.focus()).get("values")
        self.menu_modif_reservation(valeurs[0],valeurs[1],valeurs[2],valeurs[3],valeurs[4])
     
    def menu_modif_reservation(self,a,b,c,d,e):
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Modifier réservation")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        Label(self.menu, text="Id client").grid(row = 0, padx = 10)
        Label(self.menu, text="Numéro table").grid(row = 1, padx = 10)
        Label(self.menu, text="Date").grid(row = 2, padx = 10)
        Label(self.menu, text="Heure début").grid(row = 3, padx = 10)
        Label(self.menu, text="Heure fin").grid(row = 4, padx = 10)
    
        id_client = Entry(self.menu)
        id_client.insert(0,a)
        
        id_table = Entry(self.menu)
        id_table.insert(0,b)
        
        date = Entry(self.menu)
        date.insert(0,c)
        
        heure_debut = Entry(self.menu)
        heure_debut.insert(0,d)
        
        heure_fin = Entry(self.menu)
        heure_fin.insert(0,e)
        
        id_client.grid(row =0, column = 1, padx = 10, pady = 5)
        id_table.grid(row =1, column = 1, padx = 10, pady = 5)
        date.grid(row =2, column = 1, padx = 10, pady = 5)
        heure_debut.grid(row =3, column = 1, padx = 10, pady = 5)
        heure_fin.grid(row =4, column = 1, padx = 10, pady = 5)
        
        Button(self.menu, text = "Annuler", command = lambda: [self.menu.destroy()]).grid(row = 5, column = 0, pady = 4) 
        Button(self.menu, text = "Modifier", command = lambda: [curseur.execute("UPDATE reservation SET id_client = ? , id_table = ? , date = ? , heure_debut = ? , heure_fin = ? WHERE id_client = ? AND id_table = ? AND date = ? AND heure_debut = ? AND heure_fin = ?", (id_client.get(),id_table.get(),date.get(),heure_debut.get(),heure_fin.get(),a,b,c,d,e)),connection.commit(),self.actualiser_liste_reservation(id_client.get(),id_table.get(),date.get(),heure_debut.get(),heure_fin.get()),self.menu.destroy()]).grid(row = 5, column = 1, pady = 4)
    
    def actualiser_liste_reservation(self,a,b,c,d,e):
        resultat = curseur.execute("SELECT * FROM Reservation WHERE id_client = ? AND id_table = ? AND date = ? AND heure_debut = ? AND heure_fin = ?", (a,b,c,d,e)).fetchall()        
        for valeurs in resultat:
            self.tableau.item(valeurs[0], values=(valeurs[0], valeurs[1], valeurs[2], valeurs[3],valeurs[4]))
        
        
    def plus_haute_depense(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row = 0, column = 0)
        self.menu.title("Client ayant le plus dépensé")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        #resultat_nom = curseur.execute("SELECT nom FROM Client WHERE argent_depense = (Select MAX(argent_depense) from client)").fetchall()
        #resultat_prenom = curseur.execute("SELECT prenom FROM Client WHERE argent_depense = (Select MAX(argent_depense) from client)").fetchall()
        
        resultat_plus_haute_depense = curseur.execute("SELECT * FROM view1").fetchall()
        
        Label(self.menu, text="Prénom : ").grid(row = 0, padx = 10)
        Label(self.menu, text="Nom : ").grid(row = 1, padx = 10)
        #Label(self.menu, text=resultat_nom).grid(row = 1, column = 1, padx = 10)
        #Label(self.menu, text=resultat_prenom).grid(row = 0, column = 1, padx = 10)
        Label(self.menu, text = resultat_plus_haute_depense).grid(row = 1, column = 1, padx = 10)
        
        
        Button(self.menu, text = "Retour", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
        
    def plat_plus_stocke(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row =0, column =0)
        self.menu.title("Plat le plus stocké")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        resultat_plat = curseur.execute("SELECT * FROM view2").fetchall()
        
        Label(self.menu, text="Nom du plat : ").grid(row = 0, padx =10)
        Label(self.menu, text=resultat_plat).grid(row = 1, column =1, padx = 10)
        
        Button(self.menu, text = "Retour", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
        
    def table_plus_de_place(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row =0, column =0)
        self.menu.title("Table qui a le plus de place")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        resultat_tables = curseur.execute("SELECT * FROM view3").fetchall()
        
        Label(self.menu, text="Nombre de places : ").grid(row = 0, padx=10)
        Label(self.menu, text=resultat_tables).grid(row = 1, column =1, padx = 10)
        
        Button(self.menu, text = "Retour", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
    
        
    def prix_plat_plus_cher(self):
        self.fen.destroy()
        
        self.menu = Tk()
        Frame(self.menu).grid(row =0, column =0)
        self.menu.title("Prix du plat qui coute le plus cher")
        self.title_frame = Frame(self.menu)
        self.title_frame.grid(row = 0, column = 0, columnspan = 4)
        
        resultat_plat = curseur.execute("SELECT * FROM view4").fetchall()
        
        Label(self.menu, text="Prix du plat le plus cher : ").grid(row = 0, padx=10)
        Label(self.menu, text=resultat_plat).grid(row = 1, column =1, padx = 10)
        
        Button(self.menu, text = "Retour", command = lambda: [self.menu.destroy(), self.menu_principal()]).grid(row = 2, column = 0, pady = 4)
        
    def creation_base_remplie(self):
        creer_base_remplie()
                
if __name__ == '__main__':
    gui = graphique()