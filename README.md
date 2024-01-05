# Background
Follow [Channels Tutorial](https://channels.readthedocs.io/en/latest/tutorial/index.html) to create commits. It's convenience to see what difference in every steps.

# Steps
1. install django: `python3 -m pip install django`
2. install channels, daphne: `python3 -m pip install -U 'channels[daphne]'`
3. start the project: `django-admin startproject mysite`
4. start app: `python3 manage.py startapp chat`
5. removing unnecessary files in chat app
6. Add 'chat' in INSTALLED_APPS
7. Add templates/chat/index.html
8. Add chat/urls.py
9. point the root URLconf at the chat.urls module
10. Integrate the Channels library
11. Add the room view
12. Write your first consumer
13. Enable a channel layer
	1. `docker run --rm -p 6379:6379 redis:7`
	2. `python3 -m pip install channels_redis`
	3. Edit mysite/settings.py
14. Edit chat/consumers.py
15. Rewrite the consumer to be asynchronous
16. install selenium: `python3 -m pip install selenium`
17. Create chat/tests.py
18. Edit mysite/settings.py
19. Run test: `python3 manage.py test chat.tests`, please make sure the redis service is started before.

# websocat
1. Download [websocat](https://github.com/vi/websocat)
2. runworker: `python3 manage.py runworker`
3. runserver: 'python manage.py runserver`
4. send message: `echo '{"message": "hello"}' | ./websocat ws://127.0.0.1:8000/ws/chat/lobby/`
5. receive message: `./websocat ws://127.0.0.1:8000/ws/chat/lobby/`
