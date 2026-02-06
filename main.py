import time
from run_task1 import run

if __name__ == "__main__":
    print("Starting causal analysis service...")

    # Run analysis once
    results = run()
    for r in results:
        print(r)

    # Keep the service alive (Render requires this)
    while True:
        time.sleep(60)
