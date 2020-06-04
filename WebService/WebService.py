__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import datetime

from Logger import Logger
from ManagerService.ManagerService import ManagerService
from ManagerService.ServiceException import ServiceException


class WebService:
    _app = None
    _manager = None
    _logger = None
    def __init__(self, manager: ManagerService, logger: Logger):
        self._app = web.Application()
        self._logger = logger
        self._manager = manager
        path = os.path.join(os.path.dirname(__file__), "Templates")
        print(path)
        aiohttp_jinja2.setup(
            self._app,
            loader = jinja2.FileSystemLoader(path)
        )
        self._app.add_routes([web.get('/', self.ViewMainPage),
                              web.get('/{servicename}/{command}', self.ManagedService)])

    def Start(self):
        web.run_app(self._app)

    async def ViewMainPage(self, request: web.Request) -> web.Response:

        context = {
            'current_date': datetime.datetime.now().strftime("%Y.%m.%d"),
            'ls_service': self._manager.GetListService()
        }
        response = aiohttp_jinja2.render_template("main.tmpl", request,
                                              context=context)

        return response

    async def ManagedService(self, request):
        servicename = request.match_info.get("servicename", None)
        command = request.match_info.get("command", None)
        try:
            self._manager.RunCommand(servicename=servicename, command=command)
            raise web.HTTPFound('/')
        except ServiceException as err:
            self._logger.Message(err.GetErrorMessage(), 'error')
            raise web.HTTPNotFound(
                    text="<html>\n  <body>\n        " + err.GetErrorMessage() +
                         "\n  </body>\n</html>",
                    content_type="text/html")

