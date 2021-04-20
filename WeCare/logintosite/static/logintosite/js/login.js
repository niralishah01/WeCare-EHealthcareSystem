const togglepassword=document.querySelector(".togglePassword");
const password=document.querySelector("#password");

const changePasswordtype=(e)=>{
    if(togglepassword.textContent==="SHOW"){
        togglepassword.textContent="HIDE";
        password.setAttribute("type","text");
    }
    else{
        togglepassword.textContent="SHOW";
        password.setAttribute("type","password");
    }
}
togglepassword.addEventListener('click',changePasswordtype);