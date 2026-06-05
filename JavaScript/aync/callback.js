function order(callback){
    setTimeout(()=>{
        console.log('Order placed');
        callback();
    },1000)
}
function prepare(callback){
    setTimeout(()=>{
        console.log('order prepared');
        callback();
    },5000)
}
function delivery(callback){
    setTimeout(()=>{
        console.log('order deliverd');
        callback();
    },4000)
}
function eating(){
    setTimeout(()=>{
        console.log('eating pizza')
    },3000)
}
order(()=>prepare(()=>delivery(()=>eating())));