<?php
// Пространство имен
namespace app\core;

use app\core\View;

// Класс Router
class Router {
	
	// Массивы с параметрами класса
	protected $routes = [];
	protected $params = [];
	
	public function __construct() {
		
		// Подключение файла конфигурации маршрутов
		$arr = require 'app/config/routes.php';
		
		foreach ($arr as $key => $val) {
			$this->add($key, $val);
		}
	}

	// Метод добавления маршрута
	public function add($route, $params) {

		$route = '#^'.$route.'$#'; 
		$this->routes[$route] = $params;
	}
	
	// Метод проверки маршрута
	public function match() {
		
		$url = trim($_SERVER['REQUEST_URI'], '/');

		foreach ($this->routes as $route => $params) {
			
			if (preg_match($route, $url, $matches) ) {
				
				$this->params = $params;
				return true;
			}
		}
		return false;
	}
	
	// Метод запуска маршрута
	public function run() {
		
		if ($this->match() ) {
			$path = 'app\controllers\\'.ucfirst($this->params['controller']).'Controller';
			
			
			if (class_exists($path) ) {
				$action = $this->params['action'].'Action';
				
				if (method_exists($path, $action) ) {
					$controller = new $path($this->params);
					$controller->$action();
				} else {
					View::errorCode(404);
				}

			} else {
				View::errorCode(404);
			}

		} else {
			View::errorCode(404);
		}
	}
}
