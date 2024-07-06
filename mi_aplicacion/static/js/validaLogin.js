function validar(){
    var form = document.form;
    
    if (form.correo.value == 0) {
        alert("El campo correo esta vacio ");
        form.correo.value="";
        form.correo.focus();
        return false;
    }
    if (form.contraseña.value == 0) {
        alert("El campo contraseña esta vacio ");
        form.contraseña.value="";
        form.contraseña.focus();
        return false;
    }
    alert(" Inicio de sesion de forma correcta!!");
    form.submit();
    window.location.href = "index.html";
}