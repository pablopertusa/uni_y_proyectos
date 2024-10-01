create or replace FUNCTION gastos_cliente(p_NIF IN VARCHAR2) RETURN NUMBER IS
    v_number NUMBER;
    v_sum NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_number
    from pedido
    WHERE NIF_dir = p_NIF;

    IF v_number = 0 THEN
        DBMS_OUTPUT.PUT_LINE('El cliente || p_NIF || no tiene pedidos');
        RETURN 0;
    ELSE
        select sum(precio_total) into v_sum
        from pedido
        where NIF_dir = p_NIF;
        DBMS_OUTPUT.PUT_LINE('El cliente || p_NIF || tiene || v_number || pedidos con valor || v_sum');
        RETURN v_sum;
    END IF;
END;


create or replace FUNCTION compra_prom_pedido_con_producto(p_id_prod IN VARCHAR2) RETURN NUMBER IS
    v_number NUMBER;
    v_media NUMBER;
    v_precio FLOAT;
BEGIN

    SELECT COUNT(*) INTO v_number
    from líneapedido
    where id_prod = p_id_prod; 

    IF v_number = 0 THEN
        DBMS_OUTPUT.PUT_LINE('No existen pedidos con el producto');
        RETURN 0;
    END IF;
    
    SELECT precio INTO v_precio
    from producto
    where id_prod = p_id_prod; 
    
    SELECT round((sum(cantidad)/v_number),3)*v_precio INTO v_media
    from líneapedido
    WHERE id_prod = p_id_prod;
    DBMS_OUTPUT.PUT_LINE('Los pedidos que contienen ese producto, en promedio cuestan || v_media');
    RETURN v_media;

END;


create or replace function estado_pedido(
    n_id_pedido varchar2
)
return varchar2
is
    n_pedidos number;

begin
    select count(*) into n_pedidos
    from pedido
    where id_ped = n_id_pedido;

    if n_pedidos = 0 then
        return('El pedido no existe');
    end if;

    select count(*) into n_pedidos
    from confirmado
    where id_ped = n_id_pedido;

    if n_pedidos = 0 then
        return('El pedido está sin confirmar');
    end if;

    select count(*) into n_pedidos
    from preparado
    where id_ped = n_id_pedido;

    if n_pedidos = 0 then
        return('El pedido está confirmado');
    end if;

    select count(*) into n_pedidos
    from enviado
    where id_ped = n_id_pedido;

    if n_pedidos = 0 then
        return('El pedido está preparado');
    end if;

    select count(*) into n_pedidos
    from recibido
    where id_ped = n_id_pedido;

    if n_pedidos = 0 then
        return('El pedido está enviado');
    end if;

    if n_pedidos = 1 then
        return('El pedido está recibido');
    end if;
end;