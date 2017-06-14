# Fuzzy Job Application
Using fuzzy logic

## About
How about using fuzzy logic to know which of you applicants have qualified more for the post??
This alpha project uses fuzzy logic to determine who qualifies more for a job vacancy post.

### Requirements
python 3.6.1

## Installation
``` bash
cd <working dir>
git clone https://github.com/craftsmon/fuzzy-job-application.git fuzzy

python -m venv fuzzy-venv
source fuzzy-venv/bin/activate

cd fuzzy
pip install -r requirements.txt

export FLASK_APP=run.py
export FLASK_CONFIG=development

```

This is the basic setup for the flask application.


Next we create our mysql models.
Fire up the mysql server

``` bash
sudo service mysql start

flask db upgrade
```
Running the above command should be successful without any errors.
After this we can then run our web app.

``` bash
flask run
```

This should run on the default port 5000 and can open it on your browser at [localhost](localhost:5000)
It is required that your python installation be prior configured with tkinter otherwise the app wont run.

The app uses [scikit-fuzzy](http://pythonhosted.org/scikit-fuzzy) which has a dependency on matplotlib to generate graph views. This uses tkinter.

If this is not the case then you will have to run

``` bash
sudo apt-get install tk python3-tk tk8.6-dev
```

Then run make for your python version to configure it with __tkinter_
