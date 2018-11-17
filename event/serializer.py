from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=('title', 'description')

def validate_title(self, attrs, source):
    value = attrs[source]
    if "django" not in value.lower():
            raise serializers.ValidationError("Event post is not about Django")
    return attrs
