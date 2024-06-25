const list = document.querySelector(".product-category-links");
const category_btn = document.querySelector("#categories-button")
const categories_modal = document.querySelector(".filters")
const close_categories_modal = document.querySelector("#close-category-modal")

category_btn.addEventListener("click", ()=>{
    categories_modal.style.transform = "translateX(0)";
})

close_categories_modal.addEventListener("click", ()=>{
    categories_modal.style.transform = "translateX(100%)"
})

