import readline
def rlinput(prompt, prefill=''):
  readline.set_startup_hook(lambda: readline.insert_text(prefill))
  try:
      return input(prompt)  # or raw_input in Python 2
  finally:
      readline.set_startup_hook()
inpu = rlinput("","daniel")
print(inpu)