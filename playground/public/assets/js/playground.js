function init() {
    document.querySelectorAll("form.imageGenerator").forEach(form => {
        form.onsubmit = (e) => {
            e.preventDefault();

            let results = form.parentNode.getElementsByClassName("results")[0]
            let progressbar = document.createElement("div")
            progressbar.className = "progress"
            progressbar.innerHTML =  `<div class="indeterminate"></div>`
            results.appendChild(progressbar)

            fetch(form.target, {
                method: form.method,
                body: new FormData(form),
                redirect: "follow",
                mode: "no-cors"
            })
            .then(data => { 
                if (data.status === 200) {
                    console.log(data.status)
                    return data.text() 
                }
                else {
                    let warning = document.createElement("p");
                    warning.className = "card-panel red lighten-2";
                    data.text().then( txt => {
                        warning.innerText = txt;
                    })
                    results.innerHTML = ""  
                    results.appendChild(warning)
                }
            })
            .then(resp => {        
                if (resp) {
                    let image = document.createElement("img");
                    image.src = resp;
                    results.innerHTML = ""
                    results.appendChild(image)
                }
            })
        }
    })

    document.querySelectorAll("form.calculator").forEach(form => {
        form.onsubmit = (e) => {
            e.preventDefault();

            let results = form.parentNode.getElementsByClassName("results")[0]
            let progressbar = document.createElement("div")
            progressbar.className = "progress"
            progressbar.innerHTML =  `<div class="indeterminate"></div>`
            results.appendChild(progressbar)

            fetch(form.target, {
                method: form.method,
                body: new FormData(form),
                redirect: "follow",
                mode: "no-cors"
            })
            .then(data => { 
                if (data.status === 200) {
                    console.log(data.status)
                    return data.json() 
                }
                else {
                    let warning = document.createElement("p");
                    warning.className = "card-panel red lighten-2";
                    data.text().then( txt => {
                        warning.innerText = txt;
                    })
                    results.innerHTML = ""  
                    results.appendChild(warning)
                }
            })
            .then(resp => {        
                if (resp) {
                    results.innerHTML = `
                    <div class="row">
                        <div class="col l6 m6 s12">
                            <strong>Deine Nummer</strong>
                            <p>${resp.number}</p>
                        </div>
                        <div class="col l6 m6 s12">
                            <strong>Anzahl der Schritte</strong>
                            <p>${resp.steps}</p>
                        </div>
                        <div class="col l12 m12 s12">
                            <strong>Die Schritte</strong>
                            <p>${resp.numbers.join(" => ")}</p>
                        </div>
                    </div>
                    `
                }
            })
        }
    })
}

document.addEventListener("DOMContentLoaded", e => { init() })