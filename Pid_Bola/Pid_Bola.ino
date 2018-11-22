#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
String a;
int LPWM[] = {4, 3, 7};
int RPWM[] = {5, 2, 6};
int base = 100; 
float last_degree;
String baca;

void setup(){
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();  
  for(int i=0;i<3;i++){
    pinMode(LPWM[i], OUTPUT);
    pinMode(RPWM[i], OUTPUT);
  }    
}
 
void loop(){      
  lcd.clear();   
  if(Serial.available()>0){      
      baca = "";
      while(Serial.available()){
        char pyserial = ((byte)Serial.read());
        baca += pyserial;            
        delay(5);
      }
    a = baca;
    /*String perintah = a.substring(0,1);
    String nilai = a.substring(1);      */        
    if(a == "99999"){      
      lcd.print("Muter");
      muter();
    }
    else{
      last_degree = a.toFloat();
      lcd.print(a.toFloat());
      //pid(a.toFloat());
    }    
  }  
}
