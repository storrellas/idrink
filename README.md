# idrink


## Requirements

1. User walks up to machine and selects drink from UI. The UI will need to pull the drinks and ingredients from a local database as well as a remote API. If a drink is chosen and not in the local DB, then we should save the newly requested drink to the database.
2. User selects size of drink
3. Machine then starts issuing MQTT messages to the local broker
   - Messages are meant to signal to another device that can control 24v relays. The message topic would look something like this: device/drinkID/timeInSecondsToActivateRelay. There can be any number of devices and drinks. The time to run each relay is a proportion to the size the user selected. The DB should hold the recipes.
4. The remote devices would then send a message back as they complete activation of the relays
5. UI shows the user that the drink is complete and returns to the main screen

## Design

### Architecture

The design of the Drink Management System would be as follows:

![alt text](https://user-images.githubusercontent.com/3708141/40468179-e8cf0018-5f2c-11e8-8d67-91110ea9cfee.png)

DrinkUI provides the WebInterface for the user. My proposal is that it will be generated by using DjangoTemplates together with Bootstrap+Angular/JQuery
DrinkAPI refers to public API for controlling the drink machine using library paho-mqtt client (https://pypi.org/project/paho-mqtt/)
PostgresSQL corresponds to database storing information about ingredients and drinks
LocalBroker is the entity receiving messages from DrinkAPI to control drink machine

```
@startuml

title iDrink

rectangle DrinkUI
rectangle DrinkAPI
rectangle LocalBroker

database PostgreSQL {
    rectangle Drink
    rectangle Ingredient
}

DrinkUI -down-> DrinkAPI
DrinkAPI -down-> LocalBroker : MQTT
DrinkAPI -down-> PostgreSQL

@enduml
```

### Interaction Diagram: Drink Request

Here below the interaction between actors when requesting a new drink:

![alt text](https://user-images.githubusercontent.com/3708141/40468168-e1fa9e28-5f2c-11e8-9a88-5a02538fe81d.png)

```
@startuml

title Drink Request

DrinkUI -> DrinkAPI : Drink Request
DrinkUI -> DrinkAPI : Is finished drink?

note right: Polling continuouly for finished drink
activate DrinkAPI

DrinkAPI -> LocalBroker : MQTT
LocalBroker -> DrinkAPI : DrinkFinished

DrinkAPI -> DrinkUI : DrinkFinished
deactivate DrinkAPI

@enduml
```

### MQTT

MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium. For example, it has been used in sensors communicating to a broker via satellite link, over occasional dial-up connections with healthcare providers, and in a range of home automation and small device scenarios. It is also ideal for mobile applications because of its small size, low power usage, minimised data packets, and efficient distribution of information to one or many receivers.

![alt text](https://user-images.githubusercontent.com/3708141/40468176-e8592528-5f2c-11e8-9d47-dc6c92cc8906.png)

All the pump controllers are controlled by a PumpController device which are subscribed to a specific MQTT topics that control what specific pump to enable and for how long. From the DrinkAPI perspective, it will be necessary to have a python-based client to communicate with the MQTT broker that will ultimately relay the message to the PumpController. The client used to send messages to the MQTT local broker will be the python library
https://pypi.org/project/paho-mqtt/.

![alt text](https://user-images.githubusercontent.com/3708141/40468180-e8fa423c-5f2c-11e8-8dc2-1d2657f173c2.jpg)

```
@startuml

title iDrink

frame MQTTBroker
rectangle DrinkAPI
rectangle PumpController1
rectangle Pump11
rectangle Pump12
rectangle PumpController2
rectangle Pump21
rectangle Pump22
rectangle Pump23

DrinkAPI -left-> MQTTBroker : publishes

MQTTBroker -down-> PumpController1 : subscribes
MQTTBroker -down-> PumpController2 : subscribes

PumpController1 -down-> Pump11
PumpController1 -down-> Pump12

PumpController2 -down-> Pump21
PumpController2 -down-> Pump22
PumpController2 -down-> Pump23

@enduml
```

DrinkAPI will issuing the topic MQTT to the local broker in the following form:

/drinkmachine/$PiNumber/$PumpNumber/$TimeInSeconds
$PiNumber indicates the specific PumpController device
$PumpNumber corresponds to the specific Pump within the PumpController
$TimeInSeconds is the time in seconds to activate the Pump and is based on proportion from recipe

## UI

You can download the envisaged HTML template from [here](https://github.com/storrellas/idrink/files/2034068/UI-HTML.zip)

![alt text](https://user-images.githubusercontent.com/3708141/40468177-e8774738-5f2c-11e8-8740-2552d2535a01.jpg)

![alt text](https://user-images.githubusercontent.com/3708141/40468178-e8929f10-5f2c-11e8-93f6-2b8230655ad1.jpg)

- Main menu
  - Home Button redirects to home page (the current page)
  - Shot Button
  - Search Button opens up a dialog to start an already done drink
- Admin button allows user to login admin page
- Drink tile displays the latest 6 drinks requested by users
Wireframes
https://wireframepro.mockflow.com/view/idrink

## Deployment

apt-get install mosquitto
git clone https://github.com/claughinghouse/idrink.git
cd idrink
-- Only if virtualenv required --
python -v venv ./venv3/
source ./venv3/bin/activate
-- Only if virtualenv required --
pip install -r requirements3_sqlite.txt
python manage.py makemigrations combiner
python manage.py migrate
python manage.py loaddata drinks ingredients
python /repo/pump_controller.py & python /repo/manage.py runserver 0.0.0.0:80

## References

https://github.com/claughinghouse/drink-machine/blob/master/Requirements.md
