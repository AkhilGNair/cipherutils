from distutils.core import setup, Extension

module1 = Extension('ciputils', sources = ['cipherutils/ciputils.c'])

setup(name='cipherutils',
      version='1.0.1',
      description='CRC checker and fast hex2int',
      url='https://github.com/AkhilNairAmey/cipherutils',
      author='Akhil Nair',
      author_email='akhil.nair@amey.co.uk',
      license='MIT',
      packages=['cipherutils'],
      ext_modules = [module1])
