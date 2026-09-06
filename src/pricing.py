def compute_total(items):
  total = 0
  for item in items:
    if item.active:
      total += item.price
  return total
