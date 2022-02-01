# Alaffia Health Data Engineering Takehome

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
