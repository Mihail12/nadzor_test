# nadzor_test

I have spend 2 hours 40 mins for the task hope it done well

to start please clone the project  
than type next commands   
``cd nadzor_test``  

``pip install -r ../requirements.txt``

``python manage.py migrate``

``python manage.py createsuperuser`` (and provide admin credentials)

``python manage.py runserver``

visit the url http://localhost:8000/admin/  

here you could log in and took ``sessionid`` ``csrftoken`` from browser's cookie 
to use it for example in Postman(you should provide ``sessionid`` ``csrftoken`` to Postman cookies and add to HEADERS X-CSRFTOKEN=``csrftoken``)

then you could test the app on:
http://localhost:8000/block_requests/ (public url for users) (fields ['email', 'domain_or_ip', 'description'])
http://localhost:8000/block_requests/<id>/ (url for admins to approve or not the changes) (fields ['approve'])
http://localhost:8000/block_site/ (url for admins to add websites) (fields ['domain_or_ip'])


to view data you could look at http://localhost:8000/admin/

Thanks `:)`
