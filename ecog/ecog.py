import os

from pynwb import load_namespaces
from to_nwb.auto_class import get_class, get_multi_container

filepath = os.path.realpath(__file__)
basedir, filename = os.path.split(filepath)
namespace = filename[:filename.find('.py')]

load_namespaces(os.path.join(basedir, namespace + '.namespace.yaml'))


Surface = get_class(namespace, 'Surface')

CorticalSurfaces = get_multi_container(namespace, 'CorticalSurfaces', Surface)
