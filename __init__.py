# Addon Info
bl_info = {
    "name": "PBR Materials",
    "description": "PBR materials",
    "author": "Wolf <wolf.art3d@gmail.com>",
    "version": (3, 5),
    "blender": (2, 83, 0),
    "location": "Material Properties and Shader Editor",
    "doc_url": "https://3d-wolf.com/products/materials",
    "tracker_url": "https://3d-wolf.com/products/materials",
    "support": "COMMUNITY",
    "category": "Material",
    }


# Libraries
import os
from bpy.props import BoolProperty, EnumProperty, PointerProperty
from bpy.types import Operator, Panel, PropertyGroup, WindowManager
from bpy.utils import previews

import bpy


# Panel
class PBRMATERIAL_PT_Panel(Panel):
    bl_label = "PBR Materials"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return context.active_object.material_slots.data.active_material

    def draw(self, context):
        settings = context.scene.pbr_materials
        layout = self.layout
        scn = bpy.context.scene
        wm = context.window_manager
        
        # category
        col = layout.column(align=True)
        row = col.row()
        row.prop(settings, 'category', text="Category", expand=True)
            
        # icons
        row = col.row()
        row.template_icon_view(wm, "material_icons", show_labels=True)
        
        # material Name
        row = col.row(align=True)
        row.alignment = 'CENTER'
        material_name = bpy.data.window_managers["WinMan"].material_icons
        row.label(text=material_name)


