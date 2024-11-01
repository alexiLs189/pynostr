from setuptools import setup, find_packages

setup(
    name='pynostrv2',
    use_scm_version={'write_to': 'pynostr/_version.py'},
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=[
    ],
    author='alexiLs189',
    description='pynostr with async publishing',
    url='https://github.com/alexiLs189/pynostr.git', 
    python_requires='>=3.6',
)

