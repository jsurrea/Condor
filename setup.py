from setuptools import setup, find_packages
from setuptools.command.install import install

setup(
    name='Condor',
    version='1.0.0',
    author='Equipo Cóndor',
    author_email='k.arenas@uniandes.edu.co',
    description='Software y tecnología aérea, espacial y cibernética para la protección de la Amazonía',
    packages=find_packages(),
    install_requires=[
        'av',
        'torch',
        'torchvision',
        'numpy',
        'easyocr',
        'matplotlib',
        'opencv-python',
        'pandas',
        'scikit-learn',
        'flair',
        'beautifulsoup4',
    ],
)
