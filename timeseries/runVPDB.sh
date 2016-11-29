#!/bin/bash
echo "Python starting"
rm ./VPDB*.dbdb

python - << EOF

import generateAndStoreTS, TimeSeriesDistance, buildVPDBforest, mostSimilarTS
generateAndStoreTS.generateAndStoreTimeSeries()
VPDict = buildVPDBforest.createVPForest()
mostSimilarTS.mostSimilarTS('$1', VPDict, $2)

EOF

echo "Done"
