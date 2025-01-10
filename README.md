# Modélisation et Optimisation du Modèle Lotka-Volterra

Ce projet implémente une simulation et une optimisation du modèle Lotka-Volterra, un modèle classique en écologie mathématique pour décrire les dynamiques de populations proies-prédateurs. 

---

## 📖 Description

Le modèle Lotka-Volterra est un système d'équations différentielles couplées utilisé pour modéliser les interactions entre deux populations : des proies (lapins) et des prédateurs (renards). Ces interactions sont décrites par les équations suivantes :

- \( \frac{dx}{dt} = \alpha x - \beta x y \)
- \( \frac{dy}{dt} = \delta x y - \gamma y \)

où :
- \( x \) : Population de proies (lapins),
- \( y \) : Population de prédateurs (renards),
- \( \alpha, \beta, \gamma, \delta \) : Constantes du modèle.

### Objectifs du Projet
1. Simuler les populations de lapins et de renards en fonction du temps.
2. Ajuster les paramètres du modèle pour correspondre à des données réelles.
3. Visualiser les résultats de manière claire et intuitive.

---

## 🗂️ Structure du Projet

- **`main.py`** : Script principal contenant la simulation, l'optimisation et les visualisations.
- **`visualization.py`** : Fonctions pour générer des graphiques comparant les données simulées et réelles.
- **`optimization.py`** : Algorithmes pour ajuster les paramètres du modèle en minimisant l'erreur entre les données simulées et réelles.
- **`populations_lapins_renards.csv`** : Données réelles des populations de lapins et renards (provenant d'une source ou simulées).
- **`README.md`** : Documentation détaillée du projet.

---

## 🚀 Installation et Exécution

### Pré-requis
- Python 3.9 ou version ultérieure
- Les bibliothèques mentionnées dans `requirements.txt`

## 🛠️ Fonctionnalités
Simulation des Populations

Utilise l'algorithme d'Euler pour résoudre les équations différentielles du modèle Lotka-Volterra.
Les résultats sont ajustés pour correspondre à l'échelle des données réelles.
Optimisation des Paramètres

Implémente une méthode de recherche par grilles pour minimiser l'erreur quadratique moyenne (MSE) entre les populations simulées et les données réelles.
Visualisation Intuitive

Génère des graphiques comparant les populations réelles et simulées.
Présente les erreurs initiales et finales (MSE) pour évaluer l'amélioration.

## 📝 Exemple de Résultats
Un graphique typique montre l'évolution des populations de lapins et de renards :

Courbes rouges : Données réelles des lapins.
Courbes bleues : Données réelles des renards.
Lignes rouges : Populations simulées de lapins.
Lignes bleues : Populations simulées de renards.
Voici un exemple de graphique généré :


## 📊 Données d'Entrée
Les données réelles doivent être stockées dans un fichier CSV sous le format suivant :

days	lapin	renard
1	3200	1200
2	3300	1150
...	...	...
days : Temps (en jours),
lapin : Population des lapins,
renard : Population des renards.

## ⚙️ Paramètres Modifiables
Vous pouvez ajuster les paramètres suivants dans main.py :

Population initiale des lapins et renards.
Les constantes du modèle 
𝛼
,
𝛽
,
𝛾
,
𝛿
α,β,γ,δ.
La méthode et les critères d'optimisation.

## 📬 Contact
Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue sur GitHub
