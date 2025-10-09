/*
 * delete-pizza modal to confirm potential deletion
 */
const deleteButtons = document.getElementsByClassName('btn-delete');
//  modalContent and modalWindow already defined in order-pizza.js

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let message = "Are you sure you want to delete ";
        message += "this delicious Pizza?";
        /* set modal button link */
        modalConfirm.href = e.target.parentElement.href;
        /* remove primary class and add danger class for delete */
        modalConfirm.classList.remove("btn-primary");
        modalConfirm.classList.add("btn-danger");
        /* set modal title, content and button text and show the modal */
        modalConfirm.innerText = "Delete";
        document.getElementsByClassName('modal-title')[0].innerText="Confirm Delete";
        modalContent.innerHTML = message;
        modalWindow.show();
    });
}