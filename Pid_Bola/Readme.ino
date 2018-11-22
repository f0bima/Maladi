/*
 * 0       1       2
 * lpwm4   rpwm3   rpwm7
 * rpwm5   lpwm2   lpwm6
*/
/*0 ----- 1
 * \     /
 *  \   /
 *   \ /
 *    2
*/

/*CW 0
  analogWrite(LPWM[0], 100);
  analogWrite(RPWM[0], 0);
  CW 1
  analogWrite(LPWM[1], 100);
  analogWrite(RPWM[1], 0);
  CW 2
  analogWrite(LPWM[2], 100);
  analogWrite(RPWM[2], 0);
*/  
