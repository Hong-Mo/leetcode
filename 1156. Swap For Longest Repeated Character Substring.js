/**
 * @param {string} text
 * @return {number}
 */
var maxRepOpt1 = function(text) {
    let [ans, l, head] = [1, new Array(text.length).fill(1),
         new Array(26).fill(0)];
    head[text.charCodeAt(0)-97] += 1;

    for (let i=text.length-1;i>0;i--){
        if (text[i]==text[i-1]){
            l[i-1] += l[i]
        }else{
            head[text.charCodeAt(i)-97] += 1;
        }
    }
    for (let i=0;i<text.length;i++){
        let cur = l[i];
        if ((i-1<0 || l[i-1]<=cur) && (i+1==text.length || cur>=l[i+1]) &&
            (i+cur+1<text.length && text[i+cur+1]==text[i])){
            cur += l[i+cur+1];

            if(head[text.charCodeAt(i)-97]>2){
                cur += 1;
            }
        }else if(head[text.charCodeAt(i)-97]>1){
            cur += 1;
        }
        ans = Math.max(ans, cur);
    }
    return ans;
};