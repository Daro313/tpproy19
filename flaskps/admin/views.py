from flask import render_template, redirect
from flask import request
from flask_login import login_required

from flaskps import db
from flaskps.models import Configurations

from . import admin


@admin.route('/admin/configuration', methods=['GET', 'POST'])
def configuration():
    conf = Configurations.query.first()
    import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        data = request.form
        offset = data.get('offset')
        active = data.get('active')

        if offset:
            conf.offset_paginator = offset
        if active:
            active = True if active == "True" else False
        return render_template('/home/dashboard.html')
    return render_template('admin/config.html', configuration=conf)






# @app.errorhandler(404)
#def page_not_found(e):
#    # note that we set the 404 status explicitly
#    return render_template('404.html'), 404
