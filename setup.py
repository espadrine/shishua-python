from setuptools import setup, Extension
from Cython.Build import cythonize

shishua = Extension('shishuabinding',
    extra_compile_args = ['-march=native', '-g'],
    sources = ['src/binding/binding.pyx'],
    depends = [
        'src/binding/shishua.h',
        'src/binding/shishua-sse2.h',
        'src/binding/shishua-avx2.h',
        'src/binding/shishua-neon.h',
    ])

setup(ext_modules = cythonize([shishua]))
