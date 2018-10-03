from setuptools import setup, find_packages

setup(
    name='sixfab_xbee',
    version='1.0',
    author='Yasin Kaya',
    author_email='yasinkaya.121@gmail.com',
    description='sixfab xbee library',
    license='MIT',
    url='https://github.com/sixfab/Sixfab_RPi_XBee_Library',
	install_requires  = ['pyserial'],
    packages=find_packages()
)
