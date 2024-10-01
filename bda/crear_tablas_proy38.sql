------ INICIO EXTREMO PERSONA -----
CREATE TABLE Persona (
    NIF VARCHAR2(9) CONSTRAINT pk_persona PRIMARY KEY,
    nombre VARCHAR2(20) NOT NULL,
    apellidos VARCHAR2(50) NOT NULL,
    correo VARCHAR2(60) NOT NULL
);

CREATE TABLE TeléfonoPersona (
    telefono INT CONSTRAINT pk_tlf PRIMARY KEY,
    NIF VARCHAR2(9) NOT NULL,
    CONSTRAINT fk_NIF_Persona1 
        FOREIGN KEY (NIF) 
        REFERENCES Persona(NIF) 
        ON DELETE CASCADE 
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Trabajador (
    NIF varchar(9) CONSTRAINT pk_trabajador PRIMARY KEY,
    puesto varchar(30) NOT NULL,
    residencia varchar(100) NOT NULL,
    CONSTRAINT fk_NIF_Trabajador 
    FOREIGN KEY (NIF) 
    REFERENCES Persona(NIF)
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Cliente (
    NIF varchar(9) CONSTRAINT pk_cliente PRIMARY KEY,
    contraseña varchar(40) NOT NULL,
    CONSTRAINT fk_NIF_Cliente 
    FOREIGN KEY (NIF) 
    REFERENCES Persona(NIF)
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Dirección2 (
    provincia varchar(50) CONSTRAINT pk_direccion2 PRIMARY KEY,
    comunidad_autonoma varchar(50) NOT NULL
);

CREATE TABLE Dirección1 (
    NIF varchar(9) NOT NULL,
    num_dir INT NOT NULL,
    calle varchar(100) NOT NULL,
    numero INT NOT NULL,
    puerta varchar(10),
    ciudad varchar(50) NOT NULL,
    provincia varchar(50) NOT NULL,
    CONSTRAINT pk_direccion1 PRIMARY KEY (NIF, num_dir),
    CONSTRAINT fk_direccion1
        FOREIGN KEY (NIF)
        REFERENCES Cliente(NIF)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_provincia_Dirección1
        FOREIGN KEY (provincia)
        REFERENCES Dirección2(provincia)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Producto (
    id_prod varchar(4) CONSTRAINT pk_producto PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    categoria varchar(30) NOT NULL,
    stock int NOT NULL,
    peso int NOT NULL,
    imagen varchar(100) NOT NULL,
    descripcion varchar(100) NOT NULL,
    precio int NOT NULL,
    nota_media float,
    recuento_valoraciones int,
    CONSTRAINT nota_media_correcta CHECK ((nota_media IS NULL AND recuento_valoraciones = 0)
    OR (nota_media IS NOT NULL AND recuento_valoraciones > 0))
);


CREATE TABLE Pedido (
    id_ped VARCHAR2(9) CONSTRAINT pk_pedido PRIMARY KEY,
    fecha_creacion DATE NOT NULL,
    base_imponible FLOAT NOT NULL,
    IVA FLOAT NOT NULL CONSTRAINT IVA_correcto CHECK (IVA > 0 AND IVA <= 21),
    precio_total FLOAT NOT NULL,
    transportista_elegido VARCHAR2(40) NOT NULL,
    NIF_dir VARCHAR2(9) NOT NULL,
    num_dir INT NOT NULL,
    CONSTRAINT fk_direccion_pedido
        FOREIGN KEY (NIF_dir, num_dir)
        REFERENCES Dirección1(NIF, num_dir)
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_transportista_pedido
        FOREIGN KEY (transportista_elegido)
        REFERENCES Transportista(CIF)
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT precio_total_correcto
        CHECK (precio_total = base_imponible + (base_imponible * IVA / 100))
);

CREATE TABLE LíneaPedido (
    id_prod varchar(4),
    id_ped varchar(9),
    cantidad int CONSTRAINT cantidad_correcto CHECK (cantidad > 0) ,
    CONSTRAINT pk_líneapedido PRIMARY KEY (id_prod, id_ped),
    CONSTRAINT fk_producto_líneapedido 
        FOREIGN KEY (id_prod) 
        REFERENCES Producto(id_prod) 
        ON DELETE CASCADE 
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_pedido_líneapedido 
        FOREIGN KEY (id_ped) 
        REFERENCES Pedido(id_ped) 
        ON DELETE CASCADE 
        DEFERRABLE INITIALLY DEFERRED
);
----- INICIO EXTREMO COLABORADOR -----

CREATE TABLE Colaborador (
    CIF VARCHAR2(9) CONSTRAINT pk_colaborador PRIMARY KEY,
    nombre VARCHAR2(60) NOT NULL,
    direccion VARCHAR2(100) NOT NULL,
    cuenta VARCHAR2(24) NOT NULL
);

CREATE TABLE TeléfonoColaborador (
    telefono INT CONSTRAINT pk_tel_colaborador PRIMARY KEY,
    CIF VARCHAR2(9) NOT NULL,
    CONSTRAINT fk_tel_colaborador_colaborador
        FOREIGN KEY (CIF)
        REFERENCES Colaborador(CIF)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Transportista (
    CIF VARCHAR2(9) CONSTRAINT pk_transportista PRIMARY KEY,
    precio_kg FLOAT NOT NULL,
    precio_km FLOAT NOT NULL,
    peso_minimo FLOAT NOT NULL,
    peso_maximo FLOAT NOT NULL,
    CONSTRAINT fk_transportista_colaborador
        FOREIGN KEY (CIF)
        REFERENCES Colaborador(CIF)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT check_precios_pesos
        CHECK (precio_km > 0 AND precio_kg > 0 AND peso_minimo > 0 AND peso_maximo > peso_minimo)
);

CREATE TABLE Proveedor (
    CIF VARCHAR2(9) CONSTRAINT pk_proveedor PRIMARY KEY,
    correo VARCHAR2(60) NOT NULL,
    CONSTRAINT fk_proveedor_colaborador
        FOREIGN KEY (CIF)
        REFERENCES Colaborador(CIF)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED
);

--- Materia prima

CREATE TABLE Materia_prima (
    id_mat VARCHAR2(4) CONSTRAINT pk_materia_prima PRIMARY KEY,
    tipo VARCHAR2(30) NOT NULL,
    kg_stock FLOAT NOT NULL,
    cant_minima FLOAT NOT NULL,
    CONSTRAINT check_mat_prima
        CHECK (kg_stock >= 0 and cant_minima >= 0)
);

CREATE TABLE PrecioMateriaProveedor (
    id_mat VARCHAR2(4),
    CIF VARCHAR2(9),
    CONSTRAINT pk_precio_mat_proveedor 
        PRIMARY KEY (id_mat, CIF),
    precio FLOAT NOT NULL,
    CONSTRAINT fk_precio_proveedor
        FOREIGN KEY (CIF)
        REFERENCES Proveedor(CIF)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_precio_mat
        FOREIGN KEY (id_mat)
        REFERENCES Materia_prima(id_mat)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT check_precio
        CHECK (precio > 0)
);

-- Especializacion de pedido

CREATE TABLE Confirmado (
    id_ped VARCHAR2(9),
    fecha_pago DATE NOT NULL,
    CONSTRAINT pk_confirmado
        PRIMARY KEY (id_ped),
    CONSTRAINT fk_confirmado_pedido
        FOREIGN KEY (id_ped)
        REFERENCES Pedido(id_ped)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Preparado (
    id_ped VARCHAR2(9),
    fecha_preparado DATE NOT NULL,
    NIF VARCHAR2(9) NOT NULL,
    CONSTRAINT pk_preparado
        PRIMARY KEY (id_ped),
    CONSTRAINT fk_preparado_confirmado
        FOREIGN KEY (id_ped)
        REFERENCES Confirmado(id_ped)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_preparado_trabajador
        FOREIGN KEY (NIF)
        REFERENCES Trabajador(NIF)
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Enviado (
    id_ped VARCHAR2(9),
    fecha_envio DATE NOT NULL,
    CIF VARCHAR2(9) NOT NULL,
    coste_envio FLOAT NOT NULL,
    CONSTRAINT pk_enviado
        PRIMARY KEY (id_ped),
    CONSTRAINT fk_enviado_pedido
        FOREIGN KEY (id_ped)
        REFERENCES Preparado(id_ped)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_enviado_transportista
        FOREIGN KEY (CIF)
        REFERENCES Transportista(CIF)
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE Recibido (
    id_ped VARCHAR2(9),
    fecha_entrega DATE NOT NULL,
    CONSTRAINT pk_recibido
        PRIMARY KEY (id_ped),
    CONSTRAINT fk_recibido_enviado
        FOREIGN KEY (id_ped)
        REFERENCES Enviado(id_ped)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED
);
    
-- FACTURA

CREATE TABLE Factura (
    id_factura VARCHAR2(9),
    fecha_factura DATE NOT NULL,
    id_ped VARCHAR2(9) NOT NULL,
    CONSTRAINT pk_factura 
        PRIMARY KEY (id_factura),
    CONSTRAINT id_ped_unico UNIQUE (id_ped),
    CONSTRAINT fk_factura_pedido
        FOREIGN KEY (id_ped)
        REFERENCES Recibido(id_ped)
        ON DELETE SET NULL
        DEFERRABLE INITIALLY DEFERRED
);
    
-- VALORACION

CREATE TABLE Valoración (
    id_prod VARCHAR2(4),
    id_ped VARCHAR(9),
    nota FLOAT NOT NULL,
    CONSTRAINT pk_valoracion
        PRIMARY KEY (id_prod, id_ped),
    CONSTRAINT fk_valoracion_producto
        FOREIGN KEY (id_prod)
        REFERENCES Producto(id_prod)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT fk_valoracion_pedido
        FOREIGN KEY (id_ped)
        REFERENCES Recibido(id_ped)
        ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT check_valoracion
        CHECK (nota >= 0 AND nota <= 5)
);

CREATE TABLE NOMBRE (
    nombre VARCHAR2(20)
);

CREATE TABLE APELLIDO (
    apellido VARCHAR2(20)
);
    
-- INSERTAR NOMBRES Y APELLIDOS

INSERT INTO APELLIDO VALUES ('Thiem');
COMMIT;

SELECT COUNT(*)
FROM NOMBRE;

-- CARGAR BASE DE DATOS

create or replace function crear_nombre
return varchar2
is
 v_nombre varchar2(100);
 v_random number;
begin
/*Obtención de un nombre aleatorio de los 42 que hay*/
 v_random := round(dbms_random.value(0,41),0);
/*En la sentencia select con la cláusula offset indicamos que salte v_random
filas y con la cláusula fetch next indicamos que recupere sólo 1 fila (la
siguiente)*/
 select nombre
 into v_nombre
 from nombre
 offset v_random rows
 fetch next 1 rows only;
 return(v_nombre);
exception
 /*Si se produce algún error, la función devuelve el nombre
Pepa'*/
 when no_data_found then
 return('Pepa');
end;

-- APELLIDOS

create or replace function crear_apellidos
return varchar2
is
 v_nombre varchar2(100);
 v_apellido1 varchar2(100);
 v_apellido2 varchar2(100);
 v_random number;
begin
/*Obtención de dos apellidos aleatorios de los 42 que hay*/
 v_random := round(dbms_random.value(0,41),0);
 select apellido
 into v_apellido1
 from apellido
 offset v_random rows
 fetch next 1 rows only;
 v_random := round(dbms_random.value(0,41),0);
 select apellido
 into v_apellido2
 from apellido
 offset v_random rows
 fetch next 1 rows only;
 v_nombre := v_apellido1 ||' '||v_apellido2;
 return(v_nombre);
exception
 /*Si se produce algún error, la función devuelve el nombre 'Pérez Pérez*/
 when no_data_found then
 return('Pérez Pérez');
end;

COMMIT;

-- Para crear el nombre de una calle

CREATE TABLE calle (
    nombre VARCHAR2(20)
);

INSERT INTO calle VALUES ('Paseo');


create or replace function crear_direccion
return varchar2
is
 v_nombre varchar2(100);
 n varchar2(20);
 v_apellido1 varchar2(100);
 direccion varchar2(20);
 v_random number;
begin
/*Obtención de dos apellidos aleatorios de los 42 que hay*/
 v_random := round(dbms_random.value(0,41),0);
 select apellido
 into v_apellido1
 from apellido
 offset v_random rows
 fetch next 1 rows only;
 v_random := round(dbms_random.value(0,41),0);
 select nombre
 into n
 from nombre
 offset v_random rows
 fetch next 1 rows only;
 v_random := round(dbms_random.value(0,5),0);
 select nombre
 into direccion
 from calle
 offset v_random rows
 fetch next 1 rows only;
 v_nombre := direccion ||' '|| n ||' '|| v_apellido1;
 return(v_nombre);
exception
 /*Si se produce algún error, la función devuelve el nombre 'Pérez Pérez*/
 when no_data_found then
 return('Calle Rafael Nadal');
end;

-- Para materia prima y producto

create table frutas (
    nombre varchar2(20),
    categoria varchar2(20)
);

insert into frutas values ('Uva','Fruta');


create or replace function crear_producto
return varchar2
is
 v_nombre varchar2(100);
 v_random number;
begin
 v_random := round(dbms_random.value(0,13),0);
/*En la sentencia select con la cláusula offset indicamos que salte v_random
filas y con la cláusula fetch next indicamos que recupere sólo 1 fila (la
siguiente)*/
 select nombre
 into v_nombre
 from frutas
 offset v_random rows
 fetch next 1 rows only;
 return(v_nombre);
exception
 when no_data_found then
 return('Fresa');
end;


create or replace function crear_producto
return varchar2
is
 v_nombre varchar2(100);
 v_random number;
begin
 v_random := round(dbms_random.value(0,13),0);
/*En la sentencia select con la cláusula offset indicamos que salte v_random
filas y con la cláusula fetch next indicamos que recupere sólo 1 fila (la
siguiente)*/
 select nombre
 into v_nombre
 from frutas
 offset v_random rows
 fetch next 1 rows only;
 return (v_nombre);
exception
 when no_data_found then
 return 'Fresa';
end;



create or replace function crear_categoria
return varchar2
is
 categoria varchar2(20);
 v_random number;
begin
 v_random := round(dbms_random.value(0,13),0);
/*En la sentencia select con la cláusula offset indicamos que salte v_random
filas y con la cláusula fetch next indicamos que recupere sólo 1 fila (la
siguiente)*/
 select categoria
 into categoria
 from frutas
 offset v_random rows
 fetch next 1 rows only;
 return (categoria);
exception
 when no_data_found then
 return 'Tubérculo';
end;

-- PARA AÑADIR PERSONAS
declare
    p_nombre varchar2(20);
    p_apellidos varchar2(100);
    p_dni varchar2(9);
    p_email varchar2(100);
begin
for i in 1..200 loop
    p_nombre := crear_nombre;
    p_apellidos := crear_apellidos;
    p_dni := crear_nif;
    p_email := crear_email;
    insert into persona values (
        p_dni,
        p_nombre,
        p_apellidos,
        p_email);
end loop;
end;

delete from persona;

commit;


-- PARA AÑADIR CLIENTES
declare
    cursor cliente_cur is select * from persona fetch next 4900 rows only;
begin
for cliente_fila in cliente_cur loop
    insert into cliente values (
        cliente_fila.nif,
        dbms_random.string('a',20));
end loop;
end;

--PARA AÑADIR TRABAJADORES

create table puestos (
    puesto varchar2(20));
    
insert into puestos values (
    'director');
    
insert into puestos values (
    'aparejador');
    
insert into puestos values (
    'limpieza');
    
insert into puestos values (
    'ingeniero');

declare
    cursor trabajador_cur is select * from persona offset 4900 rows;
    t_residencia varchar2(100);
    t_puesto varchar2(20);
    t_random number;
begin
for trabajador_fila in trabajador_cur loop
    t_residencia := crear_direccion;
    t_random := round(dbms_random.value(0,3),0);
    select puesto
    into t_puesto
    from puestos
    offset t_random rows
    fetch next 1 rows only;
    insert into trabajador values (
        trabajador_fila.nif,
        t_puesto,
        t_residencia);
end loop;
end; 

commit;

-- PARA LOS TELEFONOS
declare
    cursor persona_cur is select * from persona;
    telefono number;
begin
for persona_fila in persona_cur loop
    telefono := crear_tlf;
    insert into teléfonopersona values (
        telefono,
        persona_fila.nif);
end loop;
end; 

commit;

-- PARA LAS DIRECCIONES
declare
    cursor cliente_cur is select * from cliente;
    num_dir number;
    calle varchar2(100);
    ciudad varchar2(30);
    provincia varchar2(50);
    random number;
begin
for cliente_fila in cliente_cur loop
    calle := crear_direccion;
    random := round(dbms_random.value(0,49),0);
    select provincia
    into ciudad
    from dirección2
    offset random rows
    fetch next 1 rows only;
    select provincia
    into provincia
    from dirección2
    offset random rows
    fetch next 1 rows only;
    insert into dirección1 values (
        cliente_fila.nif,
        1,
        calle,
        round(dbms_random.value(0,200),0),
        round(dbms_random.value(0,30),0),
        ciudad,
        provincia);
end loop;
end;


-- PARA QUE TENGAN MAS DE UNA DIRECCION

declare
    cursor cliente_cur is select * from cliente offset 2000 rows;
    num_dir number;
    calle varchar2(100);
    ciudad varchar2(30);
    provincia varchar2(50);
    random number;
begin
for cliente_fila in cliente_cur loop
    calle := crear_direccion;
    random := round(dbms_random.value(0,49),0);
    select provincia
    into ciudad
    from dirección2
    offset random rows
    fetch next 1 rows only;
    select provincia
    into provincia
    from dirección2
    offset random rows
    fetch next 1 rows only;
    insert into dirección1 values (
        cliente_fila.nif,
        2,
        calle,
        round(dbms_random.value(0,200),0),
        round(dbms_random.value(0,30),0),
        ciudad,
        provincia);
end loop;
end;

commit;

-- CARGAR PRODUCTO
declare
    cursor frutas_cur is select * from frutas;
begin
for fruta_linea in frutas_cur loop
    insert into producto values (
        round(dbms_random.value(0,1000),0),
        fruta_linea.nombre,
        fruta_linea.categoria,
        round(dbms_random.value(0,1000),0),
        round(dbms_random.value(0,3),2),
        'imagen',
        'Alimento saludable',
        round(dbms_random.value(0,7),2),
        round(dbms_random.value(0,5),2),
        round(dbms_random.value(0,100),0)
);
end loop;
end;

--CARGAR COLABORADOR

declare
    c_nombre varchar2(30);
    c_apellidos varchar2(50);
    c_completo varchar2(60);
    c_direccion varchar2(100);
begin
for i in 1..100 loop
        c_apellidos := crear_apellidos;
        c_nombre := crear_nombre;
        c_completo := c_nombre||' '||c_apellidos;
        c_direccion := crear_direccion;
        insert into colaborador values (
            TO_CHAR(round(DBMS_RANDOM.VALUE(100000000, 999999999),0)),
            c_completo,
            c_direccion,
            TO_CHAR(round(DBMS_RANDOM.VALUE(10000000000000000000000, 999999999999999999999999),0))
        );
end loop;
end;
            

delete from colaborador; 

-- PARA ACTUALIZAR COLABORADOR Y QUE LA DIRECCION ESTE NORMALIZADA
declare
    cursor colaborador_cur is select * from colaborador;
    random number;
    c_ciudad varchar2(50);
    c_provincia varchar2(50);
begin
for colab in colaborador_cur loop
    random := round(dbms_random.value(0,49),0);
    select provincia
    into c_ciudad
    from dirección2
    offset random rows
    fetch next 1 rows only;
    select provincia
    into c_provincia
    from dirección2
    offset random rows
    fetch next 1 rows only;
    
    update COLABORADOR
    set NÚMERO = round(DBMS_RANDOM.VALUE(1, 200),0),
        CIUDAD = c_ciudad,
        PROVINCIA = c_provincia
    where CIF = colab.CIF;
end loop;
end;

commit;

select count(*)
from dirección2;
-- PARA TELEFONOCOLABORADOR
declare
    cursor colab_cur is select * from colaborador;
begin
for colab_fila in colab_cur loop
    insert into teléfonocolaborador values (
        round(dbms_random.value(600000000,700000000),0),
        colab_fila.cif
    );
end loop;
end;

--PARA QUE TENGAN MAS DE UNO
declare
    cursor colab_cur is select * from colaborador offset 50 rows;
begin
for colab_fila in colab_cur loop
    insert into teléfonocolaborador values (
        round(dbms_random.value(600000000,700000000),0),
        colab_fila.cif
    );
end loop;
end;

commit;

--PARA TRANSPORTISTA Y PROVEEDOR
declare
    cursor colab_cur is select * from colaborador fetch next 50 rows only;
begin
for colab_fila in colab_cur loop
    insert into transportista values (
        colab_fila.cif,
        round(dbms_random.value(0,3),2),
        round(dbms_random.value(0,5),2),
        round(dbms_random.value(5,20),0),
        round(dbms_random.value(200,5000),2)
    );
end loop;
end;
        
        
declare
    cursor colab_cur is select * from colaborador offset 50 rows;
    p_email varchar2(60);
begin
for colab_fila in colab_cur loop
    p_email := crear_email;
    insert into proveedor values (
        colab_fila.cif,
        p_email
    );
end loop;
end;

commit;

--PARA MATERIA PRIMA
declare
    cursor frutas_cur is select * from frutas;
begin
for fruta_linea in frutas_cur loop
    insert into materia_prima values (
        to_char(round(dbms_random.value(1000,9999),0)),
        fruta_linea.nombre,
        round(dbms_random.value(0,1000),2),
        round(dbms_random.value(100,500),2)
);
end loop;
end;

commit;

select count(*)
from producto;
--PARA PRECIOMATERIAPROVEEDOR
declare
    cursor prov_cur is select * from proveedor;
    n_random number;
    m_id varchar2(4);
begin
for prov_linea in prov_cur loop
    n_random := round(dbms_random.value(0,13),0);
    select id_mat
    into m_id
    from materia_prima
    offset n_random rows
    fetch next 1 rows only;
    insert into preciomateriaproveedor values (
        m_id,
        prov_linea.cif,
        round(dbms_random.value(0,2),2)
    );
end loop;
end;

commit;

--PARA PEDIDO
create or replace function crear_fecha (fecha_min date, fecha_max date)
return date
is
begin
return TO_DATE(
 TRUNC(
 DBMS_RANDOM.VALUE(TO_CHAR(fecha_min,'J')
 ,TO_CHAR(fecha_max,'J')
)
 ),'J');
end;

--PARA LINEAPEDIDO
declare
    n_random number;
    id_p varchar2(4);
begin
for i in 1..10000 loop
    n_random := round(dbms_random.value(0,13),0);
    select id_prod
    into id_p
    from producto
    offset n_random rows
    fetch next 1 rows only;
    insert into líneapedido values (
        id_p,
        to_char(round(dbms_random.value(100000000,999999999),0)),
        round(dbms_random.value(1,20),0)
    );
end loop;
end;

-- PARA PEDIDO
declare
    cursor pedido_cur is select * from líneapedido;
    n_random number;
    base_imponible float;
    precio_total float;
    precio_km float;
    precio_kg float;
    precio_producto float;
    peso_producto float;
    fecha date;
    transportista varchar2(9);
    nif varchar2(9);
    dir number;
begin
for pedido_linea in pedido_cur loop
    n_random := round(dbms_random.value(0,49),0);
    select precio_kg, precio_km, cif
    into precio_kg, precio_km, transportista
    from transportista
    offset n_random rows
    fetch next 1 rows only;
    select precio, peso
    into precio_producto, peso_producto
    from producto
    where id_prod=pedido_linea.id_prod;
    base_imponible := precio_producto*pedido_linea.cantidad+peso_producto*pedido_linea.cantidad*precio_kg+precio_km*round(dbms_random.value(20,500),2);
    precio_total := base_imponible*(121/100);
    fecha := crear_fecha('01/01/2021', sysdate);
    n_random := round(dbms_random.value(0,7799),0);
    select nif, num_dir
    into nif, dir
    from dirección1
    offset n_random rows
    fetch next 1 rows only;
    insert into pedido values (
        pedido_linea.id_ped,
        fecha,
        base_imponible,
        21,
        precio_total,
        transportista,
        nif,
        dir
    );
end loop;
end;

-- PARA ENVIADO
declare
    cursor preparado_cur is select * from preparado fetch next 2000 rows only;
    fecha_envio date;
    coste_envio float;
    id_producto varchar2(4);
    t_cif varchar2(9);
    base float;
    precio_producto float;
    cantidad number;
    restar float;
begin
for preparado_linea in preparado_cur loop
    fecha_envio := crear_fecha(preparado_linea.fecha_preparado, sysdate);
    select transportista_elegido
    into t_cif
    from pedido
    where id_ped=preparado_linea.id_ped;
    select id_prod, cantidad
    into id_producto, cantidad
    from líneapedido
    where id_ped=preparado_linea.id_ped;
    select precio
    into precio_producto
    from producto
    where id_prod=id_producto;
    restar := precio_producto*cantidad;
    select base_imponible
    into base
    from pedido
    where id_ped=preparado_linea.id_ped;
    coste_envio := base-restar;
    insert into enviado values (
        preparado_linea.id_ped,
        fecha_envio,
        t_cif,
        coste_envio
    );
end loop;
end;

commit;


--ESPECIALIZACIONES PEDIDO
-- CREAR PEDIDOS CONFIRMADOS

declare
    cursor conf_ped_cur is select * from pedido fetch next 8000 rows only;
    fecha date;
begin
for pedido_fila in conf_ped_cur loop
    fecha := crear_fecha(pedido_fila.fecha_creacion, pedido_fila.fecha_creacion+14);
    insert into confirmado values (
        pedido_fila.id_ped,
        fecha);
end loop;
end;


-- CREAR PEDIDOS PREPARADOS
declare
    cursor prep_ped_cur is select * from confirmado fetch next 6000 rows only;
    fecha date;
    nif_select varchar2(9);
    n_random number;
begin
for pedido_fila in prep_ped_cur loop
    n_random := round(dbms_random.value(0,99),0);
    select nif
    into nif_select
    from trabajador
    offset n_random rows
    fetch next 1 rows only;
    fecha := crear_fecha(pedido_fila.fecha_pago+1, pedido_fila.fecha_pago+7);
    insert into preparado values (
        pedido_fila.id_ped,
        fecha,
        nif_select);
end loop;
end;

-- CREAR PEDIDOS ENVIADOS
declare
    cursor preparado_cur is select * from preparado fetch next 4000 rows only;
    fecha_envio date;
    coste_envio float;
    id_producto varchar2(4);
    t_cif varchar2(9);
    base float;
    precio_producto float;
    cantidad number;
    restar float;
begin
for preparado_linea in preparado_cur loop
    fecha_envio := crear_fecha(preparado_linea.fecha_preparado+1, preparado_linea.fecha_preparado+7);
    select transportista_elegido
    into t_cif
    from pedido
    where id_ped=preparado_linea.id_ped;
    select id_prod, cantidad
    into id_producto, cantidad
    from líneapedido
    where id_ped=preparado_linea.id_ped;
    select precio
    into precio_producto
    from producto
    where id_prod=id_producto;
    restar := precio_producto*cantidad;
    select base_imponible
    into base
    from pedido
    where id_ped=preparado_linea.id_ped;
    coste_envio := base-restar;
    insert into enviado values (
        preparado_linea.id_ped,
        fecha_envio,
        t_cif,
        coste_envio
    );
end loop;
end;


-- CREAR PEDIDOS RECIBIDOS
declare
    cursor reci_ped_cur is select * from enviado fetch next 2000 rows only;
    fecha date;

begin
for pedido_fila in reci_ped_cur loop
    fecha := crear_fecha(pedido_fila.fecha_envio, pedido_fila.fecha_envio+7);
    insert into recibido values (
        pedido_fila.id_ped,
        fecha);
end loop;
end;

-- PARA FACTURA
declare
 cursor recibido_cur is select * from recibido;
 fecha date;
begin
for recibido_linea in recibido_cur loop
    fecha := crear_fecha(recibido_linea.fecha_entrega+1, sysdate);
    insert into factura values (
        to_char(round(dbms_random.value(100000000,999999999),0)),
        fecha,
        recibido_linea.id_ped
    );
end loop;
end;

--PARA VALORACION
declare
    cursor recibido_cur is select * from recibido fetch next 1000 rows only;
    id_prod varchar2(4);
begin
for recibido_linea in recibido_cur loop
    select id_prod
    into id_prod
    from líneapedido
    where id_ped=recibido_linea.id_ped;
    insert into valoración values (
        id_prod,
        recibido_linea.id_ped,
        round(dbms_random.value(0,5),2)
    );
end loop;
end;
    
    
    
-- DISPARADORES

create or replace trigger ins_valoracion
after insert on VALORACIÓN
for each row
declare
    suma float;
    total float;
    nueva_nota float;
begin
    select SUM(nota)
    into suma
    from VALORACIÓN
    where id_prod = :NEW.id_prod;
    
    select count(*)
    into total
    from VALORACIÓN
    where id_prod = :NEW.id_prod;
    
    nueva_nota := suma/total;
    
    update producto
    set nota_media = nueva_nota
    where id_prod = :NEW.id_prod;
end;

select nota_media
from producto
where id_prod = 977;

select *
from pedido;

select *
from valoración
where id_prod = 977;

insert into valoración values (977, 157139409, 5);
    
    

        
        
