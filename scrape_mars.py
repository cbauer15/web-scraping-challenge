# Import BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as bs
from pprint import pprint
import time
import pandas as pd

def init_browser():
    executable_path = {"executable_path":"../chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #Headline
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    first_headline = soup.find("li", class_="slide")
    FirstHeadLine = first_headline.find("div", class_="content_title").text
    
    #Featured Image
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    featured_image_finder = soup.find("footer")
    featured_image_url = featured_image_finder.find("a", class_="button fancybox")["data-fancybox-href"]
    URL_Base = "https://www.jpl.nasa.gov"
    ImageURL = f"{URL_Base}{featured_image_url}"

    #Facts Table
    Facts_url = "https://space-facts.com/mars/"
    browser.visit(Facts_url)
    Fact_Table = pd.read_html(Facts_url)
    FactTable_df = Fact_Table[0].rename(columns={0: "Description", 1: "Mars"}).set_index("Description")

    #Hemisphere Images
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    hemi_base_url = "https://astrogeology.usgs.gov"
    browser.visit(hemi_url)
    hemisphere_images_urls = []
    time.sleep(1)
        ##Valles_Marineris 
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, "html.parser")
    Valles_Marineris_image = soup.find("img", class_="wide-image")["src"]
    browser.visit(hemi_url)
    Valles_Marineris_image_url = f"{hemi_base_url}{Valles_Marineris_image}"
    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text
    hemi_dict = {"title": hemi_title, "img_url": Valles_Marineris_image_url}
    hemisphere_images_urls.append(hemi_dict)
        ##Cerberus
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, "html.parser")
    Cerberus_image = soup.find("img", class_="wide-image")["src"]
    browser.visit(hemi_url)
    Cerberus_image_url = f"{hemi_base_url}{Cerberus_image}"
    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text
    hemi_dict = {"title": hemi_title, "img_url": Cerberus_image_url}
    hemisphere_images_urls.append(hemi_dict)
        ##Schiaparelli
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, "html.parser")
    Schiaparelli_image = soup.find("img", class_="wide-image")["src"]
    browser.visit(hemi_url)
    Schiaparelli_image_url = f"{hemi_base_url}{Schiaparelli_image}"
    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text
    hemi_dict = {"title": hemi_title, "img_url": Schiaparelli_image_url}
    hemisphere_images_urls.append(hemi_dict)
        ##Syrtis_Major
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, "html.parser")
    Syrtis_Major_image = soup.find("img", class_="wide-image")["src"]
    browser.visit(hemi_url)
    Syrtis_Major_image_url = f"{hemi_base_url}{Syrtis_Major_image}"
    text_container = soup.find("section", class_="block metadata")
    hemi_title = text_container.find("h2", class_="title").text
    hemi_dict = {"title": hemi_title, "img_url": Syrtis_Major_image_url}
    hemisphere_images_urls.append(hemi_dict)
        ##Image Dictonary
    hemisphere_images_urls

    #Final dictionary
    NASA_Data = {
        "Headline" : FirstHeadLine,
        "Featured Image" : ImageURL,
        "Facts Table" : FactTable_df,
        "Hemisphere Images" : hemisphere_images_urls
    }

    browser.quit()

    return print(NASA_Data)
scrape()