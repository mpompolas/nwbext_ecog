# nwbext_ecog
An NWB extension for ECoG data

There are two data types, `Surface` and `CorticalSurfaces`. `CorticalSurfaces` is simply a group (like a folder) to put `Surface` objects into. `Surface` holds surface mesh data (vertices and triangular faces) for sections of cortex.

## Usage

### python
```python
import pynwb
ecog_ext = pynwb.extensions['ecog']
Surface = ecog_ext.Surface
CorticalSurfaces = ecog_ext.CorticalSurfaces

nwbfile = pynwb.NWBFile(...)


...

meshes = ...

cortical_surfaces = CorticalSurfaces(source='...')
for mesh in range(meshes):
    cortical_surfaces.add_surface(name='...', source='...',faces=mesh.faces, vertices=mesh.veritices)

nwbfile.add_acquisition(cortical_surfaces)
```

### MATLAB
to install:
```matlab
generateExtension('/path/to/nwbext_ecog/nwbext_ecog/ecog.namespace.yaml');
```

to use:
```matlab
cortical_surfaces = types.ecog.CorticalSurfaces;

%%% loop me
surf = types.ecog.Surface('source', mesh_file, ...
        'faces', faces, 'vertices', vertices);
cortical_surfaces.surface.set('surf_name', surf);
%%%

file.acquisition.set('CorticalSurfaces', cortical_surfaces);

```


Author: Ben Dichter
