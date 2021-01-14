new ClipboardJS('.btn')

const searchIcon = document.getElementById('search-icon')
const searchBar = document.getElementById('search-bar')
const searchButton = document.getElementById('search-button')
const snippets = JSON.parse(document.getElementById('snippets').textContent)


searchIcon.addEventListener('click', event => {
    console.log('button has been clicked')
    searchBar.style.display = 'flex'
})

searchButton.addEventListener('click', event => {
    console.log("search button clicked")
    searchBar.style.display = 'none'
})

// markup for index.html main container for all snippets list
const mainContainer = document.getElementById('main-container')

function displaySnippets(selectedCategory) {
    const existingSnippets = document.querySelectorAll('.main-snippet-list-container')
    
    for (let snippet of existingSnippets) {
        snippet.remove()
    }

    for (let snippet of snippets) {
        // console.log(snippet.category)
        
        if (snippet.category !== selectedCategory && selectedCategory !== 'All') {
            // console.log(`category length=${snippet.category.length} : selected len = ${selectedCategory.length}`)
            continue
        }

        const mainSnippetListContainer = document.createElement('div')
        mainSnippetListContainer.classList.add("main-snippet-list-container")
        mainContainer.append(mainSnippetListContainer)
        
        // snippet.title
        const snippetTitle = document.createElement('div')
        snippetTitle.classList.add("snippet-title")
        mainSnippetListContainer.append(snippetTitle)
    
        const snippetTitleFont = document.createElement('a')
        snippetTitleFont.classList.add("snippet-title-font")
        snippetTitleFont.href = `core/details/${snippet.id}/`
        snippetTitleFont.innerText = snippet.title
        snippetTitle.append(snippetTitleFont)
    
        // snippet.created_on
        const snippetDate = document.createElement('div')
        snippetDate.classList.add("snippet-extras")
        snippetDate.classList.add("snippet-date")
        mainSnippetListContainer.append(snippetDate)
    
        const createdOnTitle = document.createElement('p')
        createdOnTitle.innerText = "Last Update"
        snippetDate.append(createdOnTitle)
    
        const createdOnDate = document.createElement('p')
        createdOnDate.innerText = dateStamp()
        snippetDate.append(createdOnDate)
    
        // snippet.user (for author)
        const snippetUser = document.createElement('div')
        snippetUser.classList.add("snippet-extras")
        snippetUser.classList.add("snippet-author")
        mainSnippetListContainer.append(snippetUser)
    
        const userTitle = document.createElement('p')
        userTitle.innerText = "Author"
        snippetUser.append(userTitle)
    
        const userName = document.createElement('p')
        userName.innerText = snippet.username
        snippetUser.append(userName)
    
        // snippet.category (for language)
        const category = document.createElement('div')
        category.classList.add("snippet-extras")
        category.classList.add("snippet-category")
        mainSnippetListContainer.append(category)
    
        const categoryTitle = document.createElement('p')
        categoryTitle.innerText = "Category"
        category.append(categoryTitle)
    
        const categoryName = document.createElement('p')
        categoryName.innerText = snippet.category
        category.append(categoryName)
    } 
    // end markup for main list container
}


// event listener for category filter tags
const filters = document.querySelectorAll('.filter-buttons')

for (let filter of filters) {
    filter.addEventListener('click', event => {
        let selectedCategory = event.target.innerText
        // console.log("button clicked", selectedCategory)

        displaySnippets(selectedCategory)
    })
}

displaySnippets('All')