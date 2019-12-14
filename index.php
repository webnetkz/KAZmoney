<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <meta name="author" content="WebNet">

    <link rel="icon" href="public/images/mini_logo.png" type="image/png">

    <title>WebNet Разработка сайтов</title>

    <script>
      // Если ширина меньше 700 пикселей подключаем мобильные стили
      var w = screen.width;
      if(w < 700) {
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "public/styles/mstyle.css";
        document.head.appendChild(link);
      } else {
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "public/styles/style.css";
        document.head.appendChild(link);
      }
    </script>

</head>
<body>
    
      <div class="section1 section">123</div>
      <div class="section2 section"></div>
      <div class="section3 section"></div>
      <div class="section4 section"></div>
      <div class="section5 section"></div>
      <div class="section6 section"></div>

    <script>
      // Смена png картинок на gif анимации, после прогрузки всех файлов
      window.onload = function() {
        var imgPng = document.querySelectorAll('.section');
        imgPng[0].setAttribute('style', 'background-image: url("public/images/gifs/1.gif")');
        imgPng[1].setAttribute('style', 'background-image: url("public/images/gifs/2.gif")');
        imgPng[2].setAttribute('style', 'background-image: url("public/images/gifs/3.gif")');
        imgPng[3].setAttribute('style', 'background-image: url("public/images/gifs/4.gif")');
        imgPng[4].setAttribute('style', 'background-image: url("public/images/gifs/5.gif")');
        imgPng[5].setAttribute('style', 'background-image: url("public/images/gifs/6.gif")');
      }
    </script>
</body>
</html>