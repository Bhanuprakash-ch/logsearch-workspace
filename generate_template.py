#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath
from os import environ
from sys import argv

THIS_DIR = dirname(abspath(__file__))
J2_ENV = Environment(loader=FileSystemLoader(THIS_DIR))

rendered_template = J2_ENV.get_template(argv[1]).render(environ)
with open('manifest.yml', 'w') as f:
  f.write(rendered_template)
