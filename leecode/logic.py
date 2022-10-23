for p in range(2):
  for q in range(2):
    for r in range(2):
      print(f"p={p},q={q},r={r}")
      print(f"assumption: p and q = {p and q}, r = {r}")
      print(f"conclusion: q and r = {q and r}")
      print("---------------------------------------")