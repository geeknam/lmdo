
from lmdo.cmds.cf.cloudformation import Cloudformation
from lmdo.cmds.lm.lambdaa import Lambda
from lmdo.cmds.api.apigateway import Apigateway
from lmdo.cmds.commands import Dispatcher, DeleteCommand
from lmdo.cmds.client_factory import ClientFactory
from lmdo.oprint import Oprint

class DestroyClient(ClientFactory):
    """Cloudformation command client"""
    def __init__(self, args):
        self._cloudformation = Cloudformation()
        self._lambda = Lambda()
        self._apigateway = Apigateway(args)
        self._dispatcher = Dispatcher()
        self._args = args

    def execute(self):
        Oprint.info('Start tear down service', 'lmdo')
        self._dispatcher.run(DeleteCommand(self._apigateway))
        self._dispatcher.run(DeleteCommand(self._lambda))
        self._dispatcher.run(DeleteCommand(self._cloudformation))
        Oprint.info('Service has been destroy', 'lmdo')


