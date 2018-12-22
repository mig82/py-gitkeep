import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name='gitkeep2',
    version='1.0.0',
	description="A tiny utility to force empty directories into a Git repo.",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url='https://github.com/mig82/py-gitkeep',
	author='Miguelangel Fernandez',
	author_email='miguelangelxfm@gmail.com',
    py_modules=['gitkeep'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Version Control :: Git',
		'Topic :: Utilities'
	],
    packages=setuptools.find_packages(),
    entry_points='''
        [console_scripts]
        gitkeep=gitkeep:gitkeep
    '''
)
