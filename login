<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comer Bem - Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: #eaeae0;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            padding: 20px;
            text-align: center;
            position: relative;
        }

        .login-container h1 {
            font-size: 24px;
            margin-bottom: 10px;
            color: #bdaa78;
            font-family: 'Brush Script MT', cursive;
        }

        .login-container p {
            margin: 0;
            color: #333;
            font-size: 18px;
            margin-bottom: 20px;
        }

        .login-container img {
            border-radius: 50%;
            width: 80px;
            height: 80px;
            margin-bottom: 20px;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }

        .login-container .eye-icon {
            position: absolute;
            top: 143px; /* Ajuste para alinhar o ícone */
            right: 30px;
            cursor: pointer;
        }

        .login-container a {
            color: #65b48a;
            text-decoration: none;
            display: block;
            margin: 10px 0;
        }

        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #bdaa78;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }

        .login-container button:hover {
            background-color: #9d8a5a;
        }

        .footer {
            font-size: 12px;
            color: #777;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>COMER BEM</h1>
        <p>Uma Vida mais Saudável</p>
        <img src="avatar-placeholder.png" alt="Avatar">
        
        <input type="text" placeholder="Conta">
        
        <div style="position: relative;">
            <input id="password" type="password" placeholder="Senha">
            <span class="eye-icon" onclick="togglePassword()">👁️</span>
        </div>

        <a href="#">Esqueci a senha</a>
        <button>Login</button>

        <div class="footer">
            <p>Política de Privacidade - Acordo do Usuário</p>
        </div>
    </div>

    <script>
        function togglePassword() {
            const passwordField = document.getElementById('password');
            const eyeIcon = document.querySelector('.eye-icon');

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                eyeIcon.textContent = '🙈'; // Muda o ícone para indicar que a senha está visível
            } else {
                passwordField.type = 'password';
                eyeIcon.textContent = '👁️'; // Muda o ícone para indicar que a senha está oculta
            }
        }
    </script>
</body>
</html>
