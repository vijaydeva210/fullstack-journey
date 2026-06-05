
document.querySelector('#checkbox').addEventListener('change',copy);
document.getElementById('checkbox').addEventListener('change',changecolor);
function changecolor(event){
    let text=document.getElementById('Permanent');
    if(event.target.checked){
       text.style.backgroundColor='blue'
    }else{
        text.style.backgroundColor=''
    }
}
function copy(event){
    if(event.target.checked){
        document.getElementById('Permanent').value=document.getElementById('Present').value;
    }else{
        document.getElementById('Permanent').value='';
    }
}