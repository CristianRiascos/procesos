
<html>

<head>
<meta charset="UTF-8">
<title>Login</title>
<link rel="stylesheet" href="estilos.css">
</head>

<body>
    <nav>
        <ul>
          <li><a href="principal.html">Inicio</a></li>
          <li><a href="index.html">Iniciar sesion</a></li>
          <li><a href="productos.html">Productos</a></li>
        </ul>
      </nav>
<form action="login_registrar.php" method="POST">
    <div class="header">
        <img src="logo.png" alt="Logo de la aplicación" width="100" height="100" />
    </div>
<h2>Iniciar sesión</h2>
<input type="text" placeholder="&#128273; Usuario" name="usuario" required>
<input type="password" placeholder="&#128274; Contraseña" name="pass" required>
<input type="submit" value="Ingresar" name="btningresar">

<br>
<a href="registrar.html" style="float:right">Crear una cuenta</a>

</form>
</body>
</html>