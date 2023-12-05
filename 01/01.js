//https://adventofcode.com/2023/day/1

const fs = require('fs');
const testFile = './test.txt'
const inputFile = './input.txt'

function readModuleFile(path, callback) {
    try {
        const filename = require.resolve(path);
        fs.readFile(filename, 'utf8', callback);
    } catch (e) {
        callback(e);
    }
}

readModuleFile(inputFile, function (err, words) {
    findMaxCals(words);
    findTopThree(words)
});

