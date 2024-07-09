
from django import template

register = template.Library()  # Get the template tag library

@register.filter
def url_by_pipe(value):
  """Splits a string by pipe ("|") and returns a string.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  try:
    url=value.split("|")[0]
  except:
    url=value    
  return value.split("|")[0]

@register.filter
def title_by_pipe(value):
  """Splits a string by pipe ("|") and returns a string.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  try:
    title = value.split("|")[1]
  except:
    title = value
  return title

@register.filter
def split_by_double_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("||")

@register.filter
def split_by_pipe(value):
  """Splits a string by pipe ("|") and returns a list.

  Args:
      value: The string to split.

  Returns:
      A list containing the substrings separated by pipes.
  """
  return value.split("||")