const searchBtn = document.querySelector("#search-button");
const searchModal = document.querySelector("#search-modal")
const closeSearch = document.querySelector("#close-search");
const cartModal = document.querySelector("#cart-modal");
const cart = document.querySelector("#cart")
const closeCart = document.querySelector("#close-cart")

const closeNav = document.querySelector("#close-nav")
const nav_container = document.querySelector(".nav-links")
const nav_bars = document.querySelector("#nav-bars")



window.addEventListener("resize", (e)=>{
    console.log(e)
    if(window.innerWidth <= 650){
        nav_container.style.transform = "translateX(100%)"
    }else{
        
        nav_container.style.transform = "translateX(0)"
        
    }
})

nav_bars.addEventListener("click", ()=>{
    nav_container.style.transform = "translateX(0)"
})

closeNav.addEventListener("click", ()=>{
    nav_container.style.transform = "translateX(100%)"
})

closeSearch.addEventListener("click", ()=>{
    searchModal.classList.remove("open")
    document.body.classList.remove("modal-open")
})

searchBtn.addEventListener("click", ()=>{
    console.log("hello")
    searchModal.classList.add("open")
    document.body.classList.add("modal-open")
})

cart.addEventListener("click", ()=>{
    cartModal.classList.add("open")
    document.body.classList.add("modal-open")
})

closeCart.addEventListener("click", ()=>{
    cartModal.classList.remove("open")
    document.body.classList.remove("modal-open")
})
