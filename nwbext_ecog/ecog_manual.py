import os

from collections import Iterable

import numpy as np
from pynwb import load_namespaces, register_class, docval
from pynwb.core import NWBContainer, MultiContainerInterface
from pynwb.form.utils import popargs

filepath = os.path.realpath(__file__)
basedir = os.path.split(filepath)[0]
name = 'ecog'

load_namespaces(os.path.join(basedir, name + '.namespace.yaml'))


@register_class('Surface', 'ecog')
class Surface(NWBContainer):
    __nwbfields__ = ('faces', 'vertices')

    @docval({'name': 'name', 'type': str, 'doc': 'name'},
            {'name': 'vertices', 'type': Iterable, 'shape': (None, 3),
             'doc': 'vertices for surface, points in 3D space'},
            {'name': 'faces', 'type': Iterable, 'shape': (None, 3),
             'doc': 'faces for surface, indexes vertices'})
    def __init__(self, **kwargs):
        name, vertices, faces = popargs('name', 'vertices', 'faces', kwargs)
        super(Surface, self).__init__(name)
        if np.max(faces) >= len(vertices):
            raise ValueError('index of faces exceeds number vertices for {}. '
                             'Faces should be 0-indexed, not 1-indexed'.
                             format(name))
        if np.min(faces) < 0:
            raise ValueError('faces hold indices of vertices and should be non-negative')
        self.faces = faces
        self.vertices = vertices


@register_class('CorticalSurfaces', 'ecog')
class CorticalSurfaces(MultiContainerInterface):
    """
    Spike data for spike events detected in raw data
    stored in this NWBFile, or events detect at acquisition
    """

    __clsconf__ = {
        'attr': 'surfaces',
        'type': Surface,
        'add': 'add_surface',
        'get': 'get_surface',
        'create': 'create_surface'
    }

    __help = "triverts for cortical surfaces"
