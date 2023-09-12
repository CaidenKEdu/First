def Fact(n):
  if n > 0:
    return n*Fact(n-1)
  else:
    return 1

def main():
  for i in range(10):
    print(f"{i}:\t{Fact(i)}")

if __name__ == "__main__":
  main()