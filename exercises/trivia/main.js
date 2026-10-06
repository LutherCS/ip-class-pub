"use strict";

/**
 * Retrieving data from the Open Trivia Database
 *
 * @author
 * @version 2026.10
 */

/**
 * Use fetch to retrieve data
 * 
 * @param {number} chosenNumber
 * @param {string} chosenCategory
 * @returns JSON of the retrieved data
 */
async function getData(chosenNumber, chosenCategory) {
    const BASE_URL = "https://opentdb.com/api.php?";
    // TODO: fetch data from opentdb
}

/**
 * Retrieve questions in the chosen category
 * 
 * @returns 
 */
async function getQuestions() {
    // TODO: use getData to retrieve data from an API
}

/**
 * Build the HTML structure to display questions
 *
 * @param {Element} questionSection section where questions are going to be displayed
 * @param {number} number number of question cards to create
 */
function buildStructure(questionSection, number) {
    // TODO: create the structure (e.g. cards or divs) to be later populated
}


/**
 * Display the results
 * 
 * @param {Element} questionSection section where questions are going to be displayed
 * @param {Array} questionPool question retrieved from the API
 */
function displayQuestion(questionSection, questionPool) {
    // TODO: attach all questions to the provided section
}
