__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
from .WebServiceView.views import MainPage

class WebService:
    _app = None
    def __init__(self):
        self._app = web.Application()
        path = os.path.join(os.path.dirname(__file__), "Templates")
        print(path)
        aiohttp_jinja2.setup(
            self._app,
            loader = jinja2.FileSystemLoader(path)
        )
        self._app.add_routes([web.get('/', MainPage)])

    def Start(self):
        web.run_app(self._app)





