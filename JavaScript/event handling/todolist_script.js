document.querySelector('#btn').addEventListener('click',copytext);
function copytext(){
    let text=document.querySelector('#textbox').value;
    let li_item=document.createElement('li');
    li_item.innerText=text;
    document.querySelector('.list').appendChild(li_item);
}