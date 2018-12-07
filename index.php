<?php

require "app/lib/Dev.php";

use app\core\Stat;
use app\core\Router;
use app\controllers\AccountController;

spl_autoload_register(function($class){
	$path = str_replace('\\', '/', $class.'.php');
	
	if (file_exists($path) ) {
		require $path;
	}
});

session_start();

$router = new Router;
$router->run();

$stat = new Stat;




