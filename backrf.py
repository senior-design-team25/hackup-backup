#!/usr/bin/env python2

import sys
from subprocess import call

def init_ibss(dev, node, ssid, freq):
    print "attempting ibss connection..."
    call(["ip", "link", "set", "down", dev])
    call(["iw", dev, "set", "type", "ibss"])
    call(["ip", "link", "set", "up", dev])
    call(["ip", "addr", "flush", "dev", dev])
    call(["ip", "addr", "add", "10.0.0.%s/24" % int(node), "dev", dev])
    call(["iw", dev, "ibss", "join", ssid, freq])

def main(*state):
    init_ibss(*state)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print "usage: %s <device> <node> <ssid> <freq>" % sys.argv[0]
        print "for example: %s wlan0 12 testnetwork 2412" % sys.argv[0]
        exit(-1)

    main(*sys.argv[1:])
