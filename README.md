# nwbext_ecog
An NWB extension for ECoG data

There are two data types, `Surface` and `CorticalSurfaces`. `CorticalSurfaces` is simply a group (like a folder) to put `Surface` objects into. `Surface` holds surface mesh data (vertices and triangular faces) for sections of cortex.

## Usage

```python
from pynwb.extensions.ecog import Surface, CorticalSurfaces

cortical_surfaces = CorticalSurfaces(source='...')
for i in range(meshes):
    cortical_surfaces.add_surface(name='...', source='...',faces=..., vertices=...)

nwbfile.add_acquisition(cortical_surfaces)
```


Author: Ben Dichter