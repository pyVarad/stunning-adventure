#!/usr/bin/env python


from twisted.internet import reactor


if __name__ == "__main__":
    print "Running the reactor..."
    reactor.run()
    print "Reactor stopped."
