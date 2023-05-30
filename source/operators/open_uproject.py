import bpy
import os 
import webbrowser

engine_path = bpy.context.scene.sna_uet_projectpath
filename = engine_path.split("\\")
remove = len(filename[-1])
open = engine_path[:-remove-1]

webbrowser.open(os.path.realpath(open))


