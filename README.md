# Free events from your city

This Project is pyhton based web scraping project. I have used BeautifulSoup/Selenium to scrape the data from couple of events related websites.
this project will output all the list of lined up events in your City which are within your budget.
Both static and dynamic scraping is used.

# Features

1. Need to scrape free events details from websites listed below (Default city = pune):
-BookMyShow ✓
-WhatsHot ✓
-EventsHigh  --site not working
-Insider.in ✓
-Townscript Events ✓ --dynamic scraping

2. Clean and Export the data in local file (text/csv/Excel) ✓
3. Take City as Input from user and show events from that city ✓
4. Make simple GUI

# Program Flow
1. Take input city from User
2. Goes to 4 event related websites and apply filter of city
3. Searches for free events
4. Grab all events data and store into temp csv files
5. Clean/Combine the data and export it to Excel file
6. Cleanup all temp files

# Dependencies

1. requests
`pip install requests`
2. BeautifulSoup
`pip install bs4`
3. Pandas
`pip install pandas`

# Comments and Suggestions

Comments and suggestions are always welcome :)