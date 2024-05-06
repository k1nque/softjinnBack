async function getAllIdeas() {
    const ideas = await fetch("/getAllIdeas")
        .then(
                (response) => response.json()
            );
    return ideas;
}

getAllIdeas().then((ideas) => {
    ideas.forEach((idea) => {
        addIdea(idea["id"], idea["shortDescription"], idea["details"]);
    });
});

async function postFormData(shortDescription, details) {
    const response = await fetch("/createNewIdea", {
        method: "POST",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "shortDescription":shortDescription,
            "details": details
        })
    });
}

function toggleAddIdea() {
    var overlay = document.getElementById("overlay");
    var addIdeaPopup = document.getElementById("add-idea-popup");

    overlay.style.display = overlay.style.display === "none" ? "block" : "none";
    addIdeaPopup.style.display = addIdeaPopup.style.display === "none" ? "block" : "none";
}

function toggleDetails() {
    var overlay = document.getElementById("overlay-details");
    var detailsPopup = document.getElementById("details-popup");

    overlay.style.display = overlay.style.display === "none" ? "block" : "none";
    detailsPopup.style.display = detailsPopup.style.display === "none" ? "block" : "none";
}

document.getElementById("add-idea-form").addEventListener("submit", function(e) {
    e.preventDefault();
    let shortDescription = document.getElementById("short-description").value;
    let details = document.getElementById("details").value;
    postFormData(shortDescription, details).then(() => undefined);
    addIdea(undefined, shortDescription, details);
    document.getElementById("add-idea-form").reset();
    toggleAddIdea();
});

function addIdea(id, shortDescription, details) {
    var ideasPanel = document.getElementById("ideas-panel");
    var newIdea = document.createElement("div");
    newIdea.className = "idea";
    var link = document.createElement('a');
    link.href = `/ideas/${id}`
    var strongElement = document.createElement("strong");
    strongElement.textContent = shortDescription;
    var brElement = document.createElement("br");
    var detailsText = document.createTextNode(details);
    var viewDetailsButton = document.createElement("button");
    viewDetailsButton.className = "view-details-button";
    viewDetailsButton.textContent = "Показать детали";
    viewDetailsButton.onclick = function() {
        showDetails(details);
    };
    link.appendChild(strongElement);
    newIdea.appendChild(link);
    newIdea.appendChild(brElement);
    newIdea.appendChild(detailsText);
    newIdea.appendChild(viewDetailsButton);
    ideasPanel.appendChild(newIdea);
}

function showDetails(details) {
    var detailsPopup = document.getElementById("details-popup");
    var detailsTextElement = document.getElementById("details-text");
    detailsTextElement.textContent = details;
    var executorsList = document.getElementById("executors-list");
    executorsList.innerHTML = "";
    toggleDetails();
}

document.getElementById("add-executor-form").addEventListener("submit", function(e) {
    e.preventDefault();
    let newExecutor = document.getElementById("new-executor").value;
    addExecutor(newExecutor);
    document.getElementById("add-executor-form").reset();
});

function addExecutor(newExecutor) {
    var executorsList = document.getElementById("executors-list");
    var newExecutorElement = document.createElement("li");
    newExecutorElement.textContent = newExecutor;
    executorsList.appendChild(newExecutorElement);
    localStorage.setItem("executors", executorsList.innerHTML);
}

window.onload = function() {
    var executorsList = document.getElementById("executors-list");
    var storedExecutors = localStorage.getItem("executors");
    if (storedExecutors) {
        executorsList.innerHTML = storedExecutors;
    }
};