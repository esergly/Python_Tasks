# Work with files
# Open the file as read-only
with open("workData.txt", "r") as work_data:
    work_data_contents = work_data.readlines()

work_data_contents.insert(1, "This goes between line 1 and 2\n")

# Re-open in write-only format to overwrite old file
with open("workData.txt", "w") as work_data:
    work_dataContents = "".join(work_data_contents)
    work_data.write(str(work_dataContents))

with open("workData.txt", "r") as work_data:
    for line in work_data:
        print(line)
