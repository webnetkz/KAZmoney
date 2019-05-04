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

        mail($to, $subject, $message, $headers);

        header('Location: https://webnet.kz/');
    }