
-- Insertar roles
INSERT INTO roles (name)
VALUES
('User'),
('Voluntario'),
('Admin');


INSERT INTO "user" (
    email, username, first_name, last_name, password,address, phone, image, date_joined,
    is_active, is_staff, is_superuser, role_id)
VALUES


('normaaliciaromero@gmail.com', 'Normi', 'Norma', 'Romero', 'pbkdf2_sha256$1000000$99e2MNRXaHJtYYfHnBIqS0$Yy4CuwwbuIKuFqedoZ+kocAz7vUR4Ce3cNjmIwl7x8c=', '123 Main St', '123456789', 'eva_williams.jpg', '2024-05-23 16:00:04', TRUE, TRUE, FALSE, 2),

('voluntarias_sanjose@gmail.com', 'Admin', 'Administrador', 'Del Sistema', 'pbkdf2_sha256$1000000$CM7xsLNuxifDNtbItJuM9Q$GPuQ8c9eEghHylJsh4xYJzeTQyV0kzaJJrncrULGMDo=', 'localhost', '123456789', 'michael_brown.jpg', '2024-05-23 16:00:04', TRUE, TRUE, TRUE, 3);
