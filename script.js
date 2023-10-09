const iconPerfil = document.getElementById('icon_perfil');
const menuSuspenso = document.getElementById('menu-suspenso');

iconPerfil.addEventListener('click', function() {
    menuSuspenso.classList.toggle('active');
});

// Feche o menu se o usuário clicar fora dele
document.addEventListener('click', function(event) {
    if (!menuSuspenso.contains(event.target) && event.target !== iconPerfil) {
        menuSuspenso.classList.remove('active');
    }
});
