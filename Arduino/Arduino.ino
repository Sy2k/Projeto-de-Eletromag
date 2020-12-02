#define botao 7 
#define buzzer 3

void buzzer_on(){
  digitalWrite(buzzer, HIGH);
}
void buzzer_off(){
  digitalWrite(buzzer, LOW);
}

void setup() {
  pinMode(botao, INPUT_PULLUP); 
  pinMode(buzzer, OUTPUT);      
}

void loop() {
  int estado_botao = digitalRead(botao); 
  if (estado_botao == LOW) {
    buzzer_on();
  }
  else if (estado_botao == HIGH) {
    buzzer_off();
  }
}
