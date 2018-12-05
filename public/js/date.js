// Script Date
var MyDate = new Date();
var year = MyDate.getFullYear();
var a = document.createElement('a');

	a.className = "date";
	a.innerHTML = 'WebNet ® '+ year;
	a.setAttribute("href", "https://webnet.kz");
	a.setAttribute("style", "text-decoration: none; text-shadow: -1px -1px 2px white;");

footer.appendChild(a);

        
    