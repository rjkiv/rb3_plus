# Harmonies 

<img src="../readme_assets/harm3.png" width="10%" height="10%" align="left"> Harmony upgrades allow for all applicable pre-RB3 songs to be sang with up to 3 people via the addition of harmony vocal tubes. All harmony files (with the exception of the forbidden harmonies) have been authored by [Rock Band: Harmonies Project (RBHP)](https://github.com/FujiSkunk/rbhp). However, many of these upgrades contained visual bugs such as lyrics displaying twice or vocal tubes being disconnected, so I went ahead and tweaked all of them. Along with being in this repo, these fixed upgrades can also be found built-in to another RB3 project, [Rock Band 3 Deluxe](https://github.com/jnackmclain/rock-band-3-deluxe).

# Installation

## Rock Band 3 Deluxe
If you have RB3DX installed onto your system, then good news - you do not need to take any further steps, as RB3DX has all of my fixed upgrade files built-in. However, if you do not have RB3DX installed, the process to install harmonies is rather involved (particularly if you are on PS3/RPCS3), but it can be done.

## Xbox
In order to install a harmony upgrade for a particular song on Xbox, you will need C3CONTools, as well as the song's original CON file.
- Launch C3CONTools, and open up the Upgrade Bundler.
- Place the song's original CON file in the left window, and the song's corresponding *_plus.mid file into the right window. Then, click the "Bundle!" button. A window may pop up expressing the song ID is "NOT FOUND IN DTA"; you can skip this by clicking OK.
- After the upgrade bundler finishes up, you should have an upgraded version of your CON. It will have the same name as the original CON, but with "(bundled)" at the end.
- Finally, take the CON file and place it in the same location you pulled it from on your Xbox. Then, boot up RB3 and enjoy your upgrade!
- IMPORTANT NOTE: the above method will work for every legacy song except for songs obtained by exporting from Rock Band. To apply harmonies to Rock Band export songs, you will need to create an upgrade CON similar to a pro strings upgrade (see the pro strings tutorial for more info on building an upgrade CON), and then add a line in the original song's songs.dta file indicating the number of vocal parts (see the RPCS3 harmony tutorial for more info on adding this line).

## RPCS3
Installing a harmony upgrade on RPCS3 requires a little more work than Xbox (or using RB3DX), as you will see. You will need C3CONTools, and the original song to be installed on your system in order to access the songs.dta file.

- Open up your system's file explorer, and navigate to where you have RPCS3 installed. 
- Go to ```dev_hdd0\game\BLUS30463\USRDIR```. Create the folder ```HMX0756``` if it does not exist. Then, navigate inside this folder.
- Paste the *_plus.mid files for the harmony upgrade you want in the folder, and depending on if you have previously placed upgrades in this folder, do one of the following:
  - If you have never posted an upgrade here before, simply paste the harmony's upgrades.dta file in.
  - If you HAVE posted an upgrade here before, open up the existing upgrades.dta, scroll down to the very bottom, and paste in the contents of the harmony's upgrades.dta file. 
  - IMPORTANT NOTE: if you have previously applied a pro string upgrade from this repo into this upgrades.dta AND it shares a name with the harmony upgrade (i.e. you applied a Blitzkrieg Bop pro string upgrade and you're trying to install the harmonies), you will need to either delete the pro string midi and corresponding upgrade info, or merge their harmony and pro string midis together.
- Navigate to the directory where the original song's files are located, and open up the songs.dta file. Within the ```(songs )``` array, add the line ```(vocal_parts X)```, where ```X``` is the number of harm parts you saw in the *_plus.mid.
- Finally, open up C3CONTools, and launch the PS3 Converter. Then click Encryption Options --> Encrypt replacement MIDI file(s). Navigate to the ```HMX0756``` folder from your RPCS3 install, and select the *_plus.mid file you placed in there. The midi should now be encrypted and recognizable by RPCS3.
- That's it! Boot up RB3 on RPCS3 and enjoy your upgrade!
