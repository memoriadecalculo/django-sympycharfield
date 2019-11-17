from django.db import models
from sympy.core.numbers import Integer
from sympy.core.symbol import Symbol
from sympy.core.expr import Expr
import sympy.physics.units as u
from sympy import sympify, Basic

# Create your models here.
# https://docs.djangoproject.com/en/1.9/howto/custom-model-fields/
# https://stackoverflow.com/questions/15895819/how-to-parse-and-simplify-a-string-like-3cm-%C2%B5s%C2%B2-4e-4-sqmiles-km-h2-treatin
def str2sympy(sympy_str):
    """Convert string to Sympy object."""
    
    subs = {} 
    for k, v in u.__dict__.items(): 
        if (isinstance(v, Expr) and v.has(u.Unit)) or isinstance(v, Integer): 
            subs[Symbol(k)] = v
    return sympify(sympy_str).subs(subs)

class SympyCharField(models.CharField):
    description = "Sympy Char Field"
    
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return str2sympy(value)
    
    def to_python(self, value):
        if isinstance(value, Basic) or value is None:
            return value
        return str2sympy(value)
    
    def get_prep_value(self, value):
        return str(value)
    
    def clean(self, value, model_instance):
        value = self.to_python(value)
        self.validate(value, model_instance)
        self.run_validators(str(value))
        return value

class SympyCharFieldTest(models.Model):
    formula = SympyCharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.formula)