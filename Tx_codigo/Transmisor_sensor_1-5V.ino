int ledRojo = 6;
int ledVerde = 9;
int ledAzul = 5; 
int dtm=200 ; //200-400 para tomar fotos en la RPI camara hasta 1m
int dtm2=250; //Delay para el inicio del mensaje
int dt=400;   //Delay para cada caracter
int dt1=500;
int cont=0; 

int vOut,vOutDec;
float vRead = A1;
float analogVal;
String s1 = "V ";
String messageV;
//long ini;



String inString = "";
//String strBytes = "";

void setup() {
  Serial.begin(9600);
  pinMode(ledRojo, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAzul, OUTPUT);
  pinMode(vRead, INPUT);
  //analogVal = analogRead(vRead);
  //vOut = (5.*analogVal)/1023.;
  //vOut = (500*analogVal)/1023;
  //vOutDec = (500.*analogVal)/1023.;
  //vOutDec %= 100;
  //messageV = vOut + s1;;
  //ini = millis();
}

void loop() {
  
  //Serial.print(ini + " ");
  //Serial.print(millis() + " ");
  //if ((millis()-ini)>30000){
  analogVal = analogRead(vRead);
  vOut = (5.*analogVal)/1023.;
  //vOut = (500*analogVal)/1023;
  //vOutDec = (500.*analogVal)/1023.;
  //vOutDec %= 100;
  messageV = vOut + s1;
  //ini = millis();
  //}
  //Serial.println(vOut);
  Serial.println(messageV);
  //Serial.println(messageV.length());
  //delay(dt);
  //readSerialPort();
  

  //Convertir a byte
  byte plain[messageV.length()];
  messageV.getBytes(plain, messageV.length());
  header();
  cont = messageV.length()-1;
  
  for (int i = 0; i < messageV.length(); i++){    
    
    //Serial.println(i);    
    on();   
    //delay(dt);
    delayMicroseconds(dt);
    for (int k = 1; k <= 2*cont; k++){  //repetir caracteres
      delayMicroseconds(dt1);
      //Serial.println(i);    
      for (int j = 7; j >=0 ; j--){
        bool n= bitRead(plain[i], j) ;
        //Serial.println(i);
        //Serial.println(n);
        MANCHESTER(n);
      }
         
    }
    cont-=1;
    //Serial.println(cont);
    //delay(100);
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

/*void readSerialPort() {
  
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
}*/


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
