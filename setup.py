from setuptools import setup, find_packages

install_requires = (
)

setup(
    name='loltree',
    version='0.0.0',
    description='loltree',
    author='dmr',
    author_email='dradetsky@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    license='WTFPL',
)
