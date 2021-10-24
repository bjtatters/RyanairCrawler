# RyanairCrawler

This code is an attempt to (legally) web-scrape airline pricing data from the Ryanair website. Screenscrapers now account for about 20% of Ryanair’s total ticket sales – double the amount they did before the Covid pandemic.

Chief executive Michael O’Leary has been outspoken about these resellers, describing them as a “pain in the ass” and saying he “can’t understand” why the European Commission and regulators won’t take action against them.

The code allows users to input any set of flight paths and it returns the prices for two weeks, one month and four months in advance. 

I managed to acheive this by locating the ryanair API call path in the companies HTML code. This API call has a standard structure, with certain consistencies for origin, destination, date, seating and so forth. By modifying the API call, and looping the process, the data for a large volume of flights can then be returned by understanding the structure of the returned API data.

For practical use, please input the 3 digit airport codes for each flight path of interest into the flight_dict variable. 
