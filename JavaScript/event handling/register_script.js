document.querySelector('#form').addEventListener('submit',validate);
function validate(event){   
    let is_prevent=true;
    let uname=document.querySelector('#uname').value;
    let pass=document.querySelector('#pass').value;
    if(uname.length<5){
        is_prevent=false;
        document.querySelector('#unameerr').innerText='incorrect username';
    }else{
        document.querySelector('#unameerr').innerText='';
    }
    if(pass.length<8){
        is_prevent=false;
        document.querySelector('#psderr').innerText='incorrect passsword';
    }else{
        document.querySelector('#psderr').innerText='';
    }
    if(is_prevent==false){
        event.preventDefault(); 
    }
    
}