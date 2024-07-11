// const http = require('http')
const prompt = require('prompt-sync')()

let n = prompt("n : ")
let range = prompt("range : ")
let res = ""

for (let i = 0; i < (n * 2); i++) {
    res += `${Math.floor(Math.random() * range)}`
    if (i != (n * 2) - 1)
        res += " "
}

console.clear()
console.log(`n : ${n}\n${res}`);
