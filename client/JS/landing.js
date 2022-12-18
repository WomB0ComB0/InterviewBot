// Create an onload for a preloader in javascrip?
function resolveAfter2Seconds() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('resolved');
    }, 2000);
  });
}

async function asyncCall() {
  console.log('calling');
  const result = await resolveAfter2Seconds();
  console.log(result);
  // expected output: "resolved"
}

window.addEventListener('load', async (event) => {
  let loading = true 
  // this loading value helps you to know when to show your loader

  await console.log('page is loading');
  await asyncCall()

  loading = false
  console.log('page is loaded');
});


// This part is for feedback, this is likely going to be a part of another page
window.addEventListener("load", function(){
    "use strict";
    const form = document.querySelector(".contact")
    form.addEventListener("submit", function (event){
        event.preventDefault()
        let fields = document.querySelectorAll(".concat .form-control")
        let valid = true
        for (var i = 0; i < fields.length; i++){
            field[i].classList.remove("no-error")
            if(fields[i].valid === ""){
                fields[i].classList.add("has-error")
                fields[i].nextElementSibling.stlye.display = "block"
                valid = false
            }else{
                fields[i].classList.remove("has-error")
                fields[i].classList.add("no-error")
                fields[i].nextElementSibling.stlye.display = "none"
            }
        }
        if(valid){
            console.log("it is valid");

        }
    })
})
