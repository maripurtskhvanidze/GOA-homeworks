let num1 = parseFloat(prompt("enter the first number"));
let num2 = parseFloat(prompt("enter the second number"));
let num3 = parseFloat(prompt("enter the third number"));

if (num1 === num2 && num2 === num3) {
alert("all numbers are equal");
} else if (num1 >= num2 && num1 >= num3) {
alert("the largest number is " + num1);
} else if (num2 >= num1 && num2 >= num3) {
alert("the largest number is " + num2);
} else {
alert("the largest number is " + num3);
}


let age = parseInt(prompt("enter your age"));

if (age >= 0 && age <= 12) {
alert("you are a child");
} else if (age >= 13 && age <= 19) {
alert("you are a teenager");
} else if (age >= 20 && age <= 59) {
alert("you are an adult");
} else if (age >= 60) {
alert("you are a senior");
} else {
alert("invalid age");
}

