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

    const data = await response.json();
    return data;
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
    postFormData(shortDescription, details).then((data) => addIdea(data, shortDescription, details));
    document.getElementById("add-idea-form").reset();
    toggleAddIdea();
});

function addIdea(id, shortDescription, details) {
    var ideasPanel = document.getElementById("ideas-panel");
    var newIdea = document.createElement("div");
    newIdea.onclick = function() {
        location.href = `/ideas/${id}`;
    }
    newIdea.className = "idea";
    var link = document.createElement('a');
    link.id = "idea-link"
    link.href = `/ideas/${id}`
    var strongElement = document.createElement("strong");
    strongElement.textContent = shortDescription;
    var detailsDiv = document.createElement('div');
    detailsDiv.className = "idea-description";
    detailsDiv.textContent = details;
    link.appendChild(strongElement);
    newIdea.appendChild(link);
    newIdea.appendChild(detailsDiv);
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