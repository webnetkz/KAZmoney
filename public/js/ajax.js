$(document).ready(function() {

	$('form').submit(function(event) {

		event.preventDefault(); // Функция отмены отправки в браузере. 
	
		$.ajax({

			type: $(this).attr('method'),
			url: $(this).attr('action'), // URL-адрес, по которому будет отправлен запрос.
			data: new FormData(this), // Данные, которые будут отправлены на сервер. 
			contentType: false, // Ожидаемый тип данных, которые пришлет сервер в ответ на запрос.
			cache: false,
			processData: false,

			success: function(result){
				$(".form").append('<div style="background:red;">'+result+'</div>');
			},
			

		});

	});

});