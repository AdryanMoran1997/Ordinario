document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('myChart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Pendiente',
                data: [],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    function updateChart(data) {
        myChart.data.labels = [];
        myChart.data.datasets[0].data = [];

        data.forEach(function (item) {
            myChart.data.labels.push(item.municipio);
            myChart.data.datasets[0].data.push(item.pendiente_count);
        });

        myChart.update();
    }

    // Hacer una solicitud inicial a la ruta '/get_data_pendiente' para obtener datos de la base de datos
    fetch('/get_data_pendiente')
        .then(response => response.json())
        .then(data => updateChart(data));
    
    // Función para volver al dashboard principal
    window.volverDashboard = function () {
        window.location.href = '/';  // Redireccionar al dashboard principal
    };
});
