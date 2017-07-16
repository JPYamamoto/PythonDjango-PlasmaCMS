# Plasma CMS

> A simple content management system for blogging, powered by Django. Template included with material design and responsiveness.

## Getting Started

Follow these notes in order to have a copy of this project working. If deploying for production, remember to read the deployment section.

### Requirements

* Python 3.x
* Django 1.11.x
* [Database backend supported by Django](https://docs.djangoproject.com/en/1.11/ref/databases/)
* Pillow Library

**Note:** This project was developed and tested using Python 3.5.2 and Django 1.11.2. I assume no responsibility for problems if used with different versions.

### Installing

Instructions to build a development env with Django 1.11 and MySQL database. Some commands may require to be prefixed with `sudo` in specific systems.

#### Env

Install virtualenv for Python 3.

```shell
pip install virtualenv
```

Set up a virtual environment.

```shell
virtualenv -p python3 plasmacms
```

Activate the virtualenv.

```shell
source path/to/virtualenv/folder/bin/activate
```

#### Dependencies

Install Django.

```shell
pip install django=1.11
```

Install MySQL client.

```shell
pip install mysqlclient
```

Install Pillow.

```shell
pip install Pillow
```

#### Download and run

Clone this project.

```shell
git clone https://github.com/JPYamamoto/plasma-cms
```

Edit the database information in the file `plasma_cms/settings.py` according to your database's settings.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB NAME',
        'USER': 'DB USER',
        'PASSWORD': 'DB PASSWORD',
        'HOST': 'DB HOST',
        'PORT': 'DB PORT'
    }
}
```

Add a secret key for your Django project. You can create one in the [Online Django Secret Key Generator](http://www.miniwebtool.com/django-secret-key-generator/).

```python
SECRET_KEY: 'YOUR SECRET KEY'
```

Make migrations.

```shell
python manage.py makemigrations
python manage.py migrate
```

Run server.

```shell
python manage.py runserver
```

## Deployment

If this code will be run for production, remember to do the following:

* Set `Debug = False` in plasma_cms/settings.py
* Run `python manage.py collectstatic` to correctly serve static files.
* It is highly recommended to use a virtualev (both in development and in production)


## Built With

### Engine

* [Python 3.5](https://www.python.org/) - Programming Language.
* [Django 1.11](https://www.djangoproject.com/) - Web Framework.
* [Pillow](https://python-pillow.org/) - Library for working with images.

### Template

* [MaterializeCSS](http://materializecss.com/) - Responsive Front End Framework.
* [jQuery](https://jquery.com/) - Javascript library for DOM manipulation.
* [Material Design Icons](https://material.io/icons/) - Icons toolkit.
* [FontAwesome](http://fontawesome.io/) - Icons toolkit.
* [Medium Editor](https://yabwe.github.io/medium-editor/) - WYSIWYG editor.
    * [Medium Editor Insert Plugin](http://linkesch.com/medium-editor-insert-plugin/) - Plugin to add images and videos.

## Release History

* 1.0.0
    * First stable release.

## Contributing

1. Fork it (<https://github.com/JPYamamoto/plasma-cms>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Author and Contributors

* **Juan Pablo Yamamoto** - *First Release* - [JPYamamoto](https://github.com/JPYamamoto) - [Website](http://jpyamamoto.com/)

Make a contribution and your name will be listed here.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
