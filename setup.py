# vim: set fenc=utf8 ts=4 sw=4 et :
from configparser import ConfigParser
from setuptools import setup, find_packages

conf = ConfigParser()
conf.read('conf.ini')

# I really prefer Markdown to reStructuredText. PyPi does not.
# from: https://coderwall.com/p/qawuyq/use-markdown-readme-s-in-python-modules
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst', format='markdown')
    long_description = long_description.replace('\r','')
    with open('README.rst', 'w') as f:
        f.write(long_description)
except (OSError, ImportError):
    print('Pandoc not found. Long_description conversion failure.')
    # pandoc is not installed, fallback to using raw contents
    with open('README.md', 'r') as f:
        long_description = f.read()

# Setup the project
setup(
    name = 'pdml2flow-{}'.format(
        conf['DEFAULT']['plugin_name']
    ),
    keywords = 'pdml2flow plugin',
    version = '0.1',
    packages = find_packages(exclude=['test']),
    install_requires = [
        'pdml2flow',
    ],
    entry_points= {
        'pdml2flow.plugins': '{} = plugin.plugin:Plugin'.format(
            conf['DEFAULT']['plugin_name']
        ),
    },
    # metadata
    author = 'Author Name',
    author_email = 'email@somwhere.com',
    description = 'Plugin skeleton',
    long_description = long_description,
    include_package_data = True,
    license = 'Apache 2.0',
    url = 'https://github.com/Username/pdml2flow-plugin-skeleton',
)
