INSERT INTO roles (name) VALUES ('User'), ('Voluntario'), ('Admin');

INSERT INTO "user" (email, username, first_name, last_name, password, address, phone, image, date_joined, is_active, is_staff, is_superuser, role_id)
VALUES
('normaaliciaromero@gmail.com', 'Normi', 'Norma', 'Romero', 'pbkdf2_sha256$600000$5AckuCNmyCM6lgLATnfxT8$nljFWwLfJnCPMsUYzrM2bmGsQdUNIraa18TdPPuJnmU=', '123 Main St', '123456789', 'eva_williams.jpg', '2024-05-23 16:00:04', TRUE, TRUE, FALSE, 2),
('parroquia_santodomingo.caritas@gmail.com', 'Admin', 'Administrador', 'Del Sistema', 'pbkdf2_sha256$600000$TM6SUusGx9g4tG3ixjFULr$2D2mz/i5G1/1mEx4bhuIm6NKwPqmg3ZafjD0KD9SLFA=', 'localhost', '123456789', 'michael_brown.jpg', '2024-05-23 16:00:04', TRUE, TRUE, TRUE, 3);
