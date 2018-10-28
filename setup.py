from setuptools import setup
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)


setup(
    name='gitkeep',
    version='0.1',
	description="A tiny utility to force empty directories into a Git repo.",
	long_description='README',
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
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gitkeep=gitkeep:gitkeep
    ''',
)
