function makeResponse(link) {
    sendResponse("/makeResponse", link).then(() => undefined);
    setTimeout(() => { location.reload(); }, 300);
}


function deleteResponse() {
    sendResponse("/deleteResponse").then(() => undefined);
    setTimeout(() => { location.reload(); }, 300);
}


function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}


async function sendResponse(command, link=undefined) {
    const response = await fetch(window.location.href + command, {
        method: "POST",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            "sessionId": getCookie("sessionid"),
            "link": link
        })
    });
}


document.getElementById("make-response-form").addEventListener("submit", function(e) {
    e.preventDefault();
    let link = document.getElementById("link-field").value;
    makeResponse(link);
});