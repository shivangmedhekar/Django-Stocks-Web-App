# Django Stocks Web App

The Stocks Web App which lets it's users to search for a information of stock by using the ticker of the company. The user's can add the stock to the add stock page to keep a track of it and also delete it. The stock information is fetched from IEX Cloud API.

![](screenshots/add%20stocks.png)



## Requirements
- Python 3.x

You can download Python [here](https://www.python.org/downloads/).

- Django 3.x

You can download Django [here](https://www.djangoproject.com/download/).

- IEX Cloud Account

You can visit their website [here](https://iexcloud.io/).

## Usage:

You should start cloning this repository:

    $ git clone https://github.com/shivangmedhekar/Django-Stocks-Web-App.git

After downloading the repository, you have to go quotes folder

    $ cd stocks/quotes
    
In this folder you have to create a config_api.py file and create a variable **api_key** and assign your key in string format.

 `config_api.py` file:
 
    # Your API Key should be inside the double quotes.
    api_key = ""
    
After that you should make migrations and migrate.

    $ python manage.py makemigrations
    $ python manage.py migrate
    
then you must run **manage.py** script with **python** like this:

    $ python manage.py runserver
    
After the server is up and running go to the web url provided by Django to view the web app in any broswer.
    

## Web App by
|  **Shivang Medhekar** |
| :---: |
| [![Shivang Medhekar](https://avatars2.githubusercontent.com/u/69140290?s=200&u=5df35a82b6d2b6b7b876dfdc22d451c92d30a5c6&v=4)](https://github.com/shivangmedhekar) | 
| <a href="https://github.com/shivangmedhekar" target="_blank">`github.com/shivangmedhekar`</a>| 



## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
