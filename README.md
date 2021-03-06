# WhatThisApp

*Projet réalisé par Hadrien Torrin, Quentin Parenti et Simon Gaillard dans le cadre du MOS 5.5 de l'Ecole Centrale Lyon*

## liens utiles:



lien de la démo: https://htorf.github.io/WhatThisApp/


lien du gdoc: https://docs.google.com/document/d/1VOVWwUy8KcJX12FCiSgTmHfniwins8xS8_SDP4HETBc/edit?usp=sharing
lien du googlesheet: https://docs.google.com/spreadsheets/d/12kn-U0xH8ii1Mv_nCxE6BW5Fj2bo3py_ueFHi3rUJ6A/edit#gid=1311625435


## Contexte:

L’application WhatsApp (avec d’autres concurrents: Messenger, Telegram..)  est depuis quelques années, et pour de nombreuses personnes, devenue une alternative au SMS conventionnels. 
Un des avantages principaux étant la facilité de communiquer en groupe.
Cette application permet de plus d’exporter l’intégralité d’une conversation en format texte, ce qui peut pour certaines discussion représenter des dizaines de milliers de messages. 
Notre outil pourrait ainsi d’adapter aux conversations de n’importe qui utilisant WhatsApp.


## Questions:

Quelles sont les périodes temporelles (échelle d’une année ou d’une journée) où un groupe donné échange le plus?
Profils de message d’un utilisateur donné (fréquence de message, longueur moyenne des messages, nombre de média envoyé)
Existe-il des patterns dans une discussion? (untel réponds toujours quand untel a écrit, ou autre)


## Les utilisateurs:

Tout utilisateurs de WhatsApp souhaitant avoir des informations ou simplement curieux de voir des statistiques sur ses groupes de discussion.

## Les données:

WhatsApp propose un fichier texte construit comme suit:

*[JJ/MM/AAAA] Utilisateur: Contenu du message*

Un script python (disponible au telechargement) transforme facilement cela en un fichier excel à trois colonnes:

*Date | Utilisateur | Contenu du message*

Pour la présentation, nous avons utilisé une de nos conversations en modifiant les noms des participants.

## Quels sont les principaux risques de collection et visualisation de ces données ?

En fonction de la mémoire disponible sur le téléphone (ou sur un cloud) et allouée à WhatsApp, il se peut que les conversations ne soient pas stockées dans leur intégralité, limitant ainsi la pertinence de l’application.


## Quels sont les possibles problèmes éthiques/données privées ?

Une conversation étant privée elle contient évidemment des données sensibles que l'utilisateur ne souhaite pas partager. Il se peut que l’application se limite au nombre de message plutôt qu’à leur contenu ce qui annulera ce problème. Dans tous les cas chaque utilisateur utilisera ses données qui ne seront pas visible par autrui.


## Apercu de la Visualisation


 <img src="img/apercu.png" >
    
La partie supérieure est un calendrier montrant le nombre de message par jour dans cette conversation grâce à une echelle de couleur (vert foncé > beaucoup de message, blanc > pas de message)

La partie inférieure est un graphique intéractif, la partie de gauche présente le nombre de message par mois, le chart de droite montre la part de chaque participant. En passant sa souris sur un des mois, le graphique de droite se met à jour et affiche les sous-totaux pour le mois choisi. En passant sa souris sur un des participants sur le graphique de droite, le chart de gaiche se met à jour pour afficher le nombre de messages par mois de cet utilisateur uniquement. 

## Remerciements

Merci à Pasha (https://bl.ocks.org/NPashaP) dont nous avons repris le diagramme pour une partie de notre visualisation.

