function validar() {
    var form = document.forms["form"];

    if (form.nombre.value.trim() === "") {
        alert("El campo nombre está vacío");
        form.nombre.value = "";
        form.nombre.focus();
        return false;
    }
    if (form.apellido.value.trim() === "") {
        alert("El campo apellido está vacío");
        form.apellido.value = "";
        form.apellido.focus();
        return false;
    }
    if (form.correo.value.trim() === "") {
        alert("El campo correo está vacío");
        form.correo.value = "";
        form.correo.focus();
        return false;
    }
    if (form.contrasena.value.trim() === "") {
        alert("El campo contraseña está vacío");
        form.contrasena.value = "";
        form.contrasena.focus();
        return false;
    }
    if (form.confirmarContrasena.value.trim() === "") {
        alert("El campo confirmar contraseña está vacío");
        form.confirmarContrasena.value = "";
        form.confirmarContrasena.focus();
        return false;
    }
    if (form.confirmarContrasena.value !== form.contrasena.value) {
        alert("La contraseña no coincide");
        form.confirmarContrasena.value = "";
        form.confirmarContrasena.focus();
        return false;
    }

    alert("¡Registro exitoso!");
  
    return true;
}
