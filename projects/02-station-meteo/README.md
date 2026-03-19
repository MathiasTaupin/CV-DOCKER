# Station Météo Arduino

## Description

Un projet de station météo développée avec Arduino, utilisant des capteurs pour mesurer la température, l'humidité et la pression atmosphérique. Les données sont affichées sur un écran LCD et transmises via le port série.

## Fonctionnalités

✓ Mesure de température via thermistance NTC  
✓ Commande de ventilateur automatique (seuil réglable)  
✓ Affichage sur écran LCD I2C 16x2  
✓ Transmission des données via port série  
✓ Mise à jour toutes les 5 secondes  

## Matériel Nécessaire

- Carte Arduino Uno (ou compatible)
- Capteur DHT11 (température/humidité)
- Capteur BMP180 (pression atmosphérique)
- Écran LCD I2C 16x2
- Breadboard et câbles de connexion
- Alimentation 5V

## Bibliothèques Arduino Requises

- DHT (pour le capteur DHT11)
- LiquidCrystal_I2C (pour l'écran LCD)
- Adafruit_BMP085 (pour le capteur BMP180)

## Installation

1. Téléchargez le fichier `station_meteo.ino`
2. Ouvrez-le dans l'IDE Arduino
3. Installez les bibliothèques nécessaires via le gestionnaire de bibliothèques
4. Connectez les composants selon le schéma (non fourni ici)
5. Téléversez le code sur votre Arduino

## Utilisation

Une fois téléversé, la station affiche :
- Température en °C
- Humidité en %
- Pression en hPa (via port série)

Les données sont mises à jour automatiquement toutes les 5 secondes.

## Structure du Projet

```
02-station-meteo/
├── index.html              (Page de présentation)
├── css/
│   └── styles.css          (Feuilles de style)
├── js/
│   └── script.js           (Code JavaScript minimal)
├── assets/
│   └── station_meteo.ino   (Code Arduino)
└── README.md              (Ce fichier)
```

---

**Créé par :** Mathias TAUPIN  
**Date :** 2026