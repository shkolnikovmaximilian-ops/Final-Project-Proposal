import bpy

from mathutils import Euler, Matrix, Vector, Quaternion
rig_id = "oizhrgp5jnxo"

### The Rig ID is expressed from a integer driver in the rig properties, and the script listens to it and connects the rig to itself

### Display bones
class MALE_PT_rigui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = "Himulation Rig UI"
    bl_idname = "MALE_PT_rigui"



    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
