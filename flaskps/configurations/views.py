from flask import render_template, redirect
from flask import request
from flask_login import login_required

from flaskps import db
from flaskps.configurations.models import Configurations

from . import configurations


@configurations.route('/configurations', methods=['GET', 'POST'])
@login_required
def configuration():
    conf = Configurations.query.first()
    if request.method == 'POST':
        data = request.form
        offset = data.get('offset')
        active = data.get('active')

        if offset:
            conf.offset_paginator = int(offset)
        if active:
            conf.active = True if active == "True" else False

        db.session.commit()
        return render_template('/home/dashboard.html')
    return render_template('admin/config.html', configuration=conf)


@configurations.route('/out_of_services')
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('admin/fuera_de_servicio.html'), 500
