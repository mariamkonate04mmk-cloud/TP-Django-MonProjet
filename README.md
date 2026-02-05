
Mariam Konaté
Ce projet a été réalisé dans le cadre d'un Travail Pratique sur la configuration d'un projet Django.

a. Les étapes suivies
1.Configuration de l'environnement**
- Création de l'environnement virtuel Python
- Installation de Django et génération du fichier requirements.txt
2.Création du projet et de l'application
- Initialisation du projet Django avec `django-admin startproject`
- Création de l'application `monapp` avec `startapp`
### 3. Configuration du projet (`settings.py`)
- Ajout de `'monapp'` à `INSTALLED_APPS`
- Configuration pour la France : langue (`fr-fr`) et fuseau horaire (`Europe/Paris`)
- Définition des chemins pour les templates et fichiers statiques
4. Développement des vues (`monapp/views.py`)
Création de 3 vues :
- `accueil()` : Page d'accueil avec message de bienvenue
- `a_propos()` : Page présentant le projet
- `contact()` : Page avec formulaire de contact statique
5. Configuration des URLs
- Définition des URLs dans `monapp/urls.py`
- Inclusion dans les URLs principales (`MonProjet/urls.py`)
6. Création des templates
- `base.html` : Template parent avec menu de navigation
- 3 templates enfants héritant de la structure commune
7. Intégration des fichiers statiques
- Création de `styles.css` avec styles personnalisés
- Ajout d'images dans le dossier statique
- Chargement via `{% load static %}`
8. Tests et validation
- Lancement du serveur avec `python manage.py runserver`
- Navigation entre les pages pour vérifier le fonctionnement
b. Les difficultés rencontrées
 1. Configuration des fichiers statiques
- Les fichiers CSS et images n'étaient pas servis par le serveur de développement
- **Solution** : Ajout de `STATICFILES_DIRS` dans `settings.py`

 2. Affichage des images
- L'image du logo Django ne s'affichait pas malgré un chemin correct
- **Solution** : Vérification de la taille du fichier et des permissions

 3. Gestion de l'environnement macOS
- Compatibilité avec Django sur macOS 12
- **Solution** : Utilisation d'un environnement virtuel Python dédié

 4.Héritage de templates
- Problèmes avec les blocs `{% block %}` mal fermés
- **Solution** : Revue de la structure HTML

 5. Upload sur GitHub
- Authentification refusée avec mot de passe normal
- **Solution** : Utilisation d'un token d'accès personnel GitHub
c. Les fonctionnalités implémentées

### **Fonctionnalités principales**
1. **Environnement Django configuré**
   - Projet `MonProjet` et application `monapp` créés
   - Configuration adaptée à la France

2. **3 vues fonctionnelles avec routage**
   - Page d'accueil (`/`)
   - Page "À propos" (`/a-propos/`)
   - Page "Contact" (`/contact/`)

3. **Héritage de templates**
   - Template de base `base.html` avec menu de navigation
   - 3 templates enfants héritant de la structure

4. **Fichiers statiques intégrés**
   - CSS personnalisé (`styles.css`)
   - Images dans le dossier statique

Pages disponibles
- **Accueil** : `/` - Page principale
- **À propos** : `/a-propos/` - Informations sur le projet
- **Contact** : `/contact/` - Formulaire et coordonnées
