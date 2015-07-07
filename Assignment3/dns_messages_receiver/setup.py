import os.path
import setuptools

import dmr

app_path = os.path.dirname(dmr.__file__)

with open(os.path.join(app_path, 'resources', 'README.rst')) as f:
      long_description = map(lambda s: s.strip(), f)

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = map(lambda s: s.strip(), f)

setuptools.setup(
    name='dmr',
    version=dmr.__version__,
    description="Receive DNS messages from a proprietary relay",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Dustin Oprea',
    author_email='dustin@openpeak.com',
    url='',
    license='GPL 2',
    packages=setuptools.find_packages(exclude=['dev']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    package_data={
        'dmr': [
            'resources/README.rst',
            'resources/requirements.txt'
            'resources/data/gunicorn*', 
        ],
    },
    scripts=[
        'dmr/resources/scripts/dmr_db_model_dns_message_print_by_hour',
        'dmr/resources/scripts/dmr_db_provision',
        'dmr/resources/scripts/dmr_server_dev',
        'dmr/resources/scripts/dmr_server_prod',
    ],
)
