<?php

namespace app\core;

class Stat {

	public $visit = [];


	public function __construct() {

		$ip = $_SERVER['ROMOTE_ADDR'];
		$this->visit[$ip];
		debug($ip);
	}

}