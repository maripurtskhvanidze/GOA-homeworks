// 2
let t = true;
let tInt = setInterval(() => {
document.title = t ? "Hello" : "Goodbye";
t = !t;
}, 1000);
setTimeout(() => clearInterval(tInt), 6000);

// 3
let box = document.createElement("div");
box.style.width = "50px";
box.style.height = "50px";
box.style.background = "red";
box.style.position = "relative";
document.body.appendChild(box);
let x = 0;
let move = setInterval(() => {
x += 10;
box.style.left = x + "px";
if (x >= 100) clearInterval(move);
}, 200);

// 5
let words = ["dog", "cat", "sun"];
for (let w of words) {
console.log(w.toUpperCase());
}

// 6
let nums = [5, 8, 2];
nums[1] = 0;
console.log(nums);

// 7
let arr = ["a", "b"];
arr.push("c");
arr.unshift("z");
arr.pop();
console.log(arr);

// 8
let n = [4, 6, 8, 2];
let sum = 0;
for (let i of n) sum += i;
console.log(sum / n.length);
