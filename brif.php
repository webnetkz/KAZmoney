<?php

    if(!empty($_POST['af_action'])) {
        
        $item = trim($_POST['color']);
        $item = htmlentities($item);

        $task = trim($_POST['contact_task']);
        $task = htmlentities($task);

        $name = trim($_POST['contact_name']);
        $name = htmlentities($name);

        $email = trim($_POST['contact_email']);
        $email = htmlentities($email);

        $phone = trim($_POST['contact_phone']);
        $phone = htmlentities($phone);

        $company = trim($_POST['contact_company']);
        $company = htmlentities($company);

        $to      = 'info@webnet.kz';
        $subject = 'Client';
        $message = $item . '---' . $task . '---' . $name . '---' . $email . '---' . $phone . '---' . $company;
        $headers = 'From: info@webnet.kz' . "\r\n" .
            'Reply-To: info@webnet.kz' . "\r\n";

        $m = mail($to, $subject, $message, $headers);

        if($m) {
            header('Location: https://webnet.kz/');
        }

        header('Location: https://webnet.kz');
    }