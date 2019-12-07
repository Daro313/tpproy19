@instruments.route('/instruments/create', methods=['GET', 'POST'])
@login_required
def create(permiso='instruments_new'):
    """
    metodo GET: renderiza form de reacion
    metodo POST: verifica los datos y crea usuaraio
    """
    if current_user.have_permissions(permiso):
        form = CreateInstrumentsForm(request.form)

        if request.method == 'POST' and form.validate():
            instrument = Instruments(
                name=request.form.get('name'),
                type=request.form.get('type'),
                inventory_number=request.form.get('inventory_number'),
                image = secure_filename(form.file.data.filename),
                form.file.data.save('uploads/' + filename)
                image_data = request.FILES[form.image.name].read()
                open(os.path.join(/static/img/instruments, form.image.data), 'w').write(image_data)
            )
            db.session.add(instrument)
            try:
                db.session.commit()
                msg = "El instrumento %s se creo con exito" % teacher.name
            except:
                db.session.rollback()
                return render_template('instruments/create.html', form=form), 403
            return redirect(url_for('instruments.detail', instrument_id=instrument.id))
        return render_template('instruments/create.html', form=form)
    else:
        flash('No tiene los permisos para acceder :(')
        return render_template('home/dashboard.html')
