/* Una lista de los nombres y apellidos dede la tabla de EMPLOYEES.*/
select LastName, FirstName from Employees
/*Una lista de todos los nombres de las ciudades que aparecen en la tabla de EMPLOYEES. No mostrar 2 veces un mismo nombre de ciudad.*/
select City from Employees group by City
/*Una lista de los nombres de productos y precios unitarios de la tabla PRODUCTS.*/
select ProductName, UnitPrice from Products
/*En la tabla EMPLOYEES: una lista de los detalles completos de quienes viven en EE.UU.*/
select * from Employees where Country = 'USA'
/*A partir de la tabla ORDERS, listar todos los pedidos que tienen un gasto de envio > 50.*/
select * from Orders where Freight > 50
/*De la tabla de CUSTOMERS: listar nombre de la empresa de clientes donde el cargo es igual a Owner.*/
select CompanyName from Customers where ContactTitle = 'owner'
/*A partir de la tabla CUSTOMERS una lista de clientes cuyo nombre comienza con la letra "A”.*/
select * from Customers where ContactName like 'a%'
/*Una lista de los nombres de clientes donde la región no está en blanco.*/
select ContactName from Customers where Region is not null
/*Una lista de todos los productos, ordenado por precio unitario (el más barato primero).*/
select * from Products order by UnitPrice asc
/*Una lista de todos los productos, ordenado por precio unitario (el más caro primero).*/
select * from Products order by UnitPrice desc
/*El número total de registros de la tabla EMPLOYEES. Nombre de la columna de salida "TotalEmpleados".*/
select COUNT(*) as TotalEmpleados from Employees
/*De la tabla de pedidos, el gasto de envío promedio y el máximo gasto de envío.*/
select AVG(Freight) as Promedio, MAX(Freight) as Maximo from Orders