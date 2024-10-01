create or replace PROCEDURE añadir_tlf
(
    p_NIF in varchar2,
    p_tlf in int
) AS

v_count number;
BEGIN

    IF p_tlf > 999999999 OR p_tlf < 100000000 THEN
        raise_application_error(-20101,'Número de teléfono no válido.');
    END IF;

    SELECT COUNT(*) INTO v_count
    FROM Persona
    WHERE NIF = p_NIF;

    IF v_count = 0 THEN
        raise_application_error(-20122, 'La persona con el NIF dado no existe en la base de datos.');

    END IF;

    SELECT COUNT(*) INTO v_count
    FROM TELÉFONOPERSONA
    WHERE telefono = p_tlf;

    IF v_count > 0 THEN
        raise_application_error(-20102,'El teléfono ya se encuentra asociado a un NIF.');
    END IF;


    INSERT INTO TELÉFONOPERSONA(telefono, nif)
    VALUES (p_tlf, p_NIF);   
    DBMS_OUTPUT.PUT_LINE('Nuevo teléfono insertado correctamente.');
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END añadir_tlf;





create or replace PROCEDURE añadir_direccion
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
    FROM Dirección1
    WHERE NIF = p_NIF and calle = p_calle and numero = p_numero
    and puerta = p_puerta and ciudad = p_ciudad and provincia = p_provincia;

    IF v_number = 1 THEN
        raise_application_error(-20023,'Dirección registrada previamente.');
    END IF;



    SELECT COUNT(*) INTO v_number
    FROM Dirección1
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        v_num_dir := 1;
    ELSE
        SELECT (MAX(num_dir) + 1) INTO v_num_dir
        FROM Dirección1
        WHERE NIF = p_NIF;
    END IF;


    INSERT INTO Dirección1 (NIF, num_dir, calle, numero, puerta, ciudad, provincia)
    VALUES (p_NIF, v_num_dir, p_calle, p_numero, p_puerta, p_ciudad, p_provincia);
    DBMS_OUTPUT.PUT_LINE('Nueva dirección agregada correctamente.');
    COMMIT;

EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END añadir_direccion;





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
        raise_application_error(-20024,'No se puede borrar una dirección asociada a un pedido.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM Dirección1
    WHERE NIF = p_NIF;

    IF v_number = 0 THEN
        raise_application_error(-20025,'El cliente no tiene direcciones asociadas.');
    ELSE

        SELECT COUNT(*) INTO v_number
        FROM Dirección1
        WHERE NIF = p_NIF and num_dir = p_num_dir;

        IF v_number = 0 THEN
            raise_application_error(-20026,'La dirección no existe.');
        ELSE
            DELETE FROM Dirección1
            WHERE NIF = p_NIF AND num_dir = p_num_dir;
            DBMS_OUTPUT.PUT_LINE('La dirección eliminada correctamente.');
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
        raise_application_error(-20028,'No se puede modificar la dirección asociada a un pedido en envío o recibido.');
    END IF;


    SELECT COUNT(*) INTO v_count
    FROM Pedido
    WHERE NIF_dir = p_NIF and ID_PED = p_ID_ped and num_dir = p_num_dir;

    IF v_count = 1 THEN
        raise_application_error(-20029,'No se puede seleccionar la misma dirección.');
    END IF;

    SELECT COUNT(*) INTO v_count
    FROM Dirección1
    WHERE NIF = p_NIF and num_dir = p_num_dir;

    IF v_count = 0 THEN
        raise_application_error(-20026,'La dirección no existe.');
    END IF;

UPDATE PEDIDO SET num_dir = p_num_dir 
where id_ped=p_ID_ped;
DBMS_OUTPUT.PUT_LINE('Dirección modificada correctamente.');
COMMIT;
EXCEPTION
    WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE(SQLERRM);
END modificar_destino_pedido;





create or replace PROCEDURE añadir_valoracion
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
        raise_application_error(-20202,'Número de pedido incorrecto.');
    END IF;


    SELECT COUNT(*) INTO v_number
    FROM líneapedido
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20203,'El producto debe haber sido adquirido para evaluarlo.');
    END IF;

    SELECT COUNT(*) INTO v_number
    FROM valoración
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 1 THEN
        raise_application_error(-20204,'No se puede valorar otra vez el producto, elimine su valoración previa primero.');
    END IF;


    IF v_nota BETWEEN 0.0 AND 5.0 THEN
        INSERT INTO valoración(id_prod, id_ped, nota)
        VALUES(p_id_prod, p_id_ped, v_nota);
        DBMS_OUTPUT.PUT_LINE('Valoración añadida correctamente.');
        COMMIT;
    ELSE
        raise_application_error(-20205,'Valor numérico no admitido.');
        RETURN;

    END IF;


EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END añadir_valoracion;






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
        raise_application_error(-20202,'Número de pedido incorrecto.');
    END IF;   


    SELECT COUNT(*) INTO v_number
    FROM valoración
    WHERE id_prod = p_id_prod
    AND id_ped = p_id_ped;

    IF v_number = 0 THEN
        raise_application_error(-20200, 'La valoración seleccionada no existe.');
    END IF;


    DELETE FROM valoración
    WHERE id_ped = p_id_ped
    AND id_prod = p_id_prod;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('Valoración eliminada satisfactoriamente.');



EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END borrar_valoracion;