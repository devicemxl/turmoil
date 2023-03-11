#
#  ████████╗██╗   ██╗██████╗ ███╗   ███╗ ██████╗ ██╗██╗     
#  ╚══██╔══╝██║   ██║██╔══██╗████╗ ████║██╔═══██╗██║██║     
#     ██║   ██║   ██║██████╔╝██╔████╔██║██║   ██║██║██║     
#     ██║   ██║   ██║██╔══██╗██║╚██╔╝██║██║   ██║██║██║     
#     ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║╚██████╔╝██║███████╗
#     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝╚══════╝
#      
import setuptools
#
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()
#
setuptools.setup(
    name='turmoil',
    version='0.0.1',
    description="Eliminates Pre-process and EDA's turmoil via Data Dictionary",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/devicemxl/turmoil/',
    author='David Ochoa',
    author_email='david@bajaanalytics.com',
    license='CC BY-NC-SA 4.0',
    zip_safe=False,
    #packages=find_packages(),
    #py_modules=['DataDictionary','operations'],
    #packages=find_packages('src', exclude=['test*']),
    #packages=['turmoil'],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.7"
)
# https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package
# https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

#python3 -m pip install --upgrade build