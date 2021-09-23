from setuptools import setup

setup(name='dsa110-catalogs',
      version='0.2',
      url='http://github.com/dsa110/dsa110-catalogs',
      packages=['catalogs'],
      requirements=['astropy', 'astroquery', 'numpy'],
      zip_safe=False)
