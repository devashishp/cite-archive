from distutils.core import setup

setup(
    name='CiteArchive',
    version='0.1.0',
    author='Dev Purandare',
    author_email='devashish@ucsc.edu',
    packages=['cite-archive', 'cite-archive.test'],
    scripts=['bin/cite-now.py'],
    license='LICENSE',
    description='Tool to help you archive and generate citation for web pages!',
    long_description=open('README.rst').read(),
    install_requires=[
        "newspaper3k >= 0.2.6",
    ],
)
