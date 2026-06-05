function order(){
    return new Promise((resolve,response)=>{
        setTimeout(()=>{
            resolve('Order placed')
        },3000)
    });
}
function prepare(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve('Order is prepared')
        },4000)
    });
}
function delivery(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve('Order is delivered')
        },2000)
    });
}
function eating(){
    return new Promise((resolve,reject)=>{
        resolve('Eating Pizza')
    },1000)
}

async function process(){
    let res;
    res = await order();
    console.log(res);
    res = await prepare();
    console.log(res);
    res = await delivery();
    console.log(res);
    res = await eating();
    console.log(res);
}
process();