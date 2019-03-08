# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:43:06 2019

@author: Hadrien
"""
import csv

fichier=open("chat.txt",encoding="utf8")
c=csv.writer(open("Données.csv","w",encoding="utf8"))
c.writerow(["Date","Auteur","Message"])

def deuxPoints(texte):
    i=0
    while i<len(texte):
        if texte[i]==":":
            return i
        i+=1
    return False
    

decoupe=fichier.read()
decoupe=decoupe[3:]
decoupe2=[]
for k in decoupe:
    L=""
    for l in k:
        if l!='\u200e' :
            L+=l
    decoupe2.append(L)
    
decoupe=decoupe2

fichier.close()

fichier=open("temp.txt","w",encoding="utf8")
for k in decoupe:
    fichier.write(k)
fichier.close()
fichier=open("temp.txt","r",encoding="utf8")
decoupe=fichier.read().split("\n[")
fichier.close()

    

print (len(decoupe),"\n")

listeDate=[]
listeAuteur=[]
listeMessage=[]
listeAjout=[]
compt=0
for k in decoupe:
    compt+=1
    #print(compt)
    #print(k[0],k[21])
    if (k[0] in ['0','1','2','3']) and k[21]!="\u200e":
       # print('OK')
        
        listeDate.append(k[:18])
        i=deuxPoints(k[18:])
        if i:
            listeAuteur.append(k[21:18+i])
            listeMessage.append(k[19+i:])
            c.writerow([k[:18],k[21:18+i],k[19+i:]])
        
def listeDesParticipants(listeDesAuteurs):
    liste=[]
    for k in listeDesAuteurs:
        if k not in liste:
            liste.append(k)
    return (liste)

listeParticipant=listeDesParticipants(listeAuteur)

def longueurMoyenne(listeAuteur=listeAuteur,listeMessage=listeMessage):
    listeParticipant=listeDesParticipants(listeAuteur)
    listeLongueur=[0]*len(listeParticipant)
    for k in range(len(listeParticipant)):
        for i in range (len(listeAuteur)):
            if listeAuteur[i]==listeParticipant[k]:
                listeLongueur[k]+=len(listeMessage[i])
    compteur=nbMessageParAuteur(listeAuteur)
    for k in range(len(compteur)):
        listeLongueur[k]=listeLongueur[k]/compteur[k]
    
    return listeLongueur
    
def nbMessageParAuteur(listeDesAuteurs):
    listeParticipant=listeDesParticipants(listeDesAuteurs)
    compteur=[0]*len(listeParticipant)
    for k in listeDesAuteurs:
        for l in range(len(listeParticipant)):
            if k==listeParticipant[l]:
                compteur[l]+=1
    return (compteur)

def nbImageParAuteur(listeDesAuteurs):
    listeParticipant=listeDesParticipants(listeDesAuteurs)
    compteur=[0]*len(listeParticipant)
    for k in range(len(listeParticipant)):
        for i in range (len(listeDesAuteurs)):
            if listeDesAuteurs[i]==listeParticipant[k] and listeMessage[i]==" image absente":
                compteur[k]+=1
    return (compteur)

def nbAudioParAuteur(listeDesAuteurs):
    listeParticipant=listeDesParticipants(listeDesAuteurs)
    compteur=[0]*len(listeParticipant)
    for k in range(len(listeParticipant)):
        for i in range (len(listeDesAuteurs)):
            if listeDesAuteurs[i]==listeParticipant[k] and listeMessage[i]==" audio omis":
                compteur[k]+=1
    return (compteur)


def nbSequencesParAuteur(sequence,listeDesAuteurs):
    listeParticipant=listeDesParticipants(listeDesAuteurs)
    compteur=[0]*len(listeParticipant)
    for k in range(len(listeParticipant)):
        for i in range (len(listeDesAuteurs)):
            if listeDesAuteurs[i]==listeParticipant[k] and sequence in listeMessage[i]:
                compteur[k]+=1
    return (compteur)


nbMessage=nbMessageParAuteur(listeAuteur)
messageMoyen=(longueurMoyenne())
nbImageParAuteur=nbImageParAuteur(listeAuteur)
nbAudioParAuteur=nbAudioParAuteur(listeAuteur)
nbCoucou=nbSequencesParAuteur("Coucou",listeAuteur)

for i in range(len(listeParticipant)):
    print(listeParticipant[i],"\n", "messages:",nbMessage[i],"moy:",round(messageMoyen[i],2),"images:",nbImageParAuteur[i],"audios:",nbAudioParAuteur[i],"Coucou:", nbCoucou[i],"\n")        
          
            
        

