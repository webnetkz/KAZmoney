<?php

    // Отобразить все данные   
    function debug($element) {
        echo '<pre>';
        var_dump($element);
        die('<hr>');
    }