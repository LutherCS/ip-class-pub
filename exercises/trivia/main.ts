"use strict";

/**
 * Retrieving data from the Open Trivia Database
 *
 * @author
 * @version 2026.10
 */

interface Question {
  type: string;
  difficulty: string;
  category: string;
  question: string;
  correct_answer: string;
  incorrect_answers: Array<string>;
}

/**
 * Use fetch to retrieve data
 *
 * @param chosenNumber number entered by the user
 * @param chosenCategory category chose by the user
 * @returns JSON of the retrieved data
 */
async function getData(chosenNumber: number, chosenCategory: string) {
  const BASE_URL = "https://opentdb.com/api.php?";
  // TODO: fetch data from opentdb
}

/**
 * Retrieve questions in the chosen category
 *
 * @returns if number cannot be processed
 */
async function getQuestions() {
  // TODO: use getData to retrieve data from an API
}

/**
 * Build the HTML structure to display questions
 *
 * @param questionSection section where questions are going to be displayed
 * @param number number of question cards to create
 * @returns if there are any errors
 */
function buildStructure(questionSection: Element, number: number): void {
  // TODO: create the structure (e.g. cards or divs) to be later populated
}

/**
 * Display the results
 *
 * @param questionSection section where questions are going to be displayed
 * @param questionPool question retrieved from the API
 */
function displayQuestion(
  questionSection: Element,
  questionPool: Array<Question>,
) {
  // TODO: attach all questions to the provided section
}

window.onload = function () {
  document
    .querySelector("[id='getQuestionsBtn']")
    ?.addEventListener("click", getQuestions);
};
