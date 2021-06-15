# Dependencies
import time
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # Create a dictionary for all of the scraped data
    mars_data = {}

    # Visit the Mars news page. 
    url = "https://redplanetscience.com/"
    browser.visit(url)
 
    # Search for news
    # Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find the latest Mars news.
    news_title = soup.find_all("div", class_="content_title")[0].get_text()
    news_p = soup.find_all("div", class_="article_teaser_body")[0].get_text()

    # Adding values to dictionary
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p

    # JPL Mars Space Images site

    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Creating BeautifulSoup object; parse with 'html.parser'
    space_image_url = browser.html
    soup = BeautifulSoup(space_image_url, 'html.parser')

    # Found and printed all images
    images = soup.findAll('img')
    img = images[1]
    image_url = img.attrs['src']
    featured_image_url = f"https://spaceimages-mars.com/{img_url}"
    
    # Add the featured image url to the dictionary
    mars_data["featured_image_url"] = featured_image_url

    # Mars Facts
    # Extracting tables
    # Determining the number of tables on the page
    mars_facts_url = 'https://galaxyfacts-mars.com/'
    dfs = pd.read_html(mars_facts_url)
    mars_properties_df = dfs[0]
    mars_properties_df.columns=["Facts", "Mars", "Earth"]
    mars_properties_df = mars_properties_df.drop(mars_properties_df.index[0])
    mars_properties_df = mars_properties_df.reset_index(drop=True)

    mars_information = mars_properties_df.to_html(classes='mars_information')
    mars_information =mars_information.replace('\n', ' ')

    # Add the Mars facts table to the dictionary
    mars_data["mars_table"] = mars_information


    # Mars Hemispheres
    url_hemisphere = 'https://marshemispheres.com/'
    browser.visit(url_hemisphere)

    mars_hemisphere_url = browser.html
    soup = BeautifulSoup(mars_hemisphere_url, 'html.parser')

    hemisphere_titles = soup.find_all('h3')
    hemisphere_titles_1 = hemisphere_titles[0].get_text()
    hemisphere_titles_2 = hemisphere_titles[1].get_text()
    hemisphere_titles_3 = hemisphere_titles[2].get_text()
    hemisphere_titles_4 = hemisphere_titles[3].get_text()

    hemisphere_1 = 'https://marshemispheres.com/cerberus.html'
    response1 = requests.get(hemisphere_1)
    soup = BeautifulSoup(response1.text, 'html.parser')

    hemisphere_images_1 = soup.findAll('img')

    first_image = hemisphere_images_1[4]
    first_image_url = first_image.attrs['src']
    first_image_url_ = f"https://marshemispheres.com/{first_image_url}"

    hemisphere_2 = 'https://marshemispheres.com/schiaparelli.html'
    response2 = requests.get(hemisphere_2)
    soup = BeautifulSoup(response2.text, 'html.parser')

    hemisphere_images_2 = soup.findAll('img')

    second_image = hemisphere_images_2[4]
    second_image_url = second_image .attrs['src']
    second_image_url_ = f"https://marshemispheres.com/{second_image_url}"

    hemisphere_3 = 'https://marshemispheres.com/syrtis.html'
    response3 = requests.get(hemisphere_3)
    soup = BeautifulSoup(response3.text, 'html.parser')

    hemisphere_images_3 = soup.findAll('img')

    third_image = hemisphere_images_3[4]
    third_image_url = third_image .attrs['src']
    third_image_url_ = f"https://marshemispheres.com/{third_image_url}"

    hemisphere_4 = 'https://marshemispheres.com/valles.html'
    response4 = requests.get(hemisphere_4)
    soup = BeautifulSoup(response4.text, 'html.parser')

    hemisphere_images_4 = soup.findAll('img')

    fourth_image = hemisphere_images_4[4]
    fourth_image_url = fourth_image .attrs['src']
    fourth_image_url_ = f"https://marshemispheres.com/{fourth_image_url}"

    hemisphere_image_urls = [{'title': hemisphere_titles_1, 'img_url': first_image_url_},
                        {'title': hemisphere_titles_2, 'img_url': second_image_url_},
                        {'title': hemisphere_titles_3, 'img_url': third_image_url_ },
                        {'title': hemisphere_titles_4, 'img_url': fourth_image_url_ }]


    mars_data['mars_hemisphere'] = hemisphere_image_urls
    # Return the dictionary
    return mars_data
