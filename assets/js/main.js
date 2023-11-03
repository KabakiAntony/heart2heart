const voice_form = document.getElementById("id_voice_form");
const email_form = document.getElementById("id_email_form");
const voice_radio = document.getElementById("id_voice_radio");
const email_radio =document.getElementById("id_email_radio");
const messages = document.querySelector(".messages");

voice_radio.addEventListener('click', ()=>{
    voice_form.classList.add('show');
    email_form.classList.remove('show');
})

email_radio.addEventListener('click', ()=>{
    email_form.classList.add('show');
    voice_form.classList.remove('show');
})

if (messages) {
  setTimeout(() => {
    messages.style.display = "none"
  }, 5000)
}