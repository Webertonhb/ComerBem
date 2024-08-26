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
