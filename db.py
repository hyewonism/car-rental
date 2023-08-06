import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class DbManager:
    """
    Implement using singleton pattern
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        # Check if it was initialized already
        if self._initialized:
            return

        self.connection = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_DATABASE'),
        )

        self.dbconn = self.connection.cursor(dictionary=True)
        self._initialized = True

    def __del__(self):
        print('db connection closed')
        # self.dbconn.close()
        # self.connection.close()

    def create_car_rental(self, data):
        """
        Create a car rental 

        inputs:
        - data: dictionary of car rental (model, registration_number, year, seating_capacity, rental_per_day, image, description)
        """
        model = data['model']
        registration_number = data['registration_number']
        year = data['year']
        seating_capacity = data['seating_capacity']
        rental_per_day = data['rental_per_day']
        image = data['image']
        description = data['description']

        self.dbconn.execute(f"""
                    INSERT INTO
                        car_rental(model, registration_number, year, seating_capacity, rental_per_day, image, description)
                        VALUES('{model}', '{registration_number}', {year}, {seating_capacity}, {rental_per_day}, '{image}', '{description}')
                    """)
        
        self.connection.commit()

    def fetch_car_rentals(self):
        """
        Read all car rental records

        outputs:
        - list of car rentals
        """
        # Execute sql
        self.dbconn.execute("""
                        SELECT *
                        FROM car_rental;
                        """)

        # Get result of sql
        cars = self.dbconn.fetchall()

        return cars

    def fetch_car_rental_by_id(self, id):
        """
        Fetch a car rental record by id

        inputs:
        - id: car rental record pk
        outputs:
        - dictionary of a car rental 
        """
        # Execute sql
        self.dbconn.execute(f"""
                        SELECT *
                        FROM car_rental
                        WHERE id={id};
                        """)

        # Get result of sql
        car = self.dbconn.fetchone()

        return car

    def update_car_rental(self, data):
        """
        Update a car rental 

        inputs:
        - data: dictionary of car rental (id, model, registration_number, year, seating_capacity, rental_per_day, image, description)
        """
        id = data['id']
        model = data['model']
        registration_number = data['registration_number']
        year = data['year']
        seating_capacity = data['seating_capacity']
        rental_per_day = data['rental_per_day']
        image = data['image']
        description = data['description']

        self.dbconn.execute(f"""
                        UPDATE car_rental
                        SET model='{model}', registration_number='{registration_number}', year={year}, seating_capacity={seating_capacity}, rental_per_day={rental_per_day}, image='{image}', description='{description}'
                        WHERE id={id};
                    """)
        
        self.connection.commit()

    def delete_car_rental(self, id):
        """
        Delete a car rental record by id

        inputs:
        - id: car rental record pk
        """
        # Execute sql
        self.dbconn.execute(f"""
                        DELETE
                        FROM car_rental
                        WHERE id={id};
                        """)

        self.connection.commit()


    def create_user(self, data):
        """
        Create a user 

        inputs:
        - data: dictionary of user (username, password, role)
        outputs:
        - created user id(pk)
        """
        username = data['username']
        password = data['password']
        role = data['role']
    
        self.dbconn.execute(f"""
                    INSERT INTO
                        user(username, password, role)
                        VALUES('{username}', '{password}', '{role}')
                    """)
        
        self.connection.commit()

        return self.dbconn.lastrowid

    def fetch_users(self):
        """
        Read all user records

        outputs:
        - list of user
        """
        # Execute sql
        self.dbconn.execute("""
                        SELECT *
                        FROM user;
                        """)

        # Get result of sql
        users = self.dbconn.fetchall()

        return users

    def fetch_user_by_id(self, id):
        """
        Fetch a user record by id

        inputs:
        - id: user record pk
        outputs:
        - dictionary of user
        """
        # Execute sql
        self.dbconn.execute(f"""
                        SELECT *
                        FROM user
                        WHERE id={id};
                        """)

        # Get result of sql
        user = self.dbconn.fetchone()

        return user

    def fetch_user_by_username(self, username):
        """
        Fetch a user record by username

        inputs:
        - username: username field value
        outputs:
        - dictionary of user OR None
        """
        # Execute sql
        self.dbconn.execute(f"""
                        SELECT *
                        FROM user
                        WHERE username='{username}';
                        """)

        # Get result of sql
        user = self.dbconn.fetchone()

        return user

    def update_user(self, data):
        """
        Update a user

        inputs:
        - data: dictionary of user (user_id, username, password)
        """
        id = data['user_id']
        username = data['username']
        password = data['password']

        self.dbconn.execute(f"""
                        UPDATE user
                        SET username='{username}', password='{password}'
                        WHERE id={id};
                    """)
        
        self.connection.commit()


    def delete_user(self, id):
        """
        Delete a user record by id

        inputs:
        - id: user record pk
        """
        # Execute sql
        self.dbconn.execute(f"""
                        DELETE
                        FROM user
                        WHERE id={id};
                        """)

        self.connection.commit()



    def create_customer(self, data):
        """
        Create a customer

        inputs:
        - data: dictionary of customer (user_id, name, address, email, phone_number)
        """
        user_id = data['user_id']
        name = data['name']
        address = data['address']
        email = data['email']
        phone_number = data['phone_number']
    
        self.dbconn.execute(f"""
                    INSERT INTO
                        customer(user_id, name, address, email, phone_number)
                        VALUES({user_id}, '{name}', '{address}', '{email}', '{phone_number}')
                    """)
        
        self.connection.commit()


    def fetch_customers(self):
        """
        Read all customer records

        outputs:
        - list of customer
        """
        # Execute sql
        self.dbconn.execute("""
                        SELECT *
                        FROM customer;
                        """)

        # Get result of sql
        customers = self.dbconn.fetchall()

        return customers


    def fetch_customer_by_user_id(self, user_id):
        """
        Fetch a customer record using a user_id

        Arguments:
        - user_id: The primary key of the user

        Returns:
        - A dictionary representing the customer record
        """
        # Execute sql
        self.dbconn.execute(f"""
                        SELECT *
                        FROM customer
                        WHERE user_id={user_id};
                        """)

        # Get result of sql
        customer = self.dbconn.fetchone()

        return customer

    
    def update_customer_by_user_id(self, data):
        """
        Update a customer record using a user_id

        Arguments:
        - data: A dictionary of customer (user_id, name, address, email, phone_number)
        """
        user_id = data['user_id']
        name = data['name']
        address = data['address']
        email = data['email']
        phone_number = data['phone_number']

        self.dbconn.execute(f"""
                        UPDATE customer
                        SET name='{name}', address='{address}', email='{email}', phone_number='{phone_number}' 
                        WHERE user_id={user_id};
                    """)
        
        self.connection.commit()
    

    def delete_customer_by_user_id(self, user_id):
        """
        Delete a customer record using a user_id

        Arguments:
        - user_id: The primary key of the user
        """
        # Execute sql
        self.dbconn.execute(f"""
                        DELETE
                        FROM customer
                        WHERE user_id={user_id};
                        """)

        self.connection.commit()



    def create_staff(self, data):
        """
        Create a staff

        inputs:
        - data: dictionary of staff (user_id, name, address, email, phone_number)
        """
        user_id = data['user_id']
        name = data['name']
        address = data['address']
        email = data['email']
        phone_number = data['phone_number']
    
        self.dbconn.execute(f"""
                    INSERT INTO
                        staff(user_id, name, address, email, phone_number)
                        VALUES({user_id}, '{name}', '{address}', '{email}', '{phone_number}')
                    """)
        
        self.connection.commit()


    def fetch_staffs(self):
        """
        Read all staff records

        outputs:
        - list of staff
        """
        # Execute sql
        self.dbconn.execute("""
                        SELECT *
                        FROM staff;
                        """)

        # Get result of sql
        staffs = self.dbconn.fetchall()

        return staffs


    def fetch_staff_by_user_id(self, user_id):
        """
        Fetch a staff record using a user_id

        Arguments:
        - user_id: The primary key of the user

        Returns:
        - A dictionary representing the staff record
        """
        # Execute sql
        self.dbconn.execute(f"""
                        SELECT *
                        FROM staff
                        WHERE user_id={user_id};
                        """)

        # Get result of sql
        staff = self.dbconn.fetchone()

        return staff


    def update_staff_by_user_id(self, data):
        """
        Update a staff record using a user_id

        Arguments:
        - data: A dictionary of staff (user_id, name, address, email, phone_number)
        """
        user_id = data['user_id']
        name = data['name']
        address = data['address']
        email = data['email']
        phone_number = data['phone_number']

        self.dbconn.execute(f"""
                        UPDATE staff
                        SET name='{name}', address='{address}', email='{email}', phone_number='{phone_number}' 
                        WHERE user_id={user_id};
                    """)
        
        self.connection.commit()


    def delete_staff_by_user_id(self, user_id):
        """
        Delete a staff record using a user_id

        Arguments:
        - user_id: The primary key of the user
        """
        # Execute sql
        self.dbconn.execute(f"""
                        DELETE
                        FROM staff
                        WHERE user_id={user_id};
                        """)

        self.connection.commit()


db = DbManager()

