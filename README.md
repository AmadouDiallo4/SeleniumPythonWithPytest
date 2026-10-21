# SeleniumPythonWithPytest — Automatisation UI et stratégie QA transverse

> Un socle Python, Selenium et Pytest pour automatiser la non-régression, avec une trajectoire vers une assurance qualité couvrant API, données et parcours utilisateurs.

## Vision et objectifs

L’automatisation ne consiste pas seulement à exécuter des scénarios : elle doit fournir une information fiable, rapide et exploitable sur les risques d’une livraison.

Ce projet illustre une première organisation de tests UI autour du **Page Object Model**, appliquée à l’interface d’administration de démonstration nopCommerce.

Sa trajectoire vise trois objectifs :

- **Sécuriser les parcours critiques** en priorisant les risques métier.
- **Accélérer le feedback** grâce à des tests répartis au bon niveau.
- **Faciliter les décisions de livraison** avec des résultats traçables et des anomalies qualifiées.

La stratégie décrite ci-dessous distingue explicitement les capacités existantes des évolutions proposées.

## État actuel du projet

| Domaine | Présent dans le dépôt | Évolution visée |
|---|---|---|
| Automatisation UI | Selenium et Pytest | Élargissement progressif des parcours critiques |
| Architecture | Page Object dédié à la connexion | Composants réutilisables et conventions homogènes |
| Navigateurs | Sélection Chrome ou Firefox | Matrice de compatibilité exécutée en CI |
| Données | Lecture de scénarios depuis Excel | Cas indépendants, validation des données et paramétrage Pytest |
| Configuration | Lecture d’un fichier INI | Configuration par environnement et secrets externalisés |
| Synchronisation | Interactions directes et attente fixe dans le test piloté par données | Attentes explicites fondées sur l’état de l’application |
| Diagnostic | Journalisation, captures sur certains échecs et rapport HTML archivé | Collecte systématique et publication des preuves |
| Tests API et SQL | Non implémentés | Couverture complémentaire des services et de la persistance |
| CI/CD | Aucun workflow identifié dans le dépôt analysé | Pipeline de non-régression et critères de qualité |

Le rapport HTML présent est un exemple historique : il ne constitue pas une preuve de bon fonctionnement de la version actuelle.

## 1. Stratégie QA : une vision End-to-End

### Prioriser selon les risques

La couverture cible est construite à partir :

- de l’impact métier d’une défaillance ;
- de la fréquence d’utilisation ;
- de la criticité des données ;
- de la fréquence des changements ;
- de l’historique des incidents.

Les fonctionnalités critiques bénéficient d’une couverture à plusieurs niveaux, sans reproduire systématiquement les mêmes vérifications dans toutes les couches.

### Répartir les contrôles au bon niveau

| Niveau | Objectif | Exemples de couverture cible |
|---|---|---|
| Tests unitaires et composants | Vérifier rapidement les règles isolées | Validations, transformations et cas limites |
| API et intégration | Contrôler les contrats et échanges entre services | Authentification, autorisations, erreurs et opérations métier |
| SQL et persistance | Vérifier les effets durables des opérations | Intégrité, unicité, relations et absence de doublons |
| UI | Vérifier les parcours réellement accessibles à l’utilisateur | Connexion, navigation et résultat visible d’une action |
| Exploratoire et non fonctionnel | Couvrir les risques moins adaptés aux scripts déterministes | Utilisabilité, accessibilité, performance et sécurité |

**Principe directeur :** privilégier les contrôles rapides et ciblés ; réserver les tests UI aux comportements qui nécessitent réellement un navigateur.

### Exemple de parcours transverse cible

Sur une application et un environnement maîtrisés :

1. Préparer une donnée synthétique par API.
2. Réaliser une action métier dans l’interface.
3. Vérifier le résultat visible par l’utilisateur.
4. Contrôler l’état exposé par l’API.
5. Vérifier en SQL les invariants de persistance pertinents.
6. Nettoyer les données créées.

Cette approche nécessite des API documentées, un accès autorisé à une base de test et une stratégie d’isolation. Ces prérequis ne sont pas fournis par le seul site public de démonstration.

Les contrôles SQL restent ciblés : ils complètent les tests fonctionnels sans coupler toute la suite au schéma interne de la base.

### Périmètre actuel

Les tests existants concernent principalement :

- le titre de la page de connexion ;
- la connexion à l’administration ;
- des combinaisons d’identifiants lues dans Excel, avec résultat attendu.

