int ledRojo = 6;
int ledVerde = 9;
int ledAzul = 5; 
int dtm=250 ; //200-400 para tomar fotos en la RPI camara hasta 1m
int dtm2=275; //Delay para el inicio del mensaje
int dt=1;   //Delay para cada caracter


String inString = "";
//String strBytes = "";

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
  //Serial.println(inString.length());
  header();
  for (int i = 0; i < inString.length(); i++){    
    
    Serial.println(i);    
    on();   
    //delay(dt);
    for (int k = 1; k <=2 ; k++){  //repetir 2 veces cada caracter
      for (int j = 7; j >=0 ; j--){
        bool n= bitRead(plain[i], j) ;
        //Serial.println(n);
        MANCHESTER(n);
      }
         
    }
  }  
}

void off(){
  digitalWrite(ledRojo,0);
  digitalWrite(ledVerde,0);
  digitalWrite(ledAzul,0);
}

void color_header(){
  digitalWrite(ledRojo,255);
  digitalWrite(ledVerde,255);
  digitalWrite(ledAzul,255);
}

void on(){
  digitalWrite(ledRojo,255);
  digitalWrite(ledVerde,255);
  digitalWrite(ledAzul,255);
}

void header(){
for(int i=0; i<2; i++){     ////cabecera 
  color_header(); //color en inicio
  //off();
  delayMicroseconds(dtm2);
  color_header(); //color en inicio
  //off();
  delayMicroseconds(dtm2);
  }
}

void readSerialPort() {
  
  if (Serial.available()) {
    inString = "";
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
