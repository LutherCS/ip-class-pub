# Geography

Connect to the SQLite3 version of the _world_ database and retrieve the following information about a _country_, a _continental region_, or a _subregion_ by visiting _/country_, _/region_, or _/subregion_ respectively:

1. Country official name
1. Capital name
1. Continental region
1. Subregion
1. Area
1. Population in 2023
1. Population density (population divided over area)
1. Government system

## Requirements

1. Use `world.sqlite3` database.
2. Use `get` method to submit selection to the server.
3. Implement function `get_data_from_db` that takes a parametrized query and optional tuple as parameters. This function must return all records retrieved by the query.
4. Implement functions `country_form`, `region_form`, and `subregion_form` that display country, region, and subregion selection forms by rendering templates _country.html_, _region.html_, and _subregion.html_, respectively.
5. Implement functions `country_info`, `region_info`, and `subregion_info` that display country, region, and subregion information by rendering template _index.html_ with different data.
6. Present the results as a table with `id` _information_.
7. Use a framework or custom CSS to style the results.
8. Handle missing data gracefully. Notice that some countries/territories don't have permanent population (e.g. $0$ in Antarctica) while the population of others is unknown (e.g. `NULL` in Territory of Christmas Island).
9. Handle `Not Found` events properly. Your application should display an informative message if a country (e.g. Aldovia), a region (Eurasia), or a subregion (Middle East) is not found in the database.

## Demo

![Demo](demo.gif)
