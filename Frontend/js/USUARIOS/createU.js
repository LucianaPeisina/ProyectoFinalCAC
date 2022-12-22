
function guardarU() {
 
    let no = document.getElementById("txtNombre").value
    let co = document.getElementById("txtCorreo").value
    let us= document.getElementById("txtUsuario").value
    let pa = document.getElementById("txtPassword").value

    let User = {
        nombre: no,
        correo: co,
        usuario: us,
        password: pa
    }
    let url = "http://lucianahpeisina.pythonanywhere.com/usuarios"
    var options = {
        body: JSON.stringify(User),
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

    