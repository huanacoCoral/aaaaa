-- Crear la tabla estudiantes
CREATE TABLE estudiantes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    ci NVARCHAR(20) NOT NULL UNIQUE,
    edad INT NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')) NOT NULL,
    direccion NVARCHAR(100),
    telefono NVARCHAR(20),
    email NVARCHAR(50)
);
GO

-- Crear la tabla docentes
CREATE TABLE docentes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    ci NVARCHAR(20) NOT NULL UNIQUE,
    edad INT NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')) NOT NULL,
    especialidad NVARCHAR(100),
    direccion NVARCHAR(100),
    telefono NVARCHAR(20),
    email NVARCHAR(50)
);
GO

-- Insertar datos en la tabla estudiantes
INSERT INTO estudiantes (nombre, ci, edad, sexo, direccion, telefono, email) VALUES
('Juan Perez', '12345678', 20, 'M', 'Calle Falsa 123', '555-1234', 'juan.perez@example.com'),
('Maria Garcia', '87654321', 22, 'F', 'Avenida Siempre Viva 456', '555-5678', 'maria.garcia@example.com'),
('Carlos López', '23456789', 19, 'M', 'Calle de la Flor 789', '555-8765', 'carlos.lopez@example.com'),
('Ana Torres', '98765432', 21, 'F', 'Paseo del Parque 101', '555-4321', 'ana.torres@example.com');
GO

-- Insertar datos en la tabla docentes
INSERT INTO docentes (nombre, ci, edad, sexo, especialidad, direccion, telefono, email) VALUES
('Luis Fernandez', '11223344', 45, 'M', 'Matemáticas', 'Calle del Sol 555', '555-9988', 'luis.fernandez@example.com'),
('Elena Martinez', '44332211', 38, 'F', 'Literatura', 'Avenida del Lago 333', '555-7766', 'elena.martinez@example.com'),
('Jorge Ramírez', '55667788', 50, 'M', 'Historia', 'Camino Real 777', '555-5544', 'jorge.ramirez@example.com'),
('Patricia Gomez', '88776655', 42, 'F', 'Ciencias', 'Paseo del Bosque 999', '555-3322', 'patricia.gomez@example.com');
GO