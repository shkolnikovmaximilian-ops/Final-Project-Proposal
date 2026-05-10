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

# This Panel will express the color wheel functionality
class MALE_PT_col_props(bpy.types.Panel):
    bl_label = "Mesh Color Properties" 
    bl_idname = "MALE_PT_col_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "MALE_PT_customprops" 
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        row = col.row() 
        split_size = 0.7
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='Mesh Color', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["Color"]', text = "Color", slider=True)


# This Panel will express the mesh visibility functionality
        class MALE_PT_vis_props(bpy.types.Panel):
    bl_label = "Visibility Properties" 
    bl_idname = "MALE_PT_vis_props"
    bl_space_type = 'VIEW_3D'
    bl_category = 'Item'
    bl_parent_id = "MALE_PT_customprops"
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        

        my_object =  bpy.data.objects['Himulation']
               
    
        mask_left_arm = my_object.modifiers["MASK_LEFT_ARM"]
        mask_left_leg = my_object.modifiers["MASK_LEFT_LEG"]
        mask_right_arm = my_object.modifiers["MASK_RIGHT_ARM"]
        mask_right_leg = my_object.modifiers["MASK_RIGHT_LEG"]
        mask_torso = my_object.modifiers["MASK_TORSO"]
        
        
        layout = self.layout
        layout.use_property_split = False
        layout.use_property_decorate = False 


        box = layout.box()
        col = box.column(align=True)
        row = col.row() 
        row.label(text='Left Arm', translate=False)   
        row.prop(mask_left_arm, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row(align = True) 
        row.label(text='Right Arm', translate=False)             
        row.prop(mask_right_arm, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row(align = True)  
        row.label(text='Left Leg', translate=False)             
        row.prop(mask_left_leg, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
      
        row = col.row(align = True)  
        row.label(text='Right Leg', translate=False)             
        row.prop(mask_right_leg, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)  
       
        row = col.row(align = True)  
        row.label(text='Torso', translate=False)             
        row.prop(mask_torso, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        

def get_matrix(armature, source_bone, target_bone):
    source_bone_rest_matrix = source_bone.bone.matrix_local
    target_bone_rest_matrix = target_bone.bone.matrix_local

    offset_matrix = source_bone_rest_matrix.inverted() @ target_bone_rest_matrix

    source_world_matrix = source_bone.matrix

    matrix_final =  source_world_matrix @ offset_matrix
    
    return matrix_final



class MALE_OT_ik_fk_arm(bpy.types.Operator):
    bl_idname = "male.ik_fk_arm"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        fk_hand = pose_bones[f'HAND_FK.{side}']
        fk_pole = pose_bones[f'MCH_IK_FK_ARM_POLE_IK.{side}']
                
        ik_hand = pose_bones[f'HAND_IK.{side}']
        ik_pole = pose_bones[f'ARM_POLE_IK.{side}']
                
        select_set = (ik_hand, ik_pole, properties) 
        
        hand_matrix = get_matrix(armature, fk_hand, ik_hand )
        pole_matrix = get_matrix(armature, fk_pole, ik_pole )
        
        ik_hand.matrix = hand_matrix
        bpy.context.view_layer.update()        
        ik_pole.matrix = pole_matrix
        bpy.context.view_layer.update()
        
        properties[f'ARM_FK_IK.{side}'] = 1        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}      


class MALE_OT_fk_ik_arm(bpy.types.Operator):
    bl_idname = "male.fk_ik_arm"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        

        fk_hand = pose_bones[f'HAND_FK.{side}']
        fk_forearm = pose_bones[f'FOREARM_FK.{side}']
        fk_arm = pose_bones[f'ARM_FK.{side}']
                
        ik_hand = pose_bones[f'HAND_IK.{side}']
        ik_forearm = pose_bones[f'MCH_FOREARM_IK.{side}']
        ik_arm = pose_bones[f'MCH_ARM_IK.{side}']
                
        select_set = (fk_hand, fk_forearm, fk_arm, properties) 
        
        hand_matrix = get_matrix(armature, ik_hand, fk_hand )
        forearm_matrix = get_matrix(armature, ik_forearm, fk_forearm )
        arm_matrix = get_matrix(armature, ik_arm, fk_arm )

        fk_arm.matrix = arm_matrix
        bpy.context.view_layer.update()
        fk_forearm.matrix = forearm_matrix
        bpy.context.view_layer.update()
        fk_hand.matrix = hand_matrix
        bpy.context.view_layer.update()        
                
        

        properties[f'ARM_FK_IK.{side}'] = 1        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}      


class MALE_OT_ik_fk_leg(bpy.types.Operator):
    bl_idname = "male.ik_fk_leg"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        fk_foot = pose_bones[f'MCH_IK_FK_FOOT_IK_MASTER.{side}']
        fk_pole = pose_bones[f'MCH_IK_FK_LEG_POLE_IK.{side}']
                
        ik_foot = pose_bones[f'FOOT_IK_MASTER.{side}']
        ik_pole = pose_bones[f'MCH_IK_FK_LEG_POLE_IK.{side}']
                
        select_set = (ik_foot, ik_pole, properties) 
        
        foot_matrix = get_matrix(armature, fk_foot, ik_foot )
        pole_matrix = get_matrix(armature, fk_pole, ik_pole )
        
        ik_foot.matrix = foot_matrix
        bpy.context.view_layer.update()        
        ik_pole.matrix = pole_matrix
        bpy.context.view_layer.update()
        
        properties[f'LEG_FK_IK.{side}'] = 0        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}      



class MALE_OT_fk_ik_leg(bpy.types.Operator):
    bl_idname = "male.fk_ik_leg"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        fk_foot = pose_bones[f'FOOT_FK.{side}']
        fk_shin = pose_bones[f'SHIN_FK.{side}']
        fk_thigh = pose_bones[f'THIGH_FK.{side}']
                
        ik_foot = pose_bones[f'FOOT_IK_MASTER.{side}']
        ik_shin = pose_bones[f'MCH_IK_SHIN.{side}']
        ik_thigh = pose_bones[f'MCH_IK_THIGH.{side}']
                
        select_set = (fk_foot, fk_shin, fk_thigh, properties) 
        
        foot_matrix = get_matrix(armature, ik_foot, fk_foot )
        shin_matrix = get_matrix(armature, ik_shin, fk_shin )
        thigh_matrix = get_matrix(armature, ik_thigh, fk_thigh )

        fk_thigh.matrix = thigh_matrix
        bpy.context.view_layer.update()
        fk_shin.matrix = shin_matrix
        bpy.context.view_layer.update()
        fk_foot.matrix = foot_matrix
        bpy.context.view_layer.update()        
                
        
        properties[f'LEG_FK_IK.{side}'] = 1        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}      



