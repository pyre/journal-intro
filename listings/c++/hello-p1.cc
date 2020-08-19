// -*- c++ -*-

// externals
#include <pyre/journal.h>

// your function
auto hello() {
    // make a channel
    pyre::journal::info_t channel("isce3.ampcor.correlate");
    // say something
    channel
        << pyre::journal::at(__HERE__)
        << "hello!"
        << pyre::journal::endl;
    // all done
    return;
}

// the main entry point
int main() {
    // invoke your function
    hello();
    // indicate success, à la u*ix
    return 0;
}

// end of file
