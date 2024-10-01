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

