from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-Corpus',
    version='1.0.24',
    packages=['Corpus'],
    url='https://github.com/StarlangSoftware/Corpus-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Corpus library',
    install_requires=['NlpToolkit-Dictionary'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
