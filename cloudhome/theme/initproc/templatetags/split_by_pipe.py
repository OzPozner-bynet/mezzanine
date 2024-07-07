from django import template

register = template.Library()

@register.filter
def split_by_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("|")

@register.filter
def split_by_double_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("||")
