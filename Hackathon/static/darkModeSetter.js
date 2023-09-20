let checkBoxEl = document.getElementById("theme-setter")

checkBoxEl.addEventListener('click' , () => {
    if (checkBoxEl.checked == true){
        document.body.style.backgroundColor = "rgb(26, 27, 27)"
        localStorage.setItem("DarkMode" , 1)
    }
    else{
        document.body.style.backgroundColor = "white"
        localStorage.setItem("DarkMode" , 0)
    }
})

if (localStorage.getItem("DarkMode") == 1){
    document.body.style.backgroundColor = "rgb(26, 27, 27)";
    document.body.style.color = '#0ceba1'
    checkBoxEl.checked = true;
}
else{
    document.body.style.backgroundColor = "white"
}