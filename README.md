# SenZeRPG
SenZeRPG is not only an annoying thing to type, but it's also a ZPG (Zero Player Game) Roleplaying Game.

My goal is to make a somewhat flexible framework for a ZPG that can be output on a Sense HAT for Raspberry Pi.

## FAQ
Q: Why would you make a zero player game for an 8x8 LED display?
A: You'll have to be more specific. I feel like there's 3 questions there.

Q: Okay, why would you want a game that plays itself?
A: Ah, good question! well, I had never heard of a ZPG when Screensavers were a bigger thing. Does anyone use a screensaver anymore? Are they even necessary? It makes me sad ZPGs didn't co-exist more with Screensavers. The closest I remember is Win95 Maze game that always turns left. But come on... what if it was a maze where more interesting things happened?

Q: Why would you make it for an 8x8 LED screen? Why not make it for a real computer?
A: The goal is to make it compatible with an 8x8 LED screen. The secondary goal is to abstract the data of the game from the display. So one could technically create a display adapter to put out larger sprites to a web browser, or SDL, or Unity, or... you get the idea.

Q: Wait, you're that guy who loves to start things but not finish them.
A: And?

## Structure
Let's define what this is. It's a single character walking through some kind of landscape. They will perform different actions according to some rudimentary AI (state machine, likely). The character can also equip items to "help" them along the way. Not sure what form that will take, but my initial thought is just a different scene to play if you have the item vs. not.
Example: wall.gif would have a wall-hasLadder.gif, when an event happens, check items, then check for a filename with that item. The person, on the other hand, that might be tricky with since the character would be dynamic...

I would LIKE to also utilize data from the Sense HAT to control the environment stuff, as well as the date for seasonal "events" :eyeroll:..

Each folder would take a config file and gifs to play (or maybe sprite sheets?)
- <root>
 - core.config
 - core.py
 - Event.py - Class
 - Action.py - Class
 - Item.py - Class
- adapters
 - BaseDisplay.py - Class
 - SenseyGif.py - Class
 - SenseyPng.py - Class
 - SenseHAT.py - Class
- events folder
 - <eventName.gif>
 - events.config
- actions folder
 - <actionName.gif>
 - <eventName>-has<itemName.gif>
 - actions.config
- items folder
 - <itemName.gif>
 - items.config inside
- scenery
 - scenery.config inside
