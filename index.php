<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <meta name="author" content="WebNet">

    <link rel="icon" href="public/img/mini_logo.png" type="image/png">

    <title>WebNet Разработка сайтов</title>

    <script>
      // Если ширина меньше 700 пикселей подключаем мобильные стили
      var w = screen.width;
      if(w < 700) {
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "public/css/mstyle.css";
        document.head.appendChild(link);
      } else {
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "public/css/style.css";
        document.head.appendChild(link);
      }
    </script>

</head>
<body>
  

    <script>
      // Смена png картинок на gif анимации, после прогрузки всех файлов
      window.onload = function() {

      }
    </script>
</body>
</html>