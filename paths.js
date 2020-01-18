var fs = require('fs');

var lines = fs.readFileSync('3000x3000.csv', 'UTF-8');
lines = lines.split('\n')

const paths = []
for (const line of lines) {
    const entries = line.split(',')
    const entriesInt = []
    for (const entry of entries)
        entriesInt.push(Number(entry))
    paths.push(entriesInt)
}

function findLargestSquareMatrix(pathsToCheck) {
    var pathsFlattened = [];
    pathsToCheck.forEach((row) => {
        row.forEach((item) => {
            pathsFlattened.push(item);
        });
    });

    //console.log(pathsFlattened);

    var pathsRowLength = pathsToCheck[0].length;

    var largestSquareMatrixData = {
        rowLength: 0,
        location: 0
    };

    var candidateRowStartIndex = 0;
    var candidateRowEndIndex = 0;

    for (candidateRowStartIndex = 0; candidateRowStartIndex < pathsFlattened.length; ++candidateRowStartIndex) {
        var isCandidateRowStartIndex = pathsFlattened[candidateRowStartIndex] === 1;

        if (!isCandidateRowStartIndex) { continue; }

        //console.log(`candidate row starting at ${candidateRowStartIndex}`);

        // start checking for more ones in a row
        candidateRowEndIndex = candidateRowStartIndex;
        var rowOfStartIndex = Math.floor(candidateRowStartIndex / pathsRowLength);
        var rowOfEndIndex = rowOfStartIndex;
        while (pathsFlattened[candidateRowEndIndex] === 1 && candidateRowEndIndex < pathsFlattened.length) {
            rowOfEndIndex = Math.floor(candidateRowEndIndex / pathsRowLength);
            if (rowOfStartIndex !== rowOfEndIndex) {
                //console.log('end index went to new row beyond start index, going to next step instead');
                break;
            }
            ++candidateRowEndIndex;
        }

        // remove last increment which puts us just past the last 1
        --candidateRowEndIndex;

        //console.log(`candidate row at ${candidateRowStartIndex} to ${candidateRowEndIndex}`);

        // this was just a single 1, can't be a square matrix,
        // continue at the next index
        if (candidateRowEndIndex === candidateRowStartIndex) {
            //console.log('just a single 1');
            continue;
        }

        var candidateRowLength = (candidateRowEndIndex - candidateRowStartIndex + 1);

        // no point checking a matrix that would be smaller than what we have so far
        if (candidateRowLength < largestSquareMatrixData.rowLength) {
            //console.log('matrix is not any larger than current largest');
            continue;
        }

        // make sure this matrix wouldn't go outside of the array
        var lastPossibleMatrixIndex = candidateRowEndIndex + (pathsRowLength * (candidateRowLength - 1));
        if (lastPossibleMatrixIndex > (pathsFlattened.length - 1)) {
            //console.log('matrix would not fit within bounds');
            continue;
        }

        // we now have the start and end of a candidate first row
        // of a possibly square matrix. let's get all indexes that have to be
        // 1s and check them.
        // this is a square matrix, so we have as many rows as columns (row length)
        var doAllRowsMatch = true;
        for (var row = 1; row < candidateRowLength; ++row) {
            var firstIndex = candidateRowStartIndex + (pathsRowLength * row);
            var lastIndex = candidateRowEndIndex + (pathsRowLength * row);
            //console.log(`checking index ${firstIndex} to ${lastIndex}`);
            for (var index = firstIndex; index <= lastIndex; ++index) {
                doAllRowsMatch = doAllRowsMatch && (pathsFlattened[index] === 1);
                if (!doAllRowsMatch) { break; }
                //console.log(`item at ${index} matches`);
            }
            // found a 0 where we wanted a 1, so let's keep looking
            if (!doAllRowsMatch) { break; }
        }

        if (!doAllRowsMatch) { continue; }

        // congrats! this is a square matrix. due to previous checks
        // this must be the largest matrix, so let's save the info
        largestSquareMatrixData.rowLength = candidateRowLength;
        largestSquareMatrixData.location = candidateRowStartIndex;

        //console.log('found new matrix');
        //console.log(largestSquareMatrixData);
    }

    return largestSquareMatrixData;
}

var result = findLargestSquareMatrix(paths);
console.log(result);