/**
 * @param {number} N
 * @param {number} K
 * @return {number}
 */
var kthGrammar = function(N, K) {
    let count = ((K-1).toString(2).match(/1/g) || []).length;

    return count%2;
};