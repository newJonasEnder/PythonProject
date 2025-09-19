from django.db import models, connection

from django.core.exceptions import FieldError

class PrefixSuffixCharField(models.CharField):
    def __init__(self, *args, sequence_name=None, prefixes=None, suffixes=None, **kwargs):
        if sequence_name:
            if isinstance(sequence_name, str):
                self.sequence_name = sequence_name
            else:
                raise TypeError("'sequence_name' must be a string")
        else:
            raise FieldError("Missing argument 'sequence_name'")
        if prefixes:
            if isinstance(prefixes, list):
                self.prefixes = prefixes
            else:
                raise TypeError("'prefixes' must be a list")
        else:
            self.prefixes = []
        if suffixes:
            if isinstance(suffixes, list):
                self.suffixes = suffixes
            else:
                raise TypeError("'suffixes' must be a list")
        else:
            self.suffixes = []
        kwargs["unique"] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['sequence_name'] = self.sequence_name
        kwargs["prefixes"] = self.prefixes
        kwargs["suffixes"] = self.suffixes
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if add and not value:
            next_sequence_value = self.get_next_sequence_value()
            next_sequence_value = str(next_sequence_value)
            next_sequence_value = [next_sequence_value]
            value = self.prefixes + next_sequence_value + self.suffixes
            value = "-".join(value)
            setattr(model_instance, self.attname, value)
        return value

    def get_next_sequence_value(self):
        with connection.cursor() as cursor:
            query = "SELECT NEXTVAL(%s)"
            cursor.execute(query, [self.sequence_name])
            row = cursor.fetchone()
            next_sequence_value = row[0]
        return next_sequence_value
