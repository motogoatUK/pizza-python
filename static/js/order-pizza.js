/*
 * order-pizza script to send order to backend 
 */
const orderButtons = document.getElementsByClassName('btn-order');
const modalContent = document.getElementById("modal-content");
const modalWindow = new bootstrap.Modal(document.getElementById('modalWindow'));

for (let button of orderButtons) {
    button.addEventListener("click", (e) => {
        let slugField = e.target.getAttribute("data-slug-field");
        modalConfirm.href = `/order-pizza/${slugField}`;
        let orderDetails = document.getElementById(slugField).innerHTML;
        modalContent.innerHTML = orderDetails;
        modalWindow.show();
    });
}
