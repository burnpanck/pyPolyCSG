import sys
from distutils.core import setup, Extension

# ==========================================================================
# Run the setup script =====================================================
# ==========================================================================
libraries = [ 'pyPolyCSG' ]

pyPolyCSG = Extension(
    'pyPolyCSG',
    sources='''
      source/mesh_functions.cpp
      source/mesh_io.cpp
      source/polyhedron_binary_op.cpp
      source/polyhedron_unary_op.cpp
      source/polyhedron.cpp
      source/triangulate.cpp
      source/python_wrapper.cpp
    '''.split(),
    define_macros=[('CSG_USE_CGAL','')],
    include_dirs=['include'],
    libraries = [
        'boost_python-py34' if sys.version_info[0]>=3 else 'boost_python-py27',
        'boost_thread',
        'python3.4m' if sys.version_info[0]>=3 else 'python2.7',
        'CGAL',
        'mpfr',
        'gmp',
        'pthread',
    ],
)
setup(
    name = 'pyPolyCSG',
    version = '1.0',
    ext_modules = [ pyPolyCSG ],
)