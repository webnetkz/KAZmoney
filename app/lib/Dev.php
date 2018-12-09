<?php

 // Отображение ошибок
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Комфортное отображение массива
function debug($str) {
    echo '<pre>';
    var_dump($str);
    echo '</pre>';
}
