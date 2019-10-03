/* jshint esversion: 7 */
/* jshint node: true */
'use strict';

async function get_individual(num, all_numbers) {

}

async function get_batch(num, all_numbers) {
}

async function clickedon() {
    let num = parseInt(document.querySelector('#number').value);
    let all_numbers = document.querySelector('#number_info');
    if (document.querySelector('#batch').checked) {
        get_batch(num, all_numbers);
    } else {
        get_individual(num, all_numbers);
    }
}
