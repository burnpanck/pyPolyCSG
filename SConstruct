import os
import os.path as op
import glob

ROOT = os.path.abspath('.')

BOOST_VERSION = 'boost-1.54.0'
BOOST_PREFIX = op.join('/opt/',BOOST_VERSION)
BOOST_INCLUDE_DIRS = [op.join(BOOST_PREFIX,'include')]
BOOST_LIB_DIRS = [op.join(BOOST_PREFIX,'lib')]
BOOST_INCLUDE_DIRS = []
BOOST_LIB_DIRS = []

LIBS = [
    'boost_python-py34',
    'boost_thread',
    'python3.4m',
    'libCGAL',
    'mpfr',
    'gmp',
    'pthread',
]


env = Environment(
    CXX = 'clang++',
#    CXX = 'g++',
    LIBPATH=[]+BOOST_LIB_DIRS,
    CPPPATH=[
        'include',
        '/usr/include/python3.4m',
    ]+BOOST_INCLUDE_DIRS,
#    CPPFLAGS=['-std=c++11','-g', '-Wall', '-Wno-sign-compare']
    CPPFLAGS=['-std=c++11', '-g', '-O3', '-Wall', '-Wno-sign-compare']
)
if 'TERM' in os.environ:
    env['ENV']['TERM'] = os.environ['TERM']

SOURCES = '''
  source/mesh_functions.cpp
  source/mesh_io.cpp
  source/polyhedron_binary_op.cpp
  source/polyhedron_unary_op.cpp
  source/polyhedron.cpp
  source/triangulate.cpp
  source/python_wrapper.cpp
'''.split()

ex1 = env.SharedLibrary(
    target = 'pyPolyCSG',
    source = SOURCES,
    SHLIBPREFIX = '',
    LIBS = LIBS,
    CPPFLAGS=['-DCSG_USE_CGAL'],
)
