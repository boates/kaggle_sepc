kaggle_sepc
===========

Kaggle AMS 2013-2014 Solar Energy Prediction Contest

$1,000 on the table!

Team KGBD

kaggle_sepc
===========

Kaggle AMS 2013-2014 Solar Energy Prediction Contest

net-cdf4 installation instructions

Install HDF5 C library:
Go to ftp://ftp.hdfgroup.org/HDF5/current/src and download hdf5-1.8.11.tar.gz

 $ gunzip < hdf5-1.8.11.tar.gz | tar xf -
 $ cd hdf5-X.Y.Z
 $ ./configure --prefix=/usr/local/hdf5 --enable-hl --enable-shared
 $ make
 $ make check                # run test suite.
 $ make install
 $ make check-install        # verify installation.
 
 $export HDF5_DIR=/usr/local/hdf5

Install netcdf4 C library:

Go to ftp://ftp.unidata.ucar.edu/pub/netcdf and download netcdf-4.3.0.tar.gz
 $gunzip < netcdf-4.3.0.tar.gz | tar xf -
 $cd netcdf-4.3.0
 $export CPPFLAGS="-I$HDF5_DIR/include"
 $export LDFLAGS="-L$HDF5_DIR/lib"
 $./configure --enable-netcdf-4 --enable-shared
 $ make
 $ make check                # run test suite.
 $ make install
 $ make check-install        # verify installation.
 
Install python library
 $pip install netcdf4
