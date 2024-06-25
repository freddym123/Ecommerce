var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2,
    spaceBetween: 30,
    breakpoints: {
        400: {
            slidesPerView: 3
        },
        500: {
            slidesPerView: 4
        },
        700: {
            slidesPerView: 5
        },
        800: {
            slidesPerView: 6
        },
        1000: {
            slidesPerView: 7
        }
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
})

const carousel_content = document.querySelectorAll(".carousel-content")
const carousel_prev_btn = document.querySelector(".carousel-control-prev")
const carousel_next_btn = document.querySelector(".carousel-control-next")

window.addEventListener("resize", (e)=>{
    console.log(e)
    if(window.innerWidth <= 500){
        carousel_content.forEach((el, index)=>{
            el.style.display = "none";
        })
        carousel_next_btn.style.display = "none"
        carousel_prev_btn.style.display = "none";
    }else{
        carousel_content.forEach((el, index)=>{
            el.style.display = "block";
        })
        carousel_next_btn.style.display = "block"
        carousel_prev_btn.style.display = "block";
    }
})

if(window.innerWidth <= 650){
    carousel_content.forEach((el, index)=>{
        el.style.display = "none";
    })
    carousel_next_btn.style.display = "none"
    carousel_prev_btn.style.display = "none";
}

