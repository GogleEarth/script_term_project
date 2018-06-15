from distutils.core import setup


files = ['Spammodule.pyd']

setup(name='Atmosphere',
version='1.0',
packages=['script_term_project'],
package_data = {'script_term_project' : files },
)
