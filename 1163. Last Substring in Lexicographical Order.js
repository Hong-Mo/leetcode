/**
 * @param {string} s
 * @return {string}
 */
var lastSubstring = function(s) {
    let i=0, j=1, offset=0;

    while (i+offset<s.length && j+offset<s.length){
        if (s[i+offset]==s[j+offset]){
            offset += 1;
            continue;
        }else if(s[i+offset]<s[j+offset]){
            i += (offset+1);
        }else{
            j += (offset+1);
        }
        if (i==j){
            j += 1;
        }
        offset = 0;
    }

    return s.substring(i, s.length);
};