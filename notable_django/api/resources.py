# api/resources.py

from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization = Authorization()
        fields = ['title', 'body']

# curl -X POST -H "Content-Type: application/json" -d '{"title": "My Second Note", "body": "This is the body for second note"}' http://localhost:8000/api/note/