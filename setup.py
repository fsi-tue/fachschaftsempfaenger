from setuptools import setup

pkg = __import__('fachschaftsempfaenger')

author =  pkg.__author__
email = pkg.__author_email__

version = pkg.__version__
classifiers = pkg.__classifiers__

description = pkg.__description__

def load_requirements(fn):
    """Read a requirements file and create a list that can be used in setup."""
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name='fachschaftsempfaenger',
    version=version,
    license='MIT',
    description=description,
    long_description=open('README.rst').read(),
    author=author,
    author_email=email,
    url='https://github.com/fsi-tue/fachschaftsempfaenger',
    classifiers=classifiers,
    platforms='Linux',
    packages=['fachschaftsempfaenger'],
    install_requires=load_requirements('requirements.txt')
)
