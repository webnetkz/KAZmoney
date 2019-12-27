
self.addEventListener('install', function(e) {
 e.waitUntil(
   caches.open('title').then(function(cache) {
     return cache.addAll([
       '/',
       'service-worker.js',
       'manifest.json',
       'public/images/mini_logo.png',
       'public/images/logo.png',
       'public/styles/allStyle.css',
       'public/styles/desktop/style.css',
       'public/styles/mobile/style.css',
       'public/scripts/main.js'
     ]);
   })
 );
});

 // Кэширование запросов с родительской страници
self.addEventListener('fetch', function(event) {

  //console.log(event.request.url);
  
  event.respondWith(
  
    caches.match(event.request).then(function(response) {
      
      return response || fetch(event.request);
      
    })
  );
});