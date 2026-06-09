#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

String apiKey = "YOUR_THINGSPEAK_KEY";

#define TRIG 5
#define ECHO 18

#define BUZZER 23

#define GREEN_LED 25
#define YELLOW_LED 26
#define RED_LED 27

float binHeight = 40.0;

void setup() {

Serial.begin(115200);

pinMode(TRIG, OUTPUT);
pinMode(ECHO, INPUT);

pinMode(BUZZER, OUTPUT);

pinMode(GREEN_LED, OUTPUT);
pinMode(YELLOW_LED, OUTPUT);
pinMode(RED_LED, OUTPUT);

WiFi.begin(ssid,password);

while(WiFi.status()!=WL_CONNECTED){
delay(1000);
}

}

float getDistance(){

digitalWrite(TRIG,LOW);
delayMicroseconds(2);

digitalWrite(TRIG,HIGH);
delayMicroseconds(10);
digitalWrite(TRIG,LOW);

long duration = pulseIn(ECHO,HIGH);

float distance = duration * 0.034 / 2;

return distance;
}

void loop(){

float distance = getDistance();

float fillPercent =
((binHeight-distance)/binHeight)*100;

if(fillPercent<0)
fillPercent=0;

if(fillPercent>100)
fillPercent=100;

String status;

digitalWrite(GREEN_LED,LOW);
digitalWrite(YELLOW_LED,LOW);
digitalWrite(RED_LED,LOW);

if(fillPercent<40){

status="EMPTY";
digitalWrite(GREEN_LED,HIGH);

}
else if(fillPercent<80){

status="HALF FULL";
digitalWrite(YELLOW_LED,HIGH);

}
else{

status="FULL";

digitalWrite(RED_LED,HIGH);

tone(BUZZER,1000,1000);

}

Serial.println(fillPercent);

if(WiFi.status()==WL_CONNECTED){

HTTPClient http;

String url =
"http://api.thingspeak.com/update?api_key="
+ apiKey +
"&field1=" + String(distance) +
"&field2=" + String(fillPercent);

http.begin(url);
http.GET();
http.end();

}

delay(15000);

}