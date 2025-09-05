import subprocess
import time

def main():
  tryies = 0
  while tryies < 3:
    print(f"Attempts {tryies + 1} ...")
    result = subprocess.run(["ssh", "dev2@jump-server"])

    if result.returncode == 0:
      print("connected.")
      return 0
    else:
      print("Failed! Try again in 5 second ...")
      tryies += 1
      time.sleep(5)

  print("Failed to connect to jump server!")

if __name__ == "__main__":
  main()