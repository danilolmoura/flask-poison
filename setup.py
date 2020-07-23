"""
Flask-Poison
-------------

This is the description for that library
"""
from setuptools import setup

setup(
    name='Flask-Poison',
    version='0.0.0',
    url='http://poison.readthedocs.org/en/latest/',
    license='MIT',
    author='Danilo Moura',
    author_email='danilolmoura@gmail.com',
    description='Flask extension to build RESTful APIs',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    py_modules=['flask_poison'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)