#!/usr/bin/env python


from twisted.internet import reactor
import datetime


def printTime():
    print datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


def stopReactor():
    reactor.stop()


if __name__ == "__main__":
    reactor.callLater(1, printTime)
    reactor.callLater(10, printTime)
    reactor.callLater(10, printTime)
    reactor.callLater(10, printTime)
    reactor.callLater(10, stopReactor)

    print "Running the reactor."
    reactor.run()
    print "Reactor stopped."
