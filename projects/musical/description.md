# High School Musical

Develop a web application that allows a director to manage various aspects of a musical production at a local high school and display the results in a visually appealing manner similar to a paper program (playbill).

## Program layout

The resulting application must include several pages and follow the general format of the provided program.

### General information

The director must be able to add a new production, including the following:

- Title of the show
- Subtitle (e.g. Disney's, Marvel's, William Shakespeare's etc)
- Cover image
- Dates of the performances
- Location of the performances (the same for all dates)
- Price of admission
- Copyright information
- Additional notes (e.g. audio/video recording permissions)

### Cast

The director must be able to assign roles to the cast members.
Note that some students may play multiple roles and some roles are grouped together (e.g. "Mersistes", "Gulls", "Munchkins", "Forest folk" etc)

You may determine the order of performers but groups must appear after individual performers in the program.

The list of students is provided (student.csv) and must be imported into the database.

### Crew

Some students are involved in the production as members of the stage crew and tech support rather than actors.
These students must be acknowledged but their specific responsibilities may be omitted.

### Creative team

The director and members of the creative team must be listed in the program.
These are adults and their number and roles may change between productions.
Note that the same role can be fulfilled by multiple people (e.g. Choreographers) and the same person may serve in multiple roles.

The following are typical roles on the creative team, even though not every production includes all of them.

- Director
- Assistant director
- Drama director
- Costume director
- Tech director
- Set designer
- Lighting designer
- Make-up artist
- Choreographer

### Song list

The program must include a list of songs, including each song's title and performer(s).

Acts of the performance must be clearly separated with the length of the intermission, if any, specified.

### Thanks and recognitions

The program must include a section of special acknowledgments and recognitions.
There is no specific requirement for the section's format as long as it is present in the program.

## Technical requirements

Your application must access data from the **SQLite database** and generate content using **Jinja templates**.
Database schema must be generated and accessed using **SQLAlchemy**.
Some data may be **imported** into the database from the (provided) CSV file while other data will be added based on user input.

The application must include several **routes** (e.g. *Cast*, *Crew*, *Team*, *Songs*, *Thanks* etc).

While authentication is not required for this project, you must differentiate between the director's and the reader's interfaces.
Use **Flask blueprints** with different prefixes (e.g. `/edit` and `/view`).

The director must be able to **add**, **remove**, and **edit** roles, responsibilities, and positions.
The director must be able to **assign** students on the roster to specific roles (acting) and responsibilities (non-acting).
The director must be able to **assign** adults (not on the roster) to specific positions on the creative team.

The director must be able to **add**, **remove**, and **edit** songs.
Songs have a title and may be performed by multiple roles.
The same song may appear in different acts as a reprise.

The interface must be **consistent** and **visually appealing**.

The application must be **stable** and **deployed** (publicly available).

| Requirement                                                    | Points |
|----------------------------------------------------------------|--------|
| **General functionality**                                      | 60     |
| Multiple routes                                                | 5      |
| Multiple Jinja templates used                                  | 5      |
| Separate blueprints to edit and view data                      | 5      |
| Ability to add responsibilities (acting, non-acting, creative) | 5      |
| Ability to edit responsibilities                               | 5      |
| Ability to remove responsibilities                             | 5      |
| Ability to assign responsibilities to people                   | 5      |
| Ability to edit assigned responsibilities                      | 5      |
| Ability to add songs                                           | 5      |
| Ability to edit songs                                          | 5      |
| Ability to remove songs                                        | 5      |
| Ability to add and edit general information                    | 5      |
| **Database**                                                   | 20     |
| Multiple tables present in the SQLite database                 | 5      |
| Data imported from CSV                                         | 5      |
| Data is updatable                                              | 5      |
| SQLAlchemy is used                                             | 5      |
| **User interface**                                             | 10     |
| User interface is consistent                                   | 5      |
| User interface is visually appealing                           | 5      |
| **Deployment**                                                 | 10     |
| Application is deployed                                        | 5      |
| Application is stable                                          | 5      |
| **Total**                                                      | 100    |

## References

- [Programme (booklet) - Wikipedia](https://en.wikipedia.org/wiki/Programme_\(booklet\))
- [Making a Musical: Key Players - The Creative Team](https://www.musicals101.com/creative.htm)
- [How to Create a Program for Your Production](https://www.theatrefolk.com/blog/how-to-create-a-program-for-your-production)
