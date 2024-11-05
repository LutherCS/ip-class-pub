/**
 * World API front-end
 * 
 * @author: Roman Yasinovskyy
 * @version: 2024.11
 */

const BASE_URL = "http://localhost:5000/api"

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

/**
 * Retrieve data using axios
 */
async function getData(inputField) {
    return await axios.get(`${BASE_URL}/${document.querySelector(inputField).value}`)
        .then(response => response.data)
        .catch(error => error.response.data);
}
/**
 * View country data
 */
async function viewCountryInfo() {
    let responseDiv = document.querySelector("#content");
    responseDiv.innerHTML = "";
    let data = await getData("#countryName");
    await sleep(1000);
    let dataList = document.createElement("dl");
    responseDiv.appendChild(dataList);
    for (let [key, value] of Object.entries(data)) {
        let dataTerm = document.createElement("dt");
        dataTerm.innerHTML = key;
        dataList.appendChild(dataTerm);
        let dataDefinition = document.createElement("dd");
        dataDefinition.innerHTML = value;
        dataList.appendChild(dataDefinition);
        await sleep(250);
    }
}