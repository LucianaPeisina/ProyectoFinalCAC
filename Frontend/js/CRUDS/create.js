
function guardar() {
 
    let te = document.getElementById("txtTema").value
    let ti = document.getElementById("txtTitulo").value
    let d = document.getElementById("txtDescripción").value
    let i = document.getElementById("txtImagen").value

    let noticia = {
        tema: te,
        titulo: ti,
        descripción: d,
        imagen: i
    }
    let url = "http://lucianahpeisina.pythonanywhere.com/noticias"
    var options = {
        body: JSON.stringify(noticia),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
    }