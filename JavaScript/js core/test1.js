/*let x=10;//global scope
function show(){
    console.log(x);
}
show()
console.log(x);*/
/*function display(){
    let x=10;//function scope.
    console.log(x);
}
display();
console.log(x);*/
function outerfun(){
    let x=10;
    function innerfun(){
        console.log(x)
    }
    return innerfun
}
fun=outerfun()
fun()