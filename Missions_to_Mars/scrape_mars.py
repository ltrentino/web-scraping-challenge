# Start by converting your Jupyter notebook into a Python script called scrape_mars.py
#    with a function called scrape that will execute all of your scraping code from above
#        and return one Python dictionary containing all of the scraped data.


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd




def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)
    img_urls_titles = mars_hemispheres(browser)

    data = {
        'news_title' : news_title,
        'news_paragraph' : news_paragraph,
        'featured_image' : featured_image(browser),
        'facts' : mars_facts(),
        'hemispheres' : img_urls_titles,
    }
    browser.quit()
    return data

# NASA Mars News
def mars_news(browser):
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    
    html = browser.html
    soup = bs(html, "html.parser")
    
    try:
        news_title = soup.find("div", class_= "content_title").text
        news_p = soup.find("div", class_="article_teaser_body").text

    except AttributeError:
        return None, None

    return news_title, news_p


# Featured Image
def featured_image(browser):
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    img_soup = bs(html, 'html.parser')
    
    try: 
        feautred_image_src = img_soup.find('img', class_="headerimage fade-in").get('src')
    except AttibuteError:
        return None
    
    feautred_image_url = url+feautred_image_src
    return feautred_image_url



# Mars Facts
def mars_facts():
    url = "https://galaxyfacts-mars.com/"
    try:
        tables = pd.read_html(url)
    except BaseException:
        return None
    
    df = tables[0]
    return df.to_html()



# Mars Hemispheres
def mars_hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []
    for h in range(4):
        browser.links.find_by_partial_text('Hemisphere')[h].click()
        html = browser.html
        soup = bs(html, "html.parser")
        img_url = soup.find(class_='description').a.get('href')
        title = soup.find('h2', class_= "title").text

        hemispheres = {}
        hemispheres['title'] = title
        hemispheres['img_url'] = url+img_url
        hemisphere_image_urls.append(hemispheres)
        browser.back()
    return hemisphere_image_urls



if __name__ == "__main__":
    print(scrape())
