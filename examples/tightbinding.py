#!/usr/bin/env python3

import sys
sys.path.append("../")

from bandstructure import Parameters
from bandstructure.system import TightBindingSystem
from bandstructure.lattice import SquareLattice

lattice = SquareLattice()

params = Parameters({
    'lattice': lattice,
    'cutoff': 2.1,
    't': 1,
    't2': 0
})

s = TightBindingSystem(params)

path = lattice.getKvectorsPath(300, ['A', 'G', 'X', 'A'])

bandstructure = s.solve(path)
bandstructure.plot("dispersion.pdf")
