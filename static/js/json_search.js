const searchSnippets = JSON.parse(document.getElementById('snippets').textContent)
console.log(searchSnippets)
const searchForm = document.getElementById('search-form')
const input = document.getElementById('search-input')
const url = 'core/search/'

function getInput() {
    searchForm.addEventListener('submit', event => {
        event.preventDefault()
        const inputValue = input.value
        // console.log('value:', inputValue)
        apiRequest(inputValue)
    })
}

function apiRequest(search_term) {
    fetch('core/search/', {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({search_term: search_term})
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
        displaySnippets('All', data)
    })
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




// function searchResults(inputvalue) {
//     console.log('value in searchResults: ', inputvalue)
//     for (let snippet of searchSnippets) {
//         let snippetTitle = snippet.title
//         console.log(snippetTitle)
//         console.log('value in after loop: ', inputvalue)
//     }
    
//     if (inputValue === snippetTitle) {
//     console.log('value in if statement: ', inputvalue)
//     console.log('search result: ', snippetTitle)
//     }
    
// }




getInput()