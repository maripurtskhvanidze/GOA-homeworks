let random = Math.floor(Math.random() * 100) + 1;

let guess = prompt("guess a number from 1 to 100");

guess = parseInt(guess);

if (!guess) {
alert("please enter a number");
} else if (guess > random) {
alert("too high");
} else if (guess < random) {
alert("too low");
} else {
alert("congrats!");
}

