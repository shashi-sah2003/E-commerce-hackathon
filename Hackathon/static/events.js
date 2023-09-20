let registerBtn = document.querySelector('.register-link')
let loginBtn = document.querySelector('.login-link')

registerBtn.addEventListener('click' , () => {
    location.href = "/register/"
})

loginBtn.addEventListener('click' , () => {
    location.href = "/login/"
})