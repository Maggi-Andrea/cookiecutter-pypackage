#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

import re

from pathlib import Path  # noqa

# -*- Distribution Meta -*-

re_meta = re.compile(r'__(\w+?)__\s*=\s*(.*)')
re_doc = re.compile(r'^"""(.+?)"""')

def add_default(m):
    attr_name, attr_value = m.groups()
    return ((attr_name, attr_value.strip("\"'")),)


def add_doc(m):
    return (('doc', m.groups()[0]),)

pats = {re_meta: add_default, re_doc: add_doc}
here = Path(__file__).parent.absolute()
with open(here / {{ cookiecutter.project_slug }} / '__init__.py') as meta_fh:
  meta = {}
  for line in meta_fh:
    if line.strip() == '# -eof meta-':
      break
    for pattern, handler in pats.items():
      m = pattern.match(line.strip())
      if m:
        meta.update(handler(m))


with open('README.rst') as readme_file:
  readme = readme_file.read()

with open('HISTORY.rst') as history_file:
  history = history_file.read()

requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %} ]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest>=3',{%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
  name=meta['project'],
  description="{{ cookiecutter.project_short_description }}",
  version=meta['version'],
  author=meta['author'],
  author_email=meta['email'],
  url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_folder }}',
  python_requires='>=3.7',
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
    '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
{%- if 'no' not in cookiecutter.command_line_interface|lower %}
  entry_points={
    'console_scripts': [
      '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
    ],
  },
{%- endif %}
  install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
  license="{{ cookiecutter.open_source_license }}",
{%- endif %}
  long_description=readme + '\n\n' + history,
  include_package_data=True,
  keywords='{{ cookiecutter.project_slug }}',
  packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    
  setup_requires=setup_requirements,
    
  test_suite='tests',
  tests_require=test_requirements,
  zip_safe=False,
)
