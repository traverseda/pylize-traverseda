This is a fork of pylize for my personal usage. To use the original, go to http://www.chrisarndt.de/software/pylize/

WHAT IS IT?:

pylize is a Python script that generates a set of HTML files that make up an
on-screen presentation from a master file. The HTML files can be viewed with
any CSS-aware browser. The master file contains the text for all the slides and
some additional information like title, author etc. pylize can also create a
template master file for you.


DOWNLOAD:

    <http://www.chrisarndt.de/software/pylize/>


INSTALL:

pylize should run on all platforms where Python does (though only tested on
Linux + Windows).

First get and install empy:

    <http://www.alcyone.com/software/empy/>

Optionally, install the Python Imaging Library (PIL). It is included in most
Linux distributions now (look for a 'python-imaging' package).

    <http://www.pythonware.com/products/pil/index.htm>

Then for all platforms:

    $ python ./install.py

(you may need to 'su' before this)


USAGE:

First you should make a new directory for your presentation:

    $ mkdir new_pres
    $ cd new_pres

Then create a template for your presentation master file:

    $ pylize [--lang=<lang>] create       # The default language is taken
    wrote: "all.html"                     # from your environment

Then edit the master file 'all.html'. It is an ordinary HTML file with some
special meta tags. The comments in it tell you what to edit.

If you specified a URL for a logo, copy it to the right place. In most cases
this should be your presentation directory.

Now, generate your presentation:

    > pylize [-v] [--lang=<lang>]         # The -v flag makes pylize show
    wrote: "toc.html"                     # the values used for the generation
    wrote: "slide_01.html"                # of the slides
    ...
    wrote: "slide_nn.html"

This also copies an index and some auxiliary files to your presentation
directory. They don't get overwritten next time you run pylize, so you can
customize them to your needs.

To view your presentation load the file 'index.html' in your favourite
CSS-aware browser.


AUTHOR:

    Christopher Arndt <chris.arndt@web.de>


CREDITS:

    pylize is a Python-clone of:

    PLies <http://www.rot13.org/~dpavlin/presentations/XLSies_to_PLies/>
    by Dobrica Pavlinusic <dpavlin@rot13.org>

    which is in turn inspired by:

    XLies <http://lempinen.net/sami/xslies/>
    by Sami Lempinen

    and:

    W3C SlideMaker <http://www.w3.org/Talks/slidemaker/YYMMsub/>
    by Stephan Montigaud, Pierre Fillault <webreq@w3.org> and
    Masayasu Ishikawa <mimasa@w3.org>

THANKS:

    - to Heiko Schiffer for reporting compapility problems with IE 6 and the
      JavaScript keyboard event handling and helping fixing it.
