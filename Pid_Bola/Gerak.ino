void pid(float kecepatan){
  float rpwm = constrain(base+a.toFloat(), 0.0, 200.0);
  float lpwm = constrain(base-a.toFloat(), 0.0, 200.0);
  //CCW 0
  analogWrite(LPWM[0], 0);
  analogWrite(RPWM[0], rpwm);
  //CW 1
  analogWrite(LPWM[1], lpwm);
  analogWrite(RPWM[1], 0);         
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Kiri");   
  lcd.setCursor(5,0);
  lcd.print(rpwm);
  lcd.setCursor(0,1);
  lcd.print("Kanan"); 
  lcd.setCursor(5,1);
  lcd.print(lpwm);
  //delay(100);
}

void maju(){
  //CCW 1
  analogWrite(LPWM[0], 0);
  analogWrite(RPWM[0], 100);
  //CW 2
  analogWrite(LPWM[1], 100);
  analogWrite(RPWM[1], 0);  
}

void muter(){
  if (last_degree<0){
    for(int i=0; i<3; i++){
      analogWrite(LPWM[i], 100);
      analogWrite(RPWM[i], 0);  
    }    
  }
  else{
    for(int i=0; i<3; i++){
      analogWrite(LPWM[i], 0);
      analogWrite(RPWM[i], 100);  
    }
  }
}
