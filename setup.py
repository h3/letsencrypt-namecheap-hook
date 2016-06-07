from distutils.core import setup

try:
    import setuptools
except ImportError:
    pass

setup(name='letsencrypt_namecheap_hook',
    version='0.0.1',
    author='Maxime Haineault',
    author_email='haineault@gmail.com',
    description='',
    long_description=open('README.md').read(),
    license='',
    url='https://github.com/h3/letsencrypt-namecheap-hook',
    packages=['namecheap'],
    scripts=['bin/letsencrypt-namecheap-hook'],
    install_requires=[],
)

