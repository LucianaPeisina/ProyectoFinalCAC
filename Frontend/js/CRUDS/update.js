var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}

console.log(args)

document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtTema").value = decodeURIComponent(parts[1][1]);
document.getElementById("txtTitulo").value = decodeURIComponent(parts[2][1]);
document.getElementById("txtResumen").value = decodeURIComponent(parts[3][1]);
document.getElementById("txtDescripción").value = decodeURIComponent(parts[4][1]);
document.getElementById("txtImagen").value = decodeURIComponent(parts[5][1]);



function modificar() {
    let id = document.getElementById("txtId").value
    let te =  document.getElementById("txtTema").value
    let ti = document.getElementById("txtTitulo").value
    let r = document.getElementById("txtResumen").value
    var d = document.getElementById("txtDescripción").value
    let i = document.getElementById("txtImagen").value
     
    d = d.replace(/\n/g, "<br />");

    let noticia = {
        tema: te,
        titulo: ti,
        resumen: r,
        descripción: d,
        imagen: i
        
    }

    let url = "http://lucianahpeisina.pythonanywhere.com/noticias/"+id
    var options = {
        body:  JSON.stringify(noticia),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
