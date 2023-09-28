<?php

require_once '../app/db.php';

if(isset($_GET['code']) && !empty($_GET['code'])) {
    echo $_GET['code'];
}