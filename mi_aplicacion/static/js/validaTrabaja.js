function validar(){
    var form = document.form;
    
    if (form.nombre.value == 0) {
        alert("El campo nombre esta vacio ");
        form.nombre.value="";
        form.nombre.focus();
        return false;
    }
    if (form.apellido.value == 0) {
        alert("El campo apellido esta vacio ");
        form.apellido.value="";
        form.apellido.focus();
        return false;
    }
    if (form.correo.value == 0) {
        alert("El campo correo esta vacio ");
        form.correo.value="";
        form.correo.focus();
        return false;
    }
    if (form.rut.value == 0) {
        alert("El campo rut esta vacio ");
        form.rut.value="";
        form.rut.focus();
        return false;
    }
    if (form.edad.value == 0) {
        alert("El campo edad esta vacio ");
        form.edad.value="";
        form.edad.focus();
        return false;
    }if (form.edad.value < 18 ) {
        alert("No cumple con la edad minima (18 años)!!");
        form.edad.value="";
        form.edad.focus();
        return false;
    }if (form.edad.value > 64) {
        alert("Ley 20.000: Excede el maximo de años (65 años)!!");
        form.edad.value="";
        form.edad.focus();
        return false;
    }
    alert(" Datos enviados con exito!!");
    form.submit();
    window.location.href = "index.html";
}