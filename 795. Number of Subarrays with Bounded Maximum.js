/**
 * @param {number[]} A
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var numSubarrayBoundedMax = function(A, L, R) {
    let cur = ans = 0;
    
    while(cur<A.length){
        let acc = 0;

        while(cur<A.length && (A[cur]<L || A[cur]>R)){
            if(A[cur]<L){
                acc += 1;
            }else{
                acc = 0;
            }
            cur += 1;
        }
        while(cur<A.length && A[cur]<=R){
            let less = 0;

            while(cur<A.length && A[cur]>=L && A[cur]<=R){
                acc += 1;
                [ans, cur] = [ans+acc, cur+1];
            }
            while(cur<A.length && A[cur]<L){
                [ans, cur, less] = [ans+acc, cur+1, less+1];
            }
            acc += less;
        }
    }
    return ans;
};