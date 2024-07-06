document.addEventListener('DOMContentLoaded', function() {
    // Incrementar cantidad
    document.querySelectorAll('.increase-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var id = this.getAttribute('data-id');
            var quantityInput = document.getElementById('quantity' + id);
            var currentQuantity = parseInt(quantityInput.value);
            quantityInput.value = currentQuantity + 1;
        });
    });

    // Decrementar cantidad
    document.querySelectorAll('.decrease-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            var id = this.getAttribute('data-id');
            var quantityInput = document.getElementById('quantity' + id);
            var currentQuantity = parseInt(quantityInput.value);
            if (currentQuantity > 1) {
                quantityInput.value = currentQuantity - 1;
            }
        });
    });

    // Agregar al carrito
    document.querySelectorAll('.add-to-cart').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var id = this.getAttribute('data-id');
            var quantity = parseInt(document.getElementById('quantity' + id).value);
            var url = this.getAttribute('href');
            $.ajax({
                url: url,
                method: 'GET',
                success: function(data) {
                    if (data.success) {
                        alert('Se agregaron ' + quantity + ' productos al carrito.');
                        // Aquí puedes agregar lógica para actualizar el carrito en el modal
                    }
                },
                error: function() {
                    alert('Error al agregar el producto al carrito.');
                }
            });
        });
    });
});
