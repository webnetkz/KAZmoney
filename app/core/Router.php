<?php

namespace app\core;

use app\core\View;


class Router {
	
	protected $routes = [];
	protected $params = [];
	public $visit = [];
	
	public function __construct() {

		$ip = $_SERVER['REMOTE_ADDR'];
		$this->visit['ip'] = $ip;

		$agent = $_SERVER['HTTP_USER_AGENT'];
		$this->visit['agent'] = $agent;
		
		$date = date('d.m.y');
		$this->visit['date'] = $date;

		$time = date('h:m');
		$this->visit['time'] = $time;

		if(!isset($_SERVER['HTTP_REFERER'])) {
			$refer = 'no';
		} else {
			$refer = $_SERVER['HTTP_REFERER'];
		}
		$this->visit['refer'] = $refer;

		$request = $_SERVER['REQUEST_URI'];
		$this->visit['request'] = $request;

		
		
		$arr = require 'app/config/routes.php';
		
		foreach ($arr as $key => $val) {
			$this->add($key, $val);
		}
	}

	public function add($route, $params) {

		$route = '#^'.$route.'$#'; 
		$this->routes[$route] = $params;
	}
	
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
