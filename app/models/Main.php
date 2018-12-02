<?php

namespace app\models;

use app\core\Model;
use app\lib\Db;

class Main extends Model {

	public function getNews() {
    	$result = $this->db->row('SELECT * FROM news');
    	return $result;
    }
}