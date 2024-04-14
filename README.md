#Kinopoisk app

this is full stack app, clone of Kinopoisk, using python, django framework, and javascript, html,css


Features
1. Browse Top Films
View the top 250 films based on average ratings.
Pagination impementation
2. Browse Films with Most Votes
View films sorted by the number of votes.
3. Browse Bottom Films
View the bottom 250 films based on average ratings.
4. Add Films
Add films to the database from  JSON file.
Automatically extract film database such as title, release year, poster picture link
5. Add Reviews
Add reviews for films, simulating user ratings and reviews.
Option to generate random reviews for testing purposes.


how to deploy project


#git clone https://github.com/Madtroublemaker/Kinopoisk.git

create virtual env
#python3 -m venv kinopoisk


#source kinopoisk/bin/activate


install requrements
#pip install -r requirements.txt


Access the Kinopisk app in your web browser at http://127.0.0.1:8000/.



Usage
1. Browse Films
Navigate to the homepage to view a list of films.
Use pagination links to browse through multiple pags.
2. View Film Details
Click on a film title to view detailed information about the film.
View film duration, genres, director, stars, overview, and poster image.
Users can also see their own ratings and reviews for the film if logged in.
3. Add Reviews
Users can add reviews for films by providing ratings.
For testing purposes, random reviews can be generated using the add_reviews view.


