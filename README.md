  IA & Cybersécurité – Détection d’anomalies réseau (PFE 2025)

Ce dépôt contient une preuve de concept (PoC) démontrant comment l’intelligence artificielle peut être utilisée dans le domaine de la **cybersécurité industrielle**, en détectant automatiquement des comportements anormaux dans des journaux réseau simulés.

  Ce projet s'inscrit dans le cadre de mon **projet de fin d'études (PFE)** et répond aux exigences de la compétence **C11** du référentiel RNCP 34237 :
> *Compréhension d’un projet en IA dans le domaine de la cybersécurité (ex : détection de menaces)*

---

  Objectif

L’objectif est de détecter automatiquement :
- des sessions réseau suspectes (exfiltration, activité soudaine, capteur compromis)
- sans supervision (pas besoin de données étiquetées)

Nous utilisons un jeu de données simulé avec :
- `bytes_sent` : nombre d’octets envoyés
- `duration` : durée de session
- 5 sessions anormales injectées

---

  Technologies utilisées

- Python 3.10+
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [matplotlib](https://matplotlib.org/)
- Isolation Forest

---

  Arborescence
│
├── README.md
├── requirements.txt
│
├── data/
│ └── simulated_network_logs.csv
│
├── images/
│ └── anomaly_detection_plot.png
│
└── src/
└── detect_anomalies.py

yaml
Copier
Modifier
 
  Lancer le projet

Active ton environnement Python et installe les dépendances :

 
pip install -r requirements.txt
Exécute le script :
python src/detect_anomalies.py
 Le graphe anomaly_detection_plot.png sera généré dans le dossier images/.
