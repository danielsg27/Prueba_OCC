int ledRojo = 6;
int ledVerde = 9;
int ledAzul = 5;
int dtm=800 ; // 400-420 480 para xd 400 para hola 360 //400 -- 600 franjas mas grandes
int dtm2=275; // 
int dt=2;   //10 o 5


String inString = "";
String strBytes = "";

void setup() {
  Serial.begin(9600);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAzul, OUTPUT);
}

void loop() {  
  readSerialPort();

  //Convertir a byte
  byte plain[inString.length()];
  inString.getBytes(plain, inString.length());
  header();
  for (int i = 0; i < inString.length(); i++){    
    
    Serial.println(plain[i], BIN);    
    on();   
    delay(dt);
    for (int j = 7; j >=0 ; j--){
      bool n= bitRead(plain[i], j) ;
      //Serial.println(n);
      MANCHESTER(n);
      /*if(bitRead(plain[i], j)){
        //Serial.print("1");
        on();on();
      }else{
        //Serial.print("0");
        off();off();
      }
      delayMicroseconds(dtm);*/
    }    
  }
  
  
  
//  for(int i=0; i<16; i++){
//    //digitalWrite(led,LOW);//for bit 0
//    if(i%2==0){
//      on();on();  
//    }else{
//      off();off();
//    }    
//    delayMicroseconds(dtm);
//    //digitalWrite(led,HIGH);
//    
//  } 
}

void off(){
  digitalWrite(ledRojo,0);
  digitalWrite(ledVerde,0);
  digitalWrite(ledAzul,0);
}

void color_header(){
  digitalWrite(ledRojo,255);
  digitalWrite(ledVerde,0);
  digitalWrite(ledAzul,0);
}

void on(){
  digitalWrite(ledRojo,255);
  digitalWrite(ledVerde,255);
  digitalWrite(ledAzul,255);
}

void header(){
for(int i=0; i<2; i++){     ////cabecera 
  //digitalWrite(led,LOW);//for bit 0
  color_header(); //color en inicio
  //off();
  delayMicroseconds(dtm2);
  //digitalWrite(led,HIGH);
  color_header(); //color en inicio
  //off();
  delayMicroseconds(dtm2);
  }
}

void readSerialPort() {
  
  if (Serial.available()) {
    inString = "";
    //Serial.println(">:c");
    delay(10);
    while(Serial.available() > 0) {
      inString += (char)Serial.read();     
    } 
    //inString = inString + "\n";   
    Serial.flush();
    Serial.println(inString);    
  }
}


void MANCHESTER(boolean n){
  if(n==1){
    off();
    delayMicroseconds(dtm);
    on();
    delayMicroseconds(dtm);
    }
  else{
    on();
    delayMicroseconds(dtm);
    off();
    delayMicroseconds(dtm);
    }
}
