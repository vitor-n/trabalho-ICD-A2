var card = document.getElementById('buttons-container');
var graph = document.getElementById('graph');

const divs = document.querySelectorAll('.preview-card');

divs.forEach(function (element) {
    element.addEventListener("click", function () {
        // Get the specific action based on the element's attributes or content
        if (element.getAttribute("id") === "graph1") {
            graph.src = "graphs/larissa/graph1.html";

        } else if (element.getAttribute("id") === "graph2") {
            graph.src = "graphs/larissa/graph2.html";

        } else if (element.getAttribute("id") === "graph3") {
            graph.src = "graphs/larissa/graph3.html";

        } else if (element.getAttribute("id") === "graph4") {
            graph.src = "graphs/pedro/graph1.html";

        } else if (element.getAttribute("id") === "graph5") {
            graph.src = "graphs/pedro/graph2.html";

        } else if (element.getAttribute("id") === "graph6") {
            graph.src = "graphs/pedro/graph3.html";

        } else if (element.getAttribute("id") === "graph7") {
            graph.src = "graphs/vitor/graph1.html";

        } else if (element.getAttribute("id") === "graph8") {
            graph.src = "graphs/vitor/graph2.html";
        } else {
            // Perform a default action for other elements
            graph.src = "graphs/vitor/graph3.html";
        }
    });
});