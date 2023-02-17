from pathlib import Path

# get the current working directory
cwd = Path().absolute()
print(cwd)

# mega_upgrade_dta = []
# cwd.joinpath("con_file_contents/songs_upgrades").mkdir(parents=True, exist_ok=True)

# # traverse through rb3_plus/Pro Strings and find both _plus.mid and upgrades.dta
# for pro_song in rb3_plus_path.glob("Pro Strings/*/*"):
#     print(pro_song.stem)
#     for pro_file in pro_song.glob("*"):
#         # if working with a dta, append it to the mega dta in here
#         if pro_file.name == "upgrades.dta":
#             mega_upgrade_dta.extend([line for line in open(pro_file, "r")])
#             mega_upgrade_dta.append("\n")
#         # if working with a mid, copy it
#         elif "_plus.mid" in pro_file.name:
#             # copy the mid from rb3_plus directly into the song update folder
#             destination_path = cwd.joinpath(f"con_file_contents/songs_upgrades/{pro_file.name}")
#             destination_path.write_bytes(pro_file.read_bytes())

# with open(cwd.joinpath("con_file_contents/songs_upgrades/upgrades.dta"),"w",encoding="ISO-8859-1") as dta_output:
#         dta_output.writelines(mega_upgrade_dta)
        
