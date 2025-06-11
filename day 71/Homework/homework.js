function getRandomNumber() {
  return Math.floor(Math.random() * 10) + 1;
}

console.log(getRandomNumber());


let num = parseFloat(prompt("enter a decimal number"));

if (isNaN(num)) {
alert("please enter a valid number");
} else {
alert("rounded down: " + Math.floor(num) +
        "\nrounded up: " + Math.ceil(num) +
        "\nrounded to nearest: " + Math.round(num));
}

