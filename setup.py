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
    py_modules=['plot','munging'],
    #packages=find_packages('src', exclude=['test*']),
    #packages=['turmoil'],
    description="Eliminates Pre-process and EDA's turmoil via Data Dictionary",
    url='https://github.com/devicemxl/turmoil/',
    author='David Ochoa',
    author_email='david@bajaanalytics.com',
    license='CC BY-NC-SA 4.0',
    zip_safe=False,
)
