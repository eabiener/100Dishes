This project aims to provide users with a list of 100 dishes they can try!

The list is curated based on user's input of their dietary preferences

The list is regionally balanced

In a webpage, users are presented with a checklist of dietary preferences; for instance, vegan, gluten-free, kosher, soy allergy.
    On the homepage, I have included an explanation for how I selected the dishes and classified them by dietary preference, as well as some statistics about the dataset
    
After selecting their dietary preferences, users click a submit button to generate their list

Behind the scenes, there is a SQL table of over 500 dishes from a dataset I created
    There is an approximately equal number of dishes from each pre-defined region
    
Each dish is tagged with dietary attributes such as, vegan, no shellfish, tree nut free

Each dish is also tagged with a region of origin

For each region, a SQL query is run to generate 10 dishes, in random order.

Flask and Python are used to run the webpage, with some CSS styling.

Users can select up to five dietary preferences, but if they try to select more they receive an error message.

The results of the SQL query are displayed in html tables on a results page
