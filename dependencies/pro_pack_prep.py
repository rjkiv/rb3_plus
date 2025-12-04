import subprocess
import sys
from pathlib import Path
# this argument is to see what type of folders we are going to use
if len(sys.argv) < 2:
    print("Usage: pro_pack_prep.py <ps3|xbox>")
    sys.exit(1)
    Usage: make_npdata
platform = sys.argv[1].lower()
if platform not in ("ps3", "xbox"):
    print("ERROR: Invalid platform")
    sys.exit(1)
# get the current working directory
cwd = Path().absolute()
print(cwd)

if platform == "xbox":
    dest_root = cwd.joinpath("_tmp/songs_upgrades")
elif platform == "ps3":
    dest_root = cwd.joinpath("_tmp/ps3/USRDIR/Rock Band 3 Plus Upgrades/songs_upgrades")

mega_upgrade_dta = []
# dest_root.mkdir(parents=True, exist_ok=True)
dest_root.mkdir(parents=True, exist_ok=True)

# traverse through rb3_plus/Pro Strings and find both _plus.mid and upgrades.dta
for pro_song in cwd.glob("Pro Strings/*/*"):
    print(pro_song.stem)
    for pro_file in pro_song.glob("*"):
        # if working with a dta, append it to the mega dta in here
        if pro_file.name == "upgrades.dta":
            mega_upgrade_dta.extend([line for line in open(pro_file, "r")])
            mega_upgrade_dta.append("\n")
        # if working with a mid, copy it
        elif "_plus.mid" in pro_file.name:
            # copy the mid from rb3_plus directly into the song update folder
            destination_path = dest_root.joinpath(pro_file.name)
            destination_path.write_bytes(pro_file.read_bytes())

with open(dest_root.joinpath("upgrades.dta"),"w",encoding="ISO-8859-1") as dta_output:
        dta_output.writelines(mega_upgrade_dta)
        
# This will copy the files from the rb3 plus/dependencies/ps3 folder
if platform == "ps3":
    ps3_metadata = cwd.joinpath("dependencies/ps3")
    ps3_info_dir = cwd.joinpath("_tmp/ps3")

    ps3_info_dir.mkdir(parents=True, exist_ok=True)

    for ps3_files in ps3_metadata.iterdir():
        print(ps3_files.stem)
        if ps3_files.is_file():
            destination_path = ps3_info_dir.joinpath(ps3_files.name)
            destination_path.write_bytes(ps3_files.read_bytes())
    for midi in dest_root.glob("*.mid"):
        # make an encrypted edat and place it in the upgrades directory        
        subprocess.run([Path().absolute().joinpath("tools").joinpath("tool_dependencies").joinpath("edattool.exe"), "encrypt", "-custom:5a4355db9bfea4a918ec92ae4110ff4f", "UP8802-BLUS30463_00-RB3PLUSPROSTRING", "00", "00", "00", midi, dest_root.joinpath(f'{midi.name}.edat')])
        midi.unlink()