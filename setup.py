from distutils.core import setup

setup(
    name='gwpy-mongodb-common',
    version='0.1',
    packages=['mongodb_common'],
    url='https://github.com/sertoltof/gwpy-mongodb-common',
    license='MIT',
    author='Garrick White',
    author_email='white.garrick935@gmail.com',
    description='common mongodb code',
    requires=['pymongo']
)
