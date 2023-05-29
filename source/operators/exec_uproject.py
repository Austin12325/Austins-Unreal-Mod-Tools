import bpy
import os 

engine_path = bpy.context.scene["sna_uet_projectpath"]
open = 'start '+engine_path


os.system(open)
print(open)

