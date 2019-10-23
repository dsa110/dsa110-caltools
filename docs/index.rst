.. dsa110-caltools documentation master file, created by
   sphinx-quickstart on Tue Oct 22 15:40:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dsa110-caltools
===========================================

dsa110-caltools has a module to help find calibrators and create calibration models.

It uses astroquery and NASA's HEASARC service to create radio catalogs. The NVSS catalog is a good starting point for the DSA band near 1.4 GHz. The nominal DSA field of view is 2 degrees.

Example usage::

    > from caltools import caltools
    > tab = caltools.get_calibrator_lists(202.78333, 30.50889)                                                                                                
    > print(tab)
    array([(202.78463, 30.509  , 14902.7), (201.56879, 31.90269,  4861.9),
    (201.88213, 31.85758,  1415.1), (200.75971, 29.69278,  1368.5),
    (202.47021, 31.90322,   829. ), (202.1025 , 30.74183,   595.7),
    (203.66   , 31.60764,   523.8)],
    dtype=[('ra', '<f8'), ('dec', '<f8'), ('flux', '<f8')])



Useful Functions
-----
.. autofunction:: caltools.caltools.list_calibrators
.. autofunction:: caltools.caltools.get_calibrator_lists
.. autofunction:: caltools.caltools.query_heasarc
		  
* :ref:`genindex`
