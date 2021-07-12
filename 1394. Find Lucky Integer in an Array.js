/**
 * @param {number[]} arr
 * @return {number}
 */
 var findLucky = function(arr) {
    let count = new Array(arr.length).fill(0);

    for(let i=0;i<arr.length;i++){
        let cur = arr[i]-1;
        count[i] += i+1;

        if(cur<count.length){
            count[cur] -= 1;
        }
    }

    for(let i=count.length-1;i>-1;i--){
        if(count[i]==0){
            return i+1;
        }
    }
    return -1;
};