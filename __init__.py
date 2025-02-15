import bpy

from . import mipanel
from .operaciones.alinear import superaliniar
from .operaciones.exportar import exportarindice
from .operaciones.exportarextras import exportarextra
from .operaciones.indice import superindice
from .operaciones.macros import add_hotkey, remove_hotkey
from .operaciones.mover import moverclip
from .operaciones.sobreponeraudio import sobreponeraudio
from .operaciones.superinsertar import superinsertar
from .operaciones.zoon import superzoon

bl_info = {
    "name": "ALSW_Plugin_Blender",
    "author": "ChepeCarlos",
    "description": "Heramientas Extra para Sequencer",
    "blender": (2, 93, 5),
    "version": (0, 0, 6),
    "license": "GPL",
    "location": "Sequencer",
    "warning": "",
    "category": "Sequencer",
}

classes = [
    sobreponeraudio,
    superinsertar,
    superaliniar,
    superzoon,
    moverclip,
    superindice,
    exportarextra,
    exportarindice,
    mipanel.mi_PT_panel
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    add_hotkey()


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    remove_hotkey()
