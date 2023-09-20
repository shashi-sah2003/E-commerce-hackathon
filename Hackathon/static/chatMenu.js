let msgBtn = document.querySelector("#msg-btn")
let textBox = document.querySelector("#text-chat")
let active = false

msgBtn.addEventListener("click" , () => {
    if (!active){
        textBox.style.display = "block"
        active = true
    }
    else{
        textBox.style.display = "none"
        active = false
    }
})