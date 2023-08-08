/* Create 20 cars */
INSERT INTO car_rental(model,registration_number, year, seating_capacity, rental_per_day, image, description)
VALUES
('Toyota Corolla', '101-001', 2020, 5, 80, '/media/car1.jpg','"Reliable and fuel-efficient compact sedan with a comfortable ride"'),
('Ford Ranger', '101-002', 2021, 5, 90, '/media/car2.jpg','"Rugged and powerful pickup truck known for its off-road capabilities"'),
('Honda Civic', '101-003', 2019, 5, 85, '/media/car3.jpeg','"Well-rounded compact car with a reputation for reliability and practicality"'),
('Mazda CX-5', '101-004', 2022, 5, 95, '/media/car4.jpg','"Stylish and sporty SUV with a well-designed interior and enjoyable driving"'),
('Mitsubishi Outlander', '101-005', 2020, 7, 100, '/media/car5.jpg','"Family-friendly SUV with three rows of seating and a spacious interior"'),
('Nissan Navara', '101-006', 2021, 5, 80, '/media/car6.jpg','"Robust and versatile pickup truck suitable for both work and leisure"'),
('Subaru Forester', '101-007', 2022, 5, 85, '/media/car7.jpg','"All-wheel-drive SUV with excellent safety ratings and ample cargo space"'),
('Hyundai Tucson', '101-008', 2021, 5, 95, '/media/car8.jpg','"Feature-packed crossover SUV offering a comfortable and quiet ride"'),
('Volkswagen Golf', '101-009', 2020, 5, 75, '/media/car9.jpeg','"Fun-to-drive hatchback with a refined interior and advanced technology"'),
('Kia Sportage', '101-0010', 2019, 5, 90, '/media/car10.jpg','"Attractive compact SUV with a user-friendly infotainment system"'),
('BMW 3 Series', '101-011', 2022, 5, 85, '/media/car11.jpg','"Luxury sports sedan known for its dynamic performance and upscale features"'),
('Benz C-Class', '101-012', 2021, 5, 85, '/media/car12.jpg','"Classy and elegant luxury sedan with advanced technology and safety features."'),
('Audi A4', '101-013', 2020, 5, 80, '/media/car13.jpg','"Premium compact sedan with a luxurious interior and smooth handling"'),
('Lexus NX', '101-014', 2022, 5, 85, '/media/car14.jpg','"Upscale compact luxury SUV with a comfortable and well-crafted cabin"'),
('Jeep Wrangler', '101-015', 2021, 5, 90, '/media/car15.jpg','"Iconic off-road SUV with a rugged design and excellent four-wheel-drive capabilities"'),
('Range Rover Evoque', '101-016', 2020, 5, 100, '/media/car16.jpg','"Stylish and luxurious compact SUV with off-road capability"'),
('Suzuki Swift', '101-017', 2019, 5, 75, '/media/car17.jpeg','"Compact hatchback with nimble handling and good fuel efficiency"'),
('Toyota Vitz', '101-018', 2021, 5, 70, '/media/car18.jpg','"Popular hatchback known for practicality, fuel efficiency, and comfortable"'),
('Peugeot 3008', '101-019', 2021, 5, 80, '/media/car19.jpeg','"Modern and stylish crossover with a spacious interior"'),
('Volvo XC60', '101-020', 2020, 5, 95, '/media/car20.jpg','"Premium midsize SUV with a focus on safety and elegant Scandinavian design"');

/* Create multiple user records */
INSERT INTO user(username, password, role)
VALUES
('lincoln123', 'pbkdf2:sha256:600000$1oEkyg7TkXjTCTRf$8f2fd9ff5bd436845ca8afaeea84ddc61dde92d857994422fe632432dfe925e9', 'customer'),
('nzlife332', 'pbkdf2:sha256:600000$zCO42nGhFJUOnm3h$5a6afe5bd6cdd01f89e92c12cb16f36a8b645896ddeb278de61402db3cdd7606', 'customer'),
('chchlife456', 'pbkdf2:sha256:600000$z2dg9UAqj51pwuRX$49238a863c59baa5cd330239c4d15be3d63ebe6189af096565f4c10338ed9888', 'customer'),
('kings876', 'pbkdf2:sha256:600000$SUnO7JZsriczpnQW$66af29e24c4553bc17f5687eeb0a35af5a421c657eca37ece870bc30f1cb4c43', 'customer'),
('nzandkorea', 'pbkdf2:sha256:600000$eiZuNCrIEapLgdlc$c02c078969c21bef07746485bf3e4e7e89e85d98a0115ca252fee9c07f449805', 'customer'),
('staff1', 'pbkdf2:sha256:600000$T4M9HcIGkri92JWd$2fef0f8a3491604f8090f0933b290e83c97ff01cb8cbed48ca52bc058d89ed5e', 'staff'),
('staff2', 'pbkdf2:sha256:600000$c2ICFIPD9mHmBZYb$1860d418ca21a32bdaaceab022c91f1a77419f031ef95e5c72d1a86f6091c793', 'staff'),
('staff3', 'pbkdf2:sha256:600000$laNrAqhAIdnPmHJG$2bb8fbba73c0b28c003b9f3d010b45203b04fbab2c4e24bda1f171305e84beef', 'staff'),
('admin', 'pbkdf2:sha256:600000$ZvKDz0LQnMoUJryn$b56d667046c172b6e612385f05230ac51b3f430b18e928ad0342687481ca4249', 'admin');

/* Create customer records */
INSERT INTO customer(user_id, name, address, email, phone_number)
VALUES
(1, 'John Smith', '123 Main Street, Auckland', 'john.smith@google.com', '02176549874'),
(2, 'Emily Johnson', '456 Park Avenue, Wellington', 'emily.johnson@google.com','02177658943'),
(3, 'Michael Brown', '789 Queens Road, Christchurch', 'brown@google.com', '02467589322'),
(4, 'Olivia Wilson', '101 Kings Lane, Hamilton', 'olivia@google.com', '02076532345'),
(5, 'James Lee', '222 Lakeview Drive, Dunedin', 'james.lee@google.com', '02187690876');

/* Create staff records */
INSERT INTO staff(user_id, name, address, email, phone_number)
VALUES
(6, 'Tom Wilson', '123 Maple Street, Auckland', 'tom.wilson@google.com', '02089769987'),
(7, 'Ria Jones', '789 Pine Road, Christchurch', 'ria.jones@google.com', '02033457766'),
(8, 'Jack Thompson', '456 Oak Avenue, Wellington', 'jack.thompson@google.com', '02199876621');
