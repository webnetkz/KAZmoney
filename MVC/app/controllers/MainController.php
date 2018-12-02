<?php

namespace app\controllers;

use app\core\Controller;

class MainController extends Controller {

	public function indexAction() {
		$this->view->render('Home');
	}

	public function contactAction() {
		$this->view->render('Contacts');
	}
}
