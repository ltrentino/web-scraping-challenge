# Web Scraping Homework - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 



## Step 1 - Scraping

Initial scraping completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. Information saved to `mission_to_mars.ipynb` 

        ### NASA Mars News

        * Scrape the [Mars News Site](https://redplanetscience.com) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


        ### JPL Mars Space Images - Featured Image

        * Visit the url for the Featured Space Image page [here](https://spaceimages-mars.com).

        * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

        * Make sure to find the image url to the full size `.jpg` image.

        * Make sure to save a complete url string for this image.

        ### Mars Facts

        * Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

        * Use Pandas to convert the data to a HTML table string.

        ### Mars Hemispheres

        * Visit the Astrogeology site [here](https://marshemispheres.com) to obtain high resolution images for each of Mar's hemispheres.

        * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

        * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

        * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executes all the scraping code from above and returns one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that imports your `scrape_mars.py` script and calls the `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Created a root route `/` that queries the Mongo database and passes the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 

