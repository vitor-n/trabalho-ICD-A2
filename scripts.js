var card = document.getElementById('buttons-container');
var graph = document.getElementById('graph');
var title = document.getElementById("title");
var text = document.getElementById("text");

const divs = document.querySelectorAll('.preview-card');

divs.forEach(function (element) {
    element.addEventListener("mouseover", function () {
        // Change the mouse cursor to pointer
        element.style.cursor = "pointer";
    });

    element.addEventListener("mouseout", function () {
        // Reset the mouse cursor
        element.style.cursor = "auto";
    });
    
    element.addEventListener("click", function () {
        // Get the specific action based on the element's attributes or content
        if (element.getAttribute("id") === "graph1") {
            graph.src = "graphs/larissa/graph1.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph2") {
            graph.src = "graphs/larissa/graph2.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph3") {
            graph.src = "graphs/larissa/graph3.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph4") {
            graph.src = "graphs/pedro/graph1.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph5") {
            graph.src = "graphs/pedro/graph2.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph6") {
            graph.src = "graphs/pedro/graph3.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph7") {
            graph.src = "graphs/vitor/graph1.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph8") {
            graph.src = "graphs/vitor/graph2.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();

        } else if (element.getAttribute("id") === "graph9") {
            graph.src = "graphs/vitor/graph3.html";
            window.scrollTo(0, 0);
            adjustGraphHeight();
        }
    });
});

function adjustGraphHeight() {
    graph.style.height = graph.contentWindow.document.body.scrollHeight + 'px';
    graph.style.width = graph.contentWindow.document.body.scrollWidth + 'px';
}
