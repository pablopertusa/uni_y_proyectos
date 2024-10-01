create or replace PROCEDURE a�adir_tlf
(
    p_NIF in varchar2,
    p_tlf in int
) AS

v_count number;
BEGIN

    IF p_tlf > 999999999 OR p_tlf < 100000000 THEN
        raise_application_error(-20101,'N�mero de tel�fono no v�lido.');
    END IF;

    SELECT COUNT(*) INTO v_count
    FROM Persona
    WHERE NIF = p_NIF;

    IF v_count = 0 THEN
        raise_application_error(-20122, 'La persona con el NIF dado no existe en la base de datos.');

    END IF;

    SELECT COUNT(*) INTO v_count
    FROM TEL�FONOPERSONA
    WHERE telefono = p_tlf;

    IF v_count > 0 THEN
        raise_application_error(-20102,'El tel�fono ya se encuentra asociado a un NIF.');
    END IF;


    INSERT INTO TEL�FONOPERSONA(telefono, nif)
    VALUES (p_tlf, p_NIF);   
    DBMS_OUTPUT.PUT_LINE('Nuevo tel�fono insertado correctamente.');
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END a�adir_tlf;





create or replace PROCEDURE a�adir_direccion
(
    p_NIF in varchar2,
    p_calle in varchar2,
    p_numero in int,
    p_puerta in varchar2,
    p_ciudad in varchar2,
    p_provincia in varchar2
) AS
    v_num_dir number;
    v_number number;
BEGIN

    SELECT COUNT(*) INTO v_number
    FROM Cliente
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        raise_application_error(-20022,'El cliente con el NIF dado no existe en la base de datos.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM Direcci�n1
    WHERE NIF = p_NIF and calle = p_calle and numero = p_numero
    and puerta = p_puerta and ciudad = p_ciudad and provincia = p_provincia;

    IF v_number = 1 THEN
        raise_application_error(-20023,'Direcci�n registrada previamente.');
    END IF;



    SELECT COUNT(*) INTO v_number
    FROM Direcci�n1
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        v_num_dir := 1;
    ELSE
        SELECT (MAX(num_dir) + 1) INTO v_num_dir
        FROM Direcci�n1
        WHERE NIF = p_NIF;
    END IF;


    INSERT INTO Direcci�n1 (NIF, num_dir, calle, numero, puerta, ciudad, provincia)
    VALUES (p_NIF, v_num_dir, p_calle, p_numero, p_puerta, p_ciudad, p_provincia);
    DBMS_OUTPUT.PUT_LINE('Nueva direcci�n agregada correctamente.');
    COMMIT;

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END a�adir_direccion;





create or replace PROCEDURE borrar_direccion
(
    p_NIF in varchar2,
    p_num_dir in int
) AS
    v_number number;
BEGIN

    SELECT COUNT(*) INTO v_number
    FROM Cliente
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        raise_application_error(-20022,'El cliente con el NIF dado no existe en la base de datos.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM Pedido
    WHERE NIF_dir = p_NIF and num_dir = p_num_dir;

    IF v_number > 0 THEN
        raise_application_error(-20024,'No se puede borrar una direcci�n asociada a un pedido.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM Direcci�n1
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        raise_application_error(-20025,'El cliente no tiene direcciones asociadas.');
    ELSE

        SELECT COUNT(*) INTO v_number
        FROM Direcci�n1
        WHERE NIF = p_NIF and num_dir = p_num_dir;

        IF v_number = 0 THEN
            raise_application_error(-20026,'La direcci�n no existe.');
        ELSE
            DELETE FROM Direcci�n1
            WHERE NIF = p_NIF AND num_dir = p_num_dir;
            DBMS_OUTPUT.PUT_LINE('La direcci�n eliminada correctamente.');
            COMMIT;
        END IF;

    END IF;



EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END borrar_direccion;






create or replace PROCEDURE modificar_destino_pedido
(
    p_NIF in varchar2,
    p_ID_ped in varchar2,
    p_num_dir in int
) AS
v_count number;

BEGIN

    SELECT COUNT(*) INTO v_count
    FROM Pedido
    WHERE NIF_dir = p_NIF and ID_PED = p_ID_ped;


    IF v_count = 0 THEN
        raise_application_error(-20027,'El pedido no existe en la base de datos.');
    END IF;

    SELECT COUNT(*) INTO v_count
    FROM Enviado
    WHERE ID_PED = p_ID_ped;


    IF v_count = 1 THEN
        raise_application_error(-20028,'No se puede modificar la direcci�n asociada a un pedido en env�o o recibido.');
    END IF;


    SELECT COUNT(*) INTO v_count
    FROM Pedido
    WHERE NIF_dir = p_NIF and ID_PED = p_ID_ped and num_dir = p_num_dir;

    IF v_count = 1 THEN
        raise_application_error(-20029,'No se puede seleccionar la misma direcci�n.');
    END IF;

    SELECT COUNT(*) INTO v_count
    FROM Direcci�n1
    WHERE NIF = p_NIF and num_dir = p_num_dir;

    IF v_count = 0 THEN
        raise_application_error(-20026,'La direcci�n no existe.');
    END IF;

UPDATE PEDIDO SET num_dir = p_num_dir 
where id_ped=p_ID_ped;
DBMS_OUTPUT.PUT_LINE('Direcci�n modificada correctamente.');
COMMIT;
EXCEPTION
    WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE(SQLERRM);
END modificar_destino_pedido;





create or replace PROCEDURE a�adir_valoracion
(
    p_id_ped in varchar2,
    p_id_prod in varchar2,
    p_nota in varchar2
) AS
v_number number;
v_nota number := TO_NUMBER(p_nota);
BEGIN


    SELECT COUNT(*) INTO v_number
    FROM producto
    WHERE id_prod = p_id_prod;

    IF v_number = 0 THEN
        raise_application_error(-20201,'ID de producto incorrecto.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM recibido
    WHERE id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20202,'N�mero de pedido incorrecto.');
    END IF;


    SELECT COUNT(*) INTO v_number
    FROM l�neapedido
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20203,'El producto debe haber sido adquirido para evaluarlo.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM valoraci�n
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 1 THEN
        raise_application_error(-20204,'No se puede valorar otra vez el producto, elimine su valoraci�n previa primero.');
    END IF;


    IF v_nota BETWEEN 0.0 AND 5.0 THEN
        INSERT INTO valoraci�n(id_prod, id_ped, nota)
        VALUES(p_id_prod, p_id_ped, v_nota);
        DBMS_OUTPUT.PUT_LINE('Valoraci�n a�adida correctamente.');
        COMMIT;
    ELSE
        raise_application_error(-20205,'Valor num�rico no admitido.');
        RETURN;

    END IF;


EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END a�adir_valoracion;






create or replace PROCEDURE borrar_valoracion
(
    p_id_ped in varchar2,
    p_id_prod in varchar2
) AS
v_number number;
BEGIN



    SELECT COUNT(*) INTO v_number
    FROM producto
    WHERE id_prod = p_id_prod;

    IF v_number = 0 THEN
        raise_application_error(-20201,'ID de producto incorrecto.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM recibido
    WHERE id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20202,'N�mero de pedido incorrecto.');
    END IF;   


    SELECT COUNT(*) INTO v_number
    FROM valoraci�n
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20200, 'La valoraci�n seleccionada no existe.');
    END IF;


    DELETE FROM valoraci�n
    WHERE id_ped = p_id_ped
    AND id_prod = p_id_prod;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Valoraci�n eliminada satisfactoriamente.');



EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END borrar_valoracion;