Art Gallery Database

Description:
This is a database for a contemporary art gallery. The database stores data for each artist, artwork, and collector. Artists’ name and location are stored in the artists table. Additionally, there is an artist_accounts table that stores each artists’ email address and password. Collectors’ names are stored along with the id for any artwork they have purchased. In the collector_accounts table, similar to the artist_accounts table, their email and password is found there. Each artwork in the artworks table has the title, date, and id of the artist who made it. There is also a categories table that stores categories or art (painting, sculpture, etc) and the corresponding id to each artwork.

_________________________________________________________________________
|           API endpoints         |       Description                   |
|_________________________________|_____________________________________|
| http://localhost:5000/artworks  | Shows a dictionary of every artwork |
|_________________________________|_____________________________________|
|http://localhost:5000/artists/24 | Shows the stored data for the artist|
|                                 | with the corresponding id           |
|_________________________________|_____________________________________|
*I am working on including more endpoints

Retrospective answering of the following questions:

How did the project's design evolve over time?

The project evolved in that it became simpler in ways and more complex in others. I had intended to store billing information and store more credentials in a more realistic way. I pared down though for the sake of time. The project became more complex with the addition of foreign keys on various tables and reorganizing the tables from the originial structure. 

Did you choose to use an ORM or raw SQL? Why?

I chose to use an ORM mostly because I wanted more practice with Python. I think that completing the project would have likely been easier and more streamline using raw SQL. 

What future improvements are in store, if any?

Oh many! I need to figure out how to organize some of the data in a more efficient way. Primary keys are used, but I need them to be able to repeat in the categories table. For example, I want and artwork that is in the category painting to be coded with an id of 2 (2, being the primary key (or foreign key) for painting). I'm not quite sure of the best way to do this. I've done some research, but have not arrived at a solution. I'd also like to go back to my original ER Diagram and add some more content to the accounts to make it more realistic. I'd also like to create more API endpoints. For now, that's what I can think of. I'm sure as I continue to dig in, I will find more.# art_gallery
