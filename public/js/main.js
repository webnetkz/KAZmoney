"use strict";
import { parallaxScroll } from './moduls/parallaxScroll.js';
import { showVisible } from './moduls/showOnScroll.js';


window.addEventListener('scroll', () => {

});

let firstStart = false;

document.querySelector('#startBtn').addEventListener('click', () => {
  let startBtn = document.querySelector('#startBtn');
  if(startBtn.querySelector('p').textContent == 'START') {
    startBtn.querySelector('p').textContent = 'STOP';
    if(firstStart == false) {
      startTimer();
      firstStart = true;
    }
  } else {
    stopTimer();
  }
});

let minutes = document.querySelector('.minutes');
let seconds = document.querySelector('.seconds');
let miliseconds = document.querySelector('.miliseconds');

function stopTimer() {
  let newRes = document.createElement('div');
  newRes.classList.add('res');
  newRes.textContent = document.querySelector('.timer').textContent;
  document.querySelector('#results').appendChild(newRes); 
}

function startTimer() {
  setInterval(() => {
    for(let dash of document.querySelectorAll('.dashes')) {
      if(dash.style.color == 'rgb(32, 32, 35)') {
        dash.style.color = 'white';
      } else {
        dash.style.color = 'rgb(32, 32, 35)';
      }
    }
  }, 500);

  setInterval(() => {
    seconds.textContent = Number(seconds.textContent) + 1;
    if(Number(seconds.textContent) < 10) {
      seconds.textContent = '0'+Number(seconds.textContent)
    }
    if(Number(seconds.textContent) == 60) {
      seconds.textContent = '00';
      minutes.textContent = Number(minutes.textContent) + 1;
    }
    if(Number(minutes.textContent) < 10) {
      minutes.textContent = '0'+Number(minutes.textContent)
    }
  }, 1000);

  setInterval(() => {
    miliseconds.textContent = Number(miliseconds.textContent) + 1;
    if(Number(miliseconds.textContent) == 10) {
      miliseconds.textContent = 0;
    }
  },100);
}