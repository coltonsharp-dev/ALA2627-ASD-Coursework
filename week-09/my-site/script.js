// script.js — your Week 9 project. One file, five days.
// Work on ONE day's section at a time. Commit and push at every save point.
//
// The rule that does not change: you never paste code you cannot explain.
// A plan tells you what to write. You type it, and you will be asked about it.

// ─────────────── MON · A click that does something ───────────────
// You already did this in Week 8. Do it again from memory — no copying.
// TODO 1: find the button by its id. The # means "id".
// const button = document.querySelector("#action");

// TODO 2: find the paragraph JavaScript writes into.
// const output = document.querySelector("#output");

// TODO 3: when the button is clicked, change the words on the page.
//         Your feature, not the starter's — change these words to yours.
// button.addEventListener("click", function () {
//   output.textContent = "You clicked it!";
// });


// ─────────────── TUE · If/else — make the page decide ───────────────
// The variable goes HERE, outside the function. That is what lets the page
// remember between clicks. Put it inside and it resets every time.
// TODO 1: a variable that remembers something.
// let clicked = false;

// TODO 2: an if/else inside your click, so the button does two different things.
//         === compares. = assigns. They are not the same and the wrong one is a silent bug.
// button.addEventListener("click", function () {
//   if (clicked === false) {
//     output.textContent = "First press.";
//     clicked = true;
//   } else {
//     output.textContent = "Second press.";
//     clicked = false;
//   }
// });


// ─────────────── WED · Loops — many times, written once ───────────────
// TODO 1: your own items, in an array. Three or more, about YOUR topic.
// const items = ["first", "second", "third"];

// TODO 2: find the empty list in your HTML.
// const list = document.querySelector("#list");

// TODO 3: one pass per item. i counts the passes; items[i] is the item on this pass.
// for (let i = 0; i < items.length; i++) {
//   const li = document.createElement("li");
//   li.textContent = items[i];
//   list.appendChild(li);
// }

// The test that it is a real loop: add a fourth item to the array, change nothing
// else, reload. One more thing should appear on the page.


// ─────────────── THU · Show it, hide it ───────────────
// The hiding is done by a CLASS in styles.css, not by a style written here.
// That way the page decides how "hidden" looks, and your JavaScript only decides when.
// TODO 1: find the thing that starts hidden, and the button that reveals it.
// const details = document.querySelector("#details");
// const toggle = document.querySelector("#toggle");

// TODO 2: toggle adds the class if it is missing and removes it if it is there,
//         so the same button both shows and hides — as many times as you like.
// toggle.addEventListener("click", function () {
//   details.classList.toggle("hidden");
// });

// TODO 3: change the button's words to match what it will do next.


// ─────────────── FRI · Put it together ───────────────
// One feature of your own that uses at least three of this week's four parts:
// a click, a condition, a loop, a show/hide. It has to change WORDS on the page,
// not just a colour, and it has to be something nobody else's site does.
//
// Write it below. Be ready to point at any line and say what it does.
