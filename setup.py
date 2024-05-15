import re

# File paths
proto_in_path = "./open-simulation-interface/osi_version.proto.in"
version_path = "./open-simulation-interface/VERSION"
proto_out_path = "./open-simulation-interface/osi_version.proto"

# Read the version from the VERSION file
with open(version_path, "r") as version_file:
    version_content = version_file.read()

# Extract the version numbers
version_major = re.search(r'VERSION_MAJOR\s*=\s*(\d+)', version_content).group(1)
version_minor = re.search(r'VERSION_MINOR\s*=\s*(\d+)', version_content).group(1)
version_patch = re.search(r'VERSION_PATCH\s*=\s*(\d+)', version_content).group(1)

# Read the content of the osi_version.proto.in file
with open(proto_in_path, "r") as proto_in_file:
    proto_in_content = proto_in_file.read()

# Replace the placeholders in the proto.in file with the version information
proto_out_content = proto_in_content.replace("@VERSION_MAJOR@", version_major)
proto_out_content = proto_out_content.replace("@VERSION_MINOR@", version_minor)
proto_out_content = proto_out_content.replace("@VERSION_PATCH@", version_patch)

# Write the updated content to the osi_version.proto file
with open(proto_out_path, "w") as proto_out_file:
    proto_out_file.write(proto_out_content)

proto_out_content
