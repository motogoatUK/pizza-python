/*
 * order-pizza confirmation modal to send order to backend 
 */
const orderButtons = document.getElementsByClassName('btn-order');
const modalContent = document.getElementById("modal-content");
const modalWindow = new bootstrap.Modal(document.getElementById('modalWindow'));
const modalConfirm = document.getElementById("modalConfirm");

for (let button of orderButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let slugField = e.target.getAttribute("data-slug-field");
        /* set modal button link */
        modalConfirm.href = `/order-pizza/${slugField}`;
        /* remove danger class and add primary class for order */
        modalConfirm.classList.remove("btn-danger");
        modalConfirm.classList.add("btn-primary");
        /* set modal title, content and button text */
        document.getElementsByClassName('modal-title')[0].innerText="Order Confirmation";
        modalConfirm.innerText = "Confirm Order";
        /* use the HTML direct from the page in the modal */
        let orderDetails = document.getElementById(slugField).innerHTML;
        orderDetails += "<p>Confirm order for collection";
        orderDetails += "<br>*Please allow 15 minutes before collecting</p>";
        modalContent.innerHTML = orderDetails;
        modalWindow.show();
    });
}
