#
#  ████████╗██╗   ██╗██████╗ ███╗   ███╗ ██████╗ ██╗██╗     
#  ╚══██╔══╝██║   ██║██╔══██╗████╗ ████║██╔═══██╗██║██║     
#     ██║   ██║   ██║██████╔╝██╔████╔██║██║   ██║██║██║     
#     ██║   ██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║██║██║     
#     ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║╚██████╔╝██║███████╗
#     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚══════╝
#      
from setuptools import setup, find_packages
#
setup(
    name='turmoil',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['DataDictionary','operations'],
    #packages=find_packages('src', exclude=['test*']),
    #packages=['turmoil'],
    description="Eliminates Pre-process and EDA's turmoil via Data Dictionary",
    url='https://github.com/devicemxl/turmoil/',
    author='David Ochoa',
    author_email='david@bajaanalytics.com',
    license='CC BY-NC-SA 4.0',
    zip_safe=False,
)
# https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package
# https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/