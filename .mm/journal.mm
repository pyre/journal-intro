# -*- Makefile -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# journal contains a "test suite"
journal.contentTypes := tests

# the journal sample listings are the "test suite"
journal.tests := examples

# set it up
examples.root := listings/
# externals
examples.extern := pyre
# c++ compiler flags
examples.c++.flags += -Wall $($(compiler.c++).std.c++17)


# clean up
listings.c++.clean += *.log
listings.logfile-p1.clean += *.log
listings.logfile-p2.clean += *.log
listings.pfg-p1.clean += *.log
listings.python.clean += *.log


# end of file
