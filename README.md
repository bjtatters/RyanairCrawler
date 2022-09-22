# RyanairCrawler

_This code is an attempt to (legally) web-scrape airline pricing data from the Ryanair website._

**Pesky screenscrapers...**

Screenscrapers now account for about 20% of Ryanair’s total ticket sales – double the amount they did before the Covid pandemic. Chief executive Michael O’Leary has been outspoken about these resellers, describing them as a “pain in the ass” and saying he “can’t understand” why the European Commission and regulators won’t take action against them. 

For fun, and to also aid the Phoenix Investment Team in their price comparison research of budget airlines, I've decided to try and scrape the website myself, and in doing so, understand why Ryanair data is so vulnerable.

**How does the code function?**

The code presented here allows users to input any set of flight paths and it returns the prices for two weeks, one month and four months in advance. 

I managed to acheive this by locating the Ryanair API call path in the companies HTML code. This API call has a standard structure, with certain consistencies for origin, destination, date, seating and so forth. By modifying the API call, and looping the process, the data for a large volume of flights can then be returned by understanding the structure of the returned API data.

**For price comparison research...**

Please input the 3 digit airport codes for each flight path of interest into the flight_dict variable. You can add as many as desired and the price for a flight on each path at three different time intervals (two weeks, one month and four months in advance) will be returned.
