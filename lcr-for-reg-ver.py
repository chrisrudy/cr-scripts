#/usr/bin/env python

# Original code here: https://git.sqcorp.co/snippets/6263e0ec11dd4acc9e86b90f673f75d0

import re
import subprocess
import sys

posver = sys.argv[1]

def lcrinfo(ver):
    regcmd = "git log -n 1 lcr-{}".format(ver)
    lcrout = subprocess.check_output(regcmd, shell=True)
    lcrdecode = lcrout.decode('utf-8')
    print("| " + "\n| ".join(lcrdecode.split("\n")[:3]))


#iOS

print("\n# iOS: {}".format(posver))
regcmd = "git archive --remote=git@git.sqcorp.co:IOS/Register converge/register-{} Podfile.lock | tar -xOf - ".format(posver)
regoutput = subprocess.check_output(regcmd, shell=True)
outputstring = regoutput.decode('utf-8')

sqrdrver = re.search("SquareReader \(([0-9\.]*)\)", outputstring).groups()[0]
print("SquareReader", sqrdrver)

sqrdcmd = "git archive --remote=git@git.sqcorp.co:IOS/squarereader podify/SquareReader/{} BuildNumber.lock | tar -xOf -".format(sqrdrver)
lcrver = subprocess.check_output(sqrdcmd, shell=True).strip()
if not lcrver:
    sqrdcmd = "git archive --remote=git@git.sqcorp.co:IOS/squarereader podify/{} BuildNumber.lock | tar -xOf -".format(sqrdrver)
    lcrver = subprocess.check_output(sqrdcmd, shell=True).strip()
outputdecode = lcrver.decode('utf-8')
print("LCR:", outputdecode)
lcrinfo(outputdecode)

#Android

print("\n# Android: {}".format(posver))
regcmd = "git archive --remote=git@git.sqcorp.co:ANDROID/register green-release_android_register_{} dependencies.gradle | tar -xOf -".format(posver)
regoutput =subprocess.check_output(regcmd, shell=True)
regdecode = regoutput.decode('utf-8')

sqrdrver = re.search("rikerVersion = '([0-9a-f_-]*)'", regdecode).groups()[0]
print("SquareReader", sqrdrver)

sqrdcmd = "git archive --remote=git@git.sqcorp.co:ANDROID/squarereader-android release-{} build.gradle | tar -xOf -".format(posver)
regoutput =subprocess.check_output(sqrdcmd, shell=True)
decodeoutput = regoutput.decode('utf-8')
lcrver = re.search("lcrVersion = '([0-9\.]*)'", decodeoutput).groups()[0]
print("LCR:", lcrver)
lcrinfo(lcrver)
