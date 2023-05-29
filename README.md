# Austins-Unreal-Mod-Tools
Tools to help with the modding process of UE4 games 

# Features 

## Create Uproject Folders
![generate_folders](https://github.com/Austin12325/Austins-Unreal-Mod-Tools/blob/main/docs/generatefolder.gif "Folder Generation")
This creates a projects folders based on the game which you're modding. If set to none it will try and get the games name from the .uproject name

## Cook files 
![cook_files](https://github.com/Austin12325/Austins-Unreal-Mod-Tools/blob/main/docs/cookfiles.gif "Cook Files")
Cooking the files will have unreal cool the specified UProject, Package the cooked files (while also supporting pak chunks set in engine) using [U4pak.py](https://github.com/panzi/u4pak), and move the files to your games folder with the option to place along side the games pak files, or nested in a folder. 
