# practice dashboard

...
## How to Run
First, you need to install dependencies. You can do this by running the following command:

```sh
pip install -r requirements.txt
```

then, run the following command to start the export environment variables in the main repo directory:

```sh
source .env
```

Run `export PYTHONPATH=${PWD}` to add the current working directory to the python path

Build django migrations by running the following command:

```sh
python src/manage.py makemigrations
python src/manage.py migrate
```

Finally, you can run the dashboard by running the following command:

```sh
streamlit run src/app.py
```