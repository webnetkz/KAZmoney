<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ajax</title>
</head>
<body>
    
    <form name="form">
        <p>
            <input type="text" name="name">
        </p>
        <p>
            <input type="text" name="phone">
        </p>
        <p>
            <input type="submit" name="go">
        </p>
    </form>
    <div id="res"></div>

    <script>
        var servRes = document.querySelector('#res');

        document.forms.form.oninput = function(event) { // Обрабатываем форму в реальном времени
            event.preventDefault(); // Отключение события по умолчанию
        
            //var userInp = document.forms.form.name.value; // Получение значение из инпута
            var xhr = new XMLHttpRequest();

            xhr.open('POST', 'ajaxPHP.php');
            
            var formData = new FormData(document.forms.form);
            
            //xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Заголовок отправки

            xhr.onreadystatechange = function() {
                if(xhr.readyState === 4 && xhr.status === 200) {
                    servRes.textContent = xhr.responseText;
                }
            }
            xhr.send(formData);
            //xhr.send('name=' + userInp); // Отправка определенного значения 

        };
    </script>
</body>
</html>