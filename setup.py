from setuptools import setup

setup(name='dsa110-caltools',
      version='0.2',
      url='http://github.com/dsa110/dsa110-caltools',
      packages=['caltools'],
      requirements=['astropy', 'astroquery', 'numpy'],
      zip_safe=False)
