import unittest2 as unittest
from pynwb import NWBFile
from datetime import datetime

import numpy as np

from .ecog_manual import ECoGSubject, CorticalSurfaces


class ECoGSubjectTest(unittest.TestCase):

    def test_init_ecog_subject(self):
        vertices = np.random.randn(20, 3)
        faces = np.random.randint(0, 20, (10, 3))

        nwbfile = NWBFile('description', 'id', datetime.now().astimezone())
        cortical_surfaces = CorticalSurfaces()
        cortical_surfaces.create_surface('test', vertices=vertices, faces=faces)
        nwbfile.subject = ECoGSubject(cortical_surfaces=cortical_surfaces)

        np.testing.assert_allclose(nwbfile.subject.cortical_surfaces.surfaces['test'].vertices, vertices)
        np.testing.assert_allclose(nwbfile.subject.cortical_surfaces.surfaces['test'].faces, faces)
