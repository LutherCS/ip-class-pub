# Geography

Connect to the SQLite3 version of the *world* database and retrieve data about the world, a continental region, a subregion, or an individual country.

## World

Display the number of countries in *the world* and the following information about each country:

1. Official name (must be a link to the specific country page)
2. Capital name
3. Continental region (must be a link to the specific region page)
4. Subregion (must be a link to the specific subregion page)
5. Area
6. Population in 2023
7. Population density (population divided over area)
8. Government system

The search form must include all countries and territories so users can quickly search for a specific country.

## Region

Same as the world but display countries in a specific *continental region*.
The search form must include distinct continental regions so users can quickly search for a specific region.

If the region is not selected, display a general invitation to use the search form.

## Subregion

Same as the region but display countries in a specific *subregion*.
The search form must include distinct subregions so users can quickly search for a subregion.

If the subregion is not selected, display a general invitation to use the search form.

## Country

Display name, administrative region, and population of every city in the country found in the *city* table of the database.
Country capital must be highlighted in the table.
The search form must include all countries and territories so users can quickly search for a specific country.

## Requirements

1. Use `world.sqlite3` database.
2. Use `get` method to submit selection to the server.
3. Implement function `get_data_from_db` that takes a parametrized query and optional tuple as parameters. This function must return all records retrieved by the query.
4. Implement functions `world`, `region`, `subregion`, and `country` that display world, region, subregion, and country-level data as a table.
5. Present the results as a table with `id` *information*.
6. Use a framework or custom CSS to style the results.
7. Handle missing data gracefully. Notice that some countries/territories don't have permanent population (e.g. $0$ in Antarctica) while the population of others is unknown (e.g. `NULL` in Territory of Christmas Island).
8. Handle `Not Found` events properly. Your application should display an informative message if a country (e.g. Aldovia), a region (Eurasia), or a subregion (Middle East) is not found in the database.

## Using the application

Run the app from the *exercises/geo* directory:

```bash
flask --app alex run
```

Test the app from the root directory of the repository:

```bash
python -m pytest tests/geo
```

## Demo

![Demo](demo.mp4)
