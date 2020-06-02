__author__ = "McRussian Andrey"
# -*- coding: utf8 -*-

from aiohttp import web
import aiohttp_jinja2
import datetime


async def MainPage(request: web.Request) -> web.Response:

    context = {
        'username': 'McRussian Andrey',
        'current_date': datetime.datetime.now().strftime("%Y.%m.%d")
    }
    response = aiohttp_jinja2.render_template("main.tmpl", request,
                                          context=context)

    return response
