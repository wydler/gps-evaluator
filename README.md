GPS Evaluator
=============

# Display position on Google Maps

## Start webserver (linux only!)

First you need to start a webserver. The included script starts a small php server, which is included in the php5 package. **USE THIS ONLY FOR DEVELOPMENT**

`./start_server.sh`

The script will start a webserver for localhost (127.0.0.1) on port 8000. Now you can open the url

`http://localhost:8000`

and you should see a map.

#### Possible problems:
You may need to install php on your machine. This can be done with the command

`sudo apt-get install php5`

### Why do I need a webserver?
The `index.html` uses AJAX (XMLHttpRequest) to read the json-file. Without the webserver this will not work!

## Start dummy gps position generator

This program generates 2 different positions and save as json-file into the specified file. At the moment, the json-file must saved in the www directory and filename `data.json`.

`../server/build/dummy_gps_generator data.json` (assuming you are in the `www` directory)

The first argument must be the name of the json-file.