La couverture actuelle ne représente donc pas encore une validation End-to-End complète du produit.

## 2. Architecture technique du framework

### Séparation des responsabilités

L’organisation repose sur plusieurs responsabilités distinctes :

- **Tests Pytest** : scénarios, orchestration et assertions.
- **Page Objects** : localisation des éléments et interactions avec les pages.
- **Fixtures** : préparation des navigateurs et contexte d’exécution.
- **Utilitaires** : configuration, lecture Excel et journalisation.
- **Artefacts** : rapports, logs et captures d’écran.

Cette séparation permet de limiter l’impact des changements d’interface et de conserver des scénarios lisibles.

### Page Object Model

La classe `LoginPage` encapsule les interactions de connexion et de déconnexion.

La cible architecturale consiste à :

- centraliser les sélecteurs dans les Page Objects ;
- exposer des actions compréhensibles du point de vue métier ;
- conserver les assertions métier dans les tests ;
- mutualiser les composants réellement communs ;
- éviter une abstraction excessive qui rendrait les échecs difficiles à comprendre.

### Données de test découplées

Le projet utilise actuellement Excel et `openpyxl` pour alimenter un scénario de connexion.

Les évolutions prioritaires sont :

- produire un résultat Pytest distinct pour chaque jeu de données ;
- valider les colonnes et les résultats attendus avant exécution ;
- refuser un jeu vide ou mal formé ;
- garantir l’indépendance des cas ;
- utiliser exclusivement des données synthétiques.

Les données fonctionnelles peuvent rester dans Excel si ce format facilite la collaboration avec les équipes métier. Les secrets ne doivent pas y être conservés.

### Synchronisation et fiabilité

Le scénario piloté par données contient actuellement une attente fixe. Les attentes dynamiques constituent donc une amélioration à réaliser, et non une capacité déjà acquise.

La cible est d’attendre des événements observables : élément visible, bouton interactif, changement d’URL ou confirmation métier.

Autres priorités :

- fermeture garantie de chaque session navigateur, même après exception ;
- absence de dépendance à l’ordre des tests ;
- gestion portable des chemins ;
- assertions précises, au-delà du seul titre de page ;
- identification et traitement des tests instables.

Une relance peut aider au diagnostic, mais ne doit jamais masquer un défaut ou transformer artificiellement un échec en succès.

### Reporting exploitable

Le reporting cible doit permettre de comprendre :

- quel scénario a échoué ;
- sur quelle version et quel environnement ;
- avec quelles données non sensibles ;
- à quelle étape ;
- avec quelles preuves.

Les captures, logs et rapports doivent être corrélés à une exécution unique, avec une durée de conservation définie et un accès contrôlé.

## 3. CI/CD et industrialisation des TNR

### Pipeline cible

Aucun pipeline CI/CD n’a été identifié dans le dépôt analysé. L’intégration suivante constitue une proposition d’évolution.

| Déclencheur | Contrôles proposés | Finalité |
|---|---|---|
| Pull request | Vérifications statiques, tests rapides, API ciblées et smoke UI | Détecter rapidement les régressions bloquantes |
| Livraison en environnement de test | Intégration, API, SQL et parcours UI critiques | Vérifier la cohérence du système déployé |
| Exécution planifiée | TNR étendue et compatibilité navigateurs | Détecter les régressions plus larges |
| Après déploiement | Smoke tests non destructifs et autorisés | Vérifier la disponibilité fonctionnelle essentielle |

### Conditions d’une exécution reproductible

Avant industrialisation :

- déclarer et maîtriser les dépendances ;
- standardiser les versions de Python et des navigateurs ;
- rendre l’exécution compatible avec un runner Linux ;
- permettre une exécution navigateur sans interface graphique ;
- injecter la configuration et les secrets de manière sécurisée ;
- préparer des données isolées ;
- publier les rapports même en cas d’échec.

La parallélisation ne doit intervenir qu’une fois l’indépendance des tests et des données démontrée.

### Critères de livraison

Les seuils doivent être convenus avec les équipes produit et développement. Une politique initiale peut retenir :

- aucun échec inexpliqué sur les parcours critiques ;
- aucun défaut bloquant connu dans le périmètre livré ;
- résultats et preuves accessibles ;
- tests instables identifiés, avec responsable et échéance ;
- dérogations documentées et explicitement acceptées.

Un incident d’environnement doit être distingué d’un défaut produit, sans être interprété comme une validation réussie.

