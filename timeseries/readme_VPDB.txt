Author: Chin Hui Chew (Team 4)

Run the following on terminal window/command line window in the same directory where ArrayTimeSeries is stored

1) Start Python
2) import generateAndStoreTS, TimeSeriesDistance, buildVPDBforest, mostSimilarTS
3) generateAndStoreTS.generateAndStoreTimeSeries()
4) VPDict = buildVPDBforest.createVPForest()
5) mostSimilarTS.mostSimilarTS('./ts_998.npy', VPDict, 10)

Nodes in search region =  101
Most similar TS sorted from most similar onwards = 
['./ts_998.npy', './ts_39.npy', './ts_352.npy', './ts_556.npy', './ts_782.npy', './ts_633.npy', './ts_447.npy', './ts_849.npy', './ts_964.npy', './ts_368.npy']


Running from commaand line
Make the runVPDB.sh file executable by this line 
$ chmod +x runVPDB.sh
run in command line with this line:
$ ./runVPDB.sh './ts_352.npy' 10
Note the second argument which represents the number of nearest neighbors is optional and defaults to one

(py35) Chins-MacBook-Air-3:timeseries chinhuichew$ ./runVPDB.sh './ts_352.npy' 5 
Python starting
Nodes in search region =  573
Most similar TS sorted from most similar TS onwards = 
['./ts_352.npy', './ts_554.npy', './ts_554.npy', './ts_832.npy', './ts_832.npy']
Done




