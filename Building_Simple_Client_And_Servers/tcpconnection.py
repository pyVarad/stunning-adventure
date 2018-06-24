#!/usr/bin/env python


from twisted.internet import reactor, protocol


class QuickDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        print "Connected successfully. %s" % self.transport.getPeer().host
        self.transport.loseConnection()


class BasicConnectionFactory(protocol.ClientFactory):
    protocol = QuickDisconnectProtocol

    def clientConnectionFailed(self, connector, reason):
        print "Connection Failed - %s", reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection Lost - %s" % reason.getErrorMessage()
        reactor.stop()


if __name__ == "__main__":
    reactor.connectTCP('www.google.com', 80, BasicConnectionFactory())
    reactor.run()
