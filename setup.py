#!/usr/bin/env python

from distutils.core import setup, Command
import shutil, os
from os.path import isdir, islink, join, dirname
from glob import glob

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
import sys
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup_data = dict(
    name="pylize",
    version="1.3b",
    description="On-Screen presentation generation tool",
    long_description="""
pylize is a Python script that generates a set of HTML files that
make up an on-screen presentation from a master file. The HTML files
can be viewed with any CSS-aware browser. The master file contains
the text for all the slides and some additional information like
title, author etc. pylize can also create a template master file for
you.
""",
    keywords="Presentation Slides HTML",
    author="Christopher Arndt",
    author_email="chris.arndt@web.de",
    url="http://www.chrisarndt.de/en/software/pylize/",
    download_url = \
      'http://chrisarndt.de/en/software/pylize/download/pylize-1.2b.tar.bz2',
    license="GPL",
    platforms='portable',
    classifiers = [
      'Intended Audience :: Education',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Multimedia :: Graphics :: Presentation',
      'Topic :: Text Processing :: Markup :: HTML'
    ],
    scripts=['pylize'],
    data_files=[
      ('', ['lib/default.tmpl', 'lib/all.tmpl', 'lib/pylize.js',
        'lib/index.tmpl', 'lib/pylize.ini', 'lib/logo.png', 'lib/roman.py']),
      ('css', glob('lib/css/*.css')),
      ('icons', glob('lib/icons/*.gif'))
    ],
)

def remove(file, force=True):
    try:
        os.unlink(file)
    except:
        if not force: raise

class clean(Command):

    user_options = []

    def run(self):
        dist_dir = os.path.dirname(sys.argv[0])
        doc_dir = join(dist_dir, 'doc')
        shutil.rmtree(join(dist_dir, 'dist'), True)
        shutil.rmtree(join(dist_dir, 'build'), True)
        doc_ccs_dir = join(doc_dir, 'css')
        if isdir(doc_ccs_dir):
            shutil.rmtree(doc_ccs_dir, True)
        elif islink(doc_ccs_dir):
            remove(doc_ccs_dir)
        doc_icons_dir = join(doc_dir, 'icons')
        if isdir(doc_icons_dir):
            shutil.rmtree(doc_icons_dir, True)
        elif islink(doc_icons_dir):
            remove(doc_icons_dir)
        for f in glob(join(doc_dir, '*.html')):
            if f != join(doc_dir, 'all.html'):
                remove(f)
        for f in [join(doc_dir, x) for x in ['pylize.js', 'logo.png',
          'keymap.js']]:
            remove(f)
        for f in [join(dist_dir, x) for x in ['MANIFEST', 'setup.cfg',
          'pylize']]:
            remove(f)

    def initialize_options(self): pass
    def finalize_options(self): pass


if __name__ == '__main__':
    setup(cmdclass={'clean': clean}, **setup_data)
