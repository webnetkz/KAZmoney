<!DOCTYPE html>
<html lang="ru">
    <head>
        <title><?=$title?></title>
            <!--META-->
        <meta charset="UTF-8">
        <meta name="author" content="TOO "WebNet">
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="index, follow">
        <link rel="shortcut icon" href="/public/img/mini_logo.png" type="image/png">
            <!--Индексация для поисковиков-->
        <!--LINKS-->
        <link rel="stylesheet" href="/public/css/style.css">
        <link rel="stylesheet" href="/public/css/scrollbar.css">
        <link rel="stylesheet" href="/public/css/mobile_style.css">
        <!--SCRIPTS-->
        <script type="text/javascript" src="/public/js/jquery.js"></script>
        <script type="text/javascript" src="/public/js/ajax.js"></script>
        <!--STYLES-->
        <style type="text/css">

            .date {
                font-family: serif;
                color: white;
                margin: 5px;
            }

            #hellopreloader>p{
                display: none;
            }


            #preloader_webnet {
                text-align: center;
                margin: 10%;
                color: white;
                font-size: 4em;
                text-shadow: 1px 2px 10px black;
            }

            #hellopreloader_preload {
                display: block;
                position: fixed;
                z-index: 99999;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-size:135px;
                background: rgba(0, 0 , 0, 0.5 ) url(/public/img/preloader.svg) center center no-repeat;
            }

        </style>
            

    </head>
    <body>
	   
    <div id="hellopreloader">
        <div id="hellopreloader_preload">
            <h1 id="preloader_webnet">WEB NET</h1>
        </div>
    </div>
   

        <div id=allItems>
            <form>
                <details>
                    <summary>form</summary>
                    <input type="text" name="">
                    <option>web</option>
                    <option>net</option>
                </details>
            </form>
        </div>
        <meter value="2">d</meter>
        <progress value="33" max="100" style="width: 100%;">

    <details>
        <summary>Hello php</summary>
        <pre><? var_dump($_SERVER);?></pre>
    </details>





        <footer id="footer">
              
        </footer>
    

    <script type="text/javascript">
        var hellopreloader = document.getElementById("hellopreloader_preload");
        function fadeOutnojquery(el){el.style.opacity = 1;
            var interhellopreloader = setInterval(function(){el.style.opacity = el.style.opacity - 0.05;
            if (el.style.opacity <=0.05){ 
                clearInterval(interhellopreloader);
                hellopreloader.style.display = "none";
            }},16);
        }window.onload = function(){setTimeout(function(){fadeOutnojquery(hellopreloader);},1000);};
    </script>
    <script type="text/javascript" src="public/js/jquery.js"></script>
    <script type="text/javascript" src="public/js/date.js"></script>
    </body>
</html>
