/**
 * @param {number[]} arr
 * @return {number}
 */
 var sumOddLengthSubarrays = function(arr) {
    let ans = 0;

    for(let i=0;i<arr.length;i++){
        let [left, right] = [i/2, (arr.length-i-1)/2];
        let [even, odd] = [(Math.floor(left)+1)*(Math.floor(right)+1), Math.ceil(left)*Math.ceil(right)];
        ans += (even+odd)*arr[i];
    }
    return ans;
};