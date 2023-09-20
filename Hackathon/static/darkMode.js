if (localStorage.getItem("DarkMode") == 1){
    document.body.style.backgroundColor = "rgb(26, 27, 27)";
    document.body.style.color = '#0ceba1'
    if (document.querySelector(".product-form")){
        document.querySelector(".product-form").style.backgroundColor = "#0ceba1"
        document.querySelector(".product-form").style.color = "white"
    }
    if (document.querySelector(".product-title")){
        document.querySelector(".product-title").style.color = "white"
    }

    if (document.querySelector(".product-btn")){
        document.querySelector(".product-btn").style.backgroundColor = 'rgb(26, 104, 71)'
    }
}
else{
    document.body.style.backgroundColor = "white"
}