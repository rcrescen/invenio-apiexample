# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 rcrescenz@gmail.com.
#
# Invenio-APIExample is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Ejemplo de API para invenio"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    'invenio_apiexample',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Render a basic view."""
    return render_template(
        "invenio_apiexample/index.html",
        module_name=_('Invenio-APIExample'))
