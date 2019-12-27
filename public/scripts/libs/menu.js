// Отображение - скрытие меню
function handlerMenu() {
    let menu = document.querySelector('menu');
    let menuClass = menu.getAttribute('class');
    let closeMenu = document.querySelector('#closeMenu');
    let btnMenu = document.querySelector('.btnMenu');

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