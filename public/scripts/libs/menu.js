// Отображение - скрытие меню
function handlerMenu() {
    let menu = document.querySelector('menu');
    let menuClass = menu.getAttribute('class');
    let closeMenu = document.querySelector('#closeMenu');

    switch(menuClass) {
        case 'hiddenMenu':
        menu.setAttribute('class', 'visibleMenu');
        closeMenu.setAttribute('class', 'visibleCloseMenu');
        break;

        case 'visibleMenu':
        menu.setAttribute('class', 'hiddenMenu');
        closeMenu.setAttribute('class', 'hiddenCloseMenu');
        break;
    }
}