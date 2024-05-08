function makeResponse() {
    const sessionCookie = getCookie("sessionid");
    const csrftoken = getCookie("csrftoken");
    console.log(sessionCookie);
    sendResponse(sessionCookie, csrftoken).then(() => undefined);
    setTimeout(() => {  location.reload(); }, 1000);
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

async function sendResponse(sessionId, csrfToken) {
    const response = await fetch(window.location.href + "/makeResponse", {
        method: "POST",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({
            "sessionId": sessionId
        })
    });
}