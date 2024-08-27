async function makeRequest(url, method = "GET", data = null) {
    let options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };
    if (data) {
        options.body = JSON.stringify(data);
    }
    let response = await fetch(url, options);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(await response.text());
        console.log(error);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let a = event.target.closest('a');
    let url = a.getAttribute('href');
    try {
        let response = await makeRequest(url, 'POST');
        let span = document.getElementById(a.getAttribute('data-span-count-id'));
        span.innerText = response.count;
        let i = a.querySelector('i');
        span.innerText = `${response.count} отметок "Нравится" `;
        if (response.liked) {
            i.classList.remove('bi-heart');
            i.classList.add('bi-heart-fill');
            i.style.color = 'red';
        } else {
            i.classList.remove('bi-heart-fill');
            i.classList.add('bi-heart');
            i.style.color = '';
        }
    } catch (err) {
        console.error('Error:', err);
    }
}

function onLoad() {
    let links = document.querySelectorAll('a.btn.likes');
    links.forEach(link => {
        link.addEventListener('click', onClick)
    });
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.addEventListener("load", onLoad);