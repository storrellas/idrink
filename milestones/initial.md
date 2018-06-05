## Main page

* [ ] Presents different choices for drinks
  * [x] Has 2 rows of 3 drinks
  * [x] Has button to make a shot
  * [x] Has the name of the drink below the picture on row
  * [x] Has list of ingredients for each as a comma seperated list without quantities
* [x] Has logo at the top left of the screen
* [x] Has admin button at top right
* [ ] Has Search bar at top
  * [ ] Search searches local db first and then remote based on user query
  * [ ] Local db is MySQL or SQLite
  * [ ] ~~Remote API docs can be seen here: [addb](https://addb.absolutdrinks.com/docs/)~~
* [ ] User login
  * Not part of this requirements set - ##TODO##
* [x] When User selects drink they are prompted for the size of drink
  * [ ] Size multiplies ingredients to match cup size and alters MQTT messages accordingly by altering `$TimeInSeconds`
* [x] Has `Make` button to start the pumps and make the drink
* [ ] Shows animation that drink is being made
* [ ] Returns to main screen when finished making drink
  
## Admin Page - Behind Admin Button

* [ ] Allows assignment of pump to topic
  * Topic is the format ($ = variable name): `/drinkmachine/$PiNumber/$PumpNumber/`
  * `$PiNumber` maps to the Pi number
  * `$PumpNumber` maps to a GPIO Pin on the Pi
  * `$TimeInSeconds` is the time in seconds to activate GPIO Pin as part of the MQTT message
    * `$TimeInSeconds` is based on proportion from recipe
  
* [ ] Allows the addition of an ingredient
  * [ ] Stores the ingredient in the database

* [ ] Allows the addition of an recipe to be added to local db
  * [ ] Recipes are proportion based
    * i.e. `1 part this, 2 parts that, 1 part etc.`
  * [ ] Recipe can have unlimited ingredients
  * [ ] Recipe can have picture
    * [ ] ~~If picture is avaliable from [addb](https://addb.absolutdrinks.com/docs/) then it is stored and presented to the user when on the main screen~~
 
* [ ] Allows configuration of API access
  * [ ] API access will be to retreive drinks and store in database
    * Only stores the drink if it has not been ordered before
    * Retreives from local DB first

* [ ] Allows configuraiton of User access
  * [ ] User can use PIN number
  * [ ] User has assigned credits
    * [ ] Each drink or shot has a credit value
    * [ ] Machine deducts credit(s) from each order

* [ ] Allows configuration of `$TimeInSeconds` in seconds for a given proportion

* [ ] All actions of the app are logged