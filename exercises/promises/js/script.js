'use strict';

/**
 * Retrieve trivia about numbers one-by-one
 * 
 * @param {number} num base number
 * @param {Object} all_numbers DOM element to append to
 */
async function get_individual(num, all_numbers) {

}

/**
 * Retrieve trivia about all numbers at once
 * 
 * @param {number} num base number
 * @param {Object} all_numbers DOM element to append to
 */
async function get_batch(num, all_numbers) {

}

/**
 * Retrieve information about numbers
 */
async function clickedon() {
    let num = parseInt(document.querySelector("#number").value);
    let all_numbers = document.querySelector("#number_info");
    if (document.querySelector("#batch").checked) {
        get_batch(num, all_numbers);
    } else {
        get_individual(num, all_numbers);
    }
}