### Indicateurs de qualité

Le pilotage ne repose pas uniquement sur le nombre de tests ou leur taux de succès.

Indicateurs utiles :

- couverture des risques critiques ;
- délai de feedback ;
- taux d’instabilité ;
- durée des suites ;
- temps de diagnostic ;
- régressions découvertes après livraison ;
- vieillissement des anomalies et des quarantaines.

Aucun résultat chiffré n’est revendiqué sans mesure reproductible.

## 4. Usage pragmatique de l’IA et des LLMs

L’IA est envisagée comme une assistance au travail QA, pas comme une source autonome de vérité.

### Usages pertinents

- Proposer des cas limites à partir de critères d’acceptation.
- Identifier des variantes négatives ou des combinaisons de données.
- Préparer des ébauches de tests et de Page Objects.
- Aider à analyser des traces Selenium ou des échecs Pytest.
- Regrouper des symptômes similaires pour accélérer le triage.
- Améliorer la lisibilité de la documentation.

### Garde-fous

- Validation humaine des scénarios, assertions et changements générés.
- Vérification des hypothèses par des preuves issues du système.
- Aucun envoi de secrets, données personnelles ou contenus confidentiels vers un service non approuvé.
- Anonymisation des logs et minimisation des données partagées.
- Traitement des logs comme des données non fiables, jamais comme des instructions.
- Aucune décision de livraison fondée uniquement sur une réponse de LLM.

Aucune intégration LLM automatisée n’est actuellement implémentée dans ce dépôt.

## 5. Prise en main et limites actuelles

Le projet nécessite un environnement Python, Selenium, Pytest, `openpyxl` et un navigateur compatible. La génération d’un rapport HTML nécessite également le plugin `pytest-html`.

Avant une exécution :

1. Préparer un environnement Python isolé et des dépendances compatibles.
2. Vérifier la configuration dans
   `/home/runner/work/SeleniumPythonWithPytest/SeleniumPythonWithPytest/SeleniumProjectPOM/Configurations/config.ini`.
3. Contrôler que les données de test sont synthétiques dans
   `/home/runner/work/SeleniumPythonWithPytest/SeleniumPythonWithPytest/SeleniumProjectPOM/TestDatas/LoginData.xlsx`.
4. Utiliser comme répertoire de travail
   `/home/runner/work/SeleniumPythonWithPytest/SeleniumPythonWithPytest/SeleniumProjectPOM`.
5. Lancer les tests avec Pytest en sélectionnant Chrome ou Firefox via l’option `--browser`.

Ces chemins absolus correspondent au clone analysé ; ils doivent être adaptés à l’emplacement du dépôt sur votre machine.

Le dépôt ne fournit pas actuellement de manifeste de dépendances ni de procédure d’installation validée. Certains chemins de logs et de captures utilisent une syntaxe Windows : la portabilité doit être fiabilisée avant de promettre une exécution Linux reproductible.

L’application de démonstration est externe et partagée. Ses changements, sa disponibilité ou son état peuvent affecter les résultats. Elle ne doit pas être utilisée pour des tests de charge, des actions destructives ou des contrôles de sécurité non autorisés.

## 6. Gouvernance et feuille de route

### Priorité 1 — Fiabiliser le socle

- Déclarer les dépendances et documenter une installation reproductible.
- Remplacer les attentes fixes.
- Garantir le nettoyage des navigateurs.
- Isoler les cas pilotés par données.
- Externaliser les secrets.
- Uniformiser les chemins et les preuves d’exécution.

### Priorité 2 — Industrialiser

- Introduire les suites smoke et régression.
- Ajouter une CI avec publication systématique des artefacts.
- Définir les critères de livraison.
- Mettre en place le suivi des tests instables.

### Priorité 3 — Étendre la couverture

- Ajouter les tests API sur un périmètre maîtrisé.
- Introduire les contrôles SQL autorisés.
- Couvrir un parcours métier transverse.
- Élargir la matrice navigateur selon les usages réels.

### Responsabilité collective

La qualité reste une responsabilité partagée :

- le produit clarifie les risques et critères d’acceptation ;
- les développeurs portent la testabilité et les tests de proximité ;
- la QA structure la couverture, les preuves et l’analyse des risques ;
- les équipes plateforme contribuent à la stabilité des environnements.

**La valeur recherchée n’est pas davantage de scripts, mais une confiance mesurable dans chaque livraison.**
