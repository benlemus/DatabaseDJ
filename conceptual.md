### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is a database management system. PostrebhgvSQL specifically is a object-relational database management system which means it uses an object oriented design.

- What is the difference between SQL and PostgreSQL?
  SQL is the relational database platform iteself. PostgreSQL uses SQL but offers more customization.

- In `psql`, how do you connect to a database?
  In psql you can connect to a database by using the `/c (database name)` in the command line when in `psql` or you can skip that and use `psql (database name)` straight from the terminal if you are in the correct file directory.

- What is the difference between `HAVING` and `WHERE`?
  `WHERE` filters data before grouping and cannot use aggregate functions like sum(), avg(), ect. `HAVING` must be used after a group by and can use aggregate functions like sum(), avg(), ect.

- What is the difference between an `INNER` and `OUTER` join?
  When doing an `INNER` join, it only joins data that matches between two tables. `OUTER` joins will join any data whether it matches or not.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  A `LEFT OUTER` join will join all data all rows from the first inputted table and join only the matching data from the second table. A `RIGHT OUTER` join will do the opposite, it will join all rows from the sencond table but only join matching data from the first table. Any data not matched will be null.

- What is an ORM? What do they do?
  An ORM is an 'Object-Relational Mapper'. This means that it does all the heavy lifting to transform something like a flask python class(object oriented class) into a format that a database can read.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?
  A main difference is that AJAX are mostly asynchronus which means that when a page is loaded, the browser can skkip the request and run it in the background and load everything else but come back to the request when called. Usually, from the server side, it waits for a response. AJAX is also used in the web browser using Javascript but servers use the web server and use a language lie python.

- What is CSRF? What is the purpose of the CSRF token?
  CSRF stands for 'Cross-Site Request Forgery'. It is when attackers make a fake pae or link that when clicked, grants them access to personal information. They ggain control over the victims account. The purpose of the token is to stop attackers by sending a specific and random token, if the token is not there, the server knows it is probably bad and does rejects the request.

- What is the purpose of `form.hidden_tag()`?
  The purpose of `form.hidden_tag()` is to render the hidden form fields, like the CSRF token, it is hidden by default so it will not be used if `form.hidden_tag()` is not included.
