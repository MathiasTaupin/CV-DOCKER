#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// On définit les pins comme tu as fait (très propre !)
#define buzzer 11
#define ledR 6
#define ledBleu 7
#define ledV 8
#define ledO 9
#define ledBlanc 10
#define btn 12
#define moteur 3
#define termistance A0

// Initialisation de l'écran (Adresse 0x27, 16 colonnes, 2 lignes)
LiquidCrystal_I2C lcd(0x27, 16, 2);

int page = 0; // Pour changer l'affichage avec le bouton

void setup() {
  // On configure les LEDs en sortie
  pinMode(ledR, OUTPUT);
  pinMode(ledBleu, OUTPUT);
  pinMode(ledV, OUTPUT);
  pinMode(ledO, OUTPUT);
  pinMode(ledBlanc, OUTPUT);

  //moteur sorti
  pinMode(moteur, OUTPUT);
  
  // Le bouton et le buzzer
  pinMode(btn, INPUT);
  pinMode(buzzer, OUTPUT);

  // Initialisation LCD
  lcd.init();
  lcd.backlight();
  
  // Petit son de démarrage cool 🎶
  tone(buzzer, 1000, 200);
  lcd.setCursor(0, 0);
  lcd.print("Salut Mathias !");
  digitalWrite(moteur, HIGH);
  digitalWrite(ledBlanc, HIGH);
  delay(2000);
  digitalWrite(moteur, LOW);
  lcd.clear();
}

void loop() {
  // 1. Lecture du bouton pour changer de page
  if (digitalRead(btn) == HIGH) {
    page++;
    if (page > 1) page = 0;
    
    tone(buzzer, 1500, 100); // Bip de confirmation
    lcd.clear();
    delay(300); // Anti-rebond
  }

  // 2. Logique d'affichage
  if (page == 0) {
    int valeurBrute = analogRead(termistance);
    // On affiche la valeur brute pour l'instant
    lcd.setCursor(0, 0);
    lcd.print("Temp brute:");
    lcd.setCursor(0, 1);
    lcd.print(valeurBrute);
  } 
  else {
    lcd.setCursor(0, 0);
    lcd.print("Mode: LEDs");
  }
}


void à{
  digitalWrite(ledBlanc, HIGH);
  digitalWrite(ledO, HIGH);
  digitalWrite(ledV, HIGH);
  digitalWrite(ledBleu, HIGH);
  digitalWrite(ledR, HIGH);
  delay(500);
  digitalWrite(ledBlanc, LOW);
  digitalWrite(ledO, LOW);
  digitalWrite(ledV, LOW);
  digitalWrite(ledBleu, LOW);
  digitalWrite(ledR, LOW);
}







