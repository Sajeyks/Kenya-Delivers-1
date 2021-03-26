# Kenya Delivers

Django web app

This web application Is the government online safe space to access government authentic websites online.

Kenya Delivers is a platform that brings not only Kenyan government websites in one space, but also provides tender opportunities for Kenyan citizens
and lets them keep track of how their politicians are performing.



### Developers
1. Fredrick Adhing'a
2. Samuel Mwangi



# Issues:

 # (a)
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




  # (b):

 ## creating superuser or running server
   
## Error =>

 `django.db.utils.OperationalError: no such table: service_user `

## Reason =>
   Who cares....

## Soln =>
   run 
   ```bash
   py manage.py migrate --run-syncdb
   ```
   

