import sys, re

def main(args):
    try:
        file = args.pop(0)
    except IndexError:
        print "Usage: fixtemplate.py FILE"
        sys.exit(0)
    fp = open(file)
    text = fp.read()
    fp.close()
    rx = re.compile('{(.*?)}', re.DOTALL)
    text = rx.sub(lambda x: "@(%s)" % x.group(1), text)
    fp = open(file, 'w')
    fp.write(text)
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
