/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
 var complexNumberMultiply = function(a, b) {
    [a, b] = [a.split('+'), b.split('+')];
    [a[1], b[1]] = [a[1].slice(0, -1), b[1].slice(0, -1)];

    let real = (a[0]*b[0])-(a[1]*b[1]);
    let im = (a[0]*b[1])+(b[0]*a[1]);

    return real+'+'+im+'i';
};