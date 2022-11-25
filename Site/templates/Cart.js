var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["1", "2", "3", "4", "5"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132',
            data: [50, 40, 25, 30, 15],
        }]
    },

    options: {}
});