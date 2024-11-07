$('#ul-buy-tickets-btn').click(function () {
    open('pageConnexion.html') //Le bouton mène de index.html a pageConnexion.html
});

$(document).ready(function () {
    const api = '/api/';

    $.ajax({
        url: api + 'items',
        type: 'GET',
        success: function (data) {
            console.log(data);
        },
    });
});
