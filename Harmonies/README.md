# Harmonies 

<img src="../readme_assets/harm3.png" width="10%" height="10%" align="left"> Harmony upgrades allow for all applicable pre-RB3 songs to be sang with up to 3 people via the addition of harmony vocal tubes. All harmony files (with the exception of the forbidden harmonies) have been authored by [Rock Band: Harmonies Project (RBHP)](https://github.com/FujiSkunk/rbhp). However, many of these upgrades contained visual bugs such as lyrics displaying twice or vocal tubes being disconnected, so I went ahead and tweaked all of them. Along with being in this repo, these fixed upgrades can also be found built-in to another RB3 project, [Rock Band 3 Deluxe](https://github.com/jnackmclain/rock-band-3-deluxe).

# Installation

## Rock Band 3 Deluxe
If you have RB3DX installed onto your system, then good news - you do not need to take any further steps, as RB3DX has all of my fixed upgrade files built-in. However, if you do not have RB3DX installed, the process to install harmonies is rather involved (especially if you are on PS3/RPCS3), but it can be done, as demonstrated below.

## Xbox
In order to install a harmony upgrade for a particular song on Xbox, you will need C3CONTools, as well as the song's original CON file. You will also need your preferred DAW (I personally use Reaper).

- Launch C3CONTools, drag the CON file directly onto the window, and extract the midi file.
- In your DAW, import the midi file you just extracted, and then import the song's upgrade file you got from this repo.
- Export the midi file from your DAW. What you should have is a new midi file with the same name as the originally extracted midi file, but now with the addition of the harmony tracks from the repo.
- Go back to C3CONTools, with the CON file dragged into the window, and replace the original midi file with the one you just exported from your DAW.
- Exit out of that window, and then launch C3CONTools' Quick DTA Editor. Drag the song's CON onto it.
- Within the song array, add the attribute (vocal_parts X), where X is the number of harm tracks you placed in your modified midi file.
- Save and exit the dta file window, wait for the CON to rebuild.
- Finally, take the CON file and place it in the same location you pulled it from on your Xbox. Then, boot up RB3 and enjoy your upgrade!

## PS3/RPCS3
TBA
