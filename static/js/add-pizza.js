/**
 * Sets an event listener on the submit button to add 
 * a temporary slug to the form
 *  
 */
const submitButton = document.getElementById('submitButton');
const slugField = document.getElementById('id_slug');
const titleField = document.getElementById('id_title');

submitButton.addEventListener("click", (event) => {
    slugField.value = 'temp-slug124578'
})
