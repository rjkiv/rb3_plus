import argparse
import json
import subprocess
from tool_dependencies.parse_song_dta import parse_song_dta
from pathlib import Path

def find_song_path(shortname: str) -> Path:
    # navigate to the Pro Strings folder
    root = Path().absolute().parent
    pro_strings = root.joinpath("Pro Strings")

    # search for that shortname's folder in all of the Rock Band etc. folders
    found = False
    target_path = Path("")
    for pro_folder in pro_strings.glob("*/*"):
        if shortname == pro_folder.stem:
            target_path = pro_folder
            found = True
            break

    # return the path we may or may not have found
    if found:
        print(f"Found {shortname}, path is {target_path}")
    else:
        print(f"Could not find {shortname}")
        exit()

    return target_path

def get_rpcs3_dir() -> Path:
    f = open(Path().absolute().joinpath("config.json"))
    data = json.load(f)
    dir = data["RPCS3_dir"]
    if dir == "":
        print("RPCS3 directory not set. Please fill in your current RPCS3 directory in config.json and try again.")
        exit()

    print(f"RPCS3 directory is set to {dir}")
    return Path(dir)

def add_upgrade_dta(shortname_dir: Path, upgrade_dir: Path):
    # get dict of this one song's upgrades.dta
    this_upgrade_dict = parse_song_dta(shortname_dir.joinpath("upgrades.dta"))
    this_shortname = [key for key in this_upgrade_dict["songs"].keys()][0]
    this_upgrade_dict = this_upgrade_dict["songs"][this_shortname]

    # get dict of the upgrades.dta in songs_upgrades, if it exists
    mega_upgrade_dict = {}
    big_upgrade_dta_exists = False
    if(upgrade_dir.joinpath("upgrades.dta").exists()):
        mega_upgrade_dict = parse_song_dta(upgrade_dir.joinpath("upgrades.dta"))
        big_upgrade_dta_exists = True
    # else:
    #     print("upgrades.dta does not exist")
    
    # write a combo of the above upgrades into songs_upgrades/upgrades.dta
    with open(upgrade_dir.joinpath("upgrades.dta"),"w",encoding="ISO-8859-1") as dta_output:
        if big_upgrade_dta_exists:
            for key in mega_upgrade_dict["songs"].keys():
                # we want to skip over the current entry for our shortname in favor of our new one
                if key != this_shortname:
                    dta_output.write(f"({key}\n  (upgrade_version 1)\n  (midi_file \"{mega_upgrade_dict['songs'][key]['midi_file']}\")\n  (song_id {mega_upgrade_dict['songs'][key]['song_id']})\n  ")
                    dta_output.write(f"(rank\n")
                    if "real_guitar" in mega_upgrade_dict['songs'][key]['rank']:
                        dta_output.write(f"    (real_guitar {mega_upgrade_dict['songs'][key]['rank']['real_guitar']})\n")
                    if "real_bass" in mega_upgrade_dict['songs'][key]['rank']:
                        dta_output.write(f"    (real_bass {mega_upgrade_dict['songs'][key]['rank']['real_bass']})\n")
                    dta_output.write(f"  )\n")
                    if "real_guitar_tuning" in mega_upgrade_dict['songs'][key]:
                        dta_output.write(f"  (real_guitar_tuning ({' '.join(str(x) for x in mega_upgrade_dict['songs'][key]['real_guitar_tuning'])}))\n")
                    if "real_bass_tuning" in mega_upgrade_dict['songs'][key]:
                        dta_output.write(f"  (real_bass_tuning ({' '.join(str(x) for x in mega_upgrade_dict['songs'][key]['real_bass_tuning'])}))\n")
                    dta_output.write(")\n\n")

        # now, write our current shortname's dta
        dta_output.write(f"({this_shortname}\n  (upgrade_version 1)\n  (midi_file \"{this_upgrade_dict['midi_file']}\")\n  (song_id {this_upgrade_dict['song_id']})\n  ")
        dta_output.write(f"(rank\n")
        if "real_guitar" in this_upgrade_dict['rank']:
            dta_output.write(f"    (real_guitar {this_upgrade_dict['rank']['real_guitar']})\n")
        if "real_bass" in this_upgrade_dict['rank']:
            dta_output.write(f"    (real_bass {this_upgrade_dict['rank']['real_bass']})\n")
        dta_output.write(f"  )\n")
        if "real_guitar_tuning" in this_upgrade_dict:
            dta_output.write(f"  (real_guitar_tuning ({' '.join(str(x) for x in this_upgrade_dict['real_guitar_tuning'])}))\n")
        if "real_bass_tuning" in this_upgrade_dict:
            dta_output.write(f"  (real_bass_tuning ({' '.join(str(x) for x in this_upgrade_dict['real_bass_tuning'])}))\n")
        dta_output.write(")\n\n")

def add_upgrade_midi(shortname_dir: Path, upgrade_dir: Path):
    for pro_file in shortname_dir.glob("*.mid"):
        print(pro_file.name)

        # if mid and edat exist in this directory, delete them
        upgrade_dir.joinpath(pro_file.name).unlink(missing_ok=True)
        upgrade_dir.joinpath(f"{pro_file.name}.edat").unlink(missing_ok=True)

        # make an encrypted edat and place it in the upgrades directory        
        subprocess.run([Path().absolute().joinpath("tool_dependencies").joinpath("edattool.exe"), "encrypt", "-custom:0B72B62DABA8CAFDA3352FF979C6D5C2", "UP8802-BLUS30463_00-RBHMXBANDCCFF0D6", "00", "00", "00", pro_file, upgrade_dir.joinpath(f'{pro_file.name}.edat'), Path().absolute().joinpath("tool_dependencies").joinpath("ntsc.rap")])

def rpcs3_insert_strings_upgrade(shortname: str):
    shortname_path = find_song_path(shortname=shortname)
    rpcs3_dir = get_rpcs3_dir()
    
    # navigate to the songs_upgrades directory, creating folders as needed
    rpcs3_dir.joinpath("dev_hdd0", "game", "BLUS30463", "USRDIR", "HMX0756", "songs_upgrades").mkdir(parents=True, exist_ok=True)
    upgrades_dir = rpcs3_dir.joinpath("dev_hdd0", "game", "BLUS30463", "USRDIR", "HMX0756", "songs_upgrades")

    # move the .mid and encrypt to .mid.edat using edattool
    add_upgrade_midi(shortname_path, upgrades_dir)

    # move the upgrades.dta and write/append/replace
    add_upgrade_dta(shortname_path, upgrades_dir)

# user must input a shortname
# search Pro Strings/all the folders for that shortname
# if the shortname is found, navigate to the set RPCS3 directory
# from there, go to RPCS3\dev_hdd0\game\BLUS30463\USRDIR\HMX0756\songs_upgrades, creating folders as necessary
# insert the shortname's _plus.mid and append upgrades.dta
# encrypt the .mid to .mid.edat using edattool
# win

if __name__ == "__main__":
    # -------------------------------------------------------------------------------------------------------------------------------
    # take in the arguments
    parser = argparse.ArgumentParser(description="Take in a shortname for a pro upgrade, and insert it into the proper place in RPCS3.")
    parser.add_argument("--shortname", "-s", help="The upgrade's shortname. NOTE: This script assumes you have a mid/dta in a folder somewhere in this repo, ready to integrate into RPCS3.", type=str, required=True)
    args = parser.parse_args()
    # -------------------------------------------------------------------------------------------------------------------------------
    rpcs3_insert_strings_upgrade(args.shortname)