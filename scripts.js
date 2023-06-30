var graphFrame = document.getElementById('graph-iframe');
backButton = document.getElementById("back");
nextButton = document.getElementById("next");
number = document.getElementById("number");

const graphs = {
    graph0: {
        src: "",
        width: "0px",
        height: "0px",
        text: document.getElementById('text-home'),
        graphId: 0
    },
    graph1: {
        src: "graphs/larissa/graph1.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph1'),
        graphId: 1
    },
    graph2: {
        src: "graphs/larissa/graph2.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph2'),
        graphId: 2
    },
    graph3: {
        src: "graphs/larissa/graph3.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph3'),
        graphId: 3
    },
    graph4: {
        src: "graphs/pedro/graph1.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph4'),
        graphId: 4
    },
    graph5: {
        src: "graphs/pedro/graph2.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph5'),
        graphId: 5
    },
    graph6: {
        src: "graphs/pedro/graph3.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph6'),
        graphId: 6
    },
    graph7: {
        src: "graphs/vitor/graph1.html",
        width: "750px",
        height: "750px",
        text: document.getElementById('text-graph7'),
        graphId: 7
    },
    graph8: {
        src: "graphs/vitor/graph2.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph8'),
        graphId: 8
    },
    graph9: {
        src: "graphs/vitor/graph3.html",
        width: "1200px",
        height: "750px",
        text: document.getElementById('text-graph9'),
        graphId: 9
    }
};

const divs = document.querySelectorAll('.preview-card');
var graphNumber = 0;

divs.forEach(function (element) {
    element.addEventListener("click", function () {

        // Get the specific action based on the element's attributes or content
        var id = element.getAttribute("id");

        get_content(id);

        graphNumber = graphs[id].graphId

    });
});

function get_content(id) {
    // Hides every text container
    document.querySelectorAll('.text-container').forEach(function (el) {
        el.style.display = 'none';
    });
    window.scrollTo({ top: 1, behavior: 'smooth' });
    
    if (graphs.hasOwnProperty(id)) {
        var selectedElement = graphs[id];
        graphFrame.src = selectedElement.src;
        graphFrame.style.width = selectedElement.width;
        graphFrame.style.height = selectedElement.height;
        selectedElement.text.style.display = "initial";

        if (id != "graph0") {
            backButton.disabled = false;
        }
    }
}

function ready() {
    backButton.disabled = true;
}

function home() {
    graphNumber = 0;

    backButton.disabled = true;

    get_content("graph" + graphNumber)
}

function next() {
    graphNumber++;
    if (graphNumber == 9) {
        nextButton.disabled = true;
    }
    backButton.disabled = false;

    get_content("graph" + graphNumber)
}

function back() {
    graphNumber--;
    if (graphNumber == 0) {
        backButton.disabled = true;
        graphFrame.style.height = "0";
    }
    nextButton.disabled = false;

    get_content("graph" + graphNumber)

}