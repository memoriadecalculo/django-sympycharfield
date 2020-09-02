from django.db import models

from sympycharfield.fields import SympyCharField

class SympyCharFieldTest(models.Model):
    formula = SympyCharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.formula)