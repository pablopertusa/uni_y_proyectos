create or replace TRIGGER TR_VALORACION
BEFORE INSERT OR DELETE ON valoración
FOR EACH ROW
DECLARE 
    v_sum NUMBER := 0;
    v_total NUMBER := 0;

BEGIN
    IF INSERTING THEN    
        select producto.recuento_valoraciones+1 into v_total
        from producto
        where producto.id_prod = :new.id_prod;

        UPDATE producto
        set producto.recuento_valoraciones = v_total
        where producto.id_prod = :new.id_prod;


        select (producto.nota_media*(v_total-1))+:new.nota into v_sum
        from producto
        where producto.id_prod = :new.id_prod;


        UPDATE producto
        set producto.nota_media = round((v_sum/v_total),3)
        where producto.id_prod = :new.id_prod;

    ELSIF DELETING THEN

        select producto.recuento_valoraciones-1 into v_total
        from producto
        where producto.id_prod = :old.id_prod;

        UPDATE producto
        set producto.recuento_valoraciones = v_total
        where producto.id_prod = :old.id_prod;


        select (producto.nota_media*(v_total+1))-:old.nota into v_sum
        from producto
        where producto.id_prod = :old.id_prod;


        UPDATE producto
        set producto.nota_media = round((v_sum/v_total),3)
        where producto.id_prod = :old.id_prod;

    ELSIF UPDATING THEN

        select producto.recuento_valoraciones into v_total
        from producto
        where producto.id_prod = :old.id_prod;

        select ((producto.nota_media*(v_total))-:old.nota+:new.nota) into v_sum
        from producto
        where producto.id_prod = :old.id_prod;

        UPDATE producto
        set producto.nota_media = round((v_sum/v_total),3)
        where producto.id_prod = :old.id_prod;


    END IF;
END;




create or replace trigger ins_enviado
before insert on enviado
for each row
declare
    elegido varchar2(9);
begin
    select transportista_elegido
    into elegido
    from pedido
    where id_ped = :new.id_ped;

    if elegido <> :new.cif then
    raise_application_error(-20001, 'El transportista no coincide con el elegido por el cliente');
    end if;
end;





create or replace trigger ins_preparado_fecha
before insert on preparado
for each row
declare
    fecha date;
begin
    select fecha_pago
    into fecha
    from confirmado
    where id_ped = :new.id_ped;

    if fecha > :new.fecha_preparado then
        raise_application_error(-20002, 'La fecha de preparado no puede ser antes que la de confirmado');
    end if;
end;




create or replace trigger ins_enviado_fecha
before insert on enviado
for each row
declare
    fecha date;
begin
    select fecha_preparado
    into fecha
    from preparado
    where id_ped = :new.id_ped;

    if fecha > :new.fecha_envio then
        raise_application_error(-20003, 'La fecha de envio no puede ser antes que la de preparado');
    end if;
end;





create or replace trigger ins_recibido_fecha
before insert on recibido
for each row
declare
    fecha date;
begin
    select fecha_envio
    into fecha
    from enviado
    where id_ped = :new.id_ped;

    if fecha > :new.fecha_entrega then
    raise_application_error(-20004, 'La fecha de entrega no puede ser antes que la de envío');
    end if;
end;

