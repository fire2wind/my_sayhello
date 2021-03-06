from flask import flash, redirect, url_for, render_template
from my_sayhello import app, db
from my_sayhello.forms import HelloForm
from my_sayhello.models import Message

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent')
        return redirect(url_for('index'))
    #加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)