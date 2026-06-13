#!/bin/bash
# Run all CR* cases in sequence (blockMesh → decomposePar → foamRun -parallel → reconstructPar)

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
N_PROCS=2

for CASE_DIR in "$BASE_DIR"/CR*/; do
    CASE=$(basename "$CASE_DIR")
    echo "========================================"
    echo "Starting case: $CASE"
    echo "========================================"

    cd "$CASE_DIR" || { echo "ERROR: cannot enter $CASE_DIR"; continue; }

    # Generate mesh
    echo "[1/4] blockMesh"
    blockMesh > log.blockMesh 2>&1 || { echo "ERROR: blockMesh failed for $CASE"; continue; }

    # Decompose for parallel
    echo "[2/4] decomposePar"
    decomposePar > log.decomposePar 2>&1 || { echo "ERROR: decomposePar failed for $CASE"; continue; }

    # Run solver in parallel
    echo "[3/4] foamRun (parallel, $N_PROCS procs)"
    mpirun -np $N_PROCS foamRun -parallel > log.foamRun 2>&1 || { echo "ERROR: foamRun failed for $CASE"; continue; }

    # Reconstruct
    echo "[4/4] reconstructPar"
    reconstructPar > log.reconstructPar 2>&1 || { echo "ERROR: reconstructPar failed for $CASE"; continue; }

    echo "Done: $CASE"
    cd "$BASE_DIR"
done

echo "========================================"
echo "All cases complete."
echo "========================================"