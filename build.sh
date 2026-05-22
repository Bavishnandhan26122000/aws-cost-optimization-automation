#!/bin/bash
set -e

mkdir -p build

echo "Packaging Stop EC2 instances function..."
zip -j build/stop_ec2_instances.zip src/stop_ec2_instances.py

echo "Packaging Delete unattached EBS function..."
zip -j build/delete_unattached_ebs.zip src/delete_unattached_ebs.py

echo "Packaging Release unused EIPs function..."
zip -j build/release_unused_eips.zip src/release_unused_eips.py

echo "Build complete. Artifacts are in the build/ directory."
