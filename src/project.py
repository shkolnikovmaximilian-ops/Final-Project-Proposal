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


        class MALE_PT_customprops(bpy.types.Panel):
    bl_category = 'Item'
    bl_label = "Rig Properties"
    bl_idname = "MALE_PT_customprops"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        layout = self.layout

# This Panel will express Head Properites
class MALE_PT_head_props(bpy.types.Panel):
    bl_label = "Head Properties" 
    bl_idname = "MALE_PT_head_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "MALE_PT_customprops" 
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
        layout = self.layout
        split_size = 0.7
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='Head Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["HEAD_ROT_FOLLOW"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Neck Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["NECK_FOLLOW"]', text = "", slider=True)
        
        # This Panel will express Arm Properites
class MALE_PT_arm_props(bpy.types.Panel):
    bl_label = "Arm Properties" 
    bl_idname = "MALE_PT_arm_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "MALE_PT_customprops" 
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        
    
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
    
        layout = self.layout
        split_size = 0.7
           
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='Left Arm - IK to FK', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM_FK-IK.L"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Left Arm - Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM_ROT_FOLLOW.L"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Left Arm IK Parent', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["HAND_IK_PARENT.L"]', text = "", slider=True)
            
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='Right Arm - IK to FK', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM_FK-IK.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Right Arm - Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM_ROT_FOLLOW.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Right Arm IK Parent', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["HAND_IK_PARENT.R"]', text = "", slider=True)
        
        # This Panel will express Leg Properites
class MALE_PT_leg_props(bpy.types.Panel):
    bl_label = "Leg Properties" 
    bl_idname = "MALE_PT_Leg_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "MALE_PT_customprops" 
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        
        
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
    
        layout = self.layout
        split_size = 0.7
          
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='Left Leg - IK to FK', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_IK-FK.L"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Left Leg - Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_ROT_FOLLOW.L"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Left Leg IK Parent', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_IK_PARENT.L"]', text = "", slider=True)
         
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='Right Leg - IK to FK', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_IK-FK.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Right Leg - Rot Follow', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_ROT_FOLLOW.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Right Leg IK Parent', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG_IK_PARENT.R"]', text = "", slider=True)