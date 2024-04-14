INSERT INTO public.admin_staff (name, email, duty) VALUES
('John Doe', 'john@example.com', 'Manager'),
('Jane Smith', 'jane@example.com', 'Scheduling'),
('Mike Johnson', 'mike@example.com', 'Gym Maintenance'),
('Emily Brown', 'emily@example.com', 'Customer Service');

INSERT INTO public.trainer (name, email, password, start_time, end_time, trainingdayavailable) VALUES
('Emma Taylor', 'Emma@training.com', 'password1', '08:00', '16:00', 'Monday'),
('May Ellis', 'May@training.com', 'password2', '09:00', '14:00', 'Tuesday'),
('Adam Smith', 'Adam@training.com', 'password3', '14:00', '18:00', 'Wednesday'),
('Chris Hart', 'Chris@training.com', 'password4', '11:00', '19:00', 'Thursday');

INSERT INTO public.fitness_classes (name, day, "time") VALUES
('Cardio', 'Monday', '08:00'),
('Strength Training', 'Wednesday', '10:00'),
('Yoga', 'Friday', '18:00'),
('Zumba', 'Saturday', '15:00');


INSERT INTO public.fitnessequipment (name, lastmaintenancedate, upcomingmaintenancedate) VALUES
('Treadmill', '2023-12-01', '2024-06-01'),
('Barbell Set', '2023-11-15', '2024-05-15'),
('Elliptical Machine', '2024-01-10', '2024-07-10');

INSERT INTO public.member (name, password, phone, email, "time", weight, fitnessaccomplishments, healthstats, exerciseroutine, fatpercentage, bonedensity, schedule) VALUES
('John Doe', 'password123', '1234567890', 'john@example.com', 60, 75.5, 'Ran a marathon last year', 'Good overall health', 'Cardio and weightlifting', 18.5, 1.2, 'Mon, Wed'),
('Alice Smith', 'alicepass', '9876543210', 'alice@example.com', 45, 62.0, 'Completed a half marathon', 'Regular exercise routine', 'Yoga and Pilates', 22.0, 1.0, 'Tue, Wed'),
('Bob Johnson', 'bobpass', '5551234567', 'bob@example.com', 30, 80.0, 'Regular gym', 'Improving fitness level', 'Strength training', 20.0, 1.1, 'Fri, Sun'),
('Emily Brown', 'emilypass', '9999999999', 'emily@example.com', 75, 70.5, 'Active lifestyle', 'Maintaining healthy habits', 'Running and cycling', 19.5, 1.15, 'Sun, Mon');

INSERT INTO public.room (capacity, availability, id, "time") VALUES
(30, true, NULL, '09:00'),
(20, true, NULL, '10:00'),
(15, true, NULL, '11:00'),
(25, true, NULL, '12:00'),
(40, true, NULL, '13:00');