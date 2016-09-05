# Flask Boiler


Flask starter project for rapid development using **Vagrant**.


## Quick Start

### Basics

1. Install Vagrant if not already.
1. Clone project.
2. Configure bootstrap.sh if needed.
3. Initialize the environment by running ```vagrant up```
4. SSH into vagrant and follow the below instructions.

### Set Environment Variables Within Vagrant Machine

Update ```project/server/config.py```, and then run:

#Option A (Fabfile)
```
# For development
$ fab set_dev
$ fab create_db
$ fab rs

#For production
$ fab set_prod
$ fab create_db
$ fab rs
```




#Option B (Manual)

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
