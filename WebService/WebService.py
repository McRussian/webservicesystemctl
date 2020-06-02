__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import datetime

from Logger import Logger
from ManagerService.ManagerService import ManagerService


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
        self._app.add_routes([web.get('/', self.ViewMainPage)])

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
