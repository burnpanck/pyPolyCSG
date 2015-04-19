from __future__ import division, print_function, absolute_import, unicode_literals

import numpy;
import pyPolyCSG as csg

A = csg.box( 1.0, 1.0, 1.0, True )

print('Mesh vertices:')
print(A.get_vertices())

print('Mesh triangles:')
print(A.get_triangles())
