// Подключение необходимых стилей
var w = screen.width;
if(w < 700) {
  var link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "public/styles/mobile/style.css";
  document.head.appendChild(link);
} else {
  var link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "public/styles/desktop/style.css";
  document.head.appendChild(link);
}

// Регистрация сервисного работника
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('service-worker.js')
        .then((reg) => {
          //console.log('Сервисный работник зарегистрирован.', reg);
        });
  });
}