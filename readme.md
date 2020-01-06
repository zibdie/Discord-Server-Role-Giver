# Discord Role Giver Bot

*Designed primarely for the NJIT YWCC Discord server but can be adopted to any server*

### Purpose
This script acts both as a web server & discord bot. You send a JSON request (primarely though a Google Script form) and it gives the role you wish the user to recieve

### Requirements
* Python 3 (tested on Python 3.7.4 only)
* [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
* [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)

You can install all necessary libraries like this:
```
pip install aiohttp && pip install cchardet && pip install aiodns && pip install -U discord.py
```
**Tip:**
* If your installing on a Linux system, you may need to type 'pip3' instead of 'pip'. Please make sure Python3 & pip3 is installed with it
* In case of folder permissions, run *pip install* as sudo
* Make sure the port you choose in the script is open. By default, the server uses 8080 but this can be changed.

## How To Set Up - Discord Bot

### Getting required tokens & ID's
1. First, visit the Discord Developers Application located [here](https://discordapp.com/developers/applications/)
2. Follow this tutorial [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) to the part where you get the token (*Make sure your bot can Manage roles, depending on the heiarchy of the server, it may be best to just give your bot administrator permissions*)
3. **Add your Guild ID:** You can find your Guild/Server ID by opening Discord in your browser and finding it in the URL (*The one with the XXXXX in the picture below*)

![](https://i.imgur.com/iUQVRPU.jpg)

Now paste it to the script where it says 'GUILD ID'

4.  **Add your Verify ID ID:** Get the ID of the Verification text channel and paste it in the 'VERIFY_ID' spot:

![](https://i.imgur.com/EzYbnta.jpg)

5.  **Add the name of the 'Admin' role of your server:** Simply type out what 'Admin' role is called in your server in the 'adminRoleName'

![](https://i.imgur.com/LMg5jX5.jpg)

6.  **Add your Verify ID ID:** Finally, type the role you wish to give to your users in the 'verifiedRoleName'. In this server, its called *Verified*

![](https://i.imgur.com/Z0spY19.jpg)

## How To Set Up - Google Forms

1. Go to your Google Forms that you wish to direct your users and press the 'Script Editor' button in the 'Settings' tab

![](https://i.imgur.com/OEflzrE.jpg)

2. When the 'Script Editor' opens, paste the code in the .gs file and replace **POST_URL** with the link to the Discord Bot server (*remember to test in Postman to be sure you can see it!*). Finally, click *Edit* -> *Current project's triggers*

![](https://i.imgur.com/UWxvg3s.jpg)

3. Add a trigger to your script and make sure its set to go off 'On Form Submit':

![](https://i.imgur.com/f7gNeeC.jpg)

## Now when your users submit their Discord name, they will automatically get the role!