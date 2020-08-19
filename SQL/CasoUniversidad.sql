/*Lista las asignaturas del tipo "optativa".*/
select * from asignatura where tipo = 'optativa'
/*Lista los nombres de Departamento de la Universidad.*/
select nombre from departamento
/*Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayúsculas*/
select upper(apellido1), upper(apellido2), upper(nombre) from persona
/*Listar  apellidos y nombres de Profesores mayores a 40 años en la Universidad.*/
select persona.apellido1, persona.apellido2, persona.nombre from profesor inner join persona on persona.id = profesor.id_profesor where dateadd(year, 40, persona.fecha_nacimiento) < getdate()