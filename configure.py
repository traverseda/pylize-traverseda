#!/usr/bin/env python

import os, sys

if len(sys.argv) > 1:
    prefix = sys.argv[1]
    exec_prefix = prefix
else:
    prefix = sys.prefix
    exec_prefix = sys.exec_prefix

if os.name == 'nt':
    import _winreg
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
      r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    appdata = _winreg.QueryValueEx(key, 'Common AppData')[0]
    datadir = os.path.join(appdata, 'pylize')
else:
    appdata = os.path.join(prefix, 'share')
datadir = os.path.join(appdata, 'pylize')

sys.stderr.write("Configuring 'pylize'...\n")
t = open('pylize.in').read()

f = open('pylize', 'wb')
f.write(t.replace('@datadir@', datadir))
f.close()

f = open('setup.cfg', 'wb')
f.write("""[install]
prefix=%s
exec_prefix=%s
install-data=%s
""" % (prefix, exec_prefix, datadir))
f.close()
