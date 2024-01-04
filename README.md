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
