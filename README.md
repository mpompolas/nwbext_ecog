# nwbext_ecog
An NWB extension for ECoG data

There are two data types, `Surface` and `CorticalSurfaces`. `CorticalSurfaces` is simply a group (like a folder) to put `Surface` objects into. `Surface` holds surface mesh data (vertices and triangular faces) for sections of cortex.

## Usage

### python
```python
import pynwb
from nwbext_ecog.ecog_manual import CorticalSurfaces

nwbfile = pynwb.NWBFile(...)

...

cortical_surfaces = CorticalSurfaces()
## loop me
    cortical_surfaces.create_surface(name='...', faces=faces, vertices=veritices)
##
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
surf = types.ecog.Surface('faces', faces, 'vertices', vertices);
cortical_surfaces.surface.set('cortical_surfaces', surf);
%%%

file.acquisition.set('CorticalSurfaces', cortical_surfaces);

```


Author: Ben Dichter
