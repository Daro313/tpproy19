from flask import render_template, redirect
from flask import request
from flask_login import login_required
from flask_user import current_user

from flaskps import db
from flaskps.app.configurations.models import Configurations

from . import configurations


@configurations.route('/admin/configuration', methods=['GET', 'POST'])
@login_required
def configuration(permiso='configuration_show'):
    if current_user.have_permissions(permiso):
        conf = Configurations.query.first()
        if request.method == 'POST':
            data = request.form
            conf.update(data)
            return render_template('/home/dashboard.html')
        return render_template('admin/config.html', configuration=conf)
    else:
        return render_template('home/dashboard.html')
