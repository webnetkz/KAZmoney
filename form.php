<?php

    if(!empty($_POST['yourphone'])) {

        $phone = trim($_POST['yourphone']);
        $phone = htmlentities($phone);

        $to      = 'dbqqbq@gmail.com';
        $subject = 'Client';
        $message = $phone;
        $headers = 'From: info@webnet.kz' . "\r\n" .
            'Reply-To: info@webnet.kz' . "\r\n" .
            'X-Mailer: PHP/';

        $m = mail($to, $subject, $message, $headers);
        
        if($m) {
            header('Location: https://webnet.kz/');
        }    

        header('Location: https://webnet.kz/');
    }