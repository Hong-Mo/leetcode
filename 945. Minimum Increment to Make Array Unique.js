/**
 * @param {number[]} A
 * @return {number}
 */
var minIncrementForUnique = function(A) {
    function compare_num(a, b){
        return a-b;
    }
    A = A.sort(compare_num);
    let ans = 0;
    for (let i=1;i<A.length;i++){
        let dif = A[i-1]-A[i];

        if (dif>=0){
            [ans, A[i]] = [ans+dif+1, A[i-1]+1];
        }
    }
    return ans;
};