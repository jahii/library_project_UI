int A = 0;
void setup() {
  
  Serial.begin(9600);

}

void loop() {
  
  Serial.println(A++);
  delay(1000);
  if(A==10){
    A=0;
  }
}