def add_material(self, context):
    settings = context.scene.pbr_materials
    material = bpy.data.window_managers["WinMan"].material_icons
    category = context.scene.pbr_materials.category
    
    # output
    active_mat = bpy.context.active_object.active_material
    active_mat.use_nodes = True
    active_mat.node_tree.nodes.clear()    
    preview_type = active_mat.preview_render_type
    output = active_mat.node_tree.nodes.new("ShaderNodeOutputMaterial")
    output.location = (300, 0)

    # dielectrics
    if category == "Dielectric":
        if material == "Acrylic Paint Black":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.05, 0.05, 0.05, 1)
            princi.inputs[5].default_value = (0.488)
            princi.inputs[7].default_value = (0)
        elif material == "Acrylic Paint White":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.8, 0.8, 0.8, 1)
            princi.inputs[5].default_value = (0.488)
            princi.inputs[7].default_value = (0)
        elif material == "Asphalt New":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.05, 0.05, 0.05, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.55)
        elif material == "Asphalt Old":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.12, 0.12, 0.12, 1)
            princi.inputs[5].default_value = (0.25)
            princi.inputs[7].default_value = (0.55)
        elif material == "Bark":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.168, 0.136, 0.105, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.6)
        elif material == "Brick":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.227, 0.147, 0.109, 1)
            princi.inputs[5].default_value = (0.588)
            princi.inputs[7].default_value = (0.78)
        elif material == "Car Paint":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0, 0.083, 0.457, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.25)
            princi.inputs[12].default_value = (1)
        elif material == "Carbon":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.015, 0.015, 0.015, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.4)
            princi.inputs[12].default_value = (1)
        elif material == "Ceramic":
            princi = principled(material, active_mat, output)
            color = rgb(princi, active_mat)
            color.outputs[0].default_value = (1, 0.898, 0.716, 1)
            princi.inputs[0].default_value = (0.6, 0.6, 0.6, 1)
            princi.inputs[1].default_value = (1)
            princi.inputs[2].default_value = (1, 0.898, 0.716)
            princi.inputs[3].default_value = (0.6, 0.6, 0.6, 1)
            princi.inputs[5].default_value = (0.525)
            princi.inputs[7].default_value = (0)
        elif material == "Chalk":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.179, 0.7, 0.39, 1)
            princi.inputs[5].default_value = (0.563)
            princi.inputs[7].default_value = (0.65)
        elif material == "Cloth":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.065, 0.08, 0.254, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.8)
            princi.inputs[10].default_value = (1)
            princi.inputs[11].default_value = (0)
        elif material == "Coal":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.04, 0.04, 0.04, 1)
            princi.inputs[5].default_value = (0.425)
            princi.inputs[7].default_value = (0.66)
        elif material == "Concrete":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.231, 0.231, 0.202, 1)
            princi.inputs[5].default_value = (1.2)
            princi.inputs[7].default_value = (0.74)
        elif material == "Dirt":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.258, 0.162, 0.109, 1)
            princi.inputs[5].default_value = (0.75)
            princi.inputs[7].default_value = (0.78)
        elif material == "Light":
            emission = active_mat.node_tree.nodes.new("ShaderNodeEmission")
            blackbody = active_mat.node_tree.nodes.new("ShaderNodeBlackbody")
            blackbody.location = (-200, 0)
            blackbody.inputs[0].default_value = (3000)
            active_mat.node_tree.links.new(blackbody.outputs[0], emission.inputs[0])
            active_mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        elif material == "Mud":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.342, 0.246, 0.165, 1)
            princi.inputs[5].default_value = (2.225)
            princi.inputs[7].default_value = (0.62)
        elif material == "Plaster":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.275, 0.262, 0.235, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.86)
        elif material == "Plastic":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.448, 0.013, 0.007, 1)
            princi.inputs[5].default_value = (0.375)
            princi.inputs[7].default_value = (0.1)
        elif material == "Rock":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.328, 0.287, 0.227, 1)
            princi.inputs[5].default_value = (0.625)
            princi.inputs[7].default_value = (0.81)
        elif material == "Rubber":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.022, 0.022, 0.022, 1)
            princi.inputs[5].default_value = (0.425)
            princi.inputs[7].default_value = (0.79)
        elif material == "Rust":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.184, 0.032, 0.007, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.82)
        elif material == "Sand":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.44, 0.386, 0.231, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.8)
            princi.inputs[10].default_value = (1)
            princi.inputs[11].default_value = (0)
        elif material == "Skin":
            princi = principled(material, active_mat, output)
            color = rgb(princi, active_mat)
            color.outputs[0].default_value = (1, 0, 0, 1)
            princi.inputs[0].default_value = (0.523, 0.251, 0.19, 1)
            princi.inputs[1].default_value = (1)
            princi.inputs[2].default_value = (1, 0, 0)
            princi.inputs[3].default_value = (0.523, 0.251, 0.19, 1)
            princi.inputs[5].default_value = (0.413)
            princi.inputs[7].default_value = (0.5)
        elif material == "Snow":
            princi = principled(material, active_mat, output)
            color = rgb(princi, active_mat)
            color.outputs[0].default_value = (1, 0.97, 0.95, 1)
            princi.inputs[0].default_value = (0.9, 0.9, 0.9, 1)
            princi.inputs[1].default_value = (1)
            princi.inputs[2].default_value = (1, 0.97, 0.95)
            princi.inputs[3].default_value = (0.9, 0.9, 0.9, 1)
            princi.inputs[5].default_value = (1.25)
            princi.inputs[7].default_value = (0.5)
        elif material == "Wax":
            princi = principled(material, active_mat, output)
            color = rgb(princi, active_mat)
            color.outputs[0].default_value = (1, 0.397, 0.16, 1)
            princi.inputs[0].default_value = (0.263, 0.084, 0.222, 1)
            princi.inputs[1].default_value = (1)
            princi.inputs[2].default_value = (1, 0.397, 0.16)
            princi.inputs[3].default_value = (0.263, 0.084, 0.222, 1)
            princi.inputs[5].default_value = (0.5)
            princi.inputs[7].default_value = (0.3)
        elif material == "Wood":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.402, 0.319, 0.231, 1)
            princi.inputs[5].default_value = (1)
            princi.inputs[7].default_value = (0.68)
    # metals
    else:
        if material == "Aluminium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.815, 0.831, 0.839, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Brass":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.956, 0.791, 0.305, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Bronze":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.973, 0.429, 0.15, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Chromium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.262, 0.258, 0.283, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Cobalt":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.392, 0.386, 0.361, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Copper":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.973, 0.356, 0.246, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Gallium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.479, 0.604, 0.578, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Gold":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.973, 0.539, 0.109, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Iron":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.552, 0.571, 0.571, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Lead":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.591, 0.591, 0.591, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Mercury":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.584, 0.571, 0.571, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0)
        elif material == "Molybdenum":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.429, 0.445, 0.361, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Nickel":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.392, 0.323, 0.235, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Pewter":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.515, 0.456, 0.392, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Platinum":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.429, 0.381, 0.314, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Pot":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.815, 0.831, 0.839, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.3)
            princi.inputs[8].default_value = (1)
            princi.inputs[9].default_value = (0.25)
        elif material == "Rhodium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.468, 0.381, 0.392, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Silver":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.93, 0.913, 0.831, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Tin":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.776, 0.776, 0.776, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Titanium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.262, 0.209, 0.165, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Tungsten":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.319, 0.319, 0.309, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Vanadium":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.407, 0.451, 0.429, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)
        elif material == "Zinc":
            princi = principled(material, active_mat, output)
            princi.inputs[0].default_value = (0.591, 0.546, 0.462, 1)
            princi.inputs[4].default_value = (1)
            princi.inputs[7].default_value = (0.1)