class MALE_PT_snap_panel(bpy.types.Panel):
    bl_category = 'Item'
    bl_label = "Snap Utilities"
    bl_idname = "MALE_PT_snap_panel"
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
        #box = layout.box()
        col = layout.column(align=True)
        row = col.row()
        row.operator("MALE.ik_fk_arm", emboss=True, text="Arm L IK > FK", icon='SNAP_ON').side = 'L'
        row.operator("MALE.ik_fk_arm", emboss=True, text="Arm R IK > FK", icon='SNAP_ON').side = 'R'
        
        row = col.row()
        row.operator("MALE.fk_ik_arm", emboss=True, text="Arm L FK > IK", icon='SNAP_ON').side = 'L'
        row.operator("MALE.fk_ik_arm", emboss=True, text="Arm R FK > IK", icon='SNAP_ON').side = 'R'
        
        col = layout.column(align=True)
        row = col.row()
        row.operator("MALE.ik_fk_leg", emboss=True, text="Leg L IK > FK", icon='SNAP_ON').side = 'L'
        row.operator("MALE.ik_fk_leg", emboss=True, text="Leg R IK > FK", icon='SNAP_ON').side = 'R'
        
        row = col.row()
        row.operator("MALE.fk_ik_leg", emboss=True, text="Leg L FK > IK", icon='SNAP_ON').side = 'L'
        row.operator("MALE.fk_ik_leg", emboss=True, text="Leg R FK > IK", icon='SNAP_ON').side = 'R'
                                            
  
                                            
classes = (MALE_PT_rigui,
           MALE_PT_customprops,
           MALE_PT_vis_props,
           MALE_PT_head_props,
           MALE_PT_arm_props,
           MALE_PT_leg_props,
           MALE_PT_col_props,
           MALE_PT_snap_panel,
           MALE_OT_ik_fk_arm,
           MALE_OT_fk_ik_arm,
           MALE_OT_ik_fk_leg,
           MALE_OT_fk_ik_leg,)
             
            
            

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()