// Import the Liquid Crystal library
#include <LiquidCrystal.h>
//Initialise the LCD with the arduino. LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // Switch on the LCD screen
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  // Print these words to my LCD screen
  lcd.print("Welcome");
  lcd.setCursor(0,1);
  lcd.print("Project");
}

void loop() {
  // put your main code here, to run repeatedly:

}
