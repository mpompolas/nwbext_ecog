from datetime import datetime

import numpy as np
import unittest2 as unittest
from pynwb import NWBFile, NWBHDF5IO

from .ecog_manual import ECoGSubject, CorticalSurfaces


class ECoGSubjectTest(unittest.TestCase):

    def setUp(self):
        self.vertices = np.random.randn(20, 3)
        self.faces = np.random.randint(0, 20, (10, 3))
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_init_ecog_subject(self):

        cortical_surfaces = CorticalSurfaces()
        cortical_surfaces.create_surface('test', vertices=self.vertices, faces=self.faces)
        self.nwbfile.subject = ECoGSubject(subject_id='id', cortical_surfaces=cortical_surfaces)

        np.testing.assert_allclose(self.nwbfile.subject.cortical_surfaces.surfaces['test'].vertices, self.vertices)
        np.testing.assert_allclose(self.nwbfile.subject.cortical_surfaces.surfaces['test'].faces, self.faces)

    def test_add_cs_to_ecog_subject(self):

        cortical_surfaces = CorticalSurfaces()
        cortical_surfaces.create_surface('test', vertices=self.vertices, faces=self.faces)
        self.nwbfile.subject = ECoGSubject()
        self.nwbfile.subject.cortical_surfaces = cortical_surfaces

    def test_io(self):

        cortical_surfaces = CorticalSurfaces()
        cortical_surfaces.create_surface('test', vertices=self.vertices, faces=self.faces)
        self.nwbfile.subject = ECoGSubject(subject_id='id', cortical_surfaces=cortical_surfaces)

        with NWBHDF5IO('test.nwb', 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO('test.nwb', 'r') as io:
            nwbfile = io.read()
            np.testing.assert_allclose(
                self.nwbfile.subject.cortical_surfaces.surfaces['test'].vertices,
                nwbfile.subject.cortical_surfaces.surfaces['test'].vertices)
            np.testing.assert_allclose(
                self.nwbfile.subject.cortical_surfaces.surfaces['test'].faces,
                nwbfile.subject.cortical_surfaces.surfaces['test'].faces)
