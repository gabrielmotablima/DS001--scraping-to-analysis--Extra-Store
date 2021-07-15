# :tada: DS001-scraping-to-analysis--Extra-Store

The present project is a basic process pipeline of extrating, transforming, loading, analysing and presenting. All of that was made by using suitable tools of web scraping, data analysis/presentation and databases.

### Objectives:
- Create a crawler able to scrape offers and reviews from Extra web store, more specifically, offers and reviews about coolers, televisions and printers;
- Save the data in a database in an automated way;
- Analyze products and reviews data;
- Create a basic presentation using Extra offers information.


# :computer: Step 1. Code code... and code

To code a programming to get web site information is needed a crawler (the crawler in DS001 project was made in Python and Scrapy).
Looking at Extra web store source code and requests in browser we can find some API URL been triggered. Using API URLs the work becomes easier.

# :motorway: Step 2. Choose a way to scrape and save the data

As reviews data can be extracted while scraping offers data, it's a good way to split the work into three spiders (coolers, televisions and printers spiders) without create additional spiders to reviews only. Basically, review objects are bigger than offer objects, then the impact of scraping the two together per spider isn't too severe.
The crawler saves the data in MongoDB database itself using the files "pipelines.py" and "items.py".

# :spider: Step 3. Run the spiders

Running the spiders with command "scrapy crawl <<SPIDER_NAME>>":
![step_3.1](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_1%20-%20open%20terminals%20and%20type%20scrapy%20crawl%20commands.png)

So...

![step_3.2](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_2%20-%20execute%20the%20code%20and%20wait%20the%20scrape%20untill%20the%20end.png)

# :floppy_disk: Step 4. Wait...

Data been saved in MongoDB database:

![step_4](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_5%20-%20products%20been%20saved.png)

- Products data format in database:

![step_4.1](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_2.1%20-%20products%20format%20in%20database.png)

- Reviews data format in database:

![step_4.2](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_2.2%20-%20reviews%20format%20in%20database.png)

I early stoped the crawlers due the time to deliver the case :flushed:. So, the result... was about 31k data documents saved within MongoDB datase.

![step_4.3](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_7.1%20-%20MongoDB%20at%20final.png)

# :dark_sunglasses: Step 5. Looking for a first undestanding about the data

MongoDB has its own tools to basic data analysis in database:

![step_5](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_7.2%20-%20MongoDB%20basic%20descriptive%20analysis.png)

# :chart_with_upwards_trend: Step 6. Making a deeper descriptive analysis

In a Jupyter Notebook some incredible things can be done. Python is a really flexible and versatile programming language. Using libraries/packages like Matplotlib, Pandas, Numpy, Seaborn a complete descriptive analysis is tangible.

![step_6](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_10%20-%20Using%20jupyter%20to%20deeper%20analysis.png)

# :art: Step 7. Exporting data and making a simple presentation

- Exporting products data from MongoDB as CSV:

![step_7.1](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_8.1%20-%20Exporting%20results%20to%20project%20folder.png)

- Exporting reviews data from MongoDB as CSV:

![step_7.2](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_8.2%20-%20Exporting%20results%20to%20project%20folder.png)

- Creating a simple presentation:

![step_7.3](https://github.com/GabrielMotaBLima/DS001-scraping-to-analysis--Extra-Store/blob/main/images/step_9%20-%20joining%20products%20and%20review%20to%20presentation.png)

# :rocket: The end.
