import os
import argparse
from itertools import islice

parser = argparse.ArgumentParser("mbth2qlq")
# TODO automate this argument, and make this obsolete
parser.add_argument("delimiter",
                    help="Whether the tags are delimited by spaces or tabs.",
                    type=str,
                    choices=['tabs', 'spaces'])
parser.add_argument("file", help="The tag hierarchy file. Must be .txt", type=str)
parser.add_argument("tag", help="The tag you want to retrieve.", type=str)

args = parser.parse_args()

# Check if it ends with .txt (MusicBee tag hierarchies tend to be)
if args.file.lower().endswith(".txt"):
    if os.path.exists(args.file) and os.access(args.file, os.R_OK):
        # Try opening the file.
        try:
            with open(args.file, 'r') as file:
                # Make it processable by the script.
                hierarchy = file.read().splitlines()
                loop_input = args.tag.lower()
                tries = 0
                try_limit = 30

                # Increase try limit if spaces are used.
                if args.delimiter == "spaces":
                    try_limit = 60

                while tries != try_limit:
                    try:
                        # Find the input the user is looking for in the hierarchy.
                        index = [tag.lower() for tag in hierarchy].index(loop_input)
                        found_tag = hierarchy[index]
                        query_num_tabs = len(found_tag) - len(found_tag.lstrip())

                        # Grab all of the tags the user wants.
                        tags = []
                        for tag_entry in islice(hierarchy, index+1, None):
                            te_num_tabs = len(tag_entry) - len(tag_entry.lstrip())
                            if te_num_tabs == query_num_tabs:
                                break
                            else:
                                if "::" in tag_entry:
                                    tags.append(tag_entry.lstrip())

                        # Convert the selected tags to something QL can read.
                        for i, tag in enumerate(tags):
                            query_input = tag.rsplit("::", 1)
                            tags[i] = f'{query_input[1]}="{query_input[0]}"'

                        # Spit out the finalised query.
                        print(f"|({','.join(tags)})")

                        break
                    except ValueError:
                        tries += 1
                        if tries == try_limit:
                            print("Error: cannot find tag with children. make sure everything is correct and you're not going for anything actually marked as a tag")
                            quit()
                        else:
                            # prepend the loop input with a tab or space.
                            if args.delimiter == "tabs":
                                loop_input = "\t" + loop_input
                            else:
                                loop_input = " " + loop_input
        except IOError:
            print("Error: Unable to read the specified file")
    else:
        print("Error: The file doesn't exist or is not readable")
else:
    print("Error: not a txt file.")
