#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved

"""
Hardwired output to a file
"""

# get the journal
import journal

# your function
def hello():
    # make a channel
    channel = journal.info("isce3.ampcor.correlate")
    # say something
    channel.log("hello!")
    # all done
    return

# your application main entry point
def main():
    # invoke
    hello()
    # all done
    return

# bootstrap
if __name__ == "__main__":
    # send all output to a logfile
    journal.logfile("hello.log")
    # invoke
    status = main()
    # share the exit code with the shell
    raise SystemExit(status)

# end of file
