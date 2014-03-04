from __future__ import print_function
import ast
import os
import codecs
from setuptools import setup


class VersionFinder(ast.NodeVisitor):
    def __init__(self):
        self.version = None

    def visit_Assign(self, node):
        if node.targets[0].id == '__version__':
            self.version = node.value.s


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*parts):
    finder = VersionFinder()
    finder.visit(ast.parse(read(*parts)))
    return finder.version


setup(
    name="ug",
    version=find_version("ug", "__init__.py"),
    url='https://github.com/python-glasgow/pythonglasgow',
    license='BSD',
    description="",
    long_description=read('README.rst'),
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com',
    packages=['ug', 'tests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)
