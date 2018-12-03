// Script Date
var MyDate = new Date();
var year = MyDate.getFullYear();
var a = document.createElement('a');

	a.className = "date";
	a.innerHTML = 'Qazaq Life® '+ year;
	a.setAttribute("href", "http://qazaqlife");
	a.setAttribute("style", "text-decoration: none;");

footer.appendChild(a);

        
    