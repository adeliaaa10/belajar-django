from django import template 

#buat variabel 
register = template_Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This function will cut out all values of "arg" from the string 
    """

    # replace adalah build method nya 
    return value.replace(arg, '')

# register.filter('cut', cut)

    