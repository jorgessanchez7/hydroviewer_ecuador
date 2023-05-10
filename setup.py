from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_all_resource_files
from tethys_apps.base.app_base import TethysAppBase

# -- Apps Definition -- #
app_package = 'hydroviewer_ecuador'
release_package = f'{TethysAppBase.package_namespace}-{app_package}'

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)

setup(
    name=release_package,
    version='2.0',
    description='',
    long_description='',
    keywords='"Hydrology", "GEOGloWS", "Hydroviewer", "Ecuador"',
    author='Jorge Luis Sanchez-Lozano, Karina Larco, Juseth E. Chancay',
    author_email='jorgessanchez7@gmail.com, karynina3@gmail.com, juseth.chancay@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)