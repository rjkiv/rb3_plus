# Pro Strings
<img src="../dependencies/progtr.png" width="20%" height="20%" align="left"> Pro Strings upgrades allow for all applicable songs to be played in either the Pro Guitar or Pro Bass mode, via the actual instruments' tabs. For details on each chart, 

## Installation
Installing Pro Strings upgrades from rb3_plus is easier than ever! Follow the instructions below for your system.

### ⚠️ [[Rock Band 3 Deluxe]](https://rb3dx.milohax.org/install) users don't need to install this as it is already included in the mod! ⚠️

### Xbox 360
It's suggested to use [[Nautilus]](https://nemosnautilus.com/nautilus/) (formerly known as C3 CON Tools) to automatically put files in the correct locations on a USB drive.
1. [[Click here to download the `.zip` file]](https://nightly.link/rjkiv/rb3_plus/workflows/build/main/RB3PlusProStrPack.zip) which contains the latest version of rb3_plus in CON file format.
2. Extract the `.zip` file.
3. Plug in your USB drive.
4. Open Nautilus and click on RBtoUSB.  
![example_rbtousb_close](../dependencies/example_rbtousb_close.png?raw=true "Opening RBtoUSB in Nautilus")
5. Click on `File` at the top then `Open USB Drive` and select your USB drive.
6. Drag the CON file you extracted into RBtoUSB.  
![example_rbtousb_drag](../dependencies/example_rbtousb_drag.gif?raw=true "Dragging RB3 Pro Strings Pack in")
7. Click on `File` at the top then `Close drive`. Remember to eject your USB drive before removing it!

#### JTAG/RGH
8. On your JTAG/RGH Xbox, open the File Manager. Navigate to ```Hdd1/Content/0000000000000000/45410914/00000001```, and paste the CON file in.
9. Delete your RB3 song cache by deleting the ```songcache``` file.
That's it! Boot up Rock Band 3 and enjoy your upgrade!

#### Xbox 360 (Retail)
8. Once you have your CON file, move it to the same place as you would your other custom CONs.
9. Also like the JTAG/RGH setup, it's recommended you delete your RB3 song cache. Navigate to your RB3 DLC location on your hard drive and delete the song cache there.

### RPCS3
Below are the steps for manually installing Pro Strings upgrades for RPCS3.

#### ⚠️ It is highly recommended to use [[Rock Band 3 Deluxe]](https://rb3dx.milohax.org/install) instead of having to do this. ⚠️

1. Open up your system's file explorer, and navigate to where you have RPCS3 installed. 
2. Go to ```dev_hdd0\game\BLUS30463\USRDIR```. Create the folder ```HMX0756``` if it does not exist. Then, navigate inside this folder.
3. Inside this folder, if it does not already exist, make a new folder titled ```songs_upgrades```. Navigate inside this folder.
4. Paste the `_plus.mid` file in the folder, and depending on if you have previously placed upgrades in this folder, do one of the following:
  a. If you have never posted an upgrade here before, simply paste the Pro Strings upgrade's `upgrades.dta` file in.
  b. If you HAVE posted an upgrade here before, open up the existing `upgrades.dta`, scroll down to the very bottom, and paste in the contents of the Pro Strings upgrade's `upgrades.dta` file.
5. Finally, open up Nautilus, and launch the PS3 Converter. Then click Encryption Options --> Encrypt replacement MIDI file(s). Navigate to the ```HMX0756``` folder from your RPCS3 install, and select the Pro Strings upgrade's `_plus.mid` you placed in there. The MIDI should now be encrypted and recognizable by RPCS3.
- That's it! Boot up RB3 on RPCS3 and enjoy your upgrades!

### PS3
Below are the steps for manually installing Pro Strings upgrades for PS3.
#### ⚠️ It is highly recommended to use [[Rock Band 3 Deluxe]](https://rb3dx.milohax.org/install) instead of having to do this. ⚠️

1. In Nautilus, launch the PS3 Converter. Then click Encryption Options --> Encrypt replacement MIDI file(s). Take the MIDI file from this repository, and encrypt it. You should end up with a file formatted as `plus.mid.edat`. You can then have this on hand for use with an FTP transfer, or put it on a flash drive with the associated `upgrades.dta`.
2. Using a tool on your PS3 like multiMAN or with an FTP connection, open up your PS3's file system. You will need a modded PS3 to do this.
3. Go to ```dev_hdd0\game\BLUS30463\USRDIR```. Create the folder ```HMX0756``` if it does not exist. Then, navigate inside this folder.
4. Inside this folder, if it does not already exist, make a new folder titled ```songs_upgrades```. Navigate inside this folder.
5. Paste the `plus.mid.edat` file in the folder, and depending on if you have previously placed upgrades in this folder, do one of the following:
  a. If you have never posted an upgrade here before, simply paste the Pro Strings upgrade's `upgrades.dta` file in.
  b. If you HAVE posted an upgrade here before, open up the existing `upgrades.dta`, scroll down to the very bottom, and paste in the contents of the Pro Strings upgrade's `upgrades.dta` file.
- That's it! Boot up RB3 and enjoy your upgrades!

### YARG
As of writing this, YARG does not support Pro Strings but will in the future! When that day comes, you will be able to enjoy Pro Strings upgrades from rb3_plus by downloading Rock Band 3 Deluxe's YARG Updates downloads.

#### ⚠️ This requires clean Rock Band content files! ⚠️

1. [[Click here to download the `.zip` file]](https://nightly.link/hmxmilohax/rock-band-3-deluxe/workflows/build/develop/RB3DX-YARG-Updates.zip) which contains the latest version of Rock Band 3 Deluxe YARG Updates.
2. Extract the .zip file.
3. Drag the `songs_updates` folder to where you have your Rock Band songs.  
  a. Do not drag `songs_updates` into the folder with your Rock Band songs!
4. In YARG, navigate to Settings > Songs > Scan Songs.

![example_YARG_folder](../dependencies/example_YARG_folder.webp?raw=true "Example YARG folder")


