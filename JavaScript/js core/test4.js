'use strict'
let x;
x=[1,2,3,4,5]
let square=x.map((n)=>n**2);
let even=x.filter((n)=>{
    return n%2==0;
})
let add=x.reduce((a,b)=>a+b);
console.log(square);
console.log(even);
console.log(add);
x.forEach((n)=>{
    console.log(n);
})
let is_even=x.every((n)=>{
    return n%2==0;
})
console.log(is_even)
let is_odd=x.some((n)=>{
    return n%2;
});
console.log(is_odd);