importScripts('/public/js/cache-polyfill.js');


self.addEventListener('install', function(e) {
 e.waitUntil(
   caches.open('title').then(function(cache) {
     return cache.addAll([
       '/index.html',
       '/public/audio/click.mp3',
       '/public/css/style.css',
       '/public/js/main.js',
       '/public/img/icons/reset.png',
       '/public/img/icons/settings.png',
     ]);
   })
 );
});

 // Кэширование запросов с родительской страници
self.addEventListener('fetch', function(event) {

  console.log(event.request.url);

  event.respondWith(

    caches.match(event.request).then(function(response) {

      return response || fetch(event.request);

    })
  );
});
