import subprocess
import os

def download():
    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Read the download links and titles
    with open("download_links.txt", "r") as links_file, open("titles.txt", "r") as titles_file:
        download_links = links_file.readlines()
        titles = titles_file.readlines()

    # Ensure the number of links and titles match
    if len(download_links) != len(titles):
        print("Error: The number of download links and titles do not match.")
        exit(1)

    index = 0
    # Loop through each link and title to download files
    for link, title in zip(download_links, titles):
        index = index + 1
        link = link.strip()  # Remove whitespace/newline characters
        title = title.strip()  # Remove whitespace/newline characters

        # Prepare the output filename
        output_file = os.path.join(output_dir, title + ".mp4")  # Assuming mp4 format

        # Prepare the wget command
        wget_command = ["wget", link, "-O", output_file]

        try:
            print(f"({index} / {len(download_links)})")
            # Run the wget command
            subprocess.run(wget_command, check=True)
            print(f"Downloaded '{title}' to '{output_file}'")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while downloading '{title}': {e}")
