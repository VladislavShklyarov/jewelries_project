document.getElementById("calculation-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Отменяем отправку формы

    var diameter = parseFloat(document.getElementById("diameter").value);
    var width = parseFloat(document.getElementById("width").value);

    var resultDiv = document.getElementById("result");

    if (diameter >= Math.sqrt(2) * width) {
        resultDiv.innerHTML = "Из заготовки диаметром " + diameter + " мм " +"можно выпилить квадратный камень с шириной стороны " + width + " мм.";
    } else {
        resultDiv.innerHTML = "Из камня диаметром " + diameter + " мм " +"нельзя выпилить квадратный камень с шириной стороны " + width + " мм.";
    }
});