# Pokémoney Spending Tracker

This was a solo project, completed in week 4 of the Professional Software Development course at CodeClan.

It makes use of (including reference links):
* Python
* [Flask web framework](https://flask.palletsprojects.com/en/2.0.x/)
* [Jinja2 in Flask](https://flask.palletsprojects.com/en/2.0.x/templating/)
* [PostgreSQL database](https://www.postgresql.org/)
* RESTful routes
* HTML / CSS
* unittest for unit testing
* pdb for breakpoint testing


Usage
------
The app allows a user to set a budget, add spending types/merchants and add transactions.  This met the MVP of our brief.
Additional functionailty was added for sorting transactions by amount and by date, as well as a feature that gives a visual reminder when spending is close to or has exceeded the set budget.
The intended user is a Pokémon traniner, just to keep it a bit more interesting 😄

Ideally I would go back in to refactor some of the code, for example in the repositories/limit_repository.py file, where the spending limit is added to the database and then the most recent db entry is used in rendering the template (templates/transactions/index.html) - it would have been cleaner to clear the spending limit table before adding a new spending limit, as there is only ever a need for one spending limit and no need for historic information in this context. 


How to run
------
1. Install Python if you don't already have it.  You can get it from here: https://www.python.org/downloads/

2. In the terminal, install Flask:
```pip3 install Flask```

3. Whilst in the app's directory, run:
```flask run```





