import sys
from setuptools import setup

extra = {}

setup(
    name='fastforms',
    use_scm_version=VERSIONING,
    setup_requires=['setuptools_scm'],
    install_requires=REQUIREMENTS
    url='',
    license='MIT',
    author='Alexander Kaftan',
    author_email='devkral@web.de',
    description='A flexible forms validation library for python web development.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'fastforms',
        'fastforms.fields',
        'fastforms.form',,
    ],
    package_data={
        'fastforms': ['locale/fastforms.pot', 'locale/*/*/*'],
    },
    test_suite='tests.runtests',
)
