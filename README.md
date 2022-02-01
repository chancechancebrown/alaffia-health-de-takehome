# Alaffia Health Data Engineering Takehome
> This flask application takes posts requests of cryptocurrency names and outputs the available markets to a file at ./data/coin_markets.json
## Running the app

You may either run start_flask_app.sh after changing execution permissions (chmod a+rx) via
```
chmod a+rx start_flask_app.sh
./start_flask_app.sh
```

Or you can run the commands manually:
```
mkdir ./data
docker build -t coin-app .
docker run -d -v $PWD/data:/src/data -p 3000:3333 coin-app
```

## Querying the data

The output data from the application is contained within the data directory. 

The expected output data is *slightly* different than originally requested for ease of processing. 

coin_markets.json has the following format:

```json 
{coin_id: {'id': coin_name, 'exchanges': list[exchanges], 'task_run': task_run_id}}
```
