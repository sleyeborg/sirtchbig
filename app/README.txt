open app.py to run program. 


specify is returning urls like this:"'/url?q=https://www.amazon.com/Caribou-Coffee-Balanced-Indonesia-Sustainable/dp/B01FTE4NEU&sa=U&ved=2ahUKEwjD3u7Czbb_AhUSGVkFHfZrBaIQqoUBegQIBxAB&usg=AOvVaw1calI3z-AmTxWHJbcy36eQ',
" the key is that "https://www.amazon.com/Caribou-Coffee-Balanced-Indonesia-Sustainable/dp/B01FTE4NEU" is valid and the rest is not. "&sa" is the point you want to trim off everything to the right of. 



TODO:
write a program suite: 
	scrapeFor
		scrapeForA
		scrapeForContact
		scrapeForProduct
		scrapeForTerm

	SCRAPE FOR NEWS
	SCRAPE FOR PRODUCT
	SCRAPE FOR SOCIAL
	SCRAPE FOR CONTACT
	SCRAPE FOR MUSIC? 


BUGS:
*input nothing into the search bar and run functionC will crash the server