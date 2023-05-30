import bpy
import os

uepath = bpy.context.scene.sna_uet_engine_path
project = bpy.context.scene.sna_uet_projectpath
gamefiles = bpy.context.scene.sna_uet_targetexe
chunkcheck = bpy.context.scene.sna_uet_chunkcheck
selection = bpy.context.scene.sna_uet_txtfiles


# for dir in os.walk("F:\\Games\\Modding\\umodel_win32\\UmodelSaved\\Game",topdown=True):
#     print(dir[0].split("F:\\Games\\Modding\\umodel_win32\\UmodelSaved\\Game\\")[-1])

# f = open(gameexe+".txt", "a")

# for dir in os.walk("F:\\Games\\Modding\\umodel_win32\\UmodelSaved\\Game",topdown=True):
#     f.write(dir[0].split("F:\\Games\\Modding\\umodel_win32\\UmodelSaved\\Game\\")[-1] +"\\end"+ "\n")



if selection == 'None':

    projectname = project.split("\\")[-1][:-9]
    projectlen = len(project.split("\\")[-1])
    file = open(os.path.join(os.path.dirname(__file__), "assets", projectname+".txt"), "rt")
    print(projectname+".txt")

    try:
        for lines in file:
            try:
                os.makedirs(os.path.join(project[:-projectlen],"GeneratedFolders\\Content\\",lines))
            except:
                pass

    except:
        self.report({"WARNING"}, "Uproject name not found in addon")
    print("None")

    file.close()


if selection == 'Foxhole':

    projectname = project.split("\\")[-1][:-9]
    projectlen = len(project.split("\\")[-1])
    file = open(os.path.join(os.path.dirname(__file__), "assets", "War.txt"), "rt")
    print(projectname+".txt")

    try:
        for lines in file:
            try:
                os.makedirs(os.path.join(project[:-projectlen],"GeneratedFolders\\Content\\",lines))
            except:
                pass

    except:
        self.report({"WARNING"}, "Uproject name not found in addon")
        print("filenot found")
    print("Foxhole")
    
    file.close()





if selection == 'StarshipTroopers:Extermination':

    projectname = project.split("\\")[-1][:-9]
    projectlen = len(project.split("\\")[-1])
    file = open(os.path.join(os.path.dirname(__file__), "assets", "Yakisoba.txt"), "rt")
    print(projectname+".txt")

    try:
        for lines in file:
            try:
                os.makedirs(os.path.join(project[:-projectlen],"GeneratedFolders\\Content\\",lines))
            except:
                pass

    except:
        self.report({"WARNING"}, "Uproject name not found in addon")
    print("Foxhole")
    
    file.close()


