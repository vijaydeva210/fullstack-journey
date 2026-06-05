function* even(x){
    for(let i of x){
        yield i;
    }
}
x=[1,2,3,4,5,6]
for(let i of even(x)){
    console.log(i);
}