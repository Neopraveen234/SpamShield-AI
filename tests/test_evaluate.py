import subprocess

print("="*50)
print("MODEL EVALUATE TEST")
print("="*50)

result=subprocess.run(
    ['python','src/evaluate.py'],
    text=True,
    capture_output=True
)

print(result.stdout)

if result.stderr:
    print(result.stderr)

print("="*50)
print("MODEL EVALUATE TEST")
print("="*50)