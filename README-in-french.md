# README-in-french

Étant donnée l'irréversiblité de l'envoie de mail, je vous conseille de lire tout le mode d'emploi avant de faire des envois.
Pour toute question, contactez moi.

Ce programme a été écrit en python 3.7

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

### Préparation :

* Il est possible que par soucis de sécurité, gmail interdise l'accès du compte à une application tierce. 
Pour corriger ce problème, aller dans le compte google du club : https://myaccount.google.com/ 
> sécurité > Accès moins sécurisé des applications > Activer

* Vous pouvez modifier les identifiants, port et serveur smtp dans le fichier "config.txt"



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

### Mode d'emploi :

1. écrire le message de son choix dans 'body.txt'.
	* l'objet doit être renseigné à la première ligne, après  'Objet :'
	* Attention ! Le message doit être en HTML
	* Pour personnaliser le message, mettre %s à chaque endroit où vous voulez ajouter une variable "de personnalisation"

-> Je vous conseille franchement de tester la mise en forme de votre body en vous envoyant vous même le mail.
Pour cela, il suffit de mettre dans "addresse.txt" la ligne suivante : 

destinataire@exemple.com <tab> variables de personnalisation 1 <tab> variables de personnalisation1	...

puis de lancer l'exécutable. L'exécutable demande votre mot de passe mais comme je suis pas un bâtard, j'ai pas mis de backdoor.

2. Le fichier "addresses.txt" doit contenir sur chaque ligne l'adresse du destinataire et éventuellement les variables de personnalisation/
Les éléments doivent être séparés d'une tabulation. (Séparation par défaut en copiant collant depuis google spreadShit).

ATTENTION : il doit y avoir autant de %s dans le body que de variables de personnalisations par ligne.
