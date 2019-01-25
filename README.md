# WhatThisApp

Contexte:

L’application WhatsApp (avec d’autres concurrents: Messenger, Telegram..)  est depuis quelques années, et pour de nombreuses personnes, devenue une alternative au SMS conventionnels. 
Un des avantages principaux étant la facilité de communiquer en groupe.
Cette application permet de plus d’exporter l’intégralité d’une conversation en format texte, ce qui peut pour certaines discussion représenter des dizaines de milliers de messages. 
Notre outil pourrait ainsi d’adapter aux conversations de n’importe qui utilisant WhatsApp.


Questions:

Quelles sont les périodes temporelles (échelle d’une année ou d’une journée) où un groupe donné échange le plus?
Profils de message d’un utilisateur donné (fréquence de message, longueur moyenne des messages, nombre de média envoyé)
Existe-il des patterns dans une discussion? (untel réponds toujours quand untel a écrit, ou autre)


Les utilisateurs:

Tout utilisateurs de WhatsApp souhaitant avoir des informations ou simplement curieux de voir des statistiques sur ses groupes de discussion.

Les données:

WhatsApp propose un fichier texte construit comme suit:
[JJ/MM/AAAA] Utilisateur: Contenu du message

Un script python (par exemple) transforme facilement cela en un fichier excel à trois colonnes:
Date | Utilisateur | Contenu du message

Pour commencer à faire des tests, on a utilisé une de nos conversations.

Quels sont les principaux risques de collection et visualisation de ces données ?

En fonction de la mémoire disponible sur le téléphone (ou sur un cloud) et alloué à WhatsApp, il se peut que les conversations ne soient pas stockées dans leur intégralité, limitant ainsi la pertinence de l’application.


Quels sont les possibles problèmes éthiques/données privées ?

Une conversation étant privée elle contient évidemment des données sensibles que l'utilisateur ne souhaite pas partager. Il se peut que l’application se limite au nombre de message plutôt qu’à leur contenu ce qui annulera ce problème. Dans tous les cas chaque utilisateur utilisera ses données qui ne seront pas visible par autrui.

