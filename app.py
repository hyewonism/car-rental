from flask import Flask, render_template, request, redirect, session, send_from_directory
from db import db
from utils import random_string
from decorator import admin_only, customer_staff_only, staff_admin_only
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__, static_url_path="/")

@app.route('/')
def index():
    return redirect('/home')

########## CAR PAGES ############

@app.route('/cars')
def cars():
    car_rentals = db.fetch_car_rentals()
    return render_template("Cars/cars.html", car_rentals=car_rentals)


@app.route('/cars_detail')
def cardetail():
    id = request.args['id']
    car_rental = db.fetch_car_rental_by_id(id)
    return render_template("Cars/carsdetail.html", car=car_rental)


########## DASHBOARD PAGES ############
##### DASHBOARD (CAR) ######
@app.route('/dash_car_add')
@staff_admin_only
def dash_car_add():
    return render_template("Dashboard/CarInfo/dash_car_add.html")


@app.route('/car_add_create', methods=['POST'])
@staff_admin_only
def car_add_create():
    data = dict(request.form)

    # Store image in local storage
    image = request.files['image']
    filename = secure_filename(random_string(10) + image.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(path)
    data['image'] = path

    db.create_car_rental(data)

    return redirect('/dash_cars')


@app.route('/dash_car_edit')
@staff_admin_only
def dash_car_edit():
    car_rental = db.fetch_car_rental_by_id(request.args['id'])
    return render_template("Dashboard/CarInfo/dash_car_edit.html", car_rental=car_rental)


@app.route('/dash_car_edit_update', methods=['POST'])
@staff_admin_only
def dash_car_edit_update():
    data = dict(request.form)

    # Store image in local storage
    image = request.files['image']
    if image.filename != '':
        filename = secure_filename(random_string(10) + image.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(path)
        data['image'] = path
    else:
        data['image'] = data['prev_image']

    db.update_car_rental(data)

    return redirect('/dash_cars')


@app.route('/dash_car_delete')
@staff_admin_only
def dash_car_delete():
    db.delete_car_rental(request.args['id'])

    return redirect('/dash_cars')

@app.route('/dash_cars')
@staff_admin_only
def dash_cars():
    car_rentals = db.fetch_car_rentals()
    return render_template("Dashboard/CarInfo/dash_cars.html", car_rentals=car_rentals)


##### DASHBOARD (CUSTOMER) ######
@app.route('/cust_add')
@admin_only
def cust_add():
    return render_template("Dashboard/CustomerInfo/cust_add.html")


@app.route('/cust_add_create', methods=['POST'])
@admin_only
def cust_add_create():
    # Add addtional colume value
    data = dict(request.form)
    data['role'] = 'customer'

    # 1. Create user record
    hashed_password = generate_password_hash(data['password'])
    data['password'] = hashed_password
    user_id = db.create_user(data)

    # 2. Create customer record
    data['user_id'] = user_id
    db.create_customer(data)

    # Redirect to /cust_list
    return redirect('/cust_list')


@app.route('/cust_edit')
@admin_only
def cust_edit():
    data = request.args # ?key=value -> dictionary

    user_id = data['user_id']
    customer = db.fetch_customer_by_user_id(user_id)
    user = db.fetch_user_by_id(user_id)

    return render_template("Dashboard/CustomerInfo/cust_edit.html", customer=customer, user=user)


@app.route('/cust_edit_update', methods=['POST'])
@admin_only
def cust_edit_update():
    data = dict(request.form)

    if data['password']:
        hashed_password = generate_password_hash(data['password'])
        data['password'] = hashed_password
    else:
        data['password'] = data['prev_password']

    db.update_customer_by_user_id(data)
    db.update_user(data)

    return redirect('/cust_list')


@app.route('/cust_delete')
@admin_only
def cust_delete():
    data = request.args

    user_id = data['user_id']
    db.delete_customer_by_user_id(user_id)
    db.delete_user(user_id)

    return redirect('/cust_list')


@app.route('/cust_list')
@staff_admin_only
def cust_list():
    customers = db.fetch_customers()
    return render_template("Dashboard/CustomerInfo/cust_list.html", customers=customers)


##### DASHBOARD (STAFF) ######
@app.route('/staff_add')
@admin_only
def staff_add():
    return render_template("Dashboard/StaffInfo/staff_add.html")


@app.route('/staff_add_create', methods=['POST'])
@admin_only
def staff_add_create():
    # Add addtional colume value
    data = dict(request.form)
    data['role'] = 'staff'

    # 1. Create user record
    hashed_password = generate_password_hash(data['password'])
    data['password'] = hashed_password
    user_id = db.create_user(data)

    # 2. Create staff record
    data['user_id'] = user_id
    db.create_staff(data)

    # Redirect to /staff_list
    return redirect('/staff_list')


@app.route('/staff_edit')
@admin_only
def staff_edit():
    """
    Staff edit page for admin user
    """
    data = request.args

    user_id = data['user_id']
    staff = db.fetch_staff_by_user_id(user_id)
    user = db.fetch_user_by_id(user_id)

    return render_template("Dashboard/StaffInfo/staff_edit.html", staff=staff, user=user)


@app.route('/staff_edit_update', methods=['POST'])
@admin_only
def staff_edit_update():
    data = dict(request.form)

    if data['password']:
        hashed_password = generate_password_hash(data['password'])
        data['password'] = hashed_password
    else:
        data['password'] = data['prev_password']

    db.update_staff_by_user_id(data)
    db.update_user(data)

    return redirect('/staff_list')


@app.route('/staff_delete')
@admin_only
def staff_delete():
    data = request.args

    user_id = data['user_id']
    db.delete_staff_by_user_id(user_id)
    db.delete_user(user_id)

    return redirect('/staff_list')


@app.route('/staff_list')
@admin_only
def staff_list():
    staffs = db.fetch_staffs()
    return render_template("Dashboard/StaffInfo/staff_list.html", staffs=staffs)


@app.route('/change_pw')
@customer_staff_only
def change_pw():
    return render_template("Dashboard/MyProfile/change_pw.html")


@app.route('/change_pw_update', methods=['POST'])
@customer_staff_only
def change_pw_update():
    data = request.form
    user = session['user']

    is_valid = True
    error = []
    if not check_password_hash(user['password'], data['old_password']):
        is_valid = False
        error.append('Old password is not correct')

    if not (data['new_password'] == data['confirm_password']):
        is_valid = False
        error.append('New password and Confirm password are not the same')

    if is_valid:
        db.update_user({
            'user_id': user['id'],
            'username': user['username'],
            'password': generate_password_hash(data['new_password'])
        })

        return redirect("/profile")
    else:
        return render_template("Dashboard/MyProfile/change_pw.html", error=error)


@app.route('/profile')
@customer_staff_only
def profile():
    user = session['user']
    if user['role'] == 'customer':
        p = db.fetch_customer_by_user_id(user['id'])
    else:
        p = db.fetch_staff_by_user_id(user['id'])
    return render_template("Dashboard/MyProfile/profile.html", profile=p, user=user)


@app.route('/profile_update', methods=['POST'])
@customer_staff_only
def profile_update():
    data = dict(request.form)
    user = session['user']

    # Add exist password
    data['password'] = user['password']

    # Update user
    db.update_user(data)

    # Update profile
    if user['role'] == 'customer':
        db.update_customer_by_user_id(data)
    else:
        db.update_staff_by_user_id(data)

    # Update session
    user['username'] = data['username']
    session['user'] = user

    return redirect('/profile')


########## HOME PAGES ############
@app.route('/home')
def home():
    return render_template("Home/home.html")


########## LOGIN / REGISTRATION PAGES ############
@app.route('/login')
def login():
    return render_template("Login/login.html", next=request.args.get('next'))


@app.route('/login_check', methods=['POST'])
def login_check():
    data = request.form

    is_valid = False
    user = db.fetch_user_by_username(data['username'])
    # Check username
    if user is not None:
        # Check password
        if check_password_hash(user['password'], data['password']):
            is_valid = True

    if is_valid:
        #session['user_id'] = user['id']
        session['user'] = user

        # if 'next' exists, redirect using it
        if 'next' in request.form:
            return redirect(request.form['next'])
        return redirect('/home')
    else:
        return render_template("Login/login.html", data=data, next=request.form.get('next'))


@app.route('/regi')
def regi():
    return render_template("Registration/regi2.html")


@app.route('/regi_create', methods=['POST'])
def regi_create():
    data = dict(request.form)
    data['role'] = 'customer'

    error = []
    is_valid = True
    # 1. Validate username is unique
    exist_user = db.fetch_user_by_username(data['username'])
    if exist_user is not None:
        is_valid = False
        error.append('This username is already taken')

    # 2. Validate password and confirm_password are same
    if data['password'] != data['confirm_password']:
        is_valid = False
        error.append('Those passwords are not same')

    if is_valid:
        # Apply hash and salt to password
        hashed_password = generate_password_hash(data['password'])
        data['password'] = hashed_password

        # Create user and customer
        user_id = db.create_user(data)

        data['user_id'] = user_id
        db.create_customer(data)

        return redirect('/login')
    else:
        return render_template("Registration/regi2.html", error=error, data=data)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/home')


@app.route('/media/<path:path>')
def send_media(path):
    """
    Media serving for develop environment
    """
    return send_from_directory('media', path)


app.config['UPLOAD_FOLDER'] = 'media'
app.secret_key=os.getenv('SECRET_KEY')
app.run(debug=True, port=5002)