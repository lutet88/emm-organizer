/*
 * rgbController.ino
 * github.com/lutet88
 * 
 * Short script that uses 6-byte packets (header=0xCD) and some basic
 * instructions to control 20 neopixel strips each with 7 neopixels separately.
 * Should be very easy to modify for your own use. 
 * 
 * Packet info:
 * 0xCD (header)
 * 0x00-0x13 (strip, up to 20), or 0x14 (clear all), or 0x15 (show all)
 * 0x00-0x06 (pixel, up to 7), or 0xAA (all)
 * 0x00-0xFF (red value)
 * 0x00-0xFF (blue value)
 * 0x00-0xFF (green value)
 */

#include <Adafruit_NeoPixel.h>

// global defines
#define STRIPCOUNT 20
#define RGBPROF NEO_GRB+NEO_KHZ800
#define foreachstrip for(int i=0;i<STRIPCOUNT;i++)

// define if you want feedback with each command (might slow things down)
// #define DEBUG

// define if you want the MCU to wait for serial on each reboot
#define WAITSERIAL

// yeah, the strip array. with 20 this is the most memory-safe way to do it
Adafruit_NeoPixel strips[] = {
  Adafruit_NeoPixel(7, A2, RGBPROF),
  Adafruit_NeoPixel(7, A3, RGBPROF),
  Adafruit_NeoPixel(7, A4, RGBPROF),
  Adafruit_NeoPixel(7, A5, RGBPROF),
  Adafruit_NeoPixel(7, SCK, RGBPROF),
  Adafruit_NeoPixel(7, MOSI, RGBPROF),
  Adafruit_NeoPixel(7, MISO, RGBPROF),
  Adafruit_NeoPixel(7, 2, RGBPROF),
  Adafruit_NeoPixel(7, 3, RGBPROF),
  Adafruit_NeoPixel(7, 4, RGBPROF),
  Adafruit_NeoPixel(7, 0, RGBPROF),
  Adafruit_NeoPixel(7, 1, RGBPROF),
  Adafruit_NeoPixel(7, SDA, RGBPROF),
  Adafruit_NeoPixel(7, SCL, RGBPROF),
  Adafruit_NeoPixel(7, 7, RGBPROF),
  Adafruit_NeoPixel(7, 9, RGBPROF),
  Adafruit_NeoPixel(7, 10, RGBPROF),
  Adafruit_NeoPixel(7, 11, RGBPROF),
  Adafruit_NeoPixel(7, 12, RGBPROF),
  Adafruit_NeoPixel(7, 13, RGBPROF)
};

void setup() {
  // init Serial
  Serial.begin(115200);
  #ifdef WAITSERIAL
    while(!Serial){
      delay(10);
    }
  #endif
  // setup strips
  foreachstrip{
    strips[i].begin();
    strips[i].clear();
    strips[i].show();
  }
  #ifdef DEBUG
    // flash MOSI (top left) at strips[5] to indicate ready
    strips[5].setPixelColor(3, strips[5].Color(0, 40, 40));
    strips[5].show();
    delay(400);
    strips[5].setPixelColor(3, strips[5].Color(0, 0, 0));
    strips[5].show();
  #endif

  Serial.println("Ready for commands.");
}

void loop() {
  
  // wait until 6 bytes available
  if (Serial.available() >= 6){
    
    byte header = Serial.read();
    if (header == 0xCD){
      
      #ifdef DEBUG
        Serial.println("Valid command header received.");
      #endif
      
      // get values
      byte strip = Serial.read();
      byte pixel = Serial.read();
      byte r = Serial.read();
      byte g = Serial.read();
      byte b = Serial.read();
    
      // strip: 0x00 - 0x13 reference strips[]. 0x14 clears all. 0x15 shows all. handle exceptions:
      if (strip < 0 || strip > 0x15){
        Serial.print("Invalid strip #: ");
        Serial.println(strip);
        return;
      } else if (strip == 0x15){ // show all (ignores pixel, r, g, b)
        foreachstrip{
          strips[i].show();
        }
        Serial.println("All strips shown");
        return;
      } else if (strip == 0x14){ // clear and show all (ignores pixel, r, g, b)
        foreachstrip{
          strips[i].clear();
          strips[i].show();
        }
        Serial.println("All strips cleared");
        return;
      }
    
      // pixel: 0x00-0x06 reference pixels. 0xAA references all. handle exceptions first:
      if (pixel < 0 || (pixel > 0x06 && pixel != 0xAA)){
        Serial.print("Invalid pixel #: ");
        Serial.println(pixel);
        return;
      }
    
      // actually set the LEDs...
      if (pixel == 0xAA) {
        // reference all LEDs in strip
        strips[strip].fill(strips[strip].Color(r, g, b));
        strips[strip].show(); // you may not want this, you might just want to send a 0x15
      } else {
        // reference pixel
        strips[strip].setPixelColor(pixel, strips[strip].Color(r, g, b));
      }
    
      #ifdef DEBUG
        Serial.print("strip: ");
        Serial.print((int) strip);
        Serial.print(", pixel: ");
        Serial.print((int) pixel);
        Serial.print(" set to ");
        Serial.print(r);
        Serial.print(", ");
        Serial.print(g);
        Serial.print(", ");
        Serial.print(b);
        Serial.println();
      #endif
      
    } else if (header == '.'){
      Serial.println("Serial is working!");
    }
  }
}
