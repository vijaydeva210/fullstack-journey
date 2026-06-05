//asynchronous
/*function task1(){
    console.log('task1 is started');
    console.log('task1 is ended')
}
function task2(){
    console.log('task2 is started');
    console.log('task2 is ended')
}
function task3(){
    console.log('task3 is started');
    console.log('task3 is ended')
}
task2()
task1()
task3()*/
//asynchronous
function sleeep(secs){
    let curr_time=new Date().getTime();
    while (curr_time+secs>new Date().getTime());
     console.log(curr_time)
}
console.log('Program Started')
function task1(){
    setTimeout(()=>{
        console.log('task1 is started')
        console.log('task1 is ended')
    },3000)  
}
function task2(){
    setTimeout(()=>{
        console.log('task2 is started');
        console.log('task2 is ended')
    },5000)
}
function task3(){
    setTimeout(()=>{
        console.log('task3 is started');
        console.log('task3 is ended')
    },4000)
}
task1();
task2();
task3();
console.log('Program ended')