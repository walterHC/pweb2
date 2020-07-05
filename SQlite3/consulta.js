function consultaSQlite() {
	
	//variables del html
	var baseDatos = document.getElementById('nameBD').value;
    	var consulta = document.getElementById('consulta').value;
	var sugerencia = "no hay sugerencias disponibles";


	var  xmlhttp, myObj, x, resultado = "",sugerencia= "";

	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
  		if (this.readyState == 4 && this.status == 200) {
    			myObj = JSON.parse(this.responseText);

	    		if(consulta.length <= 3){
		     		for(i = 0;i < myObj.length; i++){
                                	for(j = 0; j < myObj[i].length; j++){
                                        	sugerencia += myObj[i][j]+",";
                                	}
                        	}
	
	       			document.getElementById('sugerencia').innerHTML = sugerencia ; 
	    		}
	    
	    		else{
	    
				for(i = 0;i < myObj.length; i++){
					for(j = 0; j < myObj[i].length; j++){
						resultado += myObj[i][j]+" | ";
					}
					resultado +="<br />";
				}
		      		document.getElementById('resultado').innerHTML = resultado ;
	   		}
		}
	};
	xmlhttp.open("GET", "./cgi-bin/consulta.py?nameDB="+ baseDatos+" &consulta="+ consulta , true);
	xmlhttp.send();
}

function placeholderDB(param){
	switch(param){
		case 'A':
		      document.getElementById('consulta').placeholder = "consultar [Name]";
			break;
		case 'M':
		      document.getElementById('consulta').placeholder = "consultar [Title]";
			break;
	}
}
