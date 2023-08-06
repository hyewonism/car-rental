from flask import session, request, redirect, url_for, abort
from functools import wraps
from db import db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def role_required(roles):
    def inner(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login', next=request.url))

            user = db.fetch_user_by_id(session['user_id'])
            if user['role'] not in roles:
                abort(403)
            
            return f(*args, **kwargs)
        return decorated_function
    return inner

customer_only = role_required(['customer'])
staff_only = role_required(['staff'])
admin_only = role_required(['admin'])
customer_staff_only = role_required(['customer', 'staff'])
staff_admin_only = role_required(['staff', 'admin'])