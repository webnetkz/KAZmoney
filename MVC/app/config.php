<?php
/**
 * Настройки скриптов
*/
//Начало переменных замены
define('KEY_START', '{');
//Конец переменных замены
define('KEY_END', '}');
//fele exits design
define('FILEEXT', '.html');
//Папка с компьютерной версией 
define('PAGEDIRCOMPUTER', 'comp/');
//Папка с мобильной версией 
define('PAGEDIRMOBILE', 'mobile/');

//Папка с файлами отображения
define('PAGEDIRCOMP', 'app/views/'.PAGEDIRCOMPUTER);
//Доменное имя приложения
define('DOMAINSERVER', 'http://' . $_SERVER['HTTP_HOST']);
//Папка с моделями
define("PATCHMODEL", 'app/models/');
//Папка с контроллерами
define("PATCCONTROLLERS", 'app/controllers/');
//Папка с файлами javascript
define('JSFOLDER', DOMAINSERVER.'/app/views/comp/js/');
//Папка с файлами css
define('CSSFOLDER', DOMAINSERVER.'/app/views/comp/css/');
//папка с файлами images
define('IMGFOLDER', DOMAINSERVER.'/app/views/comp/images/');
/**
 * Настройки базы данных
*/
//Хост базы данных
define('DBHOST', 'localhost');
//Логин базы данных
define('DBLOGIN', '');
//Пароль базы данных
define('DBPASSWORD', '');
//Название базы данных
define('DBNAME', '');
/**
 * Настройки роутера
*/
//Контроллер по умолчанию
define("CONTROLLERDEFAULT", 'Main');
//Действие по умолчанию
define("ACTIONDEFAULT", 'Index');

//Выводим сообщение что файл config.php подключен
echo "Файл config.php подключен<br>";

?>