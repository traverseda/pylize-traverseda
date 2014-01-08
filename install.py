#!/usr/bin/env python

import os, sys

py_ver = "%i.%i" % sys.version_info[:2]

sys.stderr.write("Cleaning generated files...\n")
ret = os.system('python setup.py clean')
if ret == 0:
    sys.stderr.write("Running 'configure.py'...\n")
    ret = os.system('python configure.py %s' % (" ".join(sys.argv[1:]),))
if ret != 0:
    sys.stderr.write("Failed!")
    sys.exit(1)

sys.stderr.write("Running 'setup.py build'...\n")
ret = os.system('python setup.py build')
if ret != 0:
    sys.stderr.write("Failed!")
    sys.exit(1)

scripts1 = os.path.join('build', 'scripts')
scripts2 = os.path.join('build', 'scripts-%s' % py_ver)
if not os.path.exists(scripts2) or (os.path.exists(scripts1) and
  os.stat(scripts1)[8] > os.stat(scripts2)[8]):
    if os.path.exists(scripts2):
       try:
           import shutils
           shutils.rmtree(scripts2)
       except: pass
    try:
        os.symlink('scripts', scripts2)
    except:
        os.rename(scripts1, scripts2)
pylize_script=os.path.join(os.pardir, scripts2, 'pylize')
libdir = os.path.join(os.pardir, 'lib')

sys.stderr.write("Making documentation...\n")
os.chdir('doc')
cmd = 'python "%s" -s -L "%s"' % (pylize_script, libdir)
print cmd
ret = os.system(cmd)
os.chdir(os.pardir)
if ret != 0:
    sys.stderr.write("Failed. Re-check the installation.\n")
    sys.exit(1)
    sys.stderr.write("Ok. Open 'doc/index.html' in your browser to view the documentation.\n")

sys.stderr.write("Running 'setup.py install'...\n")
ret = os.system('python setup.py install')

if ret != 0:
   sys.stderr.write("""### Failed. #### Perhaps you have to be root to install.
Run: su -c "python%s setup.py install"\n""" % py_ver)
