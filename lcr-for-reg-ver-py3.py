#/usr/bin/env python

import re
import subprocess
import sys

posver = sys.argv[1]

def lcrinfo(ver):
    regcmd = "git log -n 1 lcr-{}".format(ver)
    lcrout =subprocess.check_output(regcmd, shell=True)
    print("| " + "\n| ".join(lcrout.split("\n")[:3]))


#iOS

print "\n# iOS: {}".format(posver)
regcmd = "git archive --remote=git@git.sqcorp.co:IOS/Register converge/register-{} Podfile.lock | tar -xOf - ".format(posver)
regoutput =subprocess.check_output(regcmd, shell=True)

sqrdrver = re.search("SquareReader \(([0-9\.]*)\)", regoutput).groups()[0]
print "SquareReader", sqrdrver

sqrdcmd = "git archive --remote=git@git.sqcorp.co:IOS/squarereader podify/SquareReader/{} BuildNumber.lock | tar -xOf -".format(sqrdrver)
lcrver = subprocess.check_output(sqrdcmd, shell=True).strip()
if not lcrver:
    sqrdcmd = "git archive --remote=git@git.sqcorp.co:IOS/squarereader podify/{} BuildNumber.lock | tar -xOf -".format(sqrdrver)
    lcrver = subprocess.check_output(sqrdcmd, shell=True).strip()
print "LCR:", lcrver
lcrinfo(lcrver)

#Android

print "\n# Android: {}".format(posver)
regcmd = "git archive --remote=git@git.sqcorp.co:ANDROID/register green-release_android_register_{} dependencies.gradle | tar -xOf -".format(posver)
regoutput =subprocess.check_output(regcmd, shell=True)

sqrdrver = re.search("rikerVersion = '([0-9a-f_-]*)'", regoutput).groups()[0]
print "SquareReader", sqrdrver

sqrdcmd = "git archive --remote=git@git.sqcorp.co:ANDROID/squarereader-android release-{} build.gradle | tar -xOf -".format(posver)
regoutput =subprocess.check_output(sqrdcmd, shell=True)
lcrver = re.search("lcrVersion = '([0-9\.]*)'", regoutput).groups()[0]
print "LCR:", lcrver
lcrinfo(lcrver)