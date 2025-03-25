import os

# Read the template
with open("template.html", "r") as f:
    template = f.read()

# Save the generated example
os.makedirs("examples", exist_ok=True)
with open("examples/example.html", "w") as f:
    f.write(template)

print("Generated example.html from template.html")
