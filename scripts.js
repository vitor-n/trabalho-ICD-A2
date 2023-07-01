// Get references to the HTML elements
var graphFrame = document.getElementById('graph-iframe');
var backButton = document.getElementById("back");
var nextButton = document.getElementById("next");
var number = document.getElementById("number");

// Define the graph data
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

// Get references to preview card elements
const divs = document.querySelectorAll('.preview-card');

// Initialize the graph number
var graphNumber = 0;

// Attach click event listeners to preview cards
divs.forEach(function (element) {
    element.addEventListener("click", function () {
        // Get the ID of the clicked element
        var id = element.getAttribute("id");

        // Update the content based on the clicked element
        get_content(id);

        // Update the graph number
        graphNumber = graphs[id].graphId;
    });
});

// Function to update the content based on the selected graph
function get_content(id) {
    // Hide every text container
    document.querySelectorAll('.text-container').forEach(function (el) {
        el.style.display = 'none';
    });

    // Scroll to the top of the page
    window.scrollTo({ top: 1, behavior: 'smooth' });

    // Check if the graph ID exists in the graphs object
    if (graphs.hasOwnProperty(id)) {
        var selectedElement = graphs[id];

        // Update the graph iframe properties
        graphFrame.src = selectedElement.src;
        graphFrame.style.width = selectedElement.width;
        graphFrame.style.height = selectedElement.height;

        // Show the corresponding text container
        selectedElement.text.style.display = "initial";

        // Enable/disable the back button based on the current graph
        if (id !== "graph0") {
            backButton.disabled = false;
        }
    }
}

// Function to initialize the page
function ready() {
    backButton.disabled = true;
}

// Function to navigate back to the home graph
function home() {
    graphNumber = 0;
    backButton.disabled = true;

    get_content("graph" + graphNumber);
}

// Function to navigate to the next graph
function next() {
    graphNumber++;
    if (graphNumber === 9) {
        nextButton.disabled = true;
    }
    backButton.disabled = false;

    get_content("graph" + graphNumber);
}

// Function to navigate back to the previous graph
function back() {
    graphNumber--;
    if (graphNumber === 0) {
        backButton.disabled = true;
        graphFrame.style.height = "0";
    }
    nextButton.disabled = false;

    get_content("graph" + graphNumber);
}
