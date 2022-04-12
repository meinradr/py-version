"""`version-semantic` lives on `GitHub <https://github.com/meinradr/version-semantic>`_."""
from setuptools import setup

from version_semantic import __version__


with open('README.md') as f:
    long_description = f.read()

setup(
    name='version-semantic',
    version=__version__,
    author='Meinrad Ruckstuhl',
    author_email='code_copyright@ruckme.ch',
    description='Implementation of semantic version',
    license='MIT',
    keywords='semver semantic version versioning versions',
    url='https://github.com/meinradr/version-semantic',
    py_modules=['version_semantic'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities'
    ]
)
