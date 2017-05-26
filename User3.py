__author__ = 'jomorais'

from pyfase import MicroService


class User3(MicroService):
    def __init__(self):
        super(User3, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.request_action('msg', {'msg': self.__class__.__name__})

    def on_broadcast(self, service, data):
        print('### on_broadcast ### service: %s - data: %s' % (service, data))

    @MicroService.action
    def msg(self, service, data):
        print data

User3().execute()
