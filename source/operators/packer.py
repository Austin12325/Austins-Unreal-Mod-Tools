import bpy
import shutil
import os
import subprocess

packerpath = os.path.join(os.path.dirname(__file__), "assets", "u4pak.py")

uepath = bpy.context.scene.sna_uet_engine_path
project = bpy.context.scene.sna_uet_projectpath
gamefiles = bpy.context.scene.sna_uet_targetexe
chunkcheck = bpy.context.scene.sna_uet_chunkcheck
foldercheck = bpy.context.scene.sna_uet_foldercheck
deletechunk = bpy.context.scene.sna_uet_deletechunk

projectname = project.split("\\")[-1][:-9]
projectlen = len(project.split("\\")[-1])
exename = gamefiles.split("\\")[-1][:-4]
chunkpath = project[:-projectlen] + "Saved\\TmpPackaging\\WindowsNoEditor"
sourcefolder = project[:-projectlen] + "Saved\\Cooked"

number = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
### The ext(extension) list is the list of files that will be moved to the packaging folder, Im not proud of it plz rewrite the reading+moving of assets in the future
extlist = [".uasset",".uexp",".ubulk"]

### This gets your blender install locatoin (your pak folders will be copied here to get packaged)
try:
    # 2.92 and older
    path = bpy.app.binary_path_python
except AttributeError:
    # 2.93 and later
    import sys

    path = sys.executable
    
exportpath = os.path.abspath(path[:-25])


### Run the cook on your project

subprocess.run(
    uepath
    + "\\Engine\\Binaries\\Win64\\UE4Editor-Cmd.exe "
    + '"'
    + project
    + '"'
    + " -run=Cook  -TargetPlatform=WindowsNoEditor"
)

### This here removes the extra folders found in the project/saved/cooked folder
   
def rmoldcook():
    
    for folder in os.listdir(sourcefolder):
        
        if folder.endswith(number):
            print("file ends with number ",folder)
            try:
                shutil.rmtree(os.path.join(sourcefolder,folder))
                print(os.path.join(sourcefolder,folder))
            except:
                print("could not remove dirs, unknown")

def packer():
    print("packer here", packerpath)
    
### Check and see if the target game already has a mods folder
    if foldercheck == True:
        try:
            os.mkdir(gamefiles[:-len(exename)-4]+exename+"\\Content\\Paks\\~mods")
        except:
            pass
        
    for folder in os.listdir(sourcefolder):
        
### Checks for game folder in blender dir (the folder gets used for packaging)
        try:
            print("removing"+exportpath+"\\"+exename)
            shutil.rmtree(exportpath+"\\"+ exename)
        except:
            print("Cant remove folder, folder must not be present")

        shutil.copytree(
            sourcefolder + "\\" + folder + "\\" + projectname,
            exportpath +"\\"+ exename,
            copy_function=shutil.copy,
        )
        print("Cook folder has been moved")

        try:
            shutil.rmtree(exportpath + "\\"+ projectname +"\\Metadata")
            os.remove(exportpath + "\\"+ projectname +"\\AssetRegistry.bin")
        except:
            pass
### Runs the packer 
        if folder.endswith(number):
            chunknumber = folder[-1]
        else:
            chunknumber = "0"
            
        subprocess.run(
            'python "'
            + packerpath
            + '" pack '
            + f'{exename+"-"+"WindowsNoEditor_"+projectname+"-"+chunknumber+".pak "}'
            +exename
        )
        
### We are moving the pak files to the game folder
                
        print("Mod name: "+exename+"-"+"WindowsNoEditor_"+projectname+"-"+chunknumber+".pak")
        
        if foldercheck == True:
            shutil.copy(exename+"-"+"WindowsNoEditor_"+projectname+"-"+chunknumber+".pak",gamefiles[:-len(exename)-4]+exename+"\\Content\\Paks\\~mods")
        else:
            shutil.copy(exename+"-"+"WindowsNoEditor_"+projectname+"-"+chunknumber+".pak",gamefiles[:-len(exename)-4]+exename+"\\Content\\Paks")

        os.remove(exename+"-"+"WindowsNoEditor_"+projectname+"-"+chunknumber+".pak")
        
        shutil.rmtree(os.path.join(exportpath,exename))

        
        
        if deletechunk == True:
            if foldercheck == True:
                try:
                    os.remove(os.path.join(path, gamefiles[:-len(exename)-4]+exename+"\\Content\\Paks\\~mods\\", exename+"-"+"WindowsNoEditor_"+projectname+"-0.pak"))
                except:
                    pass
            else:
                try:
                    os.remove(os.path.join(path, gamefiles[:-len(exename)-4]+exename+"\\Content\\Paks\\", exename+"-"+"WindowsNoEditor_"+projectname+"-0.pak"))
                except:
                    pass
                
            
### This is code I stole from my foxhole addon I wrote 6 months ago, no idea what I did then, still don't have any idea what it does now. in the process of re-writing

if chunkcheck == 1:
    for file in os.listdir(chunkpath):

        if file.endswith(number, 0, -4):
            file1 = open(chunkpath + "\\" + file, "r")
            count = 0

            while True:

                count += 1
                list = []
                line = file1.readline()

                # if line is empty
                # end of file is reached
                if not line:
                    break
                list.append(line.split("\\"))
                length = len(list[0][-1])
                string = line.strip()[:-length]
                finalpath = string.replace(
                    "WindowsNoEditor", "WindowsNoEditor" + file[:-4]
                )
                destination = (
                    line.replace("WindowsNoEditor", "WindowsNoEditor" + file[:-4])[:-1]
                )
                for x in extlist:
                    
                    source = line[:-1] + x
                    
                

                    try:
                        if not os.path.isdir(finalpath):
                            os.makedirs(finalpath)
                            print("dirs created")
                        shutil.move(source, destination+x)
                    except:
                        pass


            file1.close()
            
            packer()
            rmoldcook()
            

else:
    packer()
    rmoldcook()
