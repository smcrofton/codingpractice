
// https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one


function matchingStrings(strings, queries) {
    
    let stringMap = new Map();
    let results = [];
    
    for (let i = 0; i <= strings.length; i++){
        if (stringMap.has(strings[i])){
            stringMap.set(strings[i], (stringMap.get(strings[i]) + 1));
        }
        else{
            stringMap.set(strings[i], 1);            
        }
    }
    
    for (let i = 0; i <= queries.length; i++){
        if (stringMap.has(queries[i])){
            results[i] = stringMap.get(queries[i]);
        }
        else {
            results[i] = 0;
        }
    }
    
    return results;
}

function hourglassSum(arr) {
    let bestSum = -100;
    
    for (let i = 0; i <= 3; i++){
        
        for (let j = 0; j <= 3; j++){
             
            let topLeft = arr[i][j];
            let topMid = arr[i][j +1];
            let topRight = arr[i][j +2];
            let mid = arr[i +1][j +1];
            let botLeft = arr[i +2][j];
            let botMid = arr[i +2][j +1];
            let botRight = arr[i +2][j +2];

            let tempSum = topLeft + topMid + topRight + mid + botLeft + botMid + botRight;
            
            if (tempSum > bestSum){ bestSum = tempSum}
        }
    }
    
    return bestSum;
}


let test = [[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30],
            [31,32,33,34,35,36]];
console.log(hourglassSum(test));
