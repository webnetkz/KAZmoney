<?php

namespace app\core;

use app\lib\Db;

class Stat {

	protected $visit = [];


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

	}

	public function run_data() {
		
	}

		
	



	

}