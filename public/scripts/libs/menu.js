// Отображение - скрытие меню
function handlerMenu() {
    let menu = document.querySelector('menu');
    let menuClass = menu.getAttribute('class');
    let closeMenu = document.querySelector('#closeMenu');
    let btnMenu = document.querySelector('.btnMenu');

    // Добавление звука при открытии\закрытии меню
    var audio = document.createElement('audio');
    audio.setAttribute("autoplay", "true");
    audio.innerHTML = "<source src=\"public/audio/test.mp3\" type=\"audio/mpeg\">";
    document.body.appendChild(audio);
    setTimeout(() => audio.remove(), 1000);
    
    // Проверка если меню открыто\закрыть
    switch(menuClass) {
        case 'hiddenMenu':
        menu.setAttribute('class', 'visibleMenu');
        closeMenu.setAttribute('class', 'visibleCloseMenu');
        btnMenu.setAttribute('style', 'left: -100px');
        break;

        case 'visibleMenu':
        menu.setAttribute('class', 'hiddenMenu');
        closeMenu.setAttribute('class', 'hiddenCloseMenu');
        btnMenu.setAttribute('style', 'left: 5px');
        break;
    }
}