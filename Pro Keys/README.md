# Pro Keys
<img src="../readme_assets/prokeys.png" width="20%" height="20%" align="left"> Pro key upgrades allow for all applicable songs to be played on a real keyboard, either on the official RB3 keyboard or any MIDI keyboard via the Midi Pro Adapter. In addition to key charts, this repo also provides new audio tracks (moggs) containing isolated key stems for you to play along with. However, due to the fact acquiring the official stems is near-impossible, audio isolation algorithms such as demucs are used to separate the keys into their own stem. As a result, the key stems may not be 100% perfect (i.e., there may be some bleed from other instruments), but they are sufficient for the purposes of a proper key upgrade. To view who authored a particular key chart as well as who contributed the new mogg file with an isolated key stem, please look through that particular song's dta file.

# Installation

## Rock Band 3 Deluxe
If you consult the RB3DX repo, after running the initialization script, you will see two additional scripts - ```enable_keys``` and ```disable_keys```. Like the script names suggest, these will allow or forbid the key upgrades featured in RB3_plus to work natively in the RB3DX patch ark. Simply run the ```enable_keys``` script in order to enjoy these key upgrades baked into RB3DX.

Alternatively, if you do not have the means to install RB3DX onto your system, you can use the methods below in order to play these key upgrades - however, please note that due to how the vanilla version of RB3 handles legacy songs, the venue will be broken, and you will have one static camera angle throughout the song if you play on keys. If that does not bother you, please continue reading to see how to install these upgrades for your preferred system.

## Xbox 360 (JTAG/RGH)
In order to install a key upgrade on Xbox, you will need the song's original CON file and C3CONTools to edit the file's contents. Also, once the process is complete, this song will only be compatible with Rock Band 3 - attempting to play it in any older Rock Band will cause your game to crash.
- Open C3CONTools, and launch the Upgrade Bundler. Place the song's original CON file in the left window, and the *_plus.mid upgrade file in the right window. Click "Bundle!", and if the tool asks you for a song ID, it is fine to ignore and click OK, since you will be overwriting the songs.dta in the next step anyway.
- There should be a new CON created. It should share the same name with the original CON, except with "(bundled)" at the end. Drag this CON into the C3CONTools window.
- Click the "Contents" tab in order to view the files inside the CON. 
  - First, click the songs folder to view the original songs.dta. Right click it, select "Replace selected files", and replace it with the songs.dta you got from this repo.
  - Next, click the shortname's folder to view the midi file and the mogg file. Right click the mogg file, select "Replace selected files", and replace it with the .mogg you got from this repo.
  - Finally, click the "Information" tab and click "Save" in order to rebuild the CON with these new files.
- Your CON is now ready to play. Place it in your system where you grabbed the original CON, and then boot up RB3 and enjoy!

## RPCS3
- TBA
