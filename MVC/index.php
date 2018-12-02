<?php
// Подключение файла для отладки приложения
require "app/lib/Dev.php";


use app\core\Router;
use app\controllers\AccountController;

spl_autoload_register(function($class){
	$path = str_replace('\\', '/', $class.'.php');
	
	if (file_exists($path) ) {
		require $path;
	}
});

// Запуск сессий
session_start();


// Создание объекта и запуск метода
$router = new Router;
$router->run();

