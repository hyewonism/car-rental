/* Create 20 cars */
INSERT INTO car_rental(model,registration_number, year, seating_capacity, rental_per_day, image, discriptions)
VALUES
('Toyota Corolla', '101-001', 2020, 5, 80, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car1.jpg','"Reliable and fuel-efficient compact sedan with a comfortable ride"'),
('Ford Ranger', '101-002', 2021, 5, 90, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car2.jpg','"Rugged and powerful pickup truck known for its off-road capabilities"'),
('Honda Civic', '101-003', 2019, 5, 85, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car3.jpg','"Well-rounded compact car with a reputation for reliability and practicality"'),
('Mazda CX-5', '101-004', 2022, 5, 95, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car4.jpg','"Stylish and sporty SUV with a well-designed interior and enjoyable driving"'),
('Mitsubishi Outlander', '101-005', 2020, 7, 100, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car5.jpg','"Family-friendly SUV with three rows of seating and a spacious interior"'),
('Nissan Navara', '101-006', 2021, 5, 80, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car6.jpg','"Robust and versatile pickup truck suitable for both work and leisure"'),
('Subaru Forester', '101-007', 2022, 5, 85, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car7.jpg','"All-wheel-drive SUV with excellent safety ratings and ample cargo space"'),
('Hyundai Tucson', '101-008', 2021, 5, 95, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car8.jpg','"Feature-packed crossover SUV offering a comfortable and quiet ride"'),
('Volkswagen Golf', '101-009', 2020, 5, 75, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car9.jpg','"Fun-to-drive hatchback with a refined interior and advanced technology"'),
('Kia Sportage', '101-0010', 2019, 5, 90, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car10.jpg','"Attractive compact SUV with a user-friendly infotainment system"'),
('BMW 3 Series', '101-011', 2022, 5, 85, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car11.jpg','"Luxury sports sedan known for its dynamic performance and upscale features"'),
('Benz C-Class', '101-012', 2021, 5, 85, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car12.jpg','"Classy and elegant luxury sedan with advanced technology and safety features."'),
('Audi A4', '101-013', 2020, 5, 80, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car13.jpg','"Premium compact sedan with a luxurious interior and smooth handling"'),
('Lexus NX', '101-014', 2022, 5, 85, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car14.jpg','"Upscale compact luxury SUV with a comfortable and well-crafted cabin"'),
('Jeep Wrangler', '101-015', 2021, 5, 90, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car15.jpg','"Iconic off-road SUV with a rugged design and excellent four-wheel-drive capabilities"'),
('Range Rover Evoque', '101-016', 2020, 5, 100, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car16.jpg','"Stylish and luxurious compact SUV with off-road capability"'),
('Suzuki Swift', '101-017', 2019, 5, 75, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car17.jpg','"Compact hatchback with nimble handling and good fuel efficiency"'),
('Toyota Vitz', '101-018', 2021, 5, 70, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car18.jpg','"Popular hatchback known for practicality, fuel efficiency, and comfortable"'),
('Peugeot 3008', '101-019', 2021, 5, 80, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car19.jpg','"Modern and stylish crossover with a spacious interior"'),
('Volvo XC60', '101-020', 2020, 5, 95, 'C:/Users/myhom/Desktop/Hyewon/뉴질랜드/수업관련/COMP639/CarRental/CarRental/images/car20.jpg','"Premium midsize SUV with a focus on safety and elegant Scandinavian design"');

/* Create multiple user records */
INSERT INTO user(username, password, role)
VALUES
('lincoln123', 123456, 'customer'),
('nzlife332', 123456, 'customer'),
('chchlife456', 123456, 'customer'),
('kings876', 123456, 'customer'),
('nzandkorea', 123456, 'customer'),
('staff1', 123456, 'staff'),
('staff2', 123456, 'staff'),
('staff3', 123456, 'staff'),
('admin', 123456, 'admin');

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
(8, 'Jack Thompson', '456 Oak Avenue, Wellington', 'jack.thompson@google.com', '02199876621'),