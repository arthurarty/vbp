# vbp

[![Build Status](https://travis-ci.org/arthurarty/vbp.svg?branch=dev)](https://travis-ci.org/arthurarty/vbp)
[![Maintainability](https://api.codeclimate.com/v1/badges/eb666174c418a0ba0d23/maintainability)](https://codeclimate.com/github/arthurarty/vbp/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/arthurarty/vbp/badge.svg?branch=dev)](https://coveralls.io/github/arthurarty/vbp?branch=dev)

## Description

Application is built in Django using Django forms and templates. The aim is to build a system that can be used to manage a savings/investment club.

## How to set up

- Create a postgres database.
- Clone the repo.
- Ensure you are on the dev branch.
- Activate your virtualenv.
- Install requirements using the command `pip install -r requirements.txt`.
- Create a `.env` file from the `.env_example`.
- Run migrations using the command `python manage.py migrate`.
- Check to ensure everything is okay using the command. `python manage.py check`.
- If all is well run the application using the command. `python manage.py runserver`.
- Visit the url `127.0.0.1/signup/`.

## Built With

- `Django` : [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. .
- `Travis`: [Travis CI](https://travis-ci.org/) is hosted continuous integration service used to build and test software projects hosted at GitHub.
- `Virtualenv` : [Virtualenv](https://virtualenv.pypa.io/en/stable/) is a tool to create isolated Python environments.
- `AfricaIsTalking` : [AfricaIsTalking](https://africastalking.com/) - API used to send sms for phone_number verification.

## Authors

- **Nangai Arthur** - [Linkedin](www.linkedin.com/in/arthur-nangai)
