#define rele 6 
#define botao2 3
#define buzzer 3

void buzzer_on(){
  digitalWrite(buzzer, HIGH);
}
void buzzer_off(){
  digitalWrite(buzzer, LOW);
}

void porta_aberta(){
  buzzer_on();
  digitalWrite(rele,LOW);
  delay(2000);
}

void porta_fechada(){
  digitalWrite(rele,HIGH);
  buzzer_off();

}

void setup(){
  Serial.begin(9600);
  pinMode(rele,OUTPUT);
  pinMode(botao2,INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);      

}

void loop(){
  int estado_botao2 = digitalRead(botao2); 
  Serial.println(estado_botao2);
  if (estado_botao2 == LOW) {
    porta_fechada();

  }
  else if (estado_botao2 == HIGH){
    porta_aberta();

  }
}
