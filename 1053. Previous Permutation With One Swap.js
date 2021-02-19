/**
 * @param {number[]} arr
 * @return {number[]}
 */
var prevPermOpt1 = function(arr) {
    for(let i=arr.length-2;i>-1;i--){
        let swap = [i, 0];
        
        for(let j=i+1;j<arr.length;j++){
            if(arr[j]>swap[1] && arr[j]<arr[i]){
                swap = [j, arr[j]];
            }
        }
        if(swap[0]!=i){
            [arr[i], arr[swap[0]]] = [arr[swap[0]], arr[i]];
            break;
        }
    }
    return arr;
};