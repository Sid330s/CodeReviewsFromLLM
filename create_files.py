import os

# Define the input file and output directory
input_file = 'leetcode.txt'
output_dir = 'solution'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read URLs from file
with open(input_file, 'r') as f:
    urls = f.readlines()

# Process each URL
for url in urls:
    url = url.strip()
    if not url:
        continue
    # Extract the problem slug from the URL
    try:
        slug = url.rstrip('/').split('/')[-1]
        filename = f"{slug}.cpp"
        filepath = os.path.join(output_dir, filename)

        # Create the file only if it doesn't exist
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(f"// Solution for {slug}\n")
            print(f"Created: {filepath}")
        else:
            print(f"Exists: {filepath}")
    except IndexError:
        print(f"Skipped malformed URL: {url}")
