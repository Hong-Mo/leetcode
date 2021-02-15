/**
 * @param {number} N
 * @param {number} A
 * @param {number} B
 * @return {number}
 */
const gcd = (A, B)=>{
    if (B==0){
        return A;
    }
    return gcd(B, A%B);
}
const lcm = (A, B) =>{
    return (A*B)/gcd(A, B);
}
var nthMagicalNumber = function(N, A, B) {
    let quo = 0, AB_lcm = lcm(A, B);
    [A, B] = [Math.min(A, B), Math.max(A, B)];
    let [mutiple, addtional, turn] = [0, 0, ((AB_lcm/A)+(AB_lcm/B))-1];
    
    [quo, N] = [Math.floor(N/turn), N%turn];
    mutiple += (quo*AB_lcm);

    if (N){
        if (B%A==0){
            addtional = (A*N);
        }else{
            let step = (B/A)+1;
            let sec = Math.floor(N/step);
            let [cur, val, bound] = [sec+Math.floor((B*sec)/A), B*sec, (B*(sec+1))];

            while(cur<N){
                addtional = Math.min(((Math.floor(val/A))+1)*A, bound);
                [val, cur] = [addtional, cur+1];
            }
        }
    }
    return (mutiple+addtional)%(Math.pow(10, 9)+7); 
};