function consultarPersona() {
    const idPersona = document.getElementById('id').value;

    fetch(`/cgi-bin/consultar.py?id=${idPersona}`)
        .then(response => response.json())
        .then(data => {
            if (data) {
                document.getElementById('nombre').textContent = `Nombre: ${data.nombre}`;
                document.getElementById('correo').textContent = `Correo: ${data.correo}`;
                document.getElementById('edad').textContent = `Edad: ${data.edad}`;
                document.getElementById('imagen').src = `data:image/jpeg;base64,${data.imagen}`;
            } else {
                alert("Persona no encontrada");
            }
        })
        .catch(error => console.error('Error al consultar persona:', error));
}
