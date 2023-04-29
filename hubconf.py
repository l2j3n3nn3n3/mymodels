dependencies=['torch','math']
def some_entry_fn(*args,**kargs):
  model=build_some_model(*args,**kargs)
  return model
def another_entry_fn(*args,**kargs):
  model=build_another_model(*args,**kargs)
  return model