def principled(material, active_mat, output):
    principled = active_mat.node_tree.nodes.new("ShaderNodeBsdfPrincipled")
    principled.name = material
    principled.distribution = "MULTI_GGX"
    principled.subsurface_method = "RANDOM_WALK"
    active_mat.node_tree.links.new(principled.outputs[0], output.inputs[0])
    return principled


def rgb(principled, active_mat):
    rgbnode = active_mat.node_tree.nodes.new("ShaderNodeRGB")
    rgbnode.location = (-200, 0)
    active_mat.node_tree.links.new(rgbnode.outputs[0], principled.inputs[2])
    return rgbnode


def generate_categories(self, context):
    directory = os.path.join(os.path.dirname(__file__), "icons")
    modes = []
    for i, path in enumerate(sorted(os.listdir(directory))):
        modes.append((path, path, "", i))
    modes.sort()
    return modes


# Previews
def generate_previews(self, context):
    category = context.scene.pbr_materials.category
    directory = os.path.join(os.path.dirname(__file__), "icons/" + category)
    pcoll = materials_collection["main"]
    if directory == pcoll.images_location:
        return pcoll.material_icons
    # generate the thumbnails
    enum_items = []
    for i, image in enumerate(sorted(os.listdir(directory))):
        icon = pcoll.get(image)
        if not icon:
            filepath = os.path.join(directory, image)
            thumb = pcoll.load(image, filepath, 'IMAGE')
        else:
            thumb = pcoll[image]
        enum_items.append((image[:-4], image[:-4], "", thumb.icon_id, i))
    pcoll.material_icons = enum_items
    pcoll.images_location = directory
    bpy.context.window_manager['material_icons'] = 0
    return enum_items


# Properties
class PBRMaterialSettings(PropertyGroup):
    category : EnumProperty(
        items = generate_categories,
        description = "Type of material"
        )


#############################################################################################
materials_collection = {}

classes = (
    PBRMATERIAL_PT_Panel,
    PBRMaterialSettings
    )

register, unregister = bpy.utils.register_classes_factory(classes)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.pbr_materials = PointerProperty(type=PBRMaterialSettings)
    # icons
    WindowManager.material_icons = EnumProperty(
        name = "Icons",
        items = generate_previews,
        description = "Select a material",
        update = add_material
        )
    pcoll = bpy.utils.previews.new()
    pcoll.images_location = ""
    pcoll.material_icons = ()
    materials_collection["main"] = pcoll


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.pbr_materials
    # icons
    del WindowManager.material_icons
    for preview in materials_collection.values():
        bpy.utils.previews.remove(preview)
    materials_collection.clear()


if __name__ == "__main__":
    register()
