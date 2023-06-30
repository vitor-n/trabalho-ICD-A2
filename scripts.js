var card = document.getElementById('buttons-container');
var graph = document.getElementById('graph');
var text1 = document.getElementById('text-graph1');
var text2 = document.getElementById('text-graph2');
var text3 = document.getElementById('text-graph3');
var text4 = document.getElementById('text-graph4');
var text5 = document.getElementById('text-graph5');
var text6 = document.getElementById('text-graph6');
var text7 = document.getElementById('text-graph7');
var text8 = document.getElementById('text-graph8');
var text9 = document.getElementById('text-graph9');
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
        [].forEach.call(document.querySelectorAll('.text-container'), function (el) {
            el.style.display = 'none';
        });
        
        graph.style.height = "750px";

        // Get the specific action based on the element's attributes or content
        if (element.getAttribute("id") === "graph1") {
            window.scrollTo({top: 1, behavior: 'smooth'});
            graph.src = "graphs/larissa/graph1.html";
            graph.style.width = "1200px";
            text1.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph2") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/larissa/graph2.html";
            graph.style.width = "1200px";
            text2.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph3") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/larissa/graph3.html";
            graph.style.width = "1200px";
            text3.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph4") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/pedro/graph1.html";
            graph.style.width = "1200px";
            text4.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph5") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/pedro/graph2.html";
            graph.style.width = "1200px";
            text5.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph6") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/pedro/graph3.html";
            graph.style.width = "1200px";
            text6.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph7") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/vitor/graph1.html";
            graph.style.width = "750px";
            text7.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph8") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/vitor/graph2.html";
            graph.style.width = "1200px";
            text8.style.display = "initial";
            

        } else if (element.getAttribute("id") === "graph9") {
            window.scrollTo({top: 0, behavior: 'smooth'});
            graph.src = "graphs/vitor/graph3.html";
            graph.style.width = "1200px";
            text9.style.display = "initial";
            
        }
    });
});

