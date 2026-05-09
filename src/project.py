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

### The code below will allow you to toggle the visibility of rig bones

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        collection = bpy.data.armatures["Armature"].collections

        row = col.row(align = True)  
        row.prop(collection["PROPERTIES"], 'is_visible', toggle=True, text='PROPERTIES')
        row = col.row(align = True) 
        
        row = col.row(align = True)  
        row.prop(collection["ROOT"], 'is_visible', toggle=True, text='ROOT')
        
        row = col.row(align = True)  
        row.prop(collection["COG_GUIDE"], 'is_visible', toggle=True, text='COG_GUIDE')
        
        row = col.row(align = True)
        row = col.row(align = True)
        row = col.row(align = True)  
        row.prop(collection["TORSO"], 'is_visible', toggle=True, text='TORSO')
        row.prop(collection["TORSO_FK"], 'is_visible', toggle=True, text='TORSO_FK')
        row.prop(collection["TORSO_TWEAK"], 'is_visible', toggle=True, text='TORSO_TWEAK')
        
        row = col.row(align = True)
        row = col.row(align = True)
        row = col.row(align = True) 
        row.prop(collection["LEFT_ARM_IK"], 'is_visible', toggle=True, text='LEFT_ARM_IK')
        row.prop(collection["RIGHT_ARM_IK"], 'is_visible', toggle=True, text='RIGHT_ARM_IK')
        row = col.row(align = True)
        row.prop(collection["LEFT_ARM_FK"], 'is_visible', toggle=True, text='LEFT_ARM_FK')
        row.prop(collection["RIGHT_ARM_FK"], 'is_visible', toggle=True, text='RIGHT_ARM_FK')
        row = col.row(align = True)
        row.prop(collection["RIGHT_ARM_TWEAK"], 'is_visible', toggle=True, text='RIGHT_ARM_TWEAK')
        row.prop(collection["LEFT_ARM_TWEAK"], 'is_visible', toggle=True, text='LEFT_ARM_TWEAK')  
        
        row = col.row(align = True)
        row = col.row(align = True)
        row = col.row(align = True)
        row.prop(collection["RIGHT_HAND"], 'is_visible', toggle=True, text='RIGHT_HAND')
        row.prop(collection["LEFT_HAND"], 'is_visible', toggle=True, text='LEFT_HAND') 
        
        row = col.row(align = True)
        row = col.row(align = True)
        row = col.row(align = True) 
        row.prop(collection["LEFT_LEG_IK"], 'is_visible', toggle=True, text='LEFT_LEG_IK')
        row.prop(collection["RIGHT_LEG_IK"], 'is_visible', toggle=True, text='RIGHT_LEG_IK')               
        row = col.row(align = True)  
        row.prop(collection["LEFT_LEG_FK"], 'is_visible', toggle=True, text='LEFT_LEG_FK')
        row.prop(collection["RIGHT_LEG_FK"], 'is_visible', toggle=True, text='RIGHT_LEG_FK')
        row = col.row(align = True)
        row.prop(collection["LEFT_LEG_TWEAK"], 'is_visible', toggle=True, text='LEFT_LEG_TWEAK')
        row.prop(collection["RIGHT_LEG_TWEAK"], 'is_visible', toggle=True, text='RIGHT_LEG_TWEAK') 