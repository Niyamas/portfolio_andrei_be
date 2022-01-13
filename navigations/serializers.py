from rest_framework.serializers import ChoiceField


class TypeChoiceSerializer(ChoiceField):
  """
  See: https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
  """
  def to_representation(self, value):
    if value == '' and self.allow_blank:
      return value
    return self._choices[value]

  def to_internal_value(self, data):
    # To support inserts with the value
    if data == '' and self.allow_blank:
        return ''

    for key, val in self._choices.items():
        if val == data:
            return int(key)
    self.fail('invalid_choice', input=data)