# Kenya Delivers

Kenya Delivers is a web application platform for Kenyan Government websites.

We are a safe space for Kenyan citizens to access their government services online, tenders and keep track of their politicians's performance to
enable better voting .

## Technology

We're building the web platform using Python's Django web framework.

### Contributors

1. Fredrick Adhing'a
2. Samuel Mwangi

## Issues':'

## (a)

 Runing migrations

## Error =>

 `django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency account.0001_initial on database 'default'.`

## Reason =>

 This happened after addition of a custom User model, per the recommendation in the django docs.

## Soln =>

  1. Delete the database db.sqlite3
  2. Delete the app/migrations folder
  3. temporarily comment out `django.contrib.admin.`

        ```py
        INSTALLED_APPS = [
        ...
        #‘django.contrib.admin’,
        ...
        ]
        ```

     Also comment out the admin site in urls.py:

        ```py
        urlpatterns = [
            path('profile/', include('restapp.urls')),
            #path('admin/', admin.site.urls),
        ]

        ```

  4. Now go ahead and run:

     ```bash
     py manage.py makemigrations 
     ```

     then

     ```bash
     py manage.py migrate
     ```

  5. Now U can uncomment all of the above  

# (b)

## creating superuser or running server

## Error =>

 `django.db.utils.OperationalError: no such table: service_user`

## Reason =>

   Who cares....

## Soln =>

   run

   ```bash
   py manage.py migrate --run-syncdb
   ```
