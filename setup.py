from setuptools import setup
setup(name='turmoil',
version='0.0.1',
packages=find_packages('src', exclude=['test']),
description="Eliminates Pre-process and EDA's turmoil via Data Dictionary",
url='https://github.com/devicemxl/turmoil/',
author='David Ochoa',
author_email='david@bajaanalytics.com',
license='CC BY-NC-SA 4.0',
#packages=['turmoil'],
zip_safe=False)
