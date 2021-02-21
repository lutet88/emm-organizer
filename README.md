
# emm-organizer
brought to you by the end my missouri (emm) hackers
![enter image description here](https://media.giphy.com/media/YuRF2eB0Q1SsGYem9B/source.gif)
---------------
## event
**KU Hackfest** - [Link](kuhackfest.com)

this is literally our first hackathon. we planned our time really poorly and couldn't finish everything we wanted to.

## abstract
Do you have a small parts organizer? If you do, you know how much of a pain it is to know what you have, don't have, keep track of what's in what drawer, and do any reasonable amount of management in organization. The "Smart" Small Parts Organizer provides an integrated solution to all those problems: through a touchscreen console on top of the organizer, it's able to keep track of any parts you deposit, withdraw, or otherwise, and sync it with a SQL database where you can view its supposed contents from the web. With integrated LED instructions assisting the user in finding parts, knowing how many 470uF Electrolytic Capacitors you have is a breeze; in the click of a few buttons you can find out the name, quantity, user color, and project that these items belong to, without having to dig through cabinets to find it. At least this is what we aimed to accomplish.

## hardware
![the organizer](https://i.imgur.com/ycVpBrz.jpg)
We used a 20-tray organizer we found at Sim Lim Tower for S$13.50. 
Everything else:
- Raspberry Pi 4 (S$60ish)
- 4.3'' HDMI TFT (S$65, which is a total scam imo)
- 140 NeoPixel Strips (we totally ran out halfway lol, S$35ish)
- Adafruit ItsyBitsy M4 (S$24)
- Some old soldered breadboards (S$5)
- 20 TRS jacks and connectors (S$28, also a total scam)
- microHDMI to HDMI adapter (S$2 DAISO)
- some cables

Total cost: around S$220

![back of the organizer](https://i.imgur.com/IhR1F43.jpg)
We basically drilled 6mm holes through the breadboards, put the jack through, and soldered it to the back. Sometimes the pads tore off but it wasn't a huge issue (except one particular unit). Everything is connected at the back to an ItsyBitsy M4 (which conveniently has 20 proper GPIO pins). Power is through USB, which might be a problem if you draw too much power, but we never did.

## software

### code
`main.py` - main driver script for the application. acts as an interface and executable Qt application, and should really be separated into separate scripts

`database.py` - loads and dumps json into a `Database` object. used by main.py extensively

`test44.py` - test for an unused feature (we were probably going to use it to withdraw/deposit)

### hardware code
`rgbController/rgbController.ino` - MCU code through Arduino and Adafruit's nice board definitions. provides a 6-byte interface for controlling LEDs in a variety of ways

`RGBController.py`- confusing name, I know. provides the `RGBController` object that allows asynchronous thread-safe interfacing with `rgbController.ino`

`PinMapper.py` - provides the framework for mapping pins to actual values easily for the `RGBController`

`pinmaps.py` - literally just our pinmaps. don't use this.

## links
[devfolio project](https://devfolio.co/submissions/smart-small-parts-organizer-2983)

[imgur album](https://imgur.com/a/nXH9ZRP)

[project log](https://bit.ly/2ZxivB6)

[product demo](https://www.youtube.com/watch?v=CQ3L8HZ4Y3U)

### members
Jefferson Zhang ([lutet88](https://github.com/lutet88))

Liam Kelly ([Antarctic-Petrel](https://github.com/Antarctic-Petrel), [fillnye](https://github.com/fillnye))

Diren Gomez ([D3lta-m3](https://github.com/D3lta-m3))

Wilson Hou (no GitHub, he committed through Antarctic Petrel)


