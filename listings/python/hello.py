#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# get the journal
import journal

# your function
def hello():
    # make a channel
    channel = journal.info(name="isce3.ampcor.correlate")
    # say something
    channel.log("hello!")
    # all done
    return

# the main entry point
def main():
    # invoke
    hello()
    # indicate success, à la u*ix
    return 0

# bootstrap
if __name__ == "__main__":
    # invoke
    status = main()
    # share the exit code with the shell
    raise SystemExit(status)

# end of file
