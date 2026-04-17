# Projet_OUVINFO
Projet d'ouverture informatique

__Développeurs :__
Gwennan Fretay, Lola Corbel, Emma-Lyne Portelli, Camélia Bensemmane (cheffe de groupe)

__Résumé du projet :__ 
Dans le cadre de ce cours, nous souhaitons crée un petit jeu de plateforme (ayant un gameplay semblable à Super Mario Bros) de 3 niveaux (ou plus, cela dépendra de l'avancement du projet) dans lequel une princesse s'engage dans une aventure afin de sauver son prince. 
Les actions que le joueur pourra effectuer sont relativement simples : bouger de gauche à droite, sauter sur des plateformes, acquérir des bonus). 

Description du premier niveau (la structure étant la même pour chacun d'entre eux) : 

1) Le joueur apparaît à une position à gauche de la carte
2) Celui ci doit se déplacer à la fin du niveau (vers la droite) en récoltant des trois clés permettant d'ouvrir la porte lui permettant d'accéder au prochain level
3) Le background bouge vers la droite à une vitesse donnée, le joueur doit essayer de ne pas se faire toucher par celui-ci où il perdra la partie
4) Le joueur devra également éviter des ennemis implémentés sur la carte. Les ennemis auront une trajectoire fixe et bougeront de la droite vers la gauche 

__Liste des fichier :__

main.py ⬇️
Contient la boucle du jeu. 

__Listes de tâches :__

- [ OK ] Réaliser la boucle du jeu, sa structure principale
- [ OK ] Choix du sprite du joueur/ennemis, du background du niveau 1, du background du niveau 2, du background du niveau 3
- [ OK  ] Implémenter un background mouvant qui bouge vers la droite, celui-ci bouge constamment et le joueur doit essayer de ne pas se faire toucher par celui-ci
- [ OK ] Faire le background du niveau 1 (qui ne contient pas d'objet avec lesquels on peut entrer en contact)
- [ OK ] Faire la surcouche du niveau 1, visuel (qui contiendra des objets avec lesquels on peut entrer en colision)
- [ Partiellement ] Implementer les colisions avec les plateformes présentes sur la surcouche du niveau 1
- [ OK ] Implémenter les différents évenements (joueur qui récolte une clé, passage vers le prochain niveau, entrer en contact avec un ennemis)
- [ OK ] Faire le background du niveau 2 (qui ne contient pas d'objet avec lesquels on peut entrer en contact)
- [ ] Faire la surcouche du niveau 2, visuel (qui contiendra des objets avec lesquels on peut entrer en colision)
- [ ] Implementer les colisions avec les plateformes présentes sur la surcouche du niveau 2
- [ ] Implémenter les différents évenements (joueur qui récolte une clé, passage vers le prochain niveau, entrer en contact avec un ennemis)
- [ ] Réaliser le niveau 3 en conservant la même série d'action
- [ ] Finir le jeu le 18 mai
- [ ] Organisation de l'oral à finir le 20 mai
- [ ] Répétition orale le jeudi 21 mai
- [ ] Rapport à faire entre le 21 et le 27
- [ ] Présenter le projet le 27 mai 
 

