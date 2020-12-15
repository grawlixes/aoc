#!/usr/bin/python3

import sys

dir = sys.argv[1]
rawCurl = open(dir + "/rawCurl.txt", 'r').readlines()
sampleInputFile = open(dir + "/sampleInput.txt", 'w')

# look for <pre><code> - generally the first instance of this tag contains the example code.
# exits after we exit the first instance of these tags, or if we don't find them at all
# sometimes we have multiple pairs of these tags, but they aren't usually other samples in my experience
on = False
for line in rawCurl:
    if line[:11] == "<pre><code>":
        on = True
        line = line[11:]
    elif line[:13] == "</code></pre>":
        break
    if on:
        sampleInputFile.write(line)

