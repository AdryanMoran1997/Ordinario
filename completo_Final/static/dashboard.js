document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('myChart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Resuelto',
                data: [],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
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
            myChart.data.datasets[0].data.push(item.resuelto_count);
        });

        myChart.update();
    }

    // Hacer una solicitud a la ruta '/get_data' para obtener datos de la base de datos
    fetch('/get_data')
        .then(response => response.json())
        .then(data => updateChart(data));
});
